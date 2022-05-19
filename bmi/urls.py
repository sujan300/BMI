from django.urls import path
from . import views

urlpatterns = [
    path('',views.bmi_view,name="bmi"),
    path('save-data/',views.save_data_view,name="save"),
    path('saved-data-show/',views.show_saved_data,name="show-data"),
    path("delete-bmi/<int:id>/",views.delete_bmi_view,name="bmi-delete"),
    path('send-bmi-email/<int:id>/',views.send_bmi_mail,name="send-bmi-email")
]