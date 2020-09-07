from django.shortcuts import render
from rest_framework import viewsets
from items.serializers import ItemSerializer
from items.models import Item
from rest_framework.response import Response
from math import radians, cos, sin, asin, sqrt, acos, atan, atan2
# Create your views here.

# class ItemViewset(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

class ItemViewset(viewsets.ViewSet):
    def list(self,request, *args, **kwargs):
        to_be_shown = []
        latitude = radians(float(request.query_params.get('latitude')))
        longitude = radians(float(request.query_params.get('longitude')))
        queryset = Item.objects.all()
        for i in queryset:
            lat1 = radians(i.latitude)
            long1 = radians(i.longitude)
            dlat = latitude - lat1
            dlon = longitude - long1
            # a = sin(dlat / 2)**2 + cos(latitude) * cos(i.latitude) * sin(dlong/ 2)**2
            a = sin(dlat / 2)**2 + cos(latitude) * cos(lat1) * sin(dlon / 2)**2
            c = 2 *atan2(sqrt(a),sqrt(1 - a))
            # c = 2 * asin(sqrt(a))
            distance = c*6371
            # print(c)
            print(distance)
            if distance < 100:
                to_be_shown.append(i)
        serializer = ItemSerializer(to_be_shown, many=True)
        return Response(serializer.data)
    def create(self, request):
        Item_all_obj  = ItemSerializer(data= request.data)
        if Item_all_obj.is_valid():
            new_obj = Item_all_obj.save()
            new_obj_ser = ItemSerializer(new_obj)
            return Response(new_obj_ser.data)
        else:
            return Response(new_obj_ser.errors)