from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('election.urls')),
    url(r'^api/v1/', include('user.urls')),
    url(r'auth/token/', obtain_auth_token)
]
