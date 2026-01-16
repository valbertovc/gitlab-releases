from dataclasses import dataclass, field
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
    public_email: Optional[str] = None
    locked: Optional[bool] = None

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
    trailers: Optional[dict] = None
    extended_trailers: Optional[dict] = None
    web_url: Optional[str] = None

    def __post_init__(self):
        self.authored_date = parse_datetime(self.authored_date)
        self.committed_date = parse_datetime(self.committed_date)

    def __repr__(self):
        return (
            f"Commit(id={self.short_id}, title={self.title}, author={self.author_name})"
        )


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
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    expired: Optional[bool] = None
    web_url: Optional[str] = None
    project_id: Optional[int] = None

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
    before_sha: Optional[str] = None
    tag: Optional[bool] = None
    yaml_errors: Optional[str] = None
    user: Optional[dict] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None
    duration: Optional[int] = None
    queued_duration: Optional[int] = None
    coverage: Optional[str] = None
    detailed_status: Optional[dict] = None
    archived: Optional[bool] = None

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
    merged_by: Union[dict, User] = None
    merge_user: Union[dict, User] = None
    merged_at: Optional[datetime] = None
    closed_by: Union[dict, User] = None
    closed_at: Optional[datetime] = None
    target_branch: Optional[str] = None
    source_branch: Union[str, None] = None
    user_notes_count: Optional[int] = None
    upvotes: Optional[int] = None
    downvotes: Optional[int] = None
    author: Union[dict, User] = None
    assignees: list[Union[dict, User]] = None
    assignee: Union[dict, User] = None
    reviewers: list[Union[dict, User]] = None
    source_project_id: Optional[int] = None
    target_project_id: Optional[int] = None
    labels: list[Union[dict, Label]] = None
    draft: Optional[bool] = None
    imported: Optional[bool] = None
    imported_from: Optional[str] = None
    work_in_progress: Optional[bool] = None
    milestone: Union[dict, Milestone] = None
    merge_when_pipeline_succeeds: Optional[bool] = None
    merge_status: Optional[str] = None
    detailed_merge_status: Optional[str] = None
    merge_after: Optional[str] = None
    sha: Optional[str] = None
    merge_commit_sha: Optional[str] = None
    squash_commit_sha: Optional[str] = None
    discussion_locked: Optional[bool] = None
    should_remove_source_branch: Optional[bool] = None
    force_remove_source_branch: Optional[bool] = None
    prepared_at: Optional[datetime] = None
    reference: Optional[str] = None
    references: Optional[dict] = None
    web_url: Optional[str] = None
    time_stats: Optional[dict] = None
    squash: Optional[bool] = None
    squash_on_merge: Optional[bool] = None
    task_completion_status: Optional[dict] = None
    has_conflicts: Optional[bool] = None
    blocking_discussions_resolved: Optional[bool] = None
    subscribed: Optional[bool] = None
    changes_count: Optional[str] = None
    latest_build_started_at: Optional[datetime] = None
    latest_build_finished_at: Optional[datetime] = None
    first_deployed_to_production_at: Optional[datetime] = None
    pipeline: Union[dict, Pipeline] = None
    head_pipeline: Optional[Union[dict, Pipeline]] = None
    diff_refs: Optional[dict] = None
    merge_error: Optional[str] = None
    first_contribution: Optional[bool] = None
    user: Optional[dict] = None

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
    description: str
    commit_url: str
    type: Optional[str] = None
    context: Optional[str] = None
    merge_request_url: Optional[str] = None
    commit_sha: Optional[str] = None

    def __repr__(self):
        return f"Changelog(section={self.section}, type={self.type}, description={self.description})"

    @property
    def merge_request_id(self) -> Optional[int]:
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
    author: Union[dict, User]
    commit: Union[dict, Commit]
    commit_path: Optional[str] = None
    tag_path: Optional[str] = None
    upcoming_release: Optional[bool] = None
    assets: Optional[dict] = None
    evidences: list[Evidence] = field(default_factory=list)
    _links: Optional[dict] = None
    changelogs: Optional[list[Changelog]] = None

    def __post_init__(self):
        self.author = (
            User(**self.author) if isinstance(self.author, dict) else self.author
        )
        self.commit = (
            Commit(**self.commit) if isinstance(self.commit, dict) else self.commit
        )
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
