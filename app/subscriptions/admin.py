from django.contrib import admin

from app.subscriptions.models import LetterStatus, Mailing, MailTemplate


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sending_time', 'recipients_num', 'is_completed']
    list_display_links = list_display[:2]
    list_filter = ['is_completed']
    readonly_fields = ['sending_time']
    search_fields = ['name']
    raw_id_fields = ['template']

    def recipients_num(self, obj):
        return obj.users.count()


@admin.register(MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    list_display_links = list_display


@admin.register(LetterStatus)
class LettersStatusAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'has_been_read', 'reading_time']
    list_display_links = list_display[:2]
    list_filter = ['has_been_read']
    readonly_fields = ['reading_time', 'has_been_read', 'mailing', 'user']

    def has_add_permission(self, request):
        return False
