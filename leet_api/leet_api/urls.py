from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# yourapp/urls.yy
from django.urls import path
from .views import leetcode_data

urlpatterns = [
    path('getUserData/<str:username>/', leetcode_data, name='leetcode_data'),
]
