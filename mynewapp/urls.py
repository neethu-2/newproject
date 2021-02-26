from django.urls import path
from .import views 


app_name='mynewapp'
urlpatterns = [
	path('', views.index, name='index'),
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_home/<int:id>/', views.user_home, name='user_home'),
    path('show/<int:id>/', views.show, name='show'),
    # path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('changepassword/<int:id>/',views.changepassword, name='changepassword'),
    path('logout/', views.logout, name='logout'),
    path('image/', views.image, name='image'),
    path('imageshow/', views.imageshow, name='imageshow'),
    path('about/<int:pk>/', views.about, name='about'),
    # path(r'^.*/$', views.View_404, name='View_404')
    
    
    

  
    ]
