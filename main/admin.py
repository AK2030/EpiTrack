from django.contrib import admin
from .models import *
# Register your models here.
# Username = admin; Email = mishty.dhekial@gmail.com; Password = Python123


class TutorialAdmin(admin.ModelAdmin):

	fieldsets = [
	("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
	("Content", {"fields": ["tutorial_content"]})
	]


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Disease)