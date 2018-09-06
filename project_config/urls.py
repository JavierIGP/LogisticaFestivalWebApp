"""coreui_boilerplate URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

import logistica.views as logistica

from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', logistica.home, name='home'),

    url(r'^login/', logistica.login_user, name='login_user'),
    url(r'^logout/', logistica.logout_user, name='logout_user'),

    url(r'^actividades/', logistica.activities, name='activities'),
    url(r'^principal/', logistica.principal, name='principal'),
    url(r'^tour/', logistica.tour, name='tour'),

    url(r'^edit_activity_capacity/', logistica.edit_activity_capacity, name='edit_activity_capacity'),

    path('monitor/<str:nombreMonitor>/', logistica.monitor, name='monitor'),

    path('espacio/<str:nombreEspacio>/', logistica.espacio, name='espacio'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
