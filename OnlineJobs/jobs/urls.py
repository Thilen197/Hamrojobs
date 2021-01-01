from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jobs_url',views.jobs_insert),
    path('educational',views.educational),
    path('delivery',views.delivery),
    path('field',views.field),
    path('homebased',views.homebased),
    path('office',views.office),
    path('others',views.others),
    path('technical',views.technical),
    path('hotel',views.hotel),
    path('jobs',views.jobs_insert),
    path('showjobs',views.showjobs),
    path('jobs/delete/<id>',views.delete_jobs),
    path('jobdetail/<id>',views.jobdetail),
   # path('jobs/jobs_update/<id>',views.update_jobs),
    path('user_signup', views.user_signup),
    path('user_login',views.user_login),
    path('logout',views.logout1)
]