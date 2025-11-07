from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="ALX Travel App API",
      default_version='v1',
      description="API documentation for the ALX Travel App project. Milestone 1.",
      contact=openapi.Contact(email="contact@alxtravel.app"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
# --- End of Configuration ---


urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Swagger URL Paths ---
    # This is the line required by the project
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # (Optional) Another style of documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # (Future) This is where your app's URLs will go
    # path('api/v1/listings/', include('listings.urls')),
]
