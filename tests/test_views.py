from django.test import RequestFactory, TestCase

from gitlab_releases.views import ChangelogDetailView, ReleaseListView


class ReleaseListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.view = ReleaseListView()

    def test_get_releases_returns_expected(self):
        expected = list()
        result = self.view.get_releases()
        self.assertEqual(expected, result)

    def test_get_context_data(self):
        expected = dict()
        result = self.view.get_context_data()
        self.assertIsInstance(result, dict)


class ChangelogDetailViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.view = ChangelogDetailView()

    def test_get_release_returns_expected(self):
        expected = None
        result = self.view.get_release(tag_name="v1.0.0")
        self.assertEqual(expected, result)

    def test_get_changelog_returns_expected(self):
        expected = None
        result = self.view.get_changelog(tag_name="v1.0.0", merge_request_id=1)
        self.assertEqual(expected, result)

    def test_get_context_data(self):
        expected = dict()
        result = self.view.get_context_data()
        self.assertIsInstance(result, dict)
