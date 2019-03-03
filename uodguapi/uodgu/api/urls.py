from django.urls import path
from uodgu.api.views import SopListCreateAPIView

urlpatterns = [
    path('soplist', SopListCreateAPIView.as_view(), name='sop-list')
    # path('soplist/<int:pk>/', sop_list_view, name='sop-list')
]
