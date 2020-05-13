# --- [ config.urls -> pybo.urls -> pybo.views를 위한 소스 ] --- #
from django.urls import path
from . import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
]
