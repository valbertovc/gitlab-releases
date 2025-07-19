from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from django.utils.dateparse import parse_datetime

from gitlab_releases.parser import parse_changelogs


@dataclass
class User:
    id: int
    name: str
    username: str
    state: str
    avatar_url: str
    web_url: str
    public_email: str | None = None
    locked: bool | None = None

    def __repr__(self):
        return f"User(username={self.username})"


@dataclass
class Commit:
    id: str
    short_id: str
    title: str
    created_at: str
    parent_ids: list[str]
    message: str
    author_name: str
    author_email: str
    authored_date: datetime
    committer_name: str
    committer_email: str
    committed_date: datetime
    trailers: dict | None = None
    extended_trailers: dict | None = None
    web_url: str | None = None

    def __post_init__(self):
        self.authored_date = parse_datetime(self.authored_date)
        self.committed_date = parse_datetime(self.committed_date)

    def __repr__(self):
        return f"Commit(id={self.short_id}, title={self.title}, author={self.author_name})"


@dataclass
class Label:
    name: str


@dataclass
class Milestone:
    id: int
    iid: int
    group_id: int
    title: str
    description: str
    state: str
    created_at: datetime
    updated_at: datetime
    due_date: datetime | None = None
    start_date: datetime | None = None
    expired: bool | None = None
    web_url: str | None = None

    def __post_init__(self):
        self.created_at = parse_datetime(self.created_at)
        self.updated_at = parse_datetime(self.updated_at)
        if self.due_date:
            self.due_date = parse_datetime(self.due_date)
        if self.start_date:
            self.start_date = parse_datetime(self.start_date)

    def __repr__(self):
        return f"Milestone(id={self.id}, title={self.title}, state={self.state})"


@dataclass
class Pipeline:
    id: int
    iid: int
    project_id: int
    sha: str
    ref: str
    status: str
    source: str
    created_at: datetime
    updated_at: datetime
    web_url: str
    before_sha: str | None = None
    tag: bool | None = None
    yaml_errors: str | None = None
    user: dict | User = None
    started_at: datetime | None = None
    finished_at: datetime | None = None
    committed_at: datetime | None = None
    duration: int | None = None
    queued_duration: int | None = None
    coverage: str | None = None
    detailed_status: dict | None = None

    def __post_init__(self):
        self.created_at = parse_datetime(self.created_at)
        self.updated_at = parse_datetime(self.updated_at)
        if self.started_at:
            self.started_at = parse_datetime(self.started_at)
        if self.finished_at:
            self.finished_at = parse_datetime(self.finished_at)
        if self.committed_at:
            self.committed_at = parse_datetime(self.committed_at)
        if self.user:
            self.user = User(**self.user)

    def __repr__(self):
        return f"Pipeline(id={self.id}, ref={self.ref}, status={self.status})"


