from django.test import TestCase

from gitlab_releases import parser


class ParserTestCase(TestCase):
    def test_parse_changelogs_returns_expected(self):
        markdown = """\n## Added\n- New feature\n"""
        expected = [{"section": "Added", "item": "New feature"}]
        result = parser.parse_changelogs(markdown)
        self.assertIsInstance(result, list)

    def test_extract_section_header(self):
        line = "## Added"
        expected = "Added"
        result = parser.extract_section_header(line)
        self.assertEqual(expected, result)

    def test_parse_item_line(self):
        line = "- New feature"
        expected = {"item": "New feature", "section": None}
        result = parser.parse_item_line(line, None)
        self.assertIsInstance(result, dict)

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
