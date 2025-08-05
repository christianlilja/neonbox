from boxes import bluebox
from boxes import redbox

def main():
print("Phreaking Simulator")
print("1. Bluebox")
print("2. Redbox")
choice = input("Select a tool: ")
if choice == "1":
        while True:
            print("\n[Bluebox]")
            print("1. Play individual MF tone")
            print("2. Simulate call sequence")
            print("0. Back")
            sub = input("Choose an option: ")
            if sub == "1":
                digit = input("Enter MF digit (0-9, KP, ST): ").upper()
                bluebox.play_mf_tone(digit)
            elif sub == "2":
                bluebox.simulate_call_sequence()
            elif sub == "0":
                break
elif choice == "2":
    while True:
        print("\n[Redbox]")
        print("1. Simulate Nickel")
        print("2. Simulate Dime")
        print("3. Simulate Quarter")
        print("0. Back")
        sub = input("Choose an option: ")
        if sub == "1":
            redbox.simulate_coin("nickel")
        elif sub == "2":
            redbox.simulate_coin("dime")
        elif sub == "3":
            redbox.simulate_coin("quarter")
        elif sub == "0":
            break

if __name__ == "__main__":
    main()
