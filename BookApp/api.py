from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel

@api_view(['GET'])
def BookListApi(request):
    # fetch from db
    books = BookModel.objects.all()

    books = [{
        'name': book.name,
        "author": book.author,
        "pages": book.pages
    } for book in books]

    return Response(books)

@api_view(['POST'])
def BookCreateApi(request):
    data = request.data

    name = data.get('name')
    author = data.get('author')
    pages = data.get('pages')

    BookModel(name=name, author=author, pages=pages).save()

    return Response({
        'message': 'Book is created'
    })