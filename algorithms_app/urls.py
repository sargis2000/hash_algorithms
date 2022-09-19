from django.urls import path
from .views import *

urlpatterns = [
    path('', sha_view, name='sha_url')

]