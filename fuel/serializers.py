from rest_framework import serializers


class FuelStationSerializer(serializers.Serializer):
    OPIS_Truckstop_ID = serializers.IntegerField(source="OPIS Truckstop ID")
    Truckstop_Name = serializers.CharField(source="Truckstop Name")
    Address = serializers.CharField()
    City = serializers.CharField()
    State = serializers.CharField()
    Rack_ID = serializers.IntegerField(source="Rack ID")
    Retail_Price = serializers.FloatField(source="Retail Price")