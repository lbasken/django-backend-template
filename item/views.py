from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed, Http404
from .serializers import ItemSerializer
import json
from .models import Item


def get_all_items(request):
    query_set = Item.objects.all()
    serializer = ItemSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


def create_new_item(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        new_title = body.get("title")
        new_date = body.get("date")
        new_description = body.get("description")

        new_item = Item(name=new_title, address=new_date, latitude=new_description)
        new_item.save()

        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")


def update_item_by_id(request, item_id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        new_title = body.get("title")
        new_date = body.get("date")
        new_description = body.get("description")
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            raise Http404("Restaurant does not exist")
        item.title = new_title
        item.date = new_date
        item.description = new_description
        item.save()
        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")


def delete_item_by_id(request, item_id):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(pk=item_id)
            item.delete()
            return HttpResponse(status=200)
        except Item.DoesNotExist:
            raise Http404("Restaurant does not exist")
    else:
        raise HttpResponseNotAllowed("Method is not supported")


def get_item_by_id(request, item_id):
    try:
        query_set = Item.objects.filter(pk=item_id)
        serializer = ItemSerializer(query_set.get())
        return JsonResponse(serializer.data, safe=False)
    except Item.DoesNotExist:
        raise Http404("Restaurant does not exist")