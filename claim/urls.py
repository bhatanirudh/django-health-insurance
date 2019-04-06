from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='claim-home'),
    path('about/', views.about , name='claim-about'), 
    path('account/',views.account,name='claim-account'),
    path('result/',views.result,name='claim-result'),
    path('failInvoice/',views.invoiceReq,name='claim-invoice'),
    path('failDocument/',views.document,name='claim-document'),
    path('success/',views.success,name='claim-success'),

]
