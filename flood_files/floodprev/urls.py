from django.conf.urls import url
#from . import views
from floodprev import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='floodprev'

urlpatterns = [
    #its going in the views file and checking the machine fn
    #its in templateview file and checking the as_view fn
    url(r'^$',TemplateView.as_view(template_name="mainpage1/index.html"),name='index'),
    #url(r'^predict$',views.Machine,name='machine'),
    url(r'^predict$',views.predict1,name='machine'),
    url(r'^stuck$',views.Stuck,name='stuck'),
    url(r'^stuck/rescue$',views.What2,name='what2'),
    url(r'^predict/whattodo$',views.What1,name='what1'),
    url(r'^entry$',views.Entry,name='entry'),
    url(r'^entry/update$',views.Entry1,name='entry1')

]

urlpatterns += staticfiles_urlpatterns()




#54a37d