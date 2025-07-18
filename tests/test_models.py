from django.test import TestCase

from gitlab_releases import models


class UserTestCase(TestCase):
    def test_repr(self):
        user = models.User()
        expected = str(user)
        self.assertEqual(expected, repr(user))


class CommitTestCase(TestCase):
    def test_repr(self):
        commit = models.Commit()
        expected = str(commit)
        self.assertEqual(expected, repr(commit))


class LabelTestCase(TestCase):
    def test_label_creation(self):
        label = models.Label()
        expected = str(label)
        self.assertEqual(expected, str(label))


class MilestoneTestCase(TestCase):
    def test_repr(self):
        milestone = models.Milestone()
        expected = str(milestone)
        self.assertEqual(expected, repr(milestone))


class PipelineTestCase(TestCase):
    def test_repr(self):
        pipeline = models.Pipeline()
        expected = str(pipeline)
        self.assertEqual(expected, repr(pipeline))


class MergeRequestTestCase(TestCase):
    def test_repr(self):
        mr = models.MergeRequest()
        expected = str(mr)
        self.assertEqual(expected, repr(mr))


class ChangelogTestCase(TestCase):
    def test_repr(self):
        changelog = models.Changelog()
        expected = str(changelog)
        self.assertEqual(expected, repr(changelog))


class EvidenceTestCase(TestCase):
    def test_evidence_creation(self):
        evidence = models.Evidence()
        expected = str(evidence)
        self.assertEqual(expected, str(evidence))


class ReleaseTestCase(TestCase):
    def test_repr(self):
        release = models.Release()
        expected = str(release)
        self.assertEqual(expected, repr(release))
