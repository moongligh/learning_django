from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer

# 질문글 추천 함수
@login_required(login_url='common:login')
def vote_question(request, question_id):
    '''
    Pybo 질문추천등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

# 답글 추천 함수
@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    '''
    Pybo 답글 추천등록
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)