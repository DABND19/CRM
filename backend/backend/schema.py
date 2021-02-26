from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Alians-Rem CRM API',
                              renderer_classes=[JSONOpenAPIRenderer],
                              permission_classes=[IsAdminUser])
