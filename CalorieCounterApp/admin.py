from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AuthUserModel)
admin.site.register(UserProfileModel)
admin.site.register(DailyConsumedCalorieModel)
admin.site.register(TotalConsumedModel)