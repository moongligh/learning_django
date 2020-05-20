from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Question, Answer, Comment

# 질문글 댓글 작성하기 함수
@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    '''
    Pybo 질문글의 댓글작성
    '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id = comment.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


# 질문글 댓글 수정하기 함수
@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    '''
    Pybo 질문글의 댓글수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다!')
        return redirect('pybo:detail', question_id = comment.question.id)

    # 댓글작성자인데, 전송방식이 'POST'방식일 경우
    if request.method =='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id=comment.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


# 질문글 댓글 삭제하기 함수
@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    '''
    Pybo 질문글의 댓글삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다!')
        return redirect('pybo:detail', question_id = comment.answer.question.id)
    
    # 댓글 작성자일 경우
    else:
        comment.delete()
    return redirect('pybo:detail', question_id = comment.question.id)


# 답글 댓글 작성하기 함수
@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    '''
    Pybo 답글의 댓글작성
    '''
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id = comment.answer.question.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pybo/comment_form.html', context)


# 답글 댓글 수정하기 함수
@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    '''
    Pybo 답글의 댓글수정
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다!')
        return redirect('pybo:detail', question_id = comment.answer.question.id)

    # 댓글 작성자인데, 전송방식이 'POST'방식일 경우
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('pybo:detail', question_id = comment.answer.question.id), comment.id))
    else:
        form = CommentForm(instance = comment)
    context = {'form':form}
    return render(request, 'pybo/comment_form.html', context)


# 답글 댓글 삭제하기 함수
@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    '''
    Pybo 답글의 댓글삭제
    '''
    comment = get_object_or_404(Comment, pk=comment_id)
    # 댓글 작성자가 아닐경우
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다!')
        return redirect('pybo:detail', question_id = comment.answer.question.id)
    
    # 댓글 작성자일 경우
    else:
        comment.delete()
    return redirect('pybo:detail', question_id = comment.answer.question.id)
