from django.conf import settings

GITLAB_RELEASES = {
    "GITLAB_PROJECT_ID": None,
    "GITLAB_PRIVATE_TOKEN": None,
    "GITLAB_URL": "https://gitlab.com",
    "GITLAB_API_VERSION": "4",
    "GITLAB_TIMEOUT": 5.0,  # seconds
    "GITLAB_PER_PAGE": 10,
}

for key, default in GITLAB_RELEASES.items():
    user_config = getattr(settings, key, None)
    setattr(settings, key, user_config or default)
