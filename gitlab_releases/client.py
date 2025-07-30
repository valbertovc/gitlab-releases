from typing import Optional

import gitlab

from gitlab_releases.conf import settings
from gitlab_releases.utils import memoize


class Gitlab:
    def __init__(
        self,
        url: str = None,
        private_token: str = None,
        api_version: str = None,
        timeout: Optional[float] = None,
        per_page: Optional[int] = None,
        pagination: Optional[str] = None,
        order_by: Optional[str] = None,
    ):
        url = url or settings.GITLAB_HOST
        private_token = private_token or settings.GITLAB_TOKEN
        api_version = api_version or settings.GITLAB_API_VERSION
        timeout = timeout or settings.GITLAB_TIMEOUT
        per_page = per_page or settings.GITLAB_PER_PAGE
        self.gl = gitlab.Gitlab(
            url=url,
            private_token=private_token,
            api_version=api_version,
            timeout=timeout,
            per_page=per_page,
            pagination=pagination,
            order_by=order_by,
        )
        self.project_id = settings.GITLAB_PROJECT_ID
        self._project = None

    def project(self, **kwargs):
        if self._project is None:
            self._project = self.gl.projects.get(self.project_id, **kwargs)
        return self._project

    def releases(self, **kwargs):
        return self.project().releases.list(**kwargs)

    @memoize
    def release(self, tag_name: str, **kwargs):
        return self.project().releases.get(tag_name, **kwargs)

    def merge_requests(self, **kwargs):
        return self.project().mergerequests.list(**kwargs)

    @memoize
    def merge_request(self, merge_request_id: int, **kwargs):
        return self.project().mergerequests.get(id=merge_request_id, **kwargs)

    @memoize
    def user(self, user_id: int, **kwargs):
        return self.gl.users.get(user_id, **kwargs)

    def users(self, **kwargs):
        return self.gl.users.list(**kwargs)
