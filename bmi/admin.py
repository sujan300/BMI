from django.contrib import admin
from . models import BMIMODEL,SuggestionModel
# Register your models here.


class BMIAdmin(admin.ModelAdmin):
    list_display = ['id','height','weight','result','status','suggest','user','show','date']
admin.site.register(BMIMODEL,BMIAdmin)



class SuggestionModelAdmin(admin.ModelAdmin):
    list_display = ["id","status_suggestion","suggest_message"]
admin.site.register(SuggestionModel,SuggestionModelAdmin)