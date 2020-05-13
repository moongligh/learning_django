from django.contrib import admin

# --- [추가 import 부분] --- #
from .models import Question, Answer
admin.site.register(Question)
admin.site.register(Answer)
