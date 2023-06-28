from django.views.generic import ListView,  DetailView # new
from django.views.generic.edit import UpdateView, DeleteView # new
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

class ArticleListView(ListView):
      model = Article
      template_name = 'article_list.html'


class ArticleDetailView(ListView):
      model = Article
      template_name = 'article_detail.html'

class ArticleUpdateView(ListView):
      model = Article 
      fields = ('title', 'body',)
      template_name = 'article_edit.html'
      
class ArticleDeleteView(ListView):
      model = Article 
      template_name = 'article_delete.html'
      success_url = reverse_lazy('article_list')            