@dataclass
class MergeRequest:
    project_id: int
    id: int
    iid: int
    title: str
    description: str
    state: str
    created_at: datetime
    updated_at: datetime
    merged_by: dict | User = None
    merge_user: dict | User = None
    merged_at: datetime | None = None
    closed_by: dict | User = None
    closed_at: datetime | None = None
    target_branch: str | None = None
    source_branch: str | None = None
    user_notes_count: int | None = None
    upvotes: int | None = None
    downvotes: int | None = None
    author: dict | User = None
    assignees: list[dict | User] = None
    assignee: dict | User = None
    reviewers: list[dict | User] = None
    source_project_id: int | None = None
    target_project_id: int | None = None
    labels: list[dict | Label] = None
    draft: bool | None = None
    imported: bool | None = None
    imported_from: str | None = None
    work_in_progress: bool | None = None
    milestone: dict | Milestone = None
    merge_when_pipeline_succeeds: bool | None = None
    merge_status: str | None = None
    detailed_merge_status: str | None = None
    merge_after: str | None = None
    sha: str | None = None
    merge_commit_sha: str | None = None
    squash_commit_sha: str | None = None
    discussion_locked: bool | None = None
    should_remove_source_branch: bool | None = None
    force_remove_source_branch: bool | None = None
    prepared_at: datetime | None = None
    reference: str | None = None
    references: dict | None = None
    web_url: str | None = None
    time_stats: dict | None = None
    squash: bool | None = None
    squash_on_merge: bool | None = None
    task_completion_status: dict | None = None
    has_conflicts: bool | None = None
    blocking_discussions_resolved: bool | None = None
    subscribed: bool | None = None
    changes_count: str | None = None
    latest_build_started_at: datetime | None = None
    latest_build_finished_at: datetime | None = None
    first_deployed_to_production_at: datetime | None = None
    pipeline: dict | Pipeline | None = None
    head_pipeline: dict | Pipeline | None = None
    diff_refs: dict | None = None
    merge_error: str | None = None
    first_contribution: bool | None = None
    user: dict | None = None

    def __post_init__(self):
        self.created_at = parse_datetime(self.created_at)
        self.updated_at = parse_datetime(self.updated_at)
        if self.merged_at:
            self.merged_at = parse_datetime(self.merged_at)
        if self.closed_at:
            self.closed_at = parse_datetime(self.closed_at)
        if self.prepared_at:
            self.prepared_at = parse_datetime(self.prepared_at)
        if self.author:
            self.author = User(**self.author)
        if self.merged_by:
            self.merged_by = User(**self.merged_by)
        if self.merge_user:
            self.merge_user = User(**self.merge_user)
        if self.closed_by:
            self.closed_by = User(**self.closed_by)
        if self.assignees:
            self.assignees = [User(**assignee) for assignee in self.assignees]
        if self.assignee:
            self.assignee = User(**self.assignee)
        if self.reviewers:
            self.reviewers = [User(**reviewer) for reviewer in self.reviewers]
        if self.milestone:
            self.milestone = Milestone(**self.milestone)
        if self.labels:
            self.labels = [Label(name=label) for label in self.labels]
        if self.pipeline:
            self.pipeline = Pipeline(**self.pipeline)
        if self.head_pipeline:
            self.head_pipeline = Pipeline(**self.head_pipeline)

    def __repr__(self):
        return f"MergeRequest(id={self.iid}, title={self.title}, author={self.author.name if self.author else 'Unknown'})"


@dataclass
class Changelog:
    section: str
    type: str | None
    context: str | None
    description: str
    commit_url: str
    merge_request_url: str | None
    commit_sha: str | None

    def __repr__(self):
        return (
            f"Changelog(section={self.section}, type={self.type}, description={self.description})"
        )

    @property
    def merge_request_id(self) -> int | None:
        if self.merge_request_url:
            return int(self.merge_request_url.split("/")[-1])
        return None


@dataclass
class Evidence:
    sha: str
    filepath: str
    collected_at: str


@dataclass
class Release:
    tag_name: str
    name: str
    project_id: int
    description: str
    created_at: datetime
    released_at: datetime
    author: dict | User
    commit: dict | Commit
    commit_path: str | None
    tag_path: str | None
    upcoming_release: bool | None = None
    assets: dict | None = None
    evidences: list[Evidence] | None = None
    _links: dict | None = None
    changelogs: list[Changelog] | None = None

    def __post_init__(self):
        self.author = User(**self.author)
        self.commit = Commit(**self.commit)
        self.evidences = [Evidence(**evidence) for evidence in self.evidences]
        self.changelogs = self._load_changelogs()
        self.created_at = parse_datetime(self.created_at)
        self.released_at = parse_datetime(self.released_at)

    def __repr__(self):
        return f"Release(name={self.name}, project_id={self.project_id})"

    def _load_changelogs(self):
        items = parse_changelogs(self.description)
        return [Changelog(**item) for item in items]

    @property
    def published_by(self) -> dict:
        return {
            "author_name": self.commit.author_name,
            "author_email": self.commit.author_email,
            "authored_date": self.commit.authored_date,
        }
