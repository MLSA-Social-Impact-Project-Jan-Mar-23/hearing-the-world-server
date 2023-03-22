import os
import uuid

def create_image_file(image_bytes:bytes):
    images_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "images"))
    print(images_folder)
    image_name = str(uuid.uuid1()) + ".png"
    with open(os.path.join(images_folder,image_name),"wb") as image_file:
        image_file.write(image_bytes)
    return image_name