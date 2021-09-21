from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import *
from datetime import datetime 
class ResultsListView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request,format=None):
        data=request.data
        start_datetime=data['start_datetime']
        end_datetime=data['end_datetime']
        user_id=data['user_id']
        start_datetime =datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
        end_datetime =datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
        obs=Results.objects.filter(timestamp__gte=start_datetime,timestamp__lte=end_datetime,user_id=user_id)
        serializer=ResultsSerializer(obs, many=True)
        data={}
        data['status']="success"
        data['user_id']=user_id
        data['payload']=serializer.data
        
        return Response(data)