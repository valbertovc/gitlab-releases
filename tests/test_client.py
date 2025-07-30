from unittest.mock import patch

from django.test import TestCase, override_settings

from gitlab_releases.client import Gitlab


class GitlabTestCase(TestCase):
    gitlab_url = "https://gitlab.example.com/api/v4"
    project_id = 123

    @classmethod
    def setUpTestData(cls):
        cls.settings_patch = override_settings(
            GITLAB_HOST=cls.gitlab_url,
            GITLAB_TOKEN="fake-token",
            GITLAB_API_VERSION="4",
            GITLAB_TIMEOUT=10,
            GITLAB_PER_PAGE=10,
            GITLAB_PROJECT_ID=cls.project_id,
        )
        cls.settings_patch.enable()
        cls.project_data = {
            "id": cls.project_id,
            "name": "Example Project",
            "path": "example-project",
            "description": "An example project",
            "web_url": f"{cls.gitlab_url}/projects/{cls.project_id}",
        }
        cls.release_data = {
            "tag_name": "v1.0.0",
            "name": "Version 1.0.0",
            "description": "First stable release",
            "created_at": "2025-07-18T10:00:00.000Z",
            "author": {"name": "John Doe", "username": "johndoe"},
        }
        cls.merge_request_data = {
            "id": 1,
            "iid": 1,
            "title": "Feature: Add new functionality",
            "description": "Implements new feature X",
            "state": "merged",
            "merged_at": "2025-07-17T15:00:00.000Z",
            "author": {"name": "John Doe", "username": "johndoe"},
        }
        cls.user_data = {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@example.com",
            "state": "active",
        }

    @classmethod
    def tearDownClass(cls):
        cls.settings_patch.disable()
        super().tearDownClass()

    @patch("gitlab.Gitlab")
    def test_project_returns_project_instance(self, mock_gitlab):
        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value = self.project_data

        client = Gitlab()
        result = client.project()

        self.assertEqual(self.project_data, result)
        mock_instance.projects.get.assert_called_once_with(self.project_id)

    @patch("gitlab.Gitlab")
    def test_releases_returns_list(self, mock_gitlab):
        expected = [self.release_data]

        class Releases:
            @staticmethod
            def list(**kwargs):
                return expected

        class Project(dict):
            releases = Releases()

        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value = Project(self.project_data)

        client = Gitlab()
        result = client.releases()
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_release_returns_specific_release(self, mock_gitlab):
        expected = self.release_data

        class Releases:
            @staticmethod
            def get(tag_name, **kwargs):
                return expected

        class Project(dict):
            releases = Releases()

        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value = Project(self.project_data)

        client = Gitlab()
        result = client.release(tag_name="v1.0.0")
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_merge_requests_returns_list(self, mock_gitlab):
        expected = [self.merge_request_data]

        class MergeRequests:
            @staticmethod
            def list(**kwargs):
                return expected

        class Project(dict):
            mergerequests = MergeRequests()

        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value = Project(self.project_data)

        client = Gitlab()
        result = client.merge_requests()
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_merge_request_returns_specific_request(self, mock_gitlab):
        expected = self.merge_request_data

        class MergeRequests:
            @staticmethod
            def get(id, **kwargs):
                return expected

        class Project(dict):
            mergerequests = MergeRequests()

        mock_instance = mock_gitlab.return_value
        mock_instance.projects.get.return_value = Project(self.project_data)

        client = Gitlab()
        result = client.merge_request(merge_request_id=1)
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_user_returns_specific_user(self, mock_gitlab):
        expected = self.user_data

        class Users:
            @staticmethod
            def get(user_id, **kwargs):
                return expected

        mock_instance = mock_gitlab.return_value
        mock_instance.users = Users()

        client = Gitlab()
        result = client.user(user_id=1)
        self.assertEqual(expected, result)

    @patch("gitlab.Gitlab")
    def test_users_returns_list(self, mock_gitlab):
        expected = [self.user_data]

        class Users:
            @staticmethod
            def list(**kwargs):
                return expected

        mock_instance = mock_gitlab.return_value
        mock_instance.users = Users()

        client = Gitlab()
        result = client.users()
        self.assertEqual(expected, result)
