import io
import wave

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from say_neural import NeuralSpeaker

neural_speaker = NeuralSpeaker()
app = FastAPI()


class Message(BaseModel):
    words: str
    speaker = 'xenia'


@app.get("/")
async def root(words: str, speaker='xenia', save_file=False, sample_rate=48000):
    print(f'{words}, {speaker}, {save_file} ,{sample_rate}')
    audio_or_response = neural_speaker.speak(words=words, speaker=speaker, save_file=save_file, sample_rate=sample_rate)
    if save_file:
        f = io.BytesIO()
        obj = wave.open(f, 'w')
        obj.setnchannels(1)  # mono
        obj.setsampwidth(2)
        obj.setframerate(sample_rate)
        obj.writeframes(audio_or_response.audio_data)
        obj.close()
        f.seek(0)
        response = StreamingResponse(content=f, media_type="audio/wav")
        response.headers["Content-Disposition"] = f"attachment; filename = speech_audio.wav"
        return response
    else:
        return audio_or_response
