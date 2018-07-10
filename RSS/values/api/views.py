from django.db.models import Q
from rest_framework import generics, mixins
from values.models import Currency
from .serializers import CurrencySerializer


class CurrencyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'     # slug, id # (r'?P<pk>\d+) #
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CurrencyRudView(generics.RetrieveAPIView):
    lookup_field = 'pk'     # slug, id # (r'?P<pk>\d+) #
    serializer_class = CurrencySerializer

    queryset = Currency.objects.all()

