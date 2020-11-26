from django.urls import path
from .views import Create, bookwalker, kobo

urlpatterns = [
   path('', Create.as_view(), name='home'),
   path('bookwalker/', bookwalker, name='ebbw'),
   path('kobo/', kobo, name='ebkb'),
]