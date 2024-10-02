from rest_framework.decorators import api_view
from rest_framework.response import Response

def BookListApi(request):
    # fetch from db
    #books = BookModel.objects.all()

    books = [
        {
            "name": 'Test',
            "author": "Alex"
        }
    ]

    return Response(books)