"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from TodoListManager import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('sort_by/description/order_by/<str:ord_by>',views.index,name='index_sort_by_description'),
    path('sort_by/created_at/order_by/<str:ord_by>',views.index,name='index_sort_by_created_at'),
    path('add/', views.addToDo, name='add'),
    path('detail/<int:todo_id>', views.detail, name='detail'),
    path('remove/<int:todo_id>', views.remove, name='remove'),
    path('api', include('TodoListManager.urls')),
]

