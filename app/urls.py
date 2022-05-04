from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('home/',views.home,name="home"),
    path('',RedirectView.as_view(url="home")),
    path('login/',views.login_view),
    path('register/',views.register),
    path('logout/',views.logout_view),
    path('book/<int:id>/',views.book),
    path('search/',views.search),
    path('bookings/',views.bookings),
    path('bookings/cancel/',views.caneceld_booking),
    path('bookings/cancel/<int:id>/',views.cancel_bookings),
]