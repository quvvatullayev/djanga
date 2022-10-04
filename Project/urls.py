from django.urls import path
from app.views import sum_num,abaut,Hom,uy,helov

urlpatterns = [
    path('', helov),
    path('abaut/', abaut),
    path('uy/', uy),
    path('hom/', Hom)
]
