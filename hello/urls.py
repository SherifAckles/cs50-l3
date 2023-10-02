from django.urls import path
from . import views
#define a var as a list representing all urls can be accessed with this app

urlpatterns=[
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("sherif",views.sherif,name="sherif"),
    path("david",views.david, name="david"),
]