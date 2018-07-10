from rest_framework import serializers
from values.models import Currency


class CurrencySerializer(serializers.ModelSerializer):  # forms.ModelForm
    class Meta:
        model = Currency
        fields = [
            'date',
            'USD',
            'JPY',
            'BGN',
            'CZK',
        ]


    # converts to JSON
    # validations for data passed
    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)
