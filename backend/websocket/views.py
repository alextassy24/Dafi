from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Temperature, Pressure
from rest_framework.permissions import AllowAny
from .serializers import TemperatureSerializer, PressureSerializer

class TemperatureAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        data = Temperature.objects.all()
        serializer = TemperatureSerializer(data, many=True)
        return Response(serializer.data)

class PressureAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        data = Pressure.objects.all()
        serializer = PressureSerializer(data, many=True)
        return Response(serializer.data)