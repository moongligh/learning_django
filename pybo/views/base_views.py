from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

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

# 질문 상세보기함수
def detail(request, question_id):
    '''
    Pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)