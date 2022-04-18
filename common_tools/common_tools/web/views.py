import random
from time import time

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# @cache_page(1)
from django.views import generic as views

from common_tools.web.models import Profile


def show_index(request):
    Profile.objects.create(
        name='Doncho Minkov',
        email='doncho@minkov.it',
    )

    profiles = Profile.objects.all()

    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 10)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)

    current_page = request.GET.get('page', 1)
    context = {
        'value': random.randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count'),
        'profiles_page': paginator.get_page(current_page)
    }

    return render(request, 'index.html', context)


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles-list.html'
    paginate_by = 3


class IndexView(views.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        start_time = time()
        result = super().dispatch(*args, **kwargs)
        end_time = time()
        print(end_time - start_time)
        return result
