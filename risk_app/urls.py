from django.urls import path
from . import views
from risk_app.views import my_view

app_name = 'risk_app'  # Django의 네임스페이스 설정

urlpatterns = [
    path('', views.index, name='index'),
    path('my-dash-app/', my_view),
]