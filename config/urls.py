"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pybo.views import base_views, question_views, answer_views, comment_views

# --- [추가 import 부분 ] --- #
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- [들어온 URL요청을 각 앱.urls로 맵핑하기] --- #
    path('pybo/', include('pybo.urls')),
    path('common/',include('common.urls')),
    path('', base_views.index, name='index'),
]
