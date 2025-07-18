
# Welcome to gitlab-releases documentation

![PyPI - License](https://img.shields.io/pypi/l/gitlab-releases)
![PyPI Version](https://img.shields.io/pypi/v/gitlab-releases.svg)
![Codecov](https://codecov.io/github/valbertovc/gitlab-releases/branch/main/graph/badge.svg)
![Build Status](https://img.shields.io/github/actions/workflow/status/valbertovc/gitlab-releases/ci.yml?branch=main)
![Python Versions](https://img.shields.io/pypi/pyversions/gitlab-releases.svg)
![Django Versions](https://img.shields.io/pypi/djversions/gitlab-releases)

This site contains the project documentation for the
`gitlab-releases` project, a Django reusable app to display and manage GitLab release information in your Django projects.

## Table of contents

1. [How-To Guides](how-to-guides.md)

# Introduction


Main features:

- Display a list of releases from your GitLab repository
- Show detailed changelog for each release
- Integrate release data into your Django templates
- Custom template tags for advanced rendering
- Simple configuration and setup


## Get started
Install gitlab-releases in your virtual environment:
```bash
pip install gitlab-releases
```
Add it to your `INSTALLED_APPS` in `settings.py`:
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
Visit `/releases/` in your Django project to see the list of releases.


## Useful links

1. [Documentation](https://valbertovc.github.io/gitlab-releases/)
2. [Changelog](https://github.com/valbertovc/gitlab-releases/releases)
3. [PyPI Page](https://pypi.org/project/gitlab-releases/)
4. [Repository](https://github.com/valbertovc/gitlab-releases)
5. [Bug Tracker](https://github.com/valbertovc/gitlab-releases/issues)