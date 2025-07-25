from django.test import TestCase

from gitlab_releases import parser


class ParserTestCase(TestCase):
    def test_parse_changelogs_returns_expected(self):
        markdown = """\n## Added\n- New feature\n"""
        result = parser.parse_changelogs(markdown)
        self.assertIsInstance(result, list)

    def test_extract_section_header(self):
        pass

    def test_parse_item_line(self):
        pass

    def test_split_type_context_description(self):
        full = "fix(context): description"
        expected = ("fix", "context", "description")
        result = parser.split_type_context_description(full)
        self.assertEqual(expected, result)

    def test_extract_sha_from_url(self):
        url = "https://gitlab.com/project/commit/abcdef"
        expected = "abcdef"
        result = parser.extract_sha_from_url(url)
        self.assertEqual(expected, result)
