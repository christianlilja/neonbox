import curses
from boxes import bluebox, redbox, dtmf

MENU = [
    "Bluebox",
    "Redbox",
    "DTMF Generator",
    "Exit"
]

def draw_menu(stdscr, selected):
    stdscr.clear()
    stdscr.addstr(0, 2, "Colorbox", curses.A_BOLD | curses.A_UNDERLINE)
    for idx, item in enumerate(MENU):
        if idx == selected:
            stdscr.addstr(idx + 2, 4, f"> {item}", curses.A_REVERSE)
        else:
            stdscr.addstr(idx + 2, 4, f"  {item}")
    stdscr.refresh()

def bluebox_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "[Bluebox] - Press q to return", curses.A_BOLD)
    stdscr.addstr(2, 2, "Enter MF digit (0-9, KP, ST): ")
    curses.echo()
    digit = stdscr.getstr(2, 35, 4).decode().upper()
    curses.noecho()
    bluebox.play_mf_tone(digit)
    stdscr.addstr(4, 2, f"Played MF tone for {digit}. Press any key...")
    stdscr.getch()

def redbox_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "[Redbox] - Press q to return", curses.A_BOLD)
    stdscr.addstr(2, 2, "Simulate (nickel/dime/quarter): ")
    curses.echo()
    coin = stdscr.getstr(2, 35, 8).decode().lower()
    curses.noecho()
    redbox.simulate_coin(coin)
    stdscr.addstr(4, 2, f"Simulated {coin}. Press any key...")
    stdscr.getch()

def dtmf_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 2, "[DTMF Generator] - Press q to return", curses.A_BOLD)
    stdscr.addstr(2, 2, "Enter sequence (e.g. 123#ABCD): ")
    curses.echo()
    sequence = stdscr.getstr(2, 35, 32).decode().upper()
    curses.noecho()
    dtmf.play_dtmf_sequence(sequence)
    stdscr.addstr(4, 2, f"Played DTMF sequence. Press any key...")
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    selected = 0
    while True:
        draw_menu(stdscr, selected)
        key = stdscr.getch()
        if key == curses.KEY_UP:
            selected = (selected - 1) % len(MENU)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(MENU)
        elif key in [10, 13]: # Enter key 
            if MENU[selected] == "Bluebox":
                bluebox_menu(stdscr)
            elif MENU[selected] == "Redbox":
                redbox_menu(stdscr)
            elif MENU[selected] == "DTMF Generator":
                dtmf_menu(stdscr)
            elif MENU[selected] == "Exit":
                break

if __name__ == "__main__":
    curses.wrapper(main)
