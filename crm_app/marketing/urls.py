from django.conf.urls import patterns, include, url
from views import HomePage


urlpatterns = patterns("",

    # Marketing page
   url(r"^$", HomePage.as_view(), name="home"))


