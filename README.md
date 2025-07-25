
# gitlab-releases

![License](https://img.shields.io/github/license/valbertovc/gitlab-releases)
![Build Status](https://img.shields.io/github/actions/workflow/status/valbertovc/gitlab-releases/ci.yml?branch=main)
![Coverage](https://img.shields.io/codecov/c/github/valbertovc/gitlab-releases)
![PyPI](https://img.shields.io/pypi/v/gitlab-releases)
![Python Versions](https://img.shields.io/pypi/pyversions/gitlab-releases)
![Django Versions](https://img.shields.io/pypi/djversions/gitlab-releases)

## Short Description

`gitlab-releases` provides a release page and changelog integration for your Django project, making it easy to display your releases if you manage them using GitLab releases feature.

## Main Features

- Display a list of releases from your GitLab repository
- Show detailed changelog for each release
- Integrate release data into your Django templates
- Simple configuration and setup

## Get Started

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

Include the app's URLs in your `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ...existing urls...
    path('releases/', include('gitlab_releases.urls')),
]
```

## How to Use the Package or Django App

After installation and configuration, visit `/releases/` in your Django project to see the list of releases fetched from your GitLab repository. You can customize the templates or use the provided template tags in your own templates:

```django
{% load gitlab_releases_filters %}
{% for release in releases %}
    <h2>{{ release.title }}</h2>
    <div>{{ release.description|markdown }}</div>
{% endfor %}
```

## Useful Links

- [Documentation](https://github.com/valbertovc/gitlab-releases#readme)
- [Changelog](https://github.com/valbertovc/gitlab-releases/releases)
- [PyPI Page](https://pypi.org/project/gitlab-releases/)
- [Repository](https://github.com/valbertovc/gitlab-releases)
- [Bug Tracker](https://github.com/valbertovc/gitlab-releases/issues)
- [GitLab API Docs](https://docs.gitlab.com/ee/api/releases/)
