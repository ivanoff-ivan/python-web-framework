from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from django101.web.models import Todo


class IndexView(views.TemplateView):
    template_name = 'index.html'

    # ---------

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['tile'] = 'It works!'
        return context


class RedirectToIndexView(views.RedirectView):
    url = reverse_lazy('home page')


class TodoListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My todos'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)
        return queryset


class CreateTodoForm:
    pass


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    fields = ('title', 'description', 'category')
    success_url = reverse_lazy('home page')
