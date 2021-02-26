from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import \
    TokenObtainPairView, TokenRefreshView

from backend.schema import schema_view


auth = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]

endpoints = [
    # auth
    path('auth/jwt/', include(auth)),

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
