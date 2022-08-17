from django.shortcuts import render

from django.views.generic.list import ListView
#from django.views.generic.base import TemplateView

from .models import Word
# Create your views here.
import random

#def home_view(request):
#    return render(request, 'home.html')

class HomeView(ListView):
    template_name = 'home.html'
    model = Word

    #words = list(Word.objects.all())
    # words = Word.objects.order_by('eng_trans')

    # try:
    #     #queryset = random.sample(words, 12)
    #     #print(queryset)
    #     print('try')
    # except ValueError:
    #     print('Sample size exceeded population size.')
    #     queryset = Word.objects.order_by('eng_trans')

    def get_queryset(self):
        object_list = self.model.objects.order_by('?')[:12]
        return object_list


#Glossary views
class GlossaryView(ListView):
    print("myguy1")
    #model = Lot
    queryset = Word.objects.order_by('eng_trans')
    template_name = 'glossary/glossary.html'
    
def about_view(request):
    print("myguy2")
    return render(request, 'about.html')

def ikoria_article_view(request):
    print("myguy3")
    return render(request, 'article/ikoriareich.html')
