import numpy as np
import simpleaudio as sa

def generate_tone(frequency, duration=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    return tone

def play_tone_pair(freq1, freq2, duration=0.3, volume=0.5):
    tone1 = generate_tone(freq1, duration)
    tone2 = generate_tone(freq2, duration)
    audio = (tone1 + tone2) * (volume / 2)
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    sa.play_buffer(audio, 1, 2, 44100).wait_done()
