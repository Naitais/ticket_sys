from django.contrib import admin
from django.urls import path, include
from explorer.views import query


urlpatterns = [
    path('api/', include('tickets.urls')),
    path('api-auth/', include ('rest_framework.urls')),
    path('admin/', admin.site.urls),
    #path('explorer/', query, name='explorer'),
    path('explorer/', include('explorer.urls')),
    
]