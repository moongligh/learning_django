# --- [ config.urls -> pybo.urls -> pybo.views를 위한 URL패턴 설정 ] --- #
from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('qusetion/create/', views.question_create, name='question_create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
