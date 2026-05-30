from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="takip/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Evraklar sadece giriş yapan kullanıcıya açılsın
    path("media/<path:path>", login_required(serve), {"document_root": settings.MEDIA_ROOT}),

    path("", include("takip.urls")),
]