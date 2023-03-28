from rest_framework import serializers

from measurement.models import Measurement, Sensor



class SetMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        #fields = "__all__"
        fields = ['id_sensor','temp', 'date','image']
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temp', 'date', 'image']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']