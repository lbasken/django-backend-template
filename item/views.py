from django.http import HttpResponse, JsonResponse
from .serializers import ItemSerializer
from .models import Item


def get_all_items(request):
    query_set = Item.objects.all()
    serializer = ItemSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)
