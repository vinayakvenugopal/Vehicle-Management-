from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register,name='register'),
    path('superadmin/',views.superadmin,name='superadmin'),
    path('superadmin/add',views.superadmin_add,name='superadmin_add'),
    path('superadmin/update/<int:veh_id>',views.superadmin_update,name='superadmin_update'),
    path('superadmin/delete',views.superadmin_delete,name='superadmin_delete'),
    path('superadmin/delete/<int:veh_id>',views.superadmin_delete,name='superadmin_delete'),
    path('admin/', views.admin, name='admin'),
    path('user/', views.user, name='user'),

]