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
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/ru_v3.pt',
                                           local_file)
        self.model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        self.model.to(device)
        end = time.time()
        print(f'Model ready in {round(end - start, 2)} seconds')

    def num2words_ru(self, match):
        clean_number = match.group().replace(',', '.')
        return num2words(clean_number, lang='ru')

    # Speakers available: aidar, baya, kseniya, xenia, random
    def speak(self, words, speaker='baya'):
        if len(words) > 2:
            possible_speaker = words[0:2]
        else:
            return
        words = translit(words, 'ru')
        words = re.sub(r'-?[0-9][0-9,._]+', self.num2words_ru, words)
        # If first letter in words is digit then it will set speakers voice
        match possible_speaker:
            case '!1':
                speaker = 'baya'
            case '!2':
                speaker = 'aidar'
            case '!3':
                speaker = 'kseniya'
            case '!4':
                speaker = 'xenia'
            case '!5':
                speaker = 'random'
        # Текст который будет озвучен
        example_text = f'{words}'
        sample_rate = 48000

        # Эта функция сохраняет WAV на диск
        # model.save_wav(text=example_text,
        #                speaker=speaker,
        #                sample_rate=sample_rate)
        #
        # Эта часть запускает аудио на колонках.
        start = time.time()
        try:
            audio = self.model.apply_tts(text=example_text,
                                         speaker=speaker,
                                         sample_rate=sample_rate, )
        except ValueError:
            print('Bad input')
            return
        end = time.time()
        time_lapsed = end - start
        print(f'Model applied in {round(time_lapsed, 2)} seconds')
        audio = audio.numpy()
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()
