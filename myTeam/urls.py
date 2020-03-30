"""myTeam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views import static
from accounts.views import index, jasmine
from accounts import urls as accounts_urls
from profile_and_stats import urls as profile_urls
from groups import urls as group_urls
from matches import urls as match_urls
from team_gen import urls as team_urls
from subscriptions import urls as subscription_urls
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/', include(accounts_urls)),
    path('profile/', include(profile_urls)),
    path('group/', include(group_urls)),
    path('match/', include(match_urls)),
    path('team/', include(team_urls)),
    path('checkout/', include(subscription_urls)),
    path('media/<str:path>', static.serve, {'document_root': MEDIA_ROOT}),
    path('jasmine/', jasmine, name="jasmine"),
]
