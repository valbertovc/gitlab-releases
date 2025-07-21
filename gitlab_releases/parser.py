import re
from typing import Optional

SECTION_HEADER_RE = re.compile(r"^###\s+(?P<section>\w+)", re.IGNORECASE)
ITEM_RE = re.compile(
    r"- \[(?P<full>.+?)\]\((?P<commit_url>.+?)\)"
    r"(?: \(?\[merge request\]\((?P<mr_url>.+?)\)\)?)?",
    re.IGNORECASE,
)


def parse_changelogs(markdown: str) -> list[dict]:
    items = []
    current_section = None
    for line in markdown.splitlines():
        line = line.strip()
        if not line:
            continue
        section = extract_section_header(line)
        if section:
            current_section = section
            continue
        item = parse_item_line(line, current_section)
        if item:
            items.append(item)
    return items


def extract_section_header(line: str) -> Optional[str]:
    match = SECTION_HEADER_RE.match(line)
    if match:
        return match.group("section").lower()
    return None


def parse_item_line(line: str, section: Optional[str] = None) -> Optional[dict]:
    if not section:
        return None
    match = ITEM_RE.match(line)
    if not match:
        return None
    full = match.group("full")
    commit_url = match.group("commit_url")
    mr_url = match.group("mr_url")
    type_, context, description = split_type_context_description(full)
    commit_sha = extract_sha_from_url(commit_url)
    return {
        "section": section,
        "type": type_,
        "context": context,
        "description": description,
        "commit_url": commit_url,
        "merge_request_url": mr_url,
        "commit_sha": commit_sha,
    }


def split_type_context_description(
    full: str,
) -> tuple[Optional[str], Optional[str], str]:
    if ":" not in full:
        return None, None, full
    prefix, description = map(str.strip, full.split(":", 1))
    if "(" in prefix and prefix.endswith(")"):
        type_, context = prefix[:-1].split("(", 1)
        return type_.strip(), context.strip(), description
    else:
        return prefix.strip(), None, description


def extract_sha_from_url(url: str) -> Optional[str]:
    return url.rstrip("/").split("/")[-1] if url else None
