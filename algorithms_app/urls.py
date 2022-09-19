from django.urls import path
from .views import sha_view

urlpatterns = [
    path('', sha_view, name='sha_url')

]