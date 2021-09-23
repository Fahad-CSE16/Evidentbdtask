from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from datetime import datetime 
from .serializers import *
from .models import *

class ResultsListView(APIView):
    permission_classes=[AllowAny,]
    def post(self, request,format=None):

        # Getting input data From API Post reqest
        data=request.data
        start_datetime=data['start_datetime']
        end_datetime=data['end_datetime']
        user_id=data['user_id']

        # converting string into datetime 
        start_datetime =datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
        end_datetime =datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')

        # Filtering Results
        obs=Results.objects.filter(timestamp__gte=start_datetime,timestamp__lte=end_datetime,user_id=user_id)
        serializer=ResultsSerializer(obs, many=True)

        # Making Response
        data={}
        data['status']="success"
        data['user_id']=user_id
        data['payload']=serializer.data
        
        return Response(data)