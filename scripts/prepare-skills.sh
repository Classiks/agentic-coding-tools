#!/usr/bin/env bash
# Prepare complete skill directories without configuring an agent host.
set -euo pipefail

usage() {
  cat <<'HELP'
Usage: prepare-skills.sh --output DIR (--all | --include NAME...) [--exclude NAME...]

Include/exclude accept multiple space-separated names and may be repeated.
Exclusions win. --all and --include are mutually exclusive.
The output directory must not exist. Referenced skills are reported, not added.
Requires Bash 3.2+ and standard Unix utilities. No downloads or host changes.
HELP
}
fail() { echo "Error: $*" >&2; exit 1; }
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/../skills" && pwd -P)"
output=''
all=false
include=()
exclude=()
while (($#)); do
  case "$1" in
    --help|-h) usage; exit 0 ;;
    --output)
      (($# >= 2)) || fail '--output requires a directory'
      [[ -z "$output" ]] || fail '--output may only appear once'
      output=$2; shift 2 ;;
    --all) all=true; shift ;;
    --include|--exclude)
      option=$1; shift
      count=0
      while (($#)) && [[ "$1" != --* ]]; do
        if [[ "$option" == --include ]]; then include+=("$1"); else exclude+=("$1"); fi
        count=$((count + 1)); shift
      done
      ((count > 0)) || fail "$option requires at least one skill name" ;;
    *) fail "Unknown argument: $1" ;;
  esac
done
[[ -n "$output" ]] || fail '--output is required'
if $all; then
  ((${#include[@]} == 0)) || fail 'Choose --all or --include, not both'
else
  ((${#include[@]} > 0)) || fail 'Choose --all or --include'
fi
# Validate all requested names, including exclusions, before writing anything.
for name in "${include[@]+"${include[@]}"}" "${exclude[@]+"${exclude[@]}"}"; do
  [[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || fail "Invalid skill name: $name"
  [[ -f "$source_dir/$name/SKILL.md" ]] || fail "Unknown skill: $name"
done
selected=()
available=,
for directory in "$source_dir"/*; do
  [[ -f "$directory/SKILL.md" ]] || continue
  name=${directory##*/}
  available="$available$name,"
  chosen=$all
  for requested in "${include[@]+"${include[@]}"}"; do
    if [[ "$name" == "$requested" ]]; then chosen=true; fi
  done
  for omitted in "${exclude[@]+"${exclude[@]}"}"; do
    if [[ "$name" == "$omitted" ]]; then chosen=false; fi
  done
  if $chosen; then selected+=("$name"); fi
done
((${#selected[@]} > 0)) || fail 'Selection is empty'
[[ ! -e "$output" && ! -L "$output" ]] || fail "Output already exists: $output"
# Resolve existing ancestors, including symlinks, before rejecting source overlap.
remaining=$output
suffix=''
while [[ ! -d "$remaining" ]]; do
  [[ ! -e "$remaining" && ! -L "$remaining" ]] || fail "Not a directory: $remaining"
  component=$(basename "$remaining")
  [[ "$component" != . && "$component" != .. ]] || fail 'Resolve dot segments through existing directories only'
  suffix="/$component$suffix"
  remaining=$(dirname "$remaining")
done
resolved="$(cd "$remaining" && pwd -P)$suffix"
case "$resolved/" in "$source_dir/"*) fail 'Output must be outside the source skills directory' ;; esac
output=$resolved
mkdir -p "$(dirname "$output")"
mkdir "$output" # Exclusive creation also catches a destination created after preflight.
trap 'result=$?; if ((result != 0)); then echo "Preparation failed; inspect incomplete output: $output" >&2; fi' EXIT
for name in "${selected[@]}"; do
  cp -R "$source_dir/$name" "$output/$name"
done
printf 'Prepared %s skills in %s\n' "${#selected[@]}" "$output"

# Inspect this suite's relative Markdown links. Conditional links are not dependencies.
selection=",$(IFS=,; echo "${selected[*]}"),"
for name in "${selected[@]}"; do
  find "$output/$name" -type f -name '*.md' -exec awk -v selected="$selection" -v available="$available" '
    {
      line=$0
      while (match(line, /\]\(\.\.\/[^)]*\)/)) {
        link=substr(line, RSTART+2, RLENGTH-3)
        line=substr(line, RSTART+RLENGTH)
        sub(/^(\.\.\/)+/, "", link)
        split(link, parts, "/")
        if (index(available, "," parts[1] ",") > 0 && index(selected, "," parts[1] ",") == 0)
          print "Reference to omitted skill: " parts[1] " (from " FILENAME ")"
      }
    }
  ' {} +
done | sort -u
