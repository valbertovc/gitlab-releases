from django.views.generic import ListView

from gitlab_releases import models
from gitlab_releases.client import Gitlab
from gitlab_releases.conf import settings
from gitlab_releases.paginator import GitlabPaginator


def load_merge_request(client, changelog):
    if changelog.merge_request_url:
        gitlab_merge_request = client.merge_request(changelog.merge_request_id)
        return models.MergeRequest(**gitlab_merge_request.attributes)


def load_releases(client, page=None, sort=None):
    gitlab_releases = client.releases(page=page, sort=sort)
    return [models.Release(**release.attributes) for release in gitlab_releases]


class ReleaseListView(ListView):
    template_name = "gitlab_releases/release_list.html"
    context_object_name = "releases"
    paginate_by = settings.GITLAB_PER_PAGE
    ordering_param = settings.GITLAB_ORDERING_PARAM
    page_param = settings.GITLAB_PAGE_PARAM
    sort_param = settings.GITLAB_SORT_PARAM
    paginator_class = GitlabPaginator

    def get_ordering(self):
        if self.ordering_param in self.request.GET:
            self.ordering = self.request.GET.get(self.ordering_param)
        return self.ordering

    def get_page(self):
        page = self.request.GET.get(self.page_param, 1)
        return page

    def get_sort(self):
        sort = self.request.GET.get(self.sort_param, None)
        return sort

    def get_queryset(self):
        ordering = self.get_ordering()
        page = self.get_page()
        sort = self.get_sort()
        client = Gitlab(order_by=ordering, per_page=self.paginate_by)
        releases = load_releases(client, page=page, sort=sort)
        for release in releases:
            for changelog in release.changelogs:
                changelog.merge_request = load_merge_request(client, changelog)
        return releases
