from django.contrib import admin

# Register your models here.
from index.models import Index,Contacts

admin.site.register(Index)
admin.site.register(Contacts)

class IndexAdmin(admin.ModelAdmin):
    pass
class ContactsAdmin(admin.ModelAdmin):
    pass
