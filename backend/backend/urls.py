from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

from backend.schema import schema_view


endpoints = [
    path('schema.json', schema_view),
    path('auth/', obtain_auth_token),

    # apps API URLs
    path('core/', include('core.urls')),
    path('dosimetria/', include('dosimetria.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(endpoints)),
]
