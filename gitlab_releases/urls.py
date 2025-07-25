from django.urls import path

from gitlab_releases import views

app_name = "gitlab_releases"

urlpatterns = [
    path("", views.ReleaseListView.as_view(), name="release_list"),
]
