from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import scan_item

urlpatterns = [




    path('api/scan-item/', scan_item, name='scan-item'),
    path('', views.home, name = "dash"),
    path('commerce/', views.commerce, name = "commerce"),
    path('applied/', views.applied, name = "applied"),
    path('applied/', views.applied, name = "applied"),
    path('medicine/', views.medicine, name = "medicine"),
    path('sports/', views.sports, name = "sports"),
    path('built/', views.built, name = "built"),
    path('science/', views.science, name = "science"),
    path('applied4/', views.applied4, name = "applied4"),
    path('applied2/', views.applied2, name = "applied2"),
    path('applied2/', views.applied2, name = "applied2"),
    path('SCS1101/', views.SCS1101, name = "SCS1101"),
    path('SCS1102/', views.SCS1102, name = "SCS1102"),
    path('SCS1104/', views.SCS1104, name = "SCS1104"),
    path('SCS1203/', views.SCS1203, name = "SCS1203"),
    path('SCS2101/', views.SCS2101, name = "SCS2101"),
    path('SCS2102/', views.SCS2102, name = "SCS2102"),
    path('SCS2104/', views.SCS2104, name = "SCS2104"),
    path('SCS2203/', views.SCS2203, name = "SCS2203"),
    path('SCS4101/', views.SCS4101, name = "SCS4101"),
    path('SCS4102/', views.SCS4102, name = "SCS4102"),
    path('SCS4104/', views.SCS4104, name = "SCS4104"),
    path('SCS4203/', views.SCS4203, name = "SCS4203"),
    path('QR/', views.QR, name = "QR"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
