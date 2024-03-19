from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('ticketera/', views.TicketList.as_view(), name='ticket-lista'),
    path('ticketera/<int:pk>/', views.TicketDetalle.as_view(),name='ticket-detail'),
    path('ticketera/<int:pk>/highlight/', views.TicketHighlight.as_view(),name='ticket-highlight'),
    ])