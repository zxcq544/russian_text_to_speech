import os
import time

import torch
import numpy as np
import simpleaudio as sa
from transliterate import translit
from num2words import num2words
import re


class NeuralSpeaker:
    def __init__(self):
        print('Initializing neural model')
        start = time.time()
        device = torch.device('cpu')
        torch.set_num_threads(4)
        local_file = 'model.pt'
        if not os.path.isfile(local_file):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                           local_file)
        self.__model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        self.__model.to(device)
        end = time.time()
        print(f'Model ready in {round(end - start, 2)} seconds')

    @staticmethod
    def __num2words_ru(match):
        clean_number = match.group().replace(',', '.')
        return num2words(clean_number, lang='ru')

    # Speakers available: aidar, baya, kseniya, xenia, eugene, random
    # Speaker could be set in message using !1, !2 and alike starting chars
    def speak(self, words, speaker='xenia', save_file=False, sample_rate=48000):
        words = translit(words, 'ru')
        words = re.sub(r'-?[0-9][0-9,._]*', self.__num2words_ru, words)
        print(f'text after translit and num2words {words}')
        if len(words) > 3:
            possible_speaker = words[0:2]
        else:
            return
        match possible_speaker:
            case '!1':
                speaker = 'aidar'
            case '!2':
                speaker = 'baya'
            case '!3':
                speaker = 'ksenia'
            case '!4':
                speaker = 'xenia'
            case '!5':
                speaker = 'eugene'
            case '!0':
                speaker = 'random'
        # Текст который будет озвучен
        example_text = f'{words}'
        if sample_rate not in [48000, 24000, 8000]:
            sample_rate = 48000
        if speaker not in ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']:
            speaker = 'xenia'
        # Эта функция сохраняет WAV на диск
        # model.save_wav(text=example_text,
        #                speaker=speaker,
        #                sample_rate=sample_rate)
        #
        # Эта часть запускает аудио на колонках.
        start = time.time()
        print(f'Model started')
        try:
            audio = self.__model.apply_tts(text=example_text,
                                           speaker=speaker,
                                           sample_rate=sample_rate, )
        except ValueError:
            print('Bad input')
            return
        end = time.time()
        time_elapsed = round(end - start, 2)
        print(f'Model applied in {time_elapsed} seconds')
        audio = audio.numpy()
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        wave_obj = sa.WaveObject(audio, 1, 2, sample_rate)
        if not save_file:
            play_obj = wave_obj.play()
            play_obj.wait_done()
            return time_elapsed
        else:
            return wave_obj.audio_data
