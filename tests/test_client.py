from django.test import TestCase

from gitlab_releases.client import Gitlab


class GitlabTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Gitlab(token="fake-token", url="https://gitlab.example.com/api/v4")

    def test_project_method(self):
        expected = None
        result = self.client.project()
        self.assertEqual(expected, result)

    def test_releases_method(self):
        expected = None
        result = self.client.releases()
        self.assertEqual(expected, result)

    def test_release_method(self):
        expected = None
        result = self.client.release(tag_name="v1.0.0")
        self.assertEqual(expected, result)

    def test_merge_requests_method(self):
        expected = None
        result = self.client.merge_requests()
        self.assertEqual(expected, result)

    def test_merge_request_method(self):
        expected = None
        result = self.client.merge_request(merge_request_id=1)
        self.assertEqual(expected, result)

    def test_user_method(self):
        expected = None
        result = self.client.user(user_id=1)
        self.assertEqual(expected, result)

    def test_users_method(self):
        expected = None
        result = self.client.users()
        self.assertEqual(expected, result)
