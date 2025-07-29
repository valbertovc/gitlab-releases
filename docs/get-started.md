# Get Started with gitlab-releases

This guide will help you install, configure, and use the `gitlab-releases` in your Django project.

## Installation

```bash
pip install gitlab-releases
```

## Quick Start Example

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

## Configuration

You can configure the following environment variables in your Django `settings.py` to customize the integration:

| Setting Name            | Default Value         | Description                               |
|------------------------|----------------------|---------------------------------------------|
| GITLAB_PROJECT_ID      | None                 | Your GitLab project ID                      |
| GITLAB_PRIVATE_TOKEN   | None                 | Your GitLab private access token            |
| GITLAB_URL             | https://gitlab.com   | GitLab instance URL                         |
| GITLAB_API_VERSION     | 4                    | GitLab API version                          |
| GITLAB_TIMEOUT         | 5.0                  | Timeout for API requests (in seconds)       |
| GITLAB_PER_PAGE        | 10                   | Number of releases per page                 |
| GITLAB_ORDERING_PARAM  | order_by             | Query parameter name for ordering           |
| GITLAB_PAGE_PARAM      | page                 | Query parameter name for pagination         |
| GITLAB_SORT_PARAM      | sort                 | Query parameter name for sorting            |

Example of minimum usage in your `settings.py`:

```python
GITLAB_PROJECT_ID = 123456
GITLAB_PRIVATE_TOKEN = "your-token-here"
GITLAB_URL = "https://gitlab.com"
```

After installation and configuration, visit `/releases/` in your Django project to see the list of releases fetched from your GitLab repository.
