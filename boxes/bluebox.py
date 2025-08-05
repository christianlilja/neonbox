from utils.audio import play_tone_pair
from utils.constants import MF_TONES

def play_mf_tone(digit):
    if digit not in MF_TONES:
        print("Invalid MF digit")
        return
    f1, f2 = MF_TONES[digit]
    print(f"Playing MF tone for {digit} -> {f1}Hz + {f2}Hz")
    play_tone_pair(f1, f2)

def simulate_call_sequence():
    sequence = ["KP", "1", "2", "3", "4", "5", "ST"]
    print("Simulating MF call setup:")
    for digit in sequence:
        play_mf_tone(digit)
