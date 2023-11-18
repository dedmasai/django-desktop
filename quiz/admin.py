from django.contrib import admin


from .models import Task,  AnswerQuiz


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = "pk", "varNumber", "number", "text", "answer"

@admin.register(AnswerQuiz)
class VariantAdmin(admin.ModelAdmin):
    list_display = "taskN", "userN", "numbInV", "uAnswer"


