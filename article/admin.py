from django.contrib import admin
from .models import article,Comment
# Register your models here.
admin.site.register(Comment)
@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_filter=["created_date","author"]
    search_fields=["title"]
    
    class Meta:
        model = article

