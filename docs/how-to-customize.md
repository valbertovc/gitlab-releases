# Customizing Templates in gitlab-releases

This guide explains how to customize the templates used by `gitlab-releases` and details the variables available in the context.

## Overriding Templates

To customize the look and feel of the release list or detail pages:

1. Copy the template you want to override from `gitlab_releases/templates/gitlab_releases/` into your own app's `templates/gitlab_releases/` directory.
2. Edit the copied template as needed. Django will use your version instead of the default.

## Context Variables Available in Templates

When using the default `ReleaseListView`, the following variables are available in your template:

### `releases`
A list of `Release` objects. Each `Release` object provides:

- `tag_name`: The Git tag name for the release (e.g., `v1.0.0`)
- `name`: The release name/title
- `project_id`: The GitLab project ID
- `description`: The full release description (may include changelog in markdown)
- `created_at`: Datetime when the release was created
- `released_at`: Datetime when the release was published
- `author`: A `User` object (see below)
- `commit`: A `Commit` object (see below)
- `commit_path`, `tag_path`: Optional URLs for commit/tag
- `upcoming_release`: Boolean, if this is an upcoming release
- `changelogs`: List of `Changelog` objects (see below)
- `published_by`: Dict with commit author info

#### `Changelog` object fields (follows the conventional commits pattern)
> ATENTION: the changelog is a commit message. If you follow the [Conventional Commits Pattern](https://www.conventionalcommits.org/), you will have more detailed data.
- `section`: Section/category of the change (e.g., `added`, `changed`) is a group provided by the Gitlab default template
- `description`: Description of the change
- `commit_url`: URL to the commit
- `type`: Optional type of change (e.g., `feat`, `fix`, `tests`)
- `context`: Optional context string
- `merge_request_url`: Optional URL to the related merge request
- `commit_sha`: Optional commit SHA
- `merge_request_id`: Property, the ID of the merge request (if available)
- `merge_request`: (Populated by the view) A `MergeRequest` object with details (see below)

#### `User` object fields
- `id`, `name`, `username`, `state`, `avatar_url`, `web_url`, `public_email`, `locked`

#### `Commit` object fields
- `id`, `short_id`, `title`, `created_at`, `parent_ids`, `message`, `author_name`, `author_email`, `authored_date`, `committer_name`, `committer_email`, `committed_date`, etc.

#### `MergeRequest` object fields
- `id`, `iid`, `title`, `description`, `state`, `created_at`, `updated_at`, `author`, `tags`, and many more (see source for full list)

## Example Usage in a Template

```django
{% for release in releases %}
  <h2>{{ release.name }} ({{ release.tag_name }})</h2>
  <p>Published: {{ release.released_at }} by {{ release.author.name }}</p>
  <div>{{ release.description|linebreaks }}</div>
  <ul>
    {% for item in release.changelogs %}
      <li>
        <strong>{{ item.section|title }}:</strong> {{ item.description }}
        {% if item.merge_request %}
          (<a href="{{ item.merge_request.web_url }}">MR !{{ item.merge_request.iid }}</a> by {{ item.merge_request.author.name }})
        {% endif %}
      </li>
    {% endfor %}
  </ul>
{% endfor %}
```

## Pagination and Extra Context

If pagination is enabled (default), you can use Django's pagination variables:
- `is_paginated`, `page_obj`, `paginator`, etc.

Example:
```django
{% if is_paginated %}
  <div class="pagination">
    {% if page_obj.has_previous %}
      <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}
    <span>Page {{ page_obj.number }} of {{ paginator.num_pages }}</span>
    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
  </div>
{% endif %}
```


## Advanced Customization

### Extending ReleaseListView

You can extend or subclass `ReleaseListView` to add custom context, filtering, or behavior. For example, to add extra context or filter releases:

```python
# myapp/views.py
from gitlab_releases.views import ReleaseListView

class CustomReleaseListView(ReleaseListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        # Example: filter releases by tag prefix
        return [r for r in queryset if r.tag_name.startswith('v1.')]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_extra_var'] = 'Custom value'
        return context
```

Then, in your `urls.py`:

```python
from myapp.views import CustomReleaseListView
from django.urls import path

urlpatterns = [
    path('releases/', CustomReleaseListView.as_view(), name='custom_release_list'),
]
```

### Overriding the Template

You can override the template used by your custom view by setting `template_name`:

```python
class CustomReleaseListView(ReleaseListView):
    template_name = 'myapp/custom_release_list.html'
    # ...
```

### Creating Custom Template Tags or Filters

You can create your own template tags or filters to use in your templates:

1. Create a `templatetags` directory in your app (with `__init__.py`).
2. Add a Python file (e.g., `my_filters.py`):

```python
# myapp/templatetags/my_filters.py
from django import template

register = template.Library()

@register.filter
def highlight_feature(section):
    if section == 'feature':
        return '⭐'
    return ''
```

3. Load and use your filter in your template:

```django
{% load my_filters %}
<span>{{ item.section|highlight_feature }}</span>
```

### Example: Adding a Custom Variable to the Template

If you add a variable in `get_context_data`, you can use it in your template:

```django
<div>{{ my_extra_var }}</div>
```
