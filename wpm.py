import curses
from curses import wrapper
import time 
import random

def start_screen(stdscr):#we need to have access to stdscr to get access to the screen.
    stdscr.clear()
    stdscr.addstr("Welcome earthlings")
    stdscr.addstr("\nPress any key to start the typing test") #\n brings everything to the next line. newlinecharacter
    stdscr.refresh() 
    stdscr.getkey() #waits for the user to type something

def display_text(stdscr, target, current, wpm=0): #parameters which require values    
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}") #curly braces will be evaluated as a string
    
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        
        stdscr.addstr(0, 1, char, color)

def load_text():
    with open("wpmtest.txt", "r") as f: #load the text file with different lines for the practice test. 
        lines = f.readlines()
        return random.choice(lines).strip() #strip removes \n or any trailing and whitespace characters. 

    def wpm_test(stdscr):
        target_text = load_text()
        current_text = []
        wpm = 0 
        start_time = time.time() #to count the number of words per minute 
        stdscr.nodelay(True)
        while True:
            time_elapsed = max(time.time() - start_time, 1) #this ensures we don't get a zero division error. 
            wpm = round(len(current_text) / (time_elapsed / 60)) / 5 #if you type  30 characters by 15 minutes your wpm is 120.ofc 60 is the minute count. we round it off so we don't get crazy decimal numbers.
          
            stdscr.clear()
            display_text(stdscr, target_text, current_text)
            stdscr.refresh()

            if "".join(current_text) == target_text: #converts the current text list to a string. 
                stdscr.nodelay(False)
                break
            
            try:
                key = stdscr.getkey() #same as input function in python. If the user doesn't enter a key, this line throws an exception. 
            except: #the try/excpet ensures this line doesn't crash when the user doesn't type anything. 
                continue #even if it crashes, it will bring us back to the top of the while loop. 
            
            if ord(key) == 27: #esc key is ascii 27 ord =ordinal value
                break 
            if key in ("KEY_BACKSPACE", '\b', "\x7f"): #backspace can be represented by all 3 regardless of the OS. 
                if len(current_text) > 0:
                    current_text.pop() 
            elif len:(current_text) < len(target_text)
            current_text.append(key)
def main(stdscr): #standardoutputscreen
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED) #adding colors to the background, foreground and text
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)

    start_screen(stdscr)

    while True:
        wpm_test = (stdscr)
        stdscr.addstr(2,0, "You completed the test! Press any key to start again.")
        key = stdscr.getkey() 
        if ord(key) == 27:  #if the user presses the esc key they can exit the game, otherwise it starts again. 
            break

wrapper(main)








#it doesn't work. There's a bug somewhere. 
#running this code only on command prompt terminal for the correct output
#go to .venv then call wpm.py to run it. 