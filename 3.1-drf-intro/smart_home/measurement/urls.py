from django.urls import path, include

from measurement.views import SensorlistCreate, SensorRetrieveUpdate, MeasurementsCreate, ShowSensorMeasurementRetrieve

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    #path('api-auth/', include('rest_framework.urls')),
    path('sensors/', SensorlistCreate.as_view()),
    path('sensorupdate/<pk>/', SensorRetrieveUpdate.as_view()),
    path('measurements/', MeasurementsCreate.as_view()),
    path('sensorandmeasure/<pk>/', ShowSensorMeasurementRetrieve.as_view()),
]
