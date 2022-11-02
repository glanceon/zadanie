import json
import random
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

# Create your views here.
class EchoView(APIView):

    def post(self, request):
        token = ''
        try:
            token = request.META['HTTP_VERYSECURE']
        except:
            pass
        if not token:
            raise exceptions.AuthenticationFailed('No token provided')
        
        if token != "85136c79cbf9fe36bb9d05d0639c70c265c18d37":
            raise exceptions.AuthenticationFailed('Incorrect token value')
        else:
            print(f" Accepted request: {request.body}")

        characters = json.loads(json.dumps(len(request.body), default=str))
        ip_address = json.loads(json.dumps(request.META['REMOTE_ADDR'], default=str))
        msg_hash = json.loads(json.dumps(str(hash(request.body)), default=str))

        return Response({'characters': characters, 'ip_adress':ip_address, 'msg_hash': msg_hash}, status.HTTP_200_OK)

class StatusView(APIView):

    def get(self, request):
        token = ''
        try:
            token = request.META['HTTP_VERYSECURE']
        except:
            pass
        if not token:
            raise exceptions.AuthenticationFailed('No token provided')
        
        if token != "85136c79cbf9fe36bb9d05d0639c70c265c18d37":
            raise exceptions.AuthenticationFailed('Incorrect token value')
            
        timestamp = json.loads(json.dumps(datetime.now(), default=str))
        rng = json.loads(json.dumps(random.randint(-100, 68)))

        return Response({'timestamp': timestamp, 'rng':rng}, status.HTTP_200_OK)
