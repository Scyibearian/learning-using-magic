from django.db import models
from django.urls import reverse

# Create your models here.

class Word(models.Model):
    eng_trans = models.CharField(max_length=254)
    magic_def = models.CharField(max_length=254)
    example_card_1 = models.CharField(max_length=254, blank=True, null=True)
    example_card_2 = models.CharField(max_length=254, blank=True, null=True)
    german_trans = models.CharField(max_length=254, blank=True, null=True)
    japanese_trans = models.CharField(max_length=254, blank=True, null=True)
    furigana = models.CharField(max_length=254, blank=True, null=True)
    romaji = models.CharField(max_length=254, blank=True, null=True)
    french_trans = models.CharField(max_length=254, blank=True, null=True)
    lit_trans_list = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.eng_trans

    # def get_absolute_url(self):
    #     return reverse("word", kwargs={"pk": self.pk})  

    def class_name(self):
        return self.__class__.__name__


