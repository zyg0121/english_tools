from django.contrib import admin
from .models import Word
from .models import Sentence
from .models import Translation
from .models import Instance


# Register your models here.

class InstanceInline(admin.StackedInline):
    model = Instance


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'levels')
    search_fields = ['word']
    ordering = ('word',)
    list_filter = ('levels',)
    # inlines = [InstanceInline, ]


class SentenceAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'translation')
    search_fields = ['sentence']
    ordering = ('sentence',)

class TranslationAdmin(admin.ModelAdmin):
    list_display = ("translation",'property')
    search_fields = ['translation']



admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Translation,TranslationAdmin)

admin.site.site_title = "英语学习助手系统后台"
admin.site.site_header = "英语学习助手管理系统"
admin.site.index_title = "后台主页"
