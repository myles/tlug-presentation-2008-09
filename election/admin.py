from django.contrib import admin

from election.models import *

admin.site.register(District)
admin.site.register(Candidate)
admin.site.register(Party)