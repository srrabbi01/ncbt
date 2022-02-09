from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_view,name='home'),
    path('aboutus/',views.about_us_view,name='aboutus'),
    path('course/',views.course_view,name='course'),
    path('notice/',views.notice_view,name='notice'),
    path('contactus/',views.contact_us_view,name='contactus'),
]