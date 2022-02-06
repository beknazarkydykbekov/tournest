from django.urls import path
from tours_kg.views import BookRightNow, Success, savecomment, BaseView, joinus

urlpatterns = [
    path('book-now/', BookRightNow, name='book_now'),
    path('book-now/success/', Success, name='book-now-success'),
    path('', BaseView.as_view(), name='base'),
    path('comment/', savecomment, name='save'),
    path('join-us/', joinus, name='join-us')
    ]