from django.contrib import admin
from news.models import news_model
from django.contrib.sites.models import Site


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_time', 'status', 'author', 'category']
    list_editable = ['status', 'author', 'category']
    fields = ('title', 'pub_time', 'status', 'author', 'category', 'article')
    change_form_template = 'news/change_form.html'

admin.site.register(news_model, NewsAdmin)
admin.site.unregister(Site)
