from rest_framework import generics

from .models import Dish
from .serializers import DishSerializer

# Create your views here.


class DishListAPIView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
