from django.shortcuts import render

# --- [추가 import 부분] --- #
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404


# --- [함수 추가 부분] --- #
def index(request):
    '''
    Pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    '''
    Pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
