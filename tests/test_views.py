from unittest.mock import patch

from django.test import RequestFactory, TestCase

from gitlab_releases.views import ChangelogDetailView, ReleaseListView


class ReleaseListViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.view = ReleaseListView()

    @patch("gitlab.Gitlab")
    def test_get_releases_returns_expected(self, mock_gitlab):
        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value.releases.list.return_value = []
        expected = list()
        result = self.view.get_releases()
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_get_context_data(self, mock_gitlab):
        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value.releases.list.return_value = []
        context = self.view.get_context_data()
        self.assertIn("releases", context)
        self.assertIsInstance(context["releases"], list)
        mock_instance.projects.get.return_value.releases.list.assert_called_once_with()
