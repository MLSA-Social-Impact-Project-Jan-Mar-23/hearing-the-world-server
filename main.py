from fastapi import FastAPI
from describe import describe
from dotenv import dotenv_values
from generate_story import generate_story   
import uvicorn


config = dotenv_values(".env")
port = config["PORT"] or 3000   
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Server up and running"}

# To generate a story from an image that comes through the POST request
@app.post("/generate")
async def send_story():
    print("Generating story...")
    tags,caption = describe("doge")
    generate_story(tags,caption)
    return {"story":"This is a story for you"}

if __name__ == '__main__':
    uvicorn.run(app, port=port)