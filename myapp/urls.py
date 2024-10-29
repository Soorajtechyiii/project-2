from django.urls import path #type:ignore
from.import views
urlpatterns=[
        path('pagehtml/',views.pagehtml),
        path('getdata/',views.getdata),
        path('save/',views.save),
]