from django.urls import path
from app.views import qush, ayir, kupaytir, bul

urlpatterns = [
    path('', qush),
    path('ayirish/', ayir),
    path('ko\'paytirish/', kupaytir),
    path('bo\'lish/', bul)
]
