from PIL import Image
from resize.models import Resize, ErrorLog
import requests

URL = 'http://127.0.0.1:8000/api/images/'

def Resize_Image(image_to_resize):
    image = Image.open(image_to_resize)

    return image.resize(384,384)


def Search_for_images():
    
    database_objects = Resize.objects.all()

    for objects in database_objects:
        if objects:
            image = Resize.objects.get(id=objects.id)
            resized_to_resize = image.image_to_resize
            resized_image = Resize_Image(resized_to_resize)
            returning_data = {"id":image.image_id_from_request, "user_id": image.user_id_from_request, "image": resized_image}
            return returning_data


def Put_new_image():

    data = Search_for_images()

    response = requests.put(URL, data=data)

    if response.status_code == 200:
        Resize.objects.get(id=data.id).delete()
        return True

    
    return False, data


def Scheduling_Queue():
    response = Put_new_image()

    if not response:
        ErrorLog.objects.create(image_id=response.data.id)
        
        Resize.objects.get(id=response.data.id).delete()