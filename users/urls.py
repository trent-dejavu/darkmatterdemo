from django.urls import path, re_path, include
from users.views import dashboard, update_user

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),

    re_path(r"^accounts/update_user", update_user, name='update user')
]