from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Word
# Create your views here.

def index(request):
    return render(request, 'base.html')

#Glossary views
class GlossaryView(ListView):
    #model = Lot
    queryset = Word.objects.order_by('eng_trans')
    template_name = 'glossary/glossary.html'
    
