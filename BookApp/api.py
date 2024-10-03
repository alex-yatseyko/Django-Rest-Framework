from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel
from .serializers import BookSerializer

@api_view(['GET'])
def BookListApi(request):
    # fetch from db
    books = BookModel.objects.all()

    books = [{
        'id': book.id,
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

@api_view(["PUT"])
#def BookUpdateApi(request, id):
#    data = request.data

#    book = BookModel.objects.get(id = id)

#    book.name = data.get('name')
#    book.author = data.get('author')
#    book.pages = data.get('pages')

#    book.save()

#    return Response({
#        'message': 'Book updated',
#        'book': book
#    })
def BookUpdateApi(request, id):
    try:
        book = BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    data = request.data

    book.name = data.get('name')
    book.author = data.get('author')
    book.pages = data.get('pages')

    book.save()

    # Serialize the updated book object
    serializer = BookSerializer(book)

    return Response({
        'message': 'Book updated',
        'book': serializer.data
    })

@api_view(["DELETE"])
def BookDeleteApi(request, id):
    book = BookModel.objects.get(id = id)

    book.delete()

    return Response({
        "message": "Book deleted"
    })