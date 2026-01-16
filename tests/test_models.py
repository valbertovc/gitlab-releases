from django.test import TestCase

from gitlab_releases import models


class UserTestCase(TestCase):
    def test_repr(self):
        user = models.User(
            id="id",
            name="name",
            username="username",
            state="state",
            avatar_url="avatar_url",
            web_url="web_url",
        )
        expected = str(user)
        self.assertEqual(expected, repr(user))


class CommitTestCase(TestCase):
    def test_repr(self):
        commit = models.Commit(
            id="id",
            short_id="short_id",
            title="title",
            created_at="2023-10-01T00:00:00Z",
            parent_ids=["parent1", "parent2"],
            message="message",
            author_name="author_name",
            author_email="author@example.com",
            authored_date="2023-10-01T00:00:00Z",
            committer_name="committer_name",
            committer_email="committer@example.com",
            committed_date="2023-10-01T00:00:00Z",
        )
        expected = str(commit)
        self.assertEqual(expected, repr(commit))


class LabelTestCase(TestCase):
    def test_label_creation(self):
        label = models.Label(name="bug")
        expected = str(label)
        self.assertEqual(expected, str(label))


class MilestoneTestCase(TestCase):
    def test_repr(self):
        milestone = models.Milestone(
            id=1,
            iid=1,
            group_id=1,
            title="Milestone 1",
            description="Description for milestone 1",
            state="active",
            created_at="2023-10-01T00:00:00Z",
            updated_at="2023-10-01T00:00:00Z",
        )
        expected = str(milestone)
        self.assertEqual(expected, repr(milestone))


class PipelineTestCase(TestCase):
    def test_repr(self):
        pipeline = models.Pipeline(
            id=1,
            iid=1,
            project_id=1,
            sha="abcdef",
            ref="main",
            status="success",
            source="push",
            created_at="2023-10-01T00:00:00Z",
            updated_at="2023-10-01T00:00:00Z",
            web_url="http://example.com/pipelines/1",
        )
        expected = str(pipeline)
        self.assertEqual(expected, repr(pipeline))

    def test_archived(self):
        pipeline = models.Pipeline(
            id=2,
            iid=2,
            project_id=1,
            sha="abcdef",
            ref="main",
            status="success",
            source="push",
            created_at="2023-10-01T00:00:00Z",
            updated_at="2023-10-01T00:00:00Z",
            web_url="http://example.com/pipelines/2",
            archived=True,
        )
        expected = True
        self.assertEqual(expected, pipeline.archived)


class MergeRequestTestCase(TestCase):
    def test_repr(self):
        mr = models.MergeRequest(
            project_id=1,
            id=1,
            iid=1,
            title="Merge Request 1",
            description="Description for merge request 1",
            state="opened",
            created_at="2023-10-01T00:00:00Z",
            updated_at="2023-10-01T00:00:00Z",
        )
        expected = str(mr)
        self.assertEqual(expected, repr(mr))


class ChangelogTestCase(TestCase):
    def test_repr(self):
        changelog = models.Changelog(
            section="Added",
            description="New feature added",
            commit_url="http://example.com/commit/abcdef",
        )
        expected = str(changelog)
        self.assertEqual(expected, repr(changelog))


class EvidenceTestCase(TestCase):
    def test_evidence_creation(self):
        evidence = models.Evidence(
            filepath="/evidence/file.png",
            collected_at="2023-10-01T00:00:00Z",
            sha="abcdef",
        )
        expected = str(evidence)
        self.assertEqual(expected, str(evidence))


class ReleaseTestCase(TestCase):
    def test_repr(self):
        author = {
            "id": 1,
            "name": "Author",
            "username": "author",
            "state": "active",
            "avatar_url": "http://example.com/avatar.png",
            "web_url": "http://example.com",
        }
        commit = {
            "id": "abcdef",
            "short_id": "abc123",
            "title": "Initial commit",
            "created_at": "2023-10-01T00:00:00Z",
            "parent_ids": ["123456"],
            "message": "This is a commit message.",
            "author_name": "Author Name",
            "author_email": "author@example.com",
            "authored_date": "2023-10-01T00:00:00Z",
            "committer_name": "Committer Name",
            "committer_email": "committer@example.com",
            "committed_date": "2023-10-01T00:00:00Z",
        }
        release = models.Release(
            tag_name="v1.0.0",
            name="Release 1.0.0",
            project_id="project_id",
            description="Release description",
            created_at="2023-10-01T00:00:00Z",
            released_at="2023-10-01T00:00:00Z",
            author=author,
            commit=commit,
        )
        expected = str(release)
        self.assertEqual(expected, repr(release))
