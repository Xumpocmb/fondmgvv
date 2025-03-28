from django.urls import path
from app_home.views import index, get_document, send_question_email, custom_404_view

app_name = 'app_home'

urlpatterns = [
    path('', index, name='home'),
    path('document/', get_document, name='document'),
    path('send_question_email/', send_question_email, name='send_question_email'),
    path('404/', custom_404_view, name='404'),
]