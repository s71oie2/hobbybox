from django.views.generic import ListView, DetailView
from hobby.models import Album, Photo

from django.views.generic.edit import FormView
from .forms import SearchForm
from django.db.models import Q                  # 검색 기능에 필요한 클래스
from django.shortcuts import render




class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo
    paginate_by = 2

class SearchFormView(ListView, FormView):
    model = Album
    form_class = SearchForm
    template_name = 'hobby/album_list.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']

        post_list = Photo.objects.filter(
	        Q(title__icontains=schWord) |
	        Q(description__icontains=schWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['schWord'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)