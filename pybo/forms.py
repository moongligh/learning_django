from django import forms  # 장고의 기본 폼형식
from pybo.models import Question
# 모델 폼, 연결된 모델의 데이터를 저장할 수 있게된다. Class Meta라는 내부클래스가 필수이다.


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

    widgets = {
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
    }
    labels = {
        'subject': '제목',
        'content': '내용',
    }
