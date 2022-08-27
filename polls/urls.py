from django.urls import path
from . import views

app_name = 'polls'  # URL命名空间

urlpatterns = [
    # /polls/
    path('',views.index,name='index'),
    # /polls/5   # 假设question_id为5
    path('specifics/<int:question_id>/',views.detail,name='detail'),
    # /polls/5/results
    path('specifics/<int:question_id>/results',views.results,name='results'),
    # /polls/5/results/vote
    path('specifics/<int:question_id>/vote',views.vote,name='vote'),
]