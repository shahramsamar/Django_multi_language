
from django.urls import path
from website import views


urlpatterns = [
    path('post',views.index,name='index' ),
   

]
