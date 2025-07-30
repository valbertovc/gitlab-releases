from django.conf import settings

GITLAB_RELEASES = {
    "GITLAB_PROJECT_ID": None,
    "GITLAB_TOKEN": None,
    "GITLAB_HOST": "https://gitlab.com",
    "GITLAB_API_VERSION": "4",
    "GITLAB_TIMEOUT": 5.0,  # seconds
    "GITLAB_PER_PAGE": 10,
    "GITLAB_ORDERING_PARAM": "order_by",
    "GITLAB_PAGE_PARAM": "page",
    "GITLAB_SORT_PARAM": "sort",
}

for key, default in GITLAB_RELEASES.items():
    user_config = getattr(settings, key, None)
    setattr(settings, key, user_config or default)
