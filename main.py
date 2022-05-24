from fastapi import FastAPI
from say_neural import NeuralSpeaker
from pydantic import BaseModel

neural_speaker = NeuralSpeaker()
app = FastAPI()


class Message(BaseModel):
    words: str
    speaker = 'xenia'


@app.post("/")
async def root(message: Message):
    print(message)
    neural_speaker.speak(words=message.words, speaker=message.speaker)
    return {"message": "Hello World"}
