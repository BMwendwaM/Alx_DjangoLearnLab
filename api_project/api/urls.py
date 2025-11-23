from django.urls import path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

# Maps to the BookList view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


# Router for BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = router.urls