from django.urls import path


from .views import homePageView


app_name = 'todos'


urlpatterns = [
    path('', homePageView, name='home'),
]
