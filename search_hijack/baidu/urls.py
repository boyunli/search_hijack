from django.urls import path

from baidu.views import SearchResultView

app_name = 'baidu'

urlpatterns = [
    path('', SearchResultView.as_view(), name='baidu_result'),
]
