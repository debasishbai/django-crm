from django.conf.urls import url
import views


urlpattern = [url(r"^signup/$", views.subscriber_new, name="sub_new"),
              ]