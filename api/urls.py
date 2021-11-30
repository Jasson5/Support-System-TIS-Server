from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

from api import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('api-auth/', views.CustomAuthToken.as_view()),
    url(r'^person/$', views.PersonApi),
    url(r'^person/([0-9]+)$', views.PersonApi),

    url(r'^company/$', views.CompanyApi),
    url(r'^company/([0-9]+)$', views.CompanyApi),

    url(r'^role/$', views.RoleApi),
    url(r'^role/([0-9]+)$', views.RoleApi),

    url(r'^semester/$', views.SemesterApi),
    url(r'^semester/([0-9]+)$', views.SemesterApi),

    url(r'^announcement/$', views.AnnouncementApi),
    url(r'^announcement/([0-9]+)$', views.AnnouncementApi),

    url(r'^offer/$', views.OfferApi),
    url(r'^offer/([0-9]+)$', views.OfferApi),  

    url(r'^homework/$', views.HomeworkApi),
    url(r'^homework/([0-9]+)$', views.HomeworkApi),

    url(r'^attendance/$', views.AttendanceApi),
    url(r'^attendance/([0-9]+)$', views.AttendanceApi),  

    url(r'^calendar/$', views.CalendarApi),
    url(r'^calendar/([0-9]+)$', views.CalendarApi),    

    #path('login', views.login, name="login"),
    #path('registro', views.register, name="registro"),
]

urlpatterns = format_suffix_patterns(urlpatterns)