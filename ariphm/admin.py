from django.contrib import admin

from .models import Task, Variant, AnswerQuiz


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    

    list_display = "pk", "name", "description", "answer"
    list_display_links = "pk", "name"

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):

    list_display = "pk", "number", "theme", "created_at"
    list_display_links = "pk", "number"


@admin.register(AnswerQuiz)
class VariantAdmin(admin.ModelAdmin):

    list_display = "pk",   "uAns"
    list_display_links = "pk", "uAns"
