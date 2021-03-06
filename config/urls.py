from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "", TemplateView.as_view(template_name="veritas1/index.html"), name="homepage"
    ),
    path("home/", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('services/', TemplateView.as_view(template_name="veritas1/services.html"), name="services"),
    path('jobs/', include('jobs.urls')),
    path('events/', include('blog.urls')),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
   
    path('resume/', include('applications.urls')),
   

    path('contacts/', include('contactform.urls')),

   
    path('login/', TemplateView.as_view(template_name='veritas1/login.html'), name='login_custom'),

    path('', include('search.urls')),
    # User management
    path("users/", include("veritas.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
