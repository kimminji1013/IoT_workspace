from django.urls import path
from polls import views

app_name='polls'        #polls 앱의 namespace : 접두어로 사용할꺼임

urlpatterns=[
    # app_name으로 경로 설정되는 것. 현재: polls
    # /polls/
    path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/',views.vote, name='vote'),
]