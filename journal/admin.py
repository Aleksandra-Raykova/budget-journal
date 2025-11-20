from django.contrib import admin
from journal.models import Income

class IncomeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Income, IncomeAdmin)
