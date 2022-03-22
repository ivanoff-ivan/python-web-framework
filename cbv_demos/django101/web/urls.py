from django.urls import path
from django.views.generic import RedirectView

from django101.web.views import IndexView, TodoListView, TodoCreateView, TodoCreateView

urlpatterns = [
    path('cbv/', IndexView.as_view(), name='home page'),
    path('', TodoListView.as_view(), name='todo'),
    path('create/', TodoCreateView.as_view(), name='create todo'),
]
