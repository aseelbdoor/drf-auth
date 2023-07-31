from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import Snack
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
from .permissions import OwnerOnly

class SnackListView(ListAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer

class SnackCreateView(CreateAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer
    permission_classes = [OwnerOnly]