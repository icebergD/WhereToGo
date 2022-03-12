from django.contrib import admin
from .models import *

admin.site.register(Organization)
admin.site.register(Like)
admin.site.register(OrganizationHashtag)
admin.site.register(UserHashtag)
