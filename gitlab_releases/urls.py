from django.urls import path

from gitlab_releases import views

app_name = "gitlab_releases"

urlpatterns = [
    path("releases/", views.ReleaseListView.as_view(), name="release_list"),
    path(
        "releases/<str:tag_name>/changelog/<int:merge_request_id>",
        views.ChangelogDetailView.as_view(),
        name="changelog_detail",
    ),
]
