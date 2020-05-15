from django.shortcuts import render

# --- [추가 import 부분] --- #
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import QuestionForm, AnswerForm
from .models import Question


# --- [함수 추가 부분] --- #
def index(request):
    '''
    Pybo 목록 출력
    '''
    # 입력 파라미터 부분
    page = request.GET.get('page', '1')  # GET 방식으로 1페이지를 요청함

    # 질문글 리스트로 조회(생성시간 역순)
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 한 페이지당 10개의 글을 페이징 객체로 변환하기.
    page_obj = paginator.get_page(page)  # paginator로 page 객체 불러오기

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    '''
    Pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    '''
    Pybo 답변 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    '''
    pybo 질문 등록
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
