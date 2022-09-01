from django.shortcuts import render

from django.views.generic.list import ListView
#from django.views.generic.base import TemplateView

from .models import Word

from django.db.models import Q
from django.db.models.functions import Lower
# Create your views here.
import random

class HomeView(ListView):
    template_name = 'home.html'
    model = Word


    def get_queryset(self):
        object_list = list(self.model.objects.all())
        random.shuffle(object_list)
        object_list = object_list[0:12] #cut everything but first 12 for efficiency
        return object_list


#Glossary views
class GlossaryView(ListView):
    model = Word
    queryset = Word.objects.order_by(Lower('eng_trans'))
    template_name = 'glossary/glossary.html'

    # def get_queryset(self):
    #     object_list = self.model.objects.order_by('eng_trans') #Order alphabetically
    #     search = self.kwargs.get('q') #get keyword argument contatining search query
    #     #progress_filter = self.kwargs.get('progress_filter')
    #     if search: #checking if user search in any attributes of customer
    #         object_list = object_list.filter(
    #             Q(eng_trans__icontains=search) |
    #             Q(magic_def__icontains=search) |
    #             Q(german_trans__icontains=search)).distinct()
    #     return object_list
    
def about_view(request):
    return render(request, 'about.html')

def ikoria_article_view(request):
    return render(request, 'article/ikoriareich.html')

def google_verif_view(request):
    return render(request, 'google3ceb8259d9407416.html')
