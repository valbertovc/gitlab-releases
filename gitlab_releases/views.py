from django.views.generic import TemplateView

from gitlab_releases import models
from gitlab_releases.client import Gitlab


def load_merge_request(client, changelog):
    if changelog.merge_request_url:
        gitlab_merge_request = client.merge_request(changelog.merge_request_id)
        return models.MergeRequest(**gitlab_merge_request.attributes)


def load_releases(client):
    gitlab_releases = client.releases()
    return [models.Release(**release.attributes) for release in gitlab_releases]


class ReleaseListView(TemplateView):
    template_name = "gitlab_releases/release_list.html"

    def get_releases(self):
        client = Gitlab()
        releases = load_releases(client)
        for release in releases:
            for changelog in release.changelogs:
                changelog.merge_request = load_merge_request(client, changelog)
        return releases

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["releases"] = self.get_releases()
        return context


class ChangelogDetailView(TemplateView):
    template_name = "gitlab_releases/changelog_detail.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_name = self.kwargs.get("tag_name")
        self.merge_request_id = self.kwargs.get("merge_request_id")
        self.client = Gitlab()
        self.release = None

    def get_release(self, tag_name):
        if not self.release:
            release = self.client.release(tag_name)
            self.release = models.Release(**release.attributes)
        return self.release

    def get_changelog(self, tag_name, merge_request_id):
        release = self.get_release(tag_name)
        for changelog in release.changelogs:
            if changelog.merge_request_id and changelog.merge_request_id == merge_request_id:
                changelog.merge_request = load_merge_request(self.client, changelog)
                return changelog
        # raise ChangelogNotFound()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_name = self.kwargs.get("tag_name")
        merge_request_id = self.kwargs.get("merge_request_id")
        context["release"] = self.get_release(tag_name)
        context["changelog"] = self.get_changelog(tag_name, merge_request_id)
        return context
