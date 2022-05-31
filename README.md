## About
This text to speach works using [Silero neural network](https://github.com/snakers4/silero-models) which is 
optimized for russian language. Numbers are turned to russian words using num2words and english words are transliterated.
By default it uses cpu and 4 cores but you can switch to cuda in NeuralSpeaker.py

## Voice sound examples
Text used as example: На дворе трава, на траве дрова: раз дрова, два дрова, три дрова. На дворе трава, на траве дрова — раз дрова, два дрова, три дрова: дрова вдоль двора, дрова вширь двора, не вместит двор дров, надо дрова выдворить обратно со двора.


https://user-images.githubusercontent.com/5781268/171030534-3a6cb639-5dcf-41d9-a9e8-345e2e007ca5.mp4

https://user-images.githubusercontent.com/5781268/171030551-85d08f59-8cd5-4630-95a4-edd8ca5cafb8.mp4

https://user-images.githubusercontent.com/5781268/171030565-b2a8cf5c-28c0-4695-ab86-da01a1c9cc32.mp4

https://user-images.githubusercontent.com/5781268/171030261-eb450f8b-238c-4a90-91b7-62f8b8159ebe.mp4

https://user-images.githubusercontent.com/5781268/171030556-c3228ab5-468b-495d-9ca3-064cc12543ac.mp4

## Install dependencies
Needs python 3.10 or newer

#### Windows
```bash
pip install -r requirements.txt
```

#### Linux
Install gcc if you need to. Then:
```bash
sudo apt-get install -y python3-dev libasound2-dev
pip install -r requirements.txt
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
Visit <http://localhost:8000/get_audio_file?words=Привет&speaker=xenia&sample_rate=48000> to generate and download audio file.
Parameters for `get_audio_file` are same as for `speak`

#### OpenAPI generated docs

In dev mode you can visit <http://localhost:8000/docs> for OpenApi generated docs.

#### Speak GET request with curl
```bash
curl -X 'GET' 'http://localhost:8000/speak?words=Привет&speaker=xenia&sample_rate=48000' -H 'accept: application/json'
```

