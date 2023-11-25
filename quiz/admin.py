from django.contrib import admin


from .models import Task,  AnswerQuiz


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = "pk", "isSubmitted","varNumber", "number", "text", "answer",

@admin.register(AnswerQuiz)
class VariantAdmin(admin.ModelAdmin):
    list_display = "correct","taskN", "userN", "numbInV", "uAnswer","created_at", "correctAns", "textAns", "taskID", "userID"
    list_display_links = "taskID", "userID"



