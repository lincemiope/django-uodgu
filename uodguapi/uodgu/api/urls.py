from django.urls import path
from uodgu.api.views import SopListCreateAPIView #, MemberListCreateAPIView, GuildListCreateAPIView

urlpatterns = [
    path('soplist/', SopListCreateAPIView.as_view(), name='sop-list'),
    # path('members/', MemberListCreateAPIView.as_view(), name='member-list'),
    # path('guilds/', GuildListCreateAPIView.as_view(), name='guild-list')
    # path('soplist/<int:pk>/', sop_list_view, name='sop-list')
]
