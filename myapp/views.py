from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from datetime import datetime
from django.db.models import Q

#GET /city/ — получение всех городов из базы;
class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
# GET /city//street/ — получение всех улиц города;
class StreetListView(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.filter(city_id=city_id)

class ShopListView(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    # POST /shop/ — создание магазина
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'id': serializer.instance.id}, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            return Response({'ValidationError': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Exception': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #GET /shop/?street=&city=&open=0/1
    def get_queryset(self):
        try:
            city = self.request.GET.get('city')
            street = self.request.GET.get('street')
            open = self.request.GET.get('open')
            shops = Shop.objects.all()
            if not (street or city or open):
                return Shop.objects.all()
            if street:
                shops = shops.filter(street_id=street)
            if city:
                shops = shops.filter(city_id=city)
            if open:
                open = int(open)
                time = datetime.now().time()
                if open == 0:
                    shops = shops.filter(~(Q(open_time__lt=time) & Q(close_time__gte=time)))
                if open == 1:
                    shops = shops.filter(Q(open_time__lt=time) & Q(close_time__gte=time))
            return shops
        except Exception as e:
            return ValidationError({'Exception': str(e)})