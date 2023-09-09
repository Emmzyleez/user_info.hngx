
from .views import user_info_view
from django.urls import path

urlpatterns = [
    path('', user_info_view, name='user_info')
]