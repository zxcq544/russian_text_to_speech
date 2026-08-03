## Acerca de
Este convertidor de texto a voz utiliza la [red neuronal Silero](https://github.com/snakers4/silero-models), optimizada para el idioma ruso. Los números se convierten a palabras en ruso mediante num2words y las palabras en inglés se transliteran. Por defecto utiliza CPU y 4 núcleos, pero puedes cambiar a CUDA en NeuralSpeaker.py

Puedes probar el modelo de texto a voz de Silero aquí: https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb

## Ejemplos de sonido de voz
Texto usado como ejemplo: На дворе трава, на траве дрова: раз дрова, два дрова, три дрова. На дворе трава, на траве дрова — раз дрова, два дрова, три дрова: дрова вдоль двора, дрова вширь двора, не вместит двор дров, надо дрова выдворить обратно со двора.


https://user-images.githubusercontent.com/5781268/171030534-3a6cb639-5dcf-41d9-a9e8-345e2e007ca5.mp4

https://user-images.githubusercontent.com/5781268/171030551-85d08f59-8cd5-4630-95a4-edd8ca5cafb8.mp4

https://user-images.githubusercontent.com/5781268/171030565-b2a8cf5c-28c0-4695-ab86-da01a1c9cc32.mp4

https://user-images.githubusercontent.com/5781268/171030261-eb450f8b-238c-4a90-91b7-62f8b8159ebe.mp4

https://user-images.githubusercontent.com/5781268/171030556-c3228ab5-468b-495d-9ca3-064cc12543ac.mp4

## Instalar dependencias
Requiere Python 3.10 o superior

#### Windows
```bash
pip install -r requirements.txt
```

#### Linux
Instala gcc si lo necesitas. Luego:
```bash
sudo apt-get install -y python3-dev libasound2-dev
pip install -r requirements.txt
```

## Ejecutar en producción

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1 --proxy-headers
```

## Ejecutar servidor de desarrollo

```bash
uvicorn main:app --reload 
```

## Probar
#### GUI simple
Visita <http://localhost:8000/> 
#### Ejecutar con parámetros GET
Visita <http://localhost:8000/speak?words=Привет&speaker=xenia&sample_rate=48000>  

Puedes configurar 3 parámetros:
1. `words` - frase que deseas pronunciar 
2. `speaker` - voz a utilizar. Las voces disponibles son: `aidar`, `baya`, `kseniya`, `xenia`, `eugene`, `random`. `random` genera una nueva voz cada vez
3. `sample_rate` - establece la tasa de muestreo de audio de salida. Las opciones disponibles son `8000`, `24000`, `48000`.

#### Generar y descargar audio
Visita <http://localhost:8000/get_audio_file?words=Привет&speaker=xenia&sample_rate=48000> para generar y descargar un archivo de audio.
Los parámetros para `get_audio_file` son los mismos que para `speak`

#### Documentación OpenAPI generada

En modo desarrollo puedes visitar <http://localhost:8000/docs> para ver la documentación generada por OpenAPI.

#### Solicitud GET con curl
```bash
curl -X 'GET' 'http://localhost:8000/speak?words=Привет&speaker=xenia&sample_rate=48000' -H 'accept: application/json'
```
