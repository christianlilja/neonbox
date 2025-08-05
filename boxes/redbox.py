import time
from utils.audio import play_tone_pair

# Redbox tone specs
REDBOX_FREQS = (1700, 2200)

def play_redbox_tone(duration=0.066):
    play_tone_pair(REDBOX_FREQS[0], REDBOX_FREQS[1], duration=duration)

def simulate_coin(coin):
    if coin == "nickel":
        print("Simulating nickel...")
        play_redbox_tone()
    elif coin == "dime":
        print("Simulating dime...")
        play_redbox_tone()
        time.sleep(0.07)
        play_redbox_tone()
    elif coin == "quarter":
        print("Simulating quarter...")
        for _ in range(5):
            play_redbox_tone(duration=0.033)
            time.sleep(0.04)
    else:
        print("Unknown coin type.")
