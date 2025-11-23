from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# Paths to the BookList view, token authentication and BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('token/', obtain_auth_token, name='api_token_auth'), # Users POST username/password to get a token
]

# Router for BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns += router.urls
