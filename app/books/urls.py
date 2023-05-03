from django.urls import path

from .views import BookAPIView


app_name = 'books'

urlpatterns = [
    path('', BookAPIView.as_view({'get': 'list', 'post': 'create'}), name='list_create'),
    path('<int:pk>/', BookAPIView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='retirve_delete_update'),
]
