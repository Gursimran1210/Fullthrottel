from django.urls import path
from . import views
urlpatterns = [

    path("",views.index,name='shophome'),
    path("about/",views.about,name='aboutus'),
    path("contact/",views.contact,name='contactus'),
    path("tracker/",views.tracker,name='trackingstatus'),
    path("search/",views.search,name='search'),
    path("productview/",views.productview,name='productview'),
    path("checkout/",views.checkout,name='checkout'),
    path("new/",views.new,name='new'),

]