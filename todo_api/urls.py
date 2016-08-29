from django.conf.urls import url
from django.contrib import admin

from todo_api.todo import views

urlpatterns = [

    # Todos endpoint
    url(r'^todos/$', views.TodosView.as_view()),
    url(r'^todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view()),

    url(r'^admin/', admin.site.urls),
]
