"""uchet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import UserLoginRegistration, UserLogout, Search, Home, ShowItems, AddItem, CardItem


urlpatterns = [
    path('login', UserLoginRegistration.as_view(), name='login'),
    path('logout', UserLogout.as_view(), name='logout'),
    path('home', Home.as_view(), name='home'),
    path('search', Search.as_view(), name='search'),
    path('show_<str:items>', ShowItems.as_view(), name='show_items'),
    path('add_<str:item>', AddItem.as_view(), name='add_item'),
    path('card_<str:item>_<str:id>', CardItem.as_view(), name='card_item'),
]
