from django.contrib import admin
from .models import BuildOrder, Comment

class BuildOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'buildorder', 'matchup')


admin.site.register(BuildOrder, BuildOrderAdmin)
admin.site.register(Comment)

