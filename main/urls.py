from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path("", books, name='all_books'),
    path("book_detail/<int:id>/", book_detail, name='book_detail'),
    path("add_book/", add_book, name='addb'),
    path("book_detail/<int:id>/update_book/", update_book, name='update_book'),
    path("add_author/", add_author, name='adda'),
    path("add_publisher/", add_publisher, name='addp'),
    path('login/', login_view, name='login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
