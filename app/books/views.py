from rest_framework import viewsets

from app.books.models import Book

from .serializes import BookSerializer


class BookAPIView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    model = Book

    def get_queryset(self):
        return self.model.objects.filter(deleted_at=None)
