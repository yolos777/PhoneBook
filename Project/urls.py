from django.contrib import admin
from django.urls import path
from Pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookOfContacts.as_view(), name = 'home'),
    path('add/', views.NewContact.as_view(), name = 'add'),
    path('delete/<int:pk>', views.DeleteContact.as_view(), name = 'del')
]
