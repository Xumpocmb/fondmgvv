from django.urls import path
from app_home.views import index, get_document

app_name = 'app_home'

urlpatterns = [
    path('', index, name='home'),
    path('document/', get_document, name='document'),

]