from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from resize.models import Resize, ErrorLog
from resize.serializers import ResizeSerializers, ErrorLogSerializers



class ResizeImagesView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    

    def post(self, request):

        serializer = ResizeSerializers(data=request.data)
        
        if not serializer.is_valid:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        image_id_from_request = int(request.data['image_id_from_request'])
        user_id_from_request = int(request.data['user_id_from_request'])
        image_to_resize = request.data['image_to_resize'] 
        Resize.objects.create(image_id_from_request=image_id_from_request, user_id_from_request=user_id_from_request, image_to_resize=image_to_resize)

        return Response(status=status.HTTP_201_CREATED)


    def get(self, request):
        
        logs = ErrorLog.objects.all()

        serializers = ErrorLogSerializers(logs, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)
