import io
import wave

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from say_neural import NeuralSpeaker

neural_speaker = NeuralSpeaker()
app = FastAPI()


@app.get("/")
async def root(words: str, speaker: str = 'xenia', save_file: bool = False, sample_rate: int = 48000):
    print(f'{words}, {speaker}, {save_file} ,{sample_rate}')
    audio_or_text = neural_speaker.speak(words=words, speaker=speaker, save_file=save_file, sample_rate=sample_rate)
    if save_file:
        f = io.BytesIO()
        wav_file_in_memory = wave.open(f, 'w')
        wav_file_in_memory.setnchannels(1)  # mono
        wav_file_in_memory.setsampwidth(2)
        wav_file_in_memory.setframerate(sample_rate)
        wav_file_in_memory.writeframes(audio_or_text.audio_data)
        wav_file_in_memory.close()
        f.seek(0)
        response = StreamingResponse(content=f, media_type="audio/wav")
        response.headers["Content-Disposition"] = f"attachment; filename = speech_audio.wav"
        return response
    else:
        return audio_or_text
