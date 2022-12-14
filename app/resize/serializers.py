from rest_framework import serializers


class ResizeSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_to_resize = serializers.ImageField()
    image_id_from_request = serializers.IntegerField()
    user_id_from_request = serializers.IntegerField()


class ErrorLogSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_id : serializers.IntegerField()
    error_date = serializers.DateTimeField()