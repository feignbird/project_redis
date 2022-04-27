from django.contrib import admin
from redis_app.models import TableA, TableB, TableC, TableD, TableE
# Register your models here.

admin.site.register(TableA)
admin.site.register(TableB)
admin.site.register(TableC)
admin.site.register(TableD)
admin.site.register(TableE)
