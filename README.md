## About
This text to speach works using [Silero neural network](https://github.com/snakers4/silero-models) which is 
optimized for russian language. Numbers are turned to russian words using num2words and english words are transliterated.

На дворе трава, на траве дрова: раз дрова, два дрова, три дрова. На дворе трава, на траве дрова — раз дрова, два дрова, три дрова: дрова вдоль двора, дрова вширь двора, не вместит двор дров, надо дрова выдворить обратно со двора.

## Voice sound examples

aidar
![aidar](./voice_examples/aidar.mp4)
baya
![baya](./voice_examples/baya.mp4)
kseniya
![kseniya](./voice_examples/kseniya.mp4)
xenia
![xenia](./voice_examples/xenia.mp4)
random
![random](./voice_examples/random.mp4)
## Install dependencies
Needs python 3.10 or newer

#### Windows
```bash
pip install simpleaudio
pip install torch
pip install numpy
pip install num2words
pip install transliterate
pip install fastapi
pip install "uvicorn[standard]"
```

#### Linux
```bash
sudo apt-get install -y python3-dev libasound2-dev
pip install simpleaudio
pip install torch
pip install numpy
pip install num2words
pip install transliterate
pip install fastapi
pip install "uvicorn[standard]"
```


## Run prod

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1 --proxy-headers
```

## Run Dev Server

```bash
uvicorn main:app --reload 
```

## Try it out
#### Simple GUI
Visit <http://localhost:8000/> 
#### Run with GET parameters
Visit <http://localhost:8000/speak?words=Привет&speaker=xenia&sample_rate=48000>  

Here you can set 3 parameters:
1. `words` - phrase that you want to pronounce 
2. `speaker` - voice to use. Available voices are: `aidar`, `baya`, `kseniya`, `xenia`, `random`.`random` generates 
new voice each time
3. `sample_rate` - sets output audio sample rate. Available options are `8000`, `24000`, `48000`.

#### Generate and download audio
Visit <http://localhost:8000/get_audio_file?words=Привет&speaker=xenia&sample_rate=48000> to generate and download  
audio file. Parameters for `get_audio_file` are same as for `speak`

#### OpenAPI generated docs

In dev mode you can visit <http://localhost:8000/docs> for OpenApi generated docs.

#### Speak GET request with curl
```bash
curl -X 'GET' 'http://localhost:8000/speak?words=Привет&speaker=xenia&sample_rate=48000' -H 'accept: application/json'
```

