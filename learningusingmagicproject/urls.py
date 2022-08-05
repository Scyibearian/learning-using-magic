"""learningusingmagicproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from learningusingmagicapp import views

from learningusingmagicapp.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), 
        name='home'),

    path('glossary/', GlossaryView.as_view(),
        name="glossary" ),
    path('about/', views.about_view,
        name='about'),
    #path('articles', ArticleView.as_view(), name="articles"),
    path('article/ikoria_article', views.ikoria_article_view,
        name='ikoria_article')

]

urlpatterns += staticfiles_urlpatterns()