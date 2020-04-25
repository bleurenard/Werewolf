from django.conf.urls import url

from whokillsit import views

urlpatterns = [
    url('^home/', views.home, name='home'),
    url('^tutor/$', views.tutors, name='tutors'),
    url('^tutor/(\d+)/', views.tutor, name='tutor'),
    url('^strategy/$', views.strategies, name='strategies'),
    url('^add_strategy/', views.add_strategy, name='add_strategy'),
    url('strategy/(\d+)/', views.strategy, name='strategy'),
    url('^ranking/', views.ranking, name='ranking'),
    url('^about/', views.about, name='about'),
    url('^login/', views.login, name='login'),
    url('^mine/', views.mine, name='mine'),
    url('^register/', views.register, name='register')
]
