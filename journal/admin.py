from django.contrib import admin
from journal.models import Income, Period, Expense, Saving, Investment


admin.site.register(Income)
admin.site.register(Period)
admin.site.register(Expense)
admin.site.register(Saving)
admin.site.register(Investment)
