from django.urls import path
from . import views
urlpatterns = [
    path('',views.userLogin),
    path('logout/',views.userLogout),
    path('register/',views.register),
    path('searching/',views.search),
    path('search/',views.searchBook),
    path('delete/',views.deleteBook),
    path('edit/', views.editBook),
    path('update/',views.edit),
    path('insert/', views.insertBook),
    path('save/', views.insert),
    path('views-books/', views.viewBooks)
]
