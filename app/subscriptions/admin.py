from django.contrib import admin
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE

from app.subscriptions.models import LettersStatus, Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sending_time', 'recipients_num']
    list_display_links = list_display[:2]
    readonly_fields = ['sending_time']
    search_fields = ['name']

    formfield_overrides = {
        tinymce_models.HTMLField: {
            'widget': TinyMCE(attrs={'cols': 100, 'rows': 30})
        },
    }

    def recipients_num(self, obj):
        return obj.users.count()


@admin.register(LettersStatus)
class LettersStatusAdmin(admin.ModelAdmin):
    pass
