import curses, sys
from curses.textpad import Textbox

filename = None

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Enter a FileName!")
    exit()

def main(stdscr):
    stdscr.clear()
    win = curses.newwin(100, 10000, 2, 2)
    box = Textbox(win)
    stdscr.addstr(0, 30, "Editing " + filename + "* (Press Ctrl + G To Save!)")

    stdscr.refresh()

    box.edit()
    text = box.gather().strip()

    with open(filename, "w") as file:
        file.write(text)
        file.close()

curses.wrapper(main)
