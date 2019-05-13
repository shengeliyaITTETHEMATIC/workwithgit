from django.conf.urls import url

from . import views

urlpatterns = [
    url('delete_statements', views.delete_statements, name='delete'),
    url('delete_statement', views.delete_statement, name='delete'),
    url('add_statements', views.change_statement, name='check'),
    url('add_statement', views.add_statement, name='add'),
    url('check_statement', views.check_statement, name='check'),
    url('statement', views.check_statement, name='check'),
    url('check_login', views.check_login, name='log'),
    url(r'^$', views.login, name='change'),
]