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

    words = list(Word.objects.all())

    try:
        queryset = random.sample(words, 12)
        print(queryset)
    except ValueError:
        print('Sample size exceeded population size.')
        queryset = Word.objects.order_by('eng_trans')




    # num_words = Word.objects.count()
    # try:
    #     random.sample(range(1, num_words), 5)

    # except ValueError:
    #     print('Sample size exceeded population size.')

    # queryset = Word.objects.order_by('eng_trans')

        # def get_queryset(self):
        #     object_list = Word.objects.order_by('-id') #Order by most recent first
        #     #for object in object_list:
        #         #object.time += timedelta(hours=1)
        #         #object.time = timezone.localtime(object.time) #localtime() cannot be applied to a naive datetime
        #     return object_list

#Glossary views
class GlossaryView(ListView):
    #model = Lot
    queryset = Word.objects.order_by('eng_trans')
    template_name = 'glossary/glossary.html'
    
def about_view(request):
    return render(request, 'about.html')

def ikoria_article_view(request):
    return render(request, 'article/ikoriareich.html')
