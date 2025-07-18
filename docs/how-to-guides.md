def my_upload_generator(instance, filename):

# How-to guides

This section provides practical guides for using gitlab-releases in your Django project.

## Displaying GitLab Releases in Your Django App

After installing and configuring gitlab-releases, you can display your GitLab releases in your Django project with minimal setup.

### 1. Add to Installed Apps

In your `settings.py`:

```python
INSTALLED_APPS = [
    # ...existing apps...
    'gitlab_releases',
]
```

### 2. Include URLs

In your `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ...existing urls...
    path('releases/', include('gitlab_releases.urls')),
]
```

### 3. Access the Release List

Visit `/releases/` in your browser to see the list of releases fetched from your GitLab repository.

## Customizing Templates

You can use the provided template tags to render release data in your own templates. For example:

```django
{% load gitlab_releases_filters %}
{% for release in releases %}
    <h2>{{ release.title }}</h2>
    <div>{{ release.description|markdown }}</div>
{% endfor %}
```

## Overriding Templates

To customize the look and feel, override the default templates by copying them from `gitlab_releases/templates/gitlab_releases/` into your own app's templates directory and editing as needed.

## Filtering or Sorting Releases

You can filter or sort the releases in your views or templates using standard Django template logic or by extending the app's views.

## Advanced: Using the API in Your Own Views

If you want to fetch and display releases programmatically, you can use the internal client:

```python
from gitlab_releases.client import GitlabReleasesClient

client = GitlabReleasesClient()
releases = client.get_releases(project_id="your-gitlab-project-id")
# Use 'releases' in your custom view or context
```

---

For more advanced usage and integration, see the full documentation and API reference.