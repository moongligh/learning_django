# --- [import 부분] --- #
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


# --- [함수 추가 부분] --- #

# 리스트 출력함수
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


#질문 작성하기함수
@login_required(login_url='common:login')
def question_create(request):
    '''
    pybo 질문 등록
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


# 질문 상세보기함수
def detail(request, question_id):
    '''
    Pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# 질문 수정하기 함수
@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''
    질문 수정
    '''
    question = get_object_or_404(Question, pk=question_id)
    
    # 작성자가 아닐경우
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다!')
        return redirect('pybo:detail', question_id = question.id)
    
    # 작성자일 경우
    if request.method=='POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id = question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)


# 질문 삭제하기 함수
@login_required(login_url='common:login')
def question_delete(request, question_id):
    '''
    질문 삭제
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다!')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')


# 답변 작성하기함수
@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


# 답변 수정하기 함수
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    '''
    답변 수정
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    
    # 작성자가 아닐경우
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id = answer.question.id)
    
    # 작성자일 경우
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id = answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


# 답변 삭제하기 함수
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    '''
    Pybo 답변삭제
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다!')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)