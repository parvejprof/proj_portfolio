from django.urls import path
from . import views

urlpatterns = [
    path("", views.control_panel_index, name="control_panel_index"),
    #path('import/', views.control_panel_import, name="import"), 
    path('import2/', views.simple_upload, name="import2"), 
    path('import3/', views.model_form_upload, name="import3"), 
    path('import4/', views.import_website, name="import4"), 
]
