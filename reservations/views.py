from django.shortcuts import render
from rest_framework import viewsets
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer

def reservation_gallery(request):
    context = {}
    return render(request, 'reservations/index.html', context)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    paginate_by = 10
    paginate_by_param = 'page_size'
