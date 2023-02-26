# Hearing the World - Server

## This is the server for Hearing the World
</br>

# Server setup

Install pipenv

     sudo pip3 install pipenv

Enter a virtual environment

     pipenv shell
 
Install the necessary packages
     
     pipenv install --dev

Run the server (live reload)

     pipenv run watch

Run the server 

     pipenv run start

# Documentations

[Azure Cognitive Services SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)

[Describe Image in Stream (For local images)](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#azure-cognitiveservices-vision-computervision-operations-computervisionclientoperationsmixin-describe-image-in-stream)

[FastAPI](https://fastapi.tiangolo.com/)

# Flow

## Client sends image ----> Server stores it in local ----> Takes it and processes it with Azure Describe Image ----> Now there is access to the captions and tags for that image 
