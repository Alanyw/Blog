from django.contrib import admin
from .models import Article, Mailbox
from django import forms
from pagedown.widgets import AdminPagedownWidget


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'tag', 'pub_date')
    list_filter = ['tag','pub_date']
    search_fields = ['tag','title']
admin.site.register(Article,ArticleAdmin)
admin.site.register(Mailbox)
