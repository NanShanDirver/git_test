from django.conf.urls import url, include
from django.contrib import admin
from book.views import bookList

urlpatterns = [

    url(r'^booklist/$', bookList)
]
