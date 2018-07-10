from .views import *
from django.urls import path


app_name = 'api-values'

urlpatterns = [
    path('<int:pk>/', CurrencyRudView.as_view(), name='post-rud'),
    path('', CurrencyAPIView.as_view(), name='post-create'),

]