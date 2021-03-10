from django.contrib import admin
from django.urls import path, include

from backend.schema import schema_view


endpoints = [
    # schema
    path('schema.json', schema_view),

    # apps API URLs
    path('core/', include('core.urls')),
    path('dosimetria/', include('dosimetria.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(endpoints)),
]
