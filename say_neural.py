import os
import time

import torch
import numpy as np
import simpleaudio as sa


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
        self.model.apply_tts(text='ф',
                             speaker='baya',
                             sample_rate=48000, )
        print(f'Step 1 Complete in {round(time.time() - start, 2)}')
        self.model.apply_tts(text='ц',
                             speaker='baya',
                             sample_rate=48000, )
        end = time.time()
        print(f'Model ready in {round(end - start, 2)} seconds')

    def speak(self, words):
        # Текст который будет озвучен
        example_text = f'{words}'
        sample_rate = 48000
        speaker = 'baya'

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

# 'На дворе дрова, за двором дрова,под двором дрова, над двором дрова,дрова вдоль двора, дрова вширь двора,не вместит двор дров.Двора выдворить обратно на дровяной двор.'

