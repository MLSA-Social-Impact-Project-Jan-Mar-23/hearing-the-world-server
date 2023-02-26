from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import dotenv_values
import os

# General setup
config = dotenv_values(".env")

def describe(hash):    

    # Cognitive Services setup
    endpoint = config["COGNITIVE_SERVICES_IMAGE_PROCESSING_ENDPOINT"]
    subscription_key = config["COGNITIVE_SERVICES_IMAGE_PROCESSING_KEY1"]
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    # Processing local image using the describe_image method
    images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
    image_stream = open(os.path.join(images_folder,hash+".png"),"rb")

    description_results = computervision_client.describe_image_in_stream(image_stream)

    tags = description_results.tags
    caption = description_results.captions[0].text

    return tags,caption
