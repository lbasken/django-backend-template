from django.http import HttpResponse, JsonResponse
from .serializers import AppSerializer
from .models import App


def list_apps(request):
    query_set = App.objects.all()
    serializer = AppSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)
