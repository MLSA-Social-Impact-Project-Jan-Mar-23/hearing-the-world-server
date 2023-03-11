from fastapi import FastAPI,UploadFile
from dotenv import dotenv_values
import uvicorn
from generate_story import generate_story   
from describe import describe
from create_image_file import create_image_file


config = dotenv_values(".env")
port = config["PORT"] or 3000   
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Server up and running"}

# To generate a story from an image that comes through the POST request
@app.post("/generate")
async def send_story(image:UploadFile):
    # print(name,name.decode('UTF-8').split("=")[1])

    # Read the bytes from the image in the request
    image_content:bytes = image.file.read()

    # Write it to the images folder as an image file
    image_name:str = create_image_file(image_content)
    
    print("Generating story...")

    # Get the tags and caption from the image we just saved
    tags,caption = describe(image_name)

    # Generate the story from the tags
    story_response  = generate_story(tags,caption)

    return {"story":story_response.choices[0].text[2:]}

if __name__ == '__main__':
    uvicorn.run(app, port=port)