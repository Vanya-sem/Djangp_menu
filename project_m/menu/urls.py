from django.urls import path
from menu.views import draw_menu, index


urlpatterns = [
    path('<str:menu_url>/', draw_menu, name='draw_menu'),
    path('', index, name='home')
]