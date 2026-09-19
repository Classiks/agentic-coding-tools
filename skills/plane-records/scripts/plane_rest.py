#!/usr/bin/env python3
"""Tested Plane CE REST fallbacks for operations unavailable through MCP."""

from __future__ import annotations

import argparse
from http.cookiejar import CookieJar
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener


REQUIRED_ENVIRONMENT = ("PLANE_BASE_URL", "PLANE_WORKSPACE_SLUG", "PLANE_SERVICE_EMAIL", "PLANE_SERVICE_PASSWORD")


class PlaneRestError(RuntimeError):
    pass


def load_environment() -> None:
    if all(os.getenv(key) for key in REQUIRED_ENVIRONMENT):
        return
    configured_path = os.getenv("PLANE_SECRETS_FILE")
    if configured_path:
        path = Path(configured_path)
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as error:
            raise PlaneRestError("Cannot read the configured PLANE_SECRETS_FILE") from error
        for raw_line in lines:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key, value)
    missing = [key for key in REQUIRED_ENVIRONMENT if not os.getenv(key)]
    if missing:
        raise PlaneRestError("Missing Plane settings: " + ", ".join(missing))



class PlaneSession:
    def __init__(self) -> None:
        load_environment()
        self.base_url = os.environ["PLANE_BASE_URL"].rstrip("/")
        self.workspace = os.environ["PLANE_WORKSPACE_SLUG"]
        self.cookies = CookieJar()
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))
        self.csrf_token = ""

    def authenticate(self) -> None:
        csrf = self.request("GET", "/auth/get-csrf-token/", authenticate=False)
        self.csrf_token = csrf["csrf_token"]
        form = urlencode(
            {
                "email": os.environ["PLANE_SERVICE_EMAIL"],
                "password": os.environ["PLANE_SERVICE_PASSWORD"],
                "next_path": "/",
            }
        ).encode()
        request = Request(
            self.base_url + "/auth/sign-in/",
            data=form,
            method="POST",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": self.base_url + "/",
                "X-CSRFToken": self.csrf_token,
            },
        )
        try:
            self.opener.open(request, timeout=20).read()
        except (HTTPError, URLError) as error:
            raise PlaneRestError(f"Plane session authentication failed: {error}") from error
        if not any(cookie.name == "session-id" for cookie in self.cookies):
            raise PlaneRestError("Plane session authentication did not establish a session")
        for cookie in self.cookies:
            if cookie.name == "csrftoken":
                self.csrf_token = cookie.value

    def request(
        self,
        method: str,
        path: str,
        data: dict[str, Any] | None = None,
        *,
        authenticate: bool = True,
    ) -> Any:
        if authenticate and not any(cookie.name == "session-id" for cookie in self.cookies):
            self.authenticate()
        body = json.dumps(data).encode() if data is not None else None
        headers = {"Accept": "application/json", "Referer": self.base_url + "/"}
        if body is not None:
            headers["Content-Type"] = "application/json"
        if method not in ("GET", "HEAD"):
            headers["X-CSRFToken"] = self.csrf_token
        request = Request(self.base_url + path, data=body, method=method, headers=headers)
        try:
            with self.opener.open(request, timeout=20) as response:
                raw = response.read()
        except HTTPError as error:
            raise PlaneRestError(f"Plane REST {method} {path} failed with HTTP {error.code}") from error
        except URLError as error:
            raise PlaneRestError(f"Plane REST {method} {path} failed: {error.reason}") from error
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as error:
            raise PlaneRestError(f"Plane REST {method} {path} returned malformed JSON") from error

    def project_path(self, project_id: str, suffix: str) -> str:
        return f"/api/workspaces/{self.workspace}/projects/{project_id}/{suffix.lstrip('/')}"


def description_from_stdin(enabled: bool) -> str | None:
    return sys.stdin.read() if enabled else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)

    page_list = subparsers.add_parser("page-list")
    page_list.add_argument("project_id")

    page_get = subparsers.add_parser("page-get")
    page_get.add_argument("project_id")
    page_get.add_argument("page_id")

    page_create = subparsers.add_parser("page-create")
    page_create.add_argument("project_id")
    page_create.add_argument("name")
    page_create.add_argument("--access", type=int, default=0)
    page_create.add_argument("--description-stdin", action="store_true")

    page_update = subparsers.add_parser("page-update")
    page_update.add_argument("project_id")
    page_update.add_argument("page_id")
    page_update.add_argument("--name")
    page_update.add_argument("--description-stdin", action="store_true")

    for operation in ("page-archive", "page-unarchive"):
        command = subparsers.add_parser(operation)
        command.add_argument("project_id")
        command.add_argument("page_id")

    page_delete = subparsers.add_parser("page-delete")
    page_delete.add_argument("project_id")
    page_delete.add_argument("page_id")
    page_delete.add_argument("--confirm-delete", action="store_true", required=True)

    for operation in ("workitem-archive", "workitem-unarchive"):
        command = subparsers.add_parser(operation)
        command.add_argument("project_id")
        command.add_argument("workitem_id")

    return parser


def execute(arguments: argparse.Namespace) -> Any:
    plane = PlaneSession()
    operation = arguments.operation

    if operation == "page-list":
        return plane.request("GET", plane.project_path(arguments.project_id, "pages/"))
    if operation == "page-get":
        return plane.request("GET", plane.project_path(arguments.project_id, f"pages/{arguments.page_id}/"))
    if operation == "page-create":
        data: dict[str, Any] = {"name": arguments.name, "access": arguments.access}
        description = description_from_stdin(arguments.description_stdin)
        if description is not None:
            data["description_html"] = description
        return plane.request("POST", plane.project_path(arguments.project_id, "pages/"), data)
    if operation == "page-update":
        data = {}
        if arguments.name is not None:
            data["name"] = arguments.name
        description = description_from_stdin(arguments.description_stdin)
        if description is not None:
            data["description_html"] = description
        if not data:
            raise PlaneRestError("page-update requires --name or --description-stdin")
        return plane.request("PATCH", plane.project_path(arguments.project_id, f"pages/{arguments.page_id}/"), data)
    if operation == "page-archive":
        return plane.request("POST", plane.project_path(arguments.project_id, f"pages/{arguments.page_id}/archive/"), {})
    if operation == "page-unarchive":
        return plane.request("DELETE", plane.project_path(arguments.project_id, f"pages/{arguments.page_id}/archive/"))
    if operation == "page-delete":
        return plane.request("DELETE", plane.project_path(arguments.project_id, f"pages/{arguments.page_id}/"))
    if operation == "workitem-archive":
        return plane.request(
            "POST", plane.project_path(arguments.project_id, f"issues/{arguments.workitem_id}/archive/"), {}
        )
    if operation == "workitem-unarchive":
        return plane.request(
            "DELETE", plane.project_path(arguments.project_id, f"issues/{arguments.workitem_id}/archive/")
        )
    raise PlaneRestError(f"Unsupported operation: {operation}")


def main() -> None:
    try:
        result = execute(build_parser().parse_args())
    except PlaneRestError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1) from error
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
