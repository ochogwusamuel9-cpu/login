from django.contrib import admin
from django.urls import include, path
from matcher import views as matcher_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/register/", matcher_views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("matcher.urls")),
]