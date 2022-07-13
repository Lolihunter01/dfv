from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from server.models import Location
from .serializers import LocatoinSerializer


def access(request):
    context = {
        "lat":Location.objects.latest().latitude,
        "lon":Location.objects.latest().lontitude
    }
    print(context['lat'])
    print(context['lon'])
    return render(request, 'home.html', context=context)


@api_view(['POST'])
def update(request):
    serializer = LocatoinSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

