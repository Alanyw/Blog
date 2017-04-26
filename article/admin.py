from django.contrib import admin
from .models import Article, Mailbox



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'pub_date')
    list_filter = ['tag','pub_date']
    search_fields = ['tag','title']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Mailbox)