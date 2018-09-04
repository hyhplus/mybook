from django.contrib import admin
from .models import BookInfo, HeroInfo

# Register your models here.
# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','h_name','gender','h_content']