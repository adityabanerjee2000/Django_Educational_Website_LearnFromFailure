from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "LEARN FROM FAILURE"
admin.site.site_title = ""
admin.site.index_title = "Welcome Aditya's Company Learn From Failure"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
