from django.contrib import admin
from .models import Article, ArticleTags, Tags
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError



class RelationshipInlineForm(BaseInlineFormSet):
    def clean(self):
        is_main = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data:
                print(form.cleaned_data['is_main'])
                if form.cleaned_data['is_main']==True:
                    is_main += True
        if is_main == 1:
            return super().clean()
        elif is_main == 0:
            raise ValidationError('Укажите основной раздел')
        else:
            raise ValidationError('Основным может быть только один раздел')

class RelationshipInline(admin.TabularInline):
    model = ArticleTags
    formset = RelationshipInlineForm
    extra = 1

@admin.register(Article)
class ArticlAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleTags)
class ArticleTagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag', 'is_main']
