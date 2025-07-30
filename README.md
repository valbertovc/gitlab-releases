
# gitlab-releases

![License](https://img.shields.io/github/license/valbertovc/gitlab-releases)
![Build Status](https://img.shields.io/github/actions/workflow/status/valbertovc/gitlab-releases/release.yml)
![Coverage](https://img.shields.io/codecov/c/github/valbertovc/gitlab-releases)
![PyPI](https://img.shields.io/pypi/v/gitlab-releases)
![Python Versions](https://img.shields.io/pypi/pyversions/gitlab-releases)
![Django Versions](https://img.shields.io/pypi/frameworkversions/django/gitlab-releases)

## Short Description

`gitlab-releases` provides an in-memory release page and changelog integration for your Django project, making it easy to display your releases if you manage them using GitLab releases feature.

## Main Features

- Display a list of releases from your GitLab repository
- Show detailed changelog for each release
- Integrate release data into your Django templates
- Simple configuration and setup

## Get started

### Installation

```bash
pip install gitlab-releases
```

### Quick Start Example

Add `gitlab_releases` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...existing apps...
    'gitlab_releases',
]
```

### Include the app's URLs in your `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ...existing urls...
    path('releases/', include('gitlab_releases.urls')),
]
```

### Configure your `settings.py` file

```python
GITLAB_PROJECT_ID = 123456
GITLAB_TOKEN = "your-token-here"
GITLAB_HOST = "https://gitlab.com"
```

### Visit your release page 

After installation and configuration, visit `/releases/` in your Django project to see the list of releases fetched from your GitLab repository.

## Useful Links

- [Detailed Documentation](https://github.com/valbertovc/gitlab-releases/tree/main/docs)
- [Changelog](https://github.com/valbertovc/gitlab-releases/releases)
- [PyPI Page](https://pypi.org/project/gitlab-releases/)
- [Repository](https://github.com/valbertovc/gitlab-releases)
- [Bug Tracker](https://github.com/valbertovc/gitlab-releases/issues)
- [GitLab API Docs](https://docs.gitlab.com/ee/api/releases/)
