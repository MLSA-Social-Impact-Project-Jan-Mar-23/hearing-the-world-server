# Hearing the World - Server

## This is the server for Hearing the World
</br>

# Server setup

## Perform the following steps on the command line
</br>

Copy environment variables and provide the appropriate values

     cp .env.example .env

Install pipenv

     sudo pip3 install pipenv

Enter a virtual environment

     pipenv shell
 
Install the necessary packages
     
     pipenv install --dev

To run the server in development (live reload)

     pipenv run dev

To run the server in production 

     pipenv run prod

To exit pipenv

     Ctrl + D

# Documentations

[Azure Cognitive Services SDK for Python](https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)

[Describe Image in Stream (For local images)](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python#azure-cognitiveservices-vision-computervision-operations-computervisionclientoperationsmixin-describe-image-in-stream)

[FastAPI](https://fastapi.tiangolo.com/)

# Flow

## Client sends image ----> Server stores it in the filesystem ----> Takes it and processes it with Azure Describe Image ----> Now there is access to the captions and tags for that image ---> Using those tags and caption design a prompt to provide to OpenAI and generate the story
