from django.conf.urls import url

from .views import CreateTestView, CreateTestCaseView, ShowResultView

urlpatterns = [
     url(r'result/(?P<id>\d+)', ShowResultView.as_view(), name='show_result'),
     url(r'(?P<id>\d+)', CreateTestCaseView.as_view(), name='create_test_case'),
     url(r'create_test', CreateTestView.as_view(), name='create_test'),

    ]
