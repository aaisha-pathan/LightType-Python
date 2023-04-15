# Name: Aaisha
# Date: Dec. 24, 2022
# File Name: typingtest-aaisha.py
# Description: This program allows user to check their typing speed. 

import tkinter
import random
import time
import threading # uses different threads for different tasks (to be faster)


# initial variables
bg_color = "light blue"
restart_pressed = False
wrongwords = 0
users_wordcount = 0 


# FUNCTIONS -------------------------------------------------------------------

# menu choice function for buttons in start window
def menuchoice(choice):
    global timernum

    # calling the type window function 
    display_typewindow()
    timernum = choice

    # removes the previous window instead of destroying it
    window.withdraw()

        

# timer function
def timer():
    global restart_pressed
    global remaining_time
    global event

    restart_pressed = False
    
    # disabling start button from normal --> disabled
    start_button.config(state="disabled")
    
    # activating textbox as soon as user clicks start
    textbox.focus()
    
    # changing textbox state from disabled --> normal
    textbox.config(state="normal")

    # activating restart button from normal --> disabled
    restart_button.config(state="normal")

    remaining_time = timernum
    
    # displaying timer countdown
    for second in range(1, timernum+1):
        timeleft_num.config(text=remaining_time)

        remaining_time = timernum - second
        
        event.wait(1)
        window.update()

    timeleft_num.config(text=0)


    if not restart_pressed:
        wpm()


    # after timer countdown done
    # disabling textbox from normal --> disabled
    textbox.config(state="disabled")

    

# words per minute calculation function
def wpm():
    global wrongwords
    global users_wordcount

    # getting the word count and character count for user's text
    users_words = textbox.get(1.0, "end-1c").split()
    users_wordcount = len(users_words)
    users_charactercount = len(textbox.get(1.0, "end-1c"))


    # getting the word count and character count for the text
    original_words = textpiece_label['text'].split()
    original_wordcount = len(original_words)

    # calculating words per min, accuracy and displaying time taken
    if users_wordcount > 0:
        for wordcheck in list(zip(original_words, users_words)):
            if wordcheck[0] != wordcheck[1]:
                wrongwords += 1
        
        # words per min
        wpm = users_charactercount * 60 / (5*timernum)
        wpm_num.config(text=wpm)


        # accuracy 
        accuracy = round((users_wordcount - wrongwords)/users_wordcount * 100)
        accuracy_num.config(text=f"{accuracy}%")

        # time taken 
        timetaken_num.config(text=f"{timernum}s")

        # keeping error message blank
        errorcheck_msg.config(text="")
        

    # error checking message if user does not enter anything
    if users_wordcount == 0:
        errorcheck_msg.config(text="Please make sure you type the \
text next time!")
        



# start button function on type frame function
def startbutton():
    global event

    # using wait instead of time.sleep
    event = threading.Event()
    
    # using multiple threads to run faster
    t1 = threading.Thread(target=timer)
    t1.start()
    

def restartbutton():
    # restart means to reset everything so initializing all required variables
    users_wordcount = 0
    wrongwords = 0
    textpiece = get_random_paragraph()
    textpiece_label.config(text=textpiece)
    restart_pressed = True
    start_button.config(state="normal")
    restart_button.config(state="disabled")
    textbox.config(state="normal")
    textbox.delete(1.0, "end-1c")
    textbox.config(state="disabled")

    # stopping time
    event.set()

    # changing results from labels and making them empty as well
    timeleft_num.config(text="")
    wpm_num.config(text="")
    accuracy_num.config(text="")
    timetaken_num.config(text="")

    # updating these changes on the window
    type_window.update()
    

# function for getting random pieces of text from textpieces list
def get_random_paragraph():

    textpieces = ["Sometimes it's the first moment of the day that catches you \
off guard. That's what Wendy was thinking. She opened her window to see fire \
engines screeching down the street. While this wasn't something completely \
unheard of, it also wasn't normal. It was a sure sign of what was going to \
happen that day. She counted. One. She could hear the steps coming closer. \
Two. Puffs of breath could be seen coming from his mouth. Three. He stopped \
beside her. Four. She pulled the trigger of the gun.",
                  "I'm going to hire professional help tomorrow. I can't \
handle this anymore. She fell over the coffee table and now there is blood \
in her catheter. This is much more than I ever signed up to do. She counted. \
One. She could hear the steps coming closer. \
Two. Puffs of breath could be seen coming from his mouth. Three. He stopped \
beside her. Four. She pulled the trigger of the gun.",
                  "Cake or pie? I can tell a lot about you by which one you \
pick. It may seem silly, but cake people and pie people are really different. \
I know which one I hope you are, but that's not for me to decide. So, what is \
it? Cake or pie? Make sure you are making a good decision and not regretting \
later on about which one you pick. Once again, cake or pie?",
                  "She sat down with her notebook in her hand, her mind \
wandering to faraway places. She paused and considered all that had happened. \
It hadn't gone as expected. When the day began she thought it was going to be \
a bad one, but as she sat recalling the day's events to write them down, she \
had to admit, it had been a rather marvelous day.",
                  'His parents continued to question him. He didn\'t know what\
to say to them since they refused to believe the truth. He explained again and \
again, and they dismissed his explanation as a figment of his imagination. \
There was no way that grandpa, who had been dead for five years, could have \
told him where the treasure had been hidden. Of course, it didn\'t help that \
grandpa was roaring with laughter in the chair next to him as he tried to \
explain once again how he\'d found it',
                  '"Can I get you anything else?" David asked. It was a \
question he asked a hundred times a day and he always received the same \
answer. It had become such an ingrained part of his daily routine that he \
had to step back and actively think when he heard the little girl\'s reply. \
Nobody had before answered the question the way that she did, and David \
didn\'t know how he should respond.',
                  'They told her that this was her once chance to show the \
world what she was made of. She believed them at the time. It was the big \
stage and she knew the world would be there to see. The only one who had \
disagreed with this sentiment was her brother. He had told her that you \
don\'t show the world what you\'re made of when they are all watching, you \
show that in your actions when nobody was looking. It was looking more and\
more like her brother was correct.',
                  'Green vines attached to the trunk of the tree had wound \
themselves toward the top of the canopy. Ants used the vine as their private \
highway, avoiding all the creases and crags of the bark, to freely move at \
top speed from top to bottom or bottom to top depending on their current \
chore. At least this was the way it was supposed to be. Something had damaged \
the vine overnight halfway up the tree leaving a gap in the once pristine ant \
highway.',
                  'The fog was as thick as pea soup. This was a problem. Gary \
was driving but couldn\'t see a thing in front of him. He knew he should \
stop, but the road was narrow so if he did, it would be right in the center \
of the road. He was sure that another car would end up rear-ending him, so he \
continued forward despite the lack of visibility. This was an unwise move.',
                  'You\'re going to make a choice today that will have a \
direct impact on where you are five years from now. The truth is, you\'ll \
make choice like that every day of your life. The problem is that on most \
days, you won\'t know the choice you make will have such a huge impact on \
your life in the future. So if you want to end up in a certain place in the \
future, you need to be careful of the choices you make today.',
                  'There once lived an old man and an old woman who were \
peasants and had to work hard to earn their daily bread. The old man used to \
go to fix fences and do other odd jobs for the farmers around, and while he \
was gone the old woman, his wife, did the work of the house and worked in \
their own little plot of land.',
                  'There had to be a better way. That\'s all Nancy could \
think as she sat at her desk staring at her computer screen. She\'d already \
spent five years of her life in this little cubicle staring at her computer \
doing "work" that didn\'t seem to matter to anyone including her own boss. \
There had to be more to her life than this and there had to be a better way \
to make a living. That\'s what she was thinking when the earthquake struck.',
                  'The light blinded him. It was dark and he thought he was \
the only one in the area, but the light shining in his eyes proved him wrong. \
It came from about 100 feet away and was shining so directly into his eyes he \
couldn\'t make out anything about the person holding the light. There was only \
one thing to do in this situation. He reached into his pocket and pulled out \
a flashlight of his own that was much stronger than the one currently blinding \
him. He turned it on and pointed it into the stranger\'s eyes.']

    # shuffling and randomly selecting a textpiece
    random.shuffle(textpieces)
    textpiece = random.choice(textpieces)
    return textpiece



# back to main button (to go back to first start screen with menu options)
def backtomenu():
    
    # hiding the type window
    type_window.withdraw()

    # show the main start window
    window.deiconify()



# function to display the second window (typing window)
def display_typewindow():
    global type_window
    global start_button
    global textbox
    global restart_button
    global timeleft_num
    global wpm_num
    global accuracy_num
    global timetaken_num
    global textpiece_label
    global errorcheck_msg
    
    # TYPING WINDOW FRAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # new window on second level 
    type_window = tkinter.Toplevel()
    type_window.title("✦ LIGHT TYPE ✦  by Aaisha")
    type_window.config(bg=bg_color)

    width = 1200
    height = 700

    # getting the user's screen dimesions 
    screenwidth = type_window.winfo_screenwidth()
    screenheight = type_window.winfo_screenheight()

    # finding center coordinates
    x = int((screenwidth/2) - (width/2))
    y = int((screenheight/2) - (height/2))

    type_window.geometry(f"{width}x{height}+{x}+{y}")


    # creating the typing frame (screen after clicking menu options in start frame)
    type_frame = tkinter.Frame(type_window, bg=bg_color)
    type_frame.grid()


    # frame for main heading
    heading_frame = tkinter.Frame(type_frame, bg=bg_color)
    heading_frame.grid()


    # light type heading in heading frame
    lighttype_heading = tkinter.Label(heading_frame, text="✦ L I G H T  T Y P E ✦",
                                      font="Arial, 30",
                                      fg="black",
                                      bg=bg_color,
                                      width=50)
    lighttype_heading.grid(pady=5)
    
     # frame for press start to begin
    pressstart_frame = tkinter.Frame(type_frame, bg=bg_color)
    pressstart_frame.grid()


    # press start to begin label 
    presstart_label = tkinter.Label(pressstart_frame, text=f"PRESS START WHEN READY!", \
                                   bg=bg_color, fg="black",
                                    font=("Arial, 18"))
    presstart_label.grid(pady=5)



    # frame for text + user's textbox
    text_frame = tkinter.Frame(type_frame, bg=bg_color)
    text_frame.grid()

    textpiece = get_random_paragraph()


    # text piece that user has to type label
    textpiece_label = tkinter.Label(text_frame, text=f"{textpiece}\n", \
                                    font="Arial, 20", bg=bg_color, width=100,
                                    justify="left", wraplength=1000,
                                    fg="black")
    textpiece_label.grid(pady=5)


    # frame for textbox
    textbox_frame = tkinter.Frame(type_frame, bg=bg_color)
    textbox_frame.grid()


    # textbox for user to type in 
    textbox = tkinter.Text(textbox_frame, width=100, font="Arial, 15",\
                            state="disabled", wrap="word", height=7,
                           bd=4)
    textbox.grid()


    # frame for start, restart & back buttons
    buttons2_frame = tkinter.Frame(type_frame, bg=bg_color)
    buttons2_frame.grid()


    # start, restart & back frames

    start_button = tkinter.Button(buttons2_frame, text="Start", bg="red",
                                 font="Arial, 15", width=15,
                                  command=startbutton)
    start_button.grid(row=0, column=0, padx=10, pady=20)


    restart_button = tkinter.Button(buttons2_frame, text="Restart", bg="red",
                                   state="disabled", font="Arial, 15",
                                   width=15, command=restartbutton)
    restart_button.grid(row=0, column=1, padx=10, pady=20)


    backmenu_button = tkinter.Button(buttons2_frame, text="Back to Menu",
                                     bg=bg_color,font="Arial, 15", width=15,
                                     command=backtomenu)
    backmenu_button.grid(row=0, column=2, padx=10, pady=20)
    

    # empty label for error check related messages in the future

    errorcheck_msg = tkinter.Label(buttons2_frame, text="", bg=bg_color,
                                   font="Arial, 14")
    errorcheck_msg.grid(row=1, column=1, pady=5)

    # frame for time left 
    timeleft_frame = tkinter.Frame(type_frame, bg=bg_color)
    timeleft_frame.grid()

    # time left label
    timeleft_label = tkinter.Label(timeleft_frame, text=f"\nTIME LEFT\n", \
                             bg=bg_color,font=("Arial", 18, "bold"),
                                   fg="black", width=20)
    timeleft_label.grid()

    timeleft_num = tkinter.Label(timeleft_frame, text="", \
                             bg=bg_color,font=("Arial", 35, "bold"),
                                   fg="white", width=20)
    timeleft_num.grid(row=1, column=0)


    # frame for results 
    results_frame = tkinter.Frame(type_frame, bg=bg_color)
    results_frame.grid()


    # results labels
    wpm_label = tkinter.Label(results_frame, text=f"\nWORDS PER MINUTE\n", \
                             bg=bg_color,font=("Arial", 18, "bold"),
                             fg="black",  width=20)
    wpm_label.grid(row=0, column=0)


    wpm_num = tkinter.Label(results_frame, text="", \
                             bg=bg_color,font=("Arial", 35, "bold"),
                             fg="white",  width=20)
    wpm_num.grid(row=1, column=0)
    

    accuracy_label = tkinter.Label(results_frame, text=f"\nACCURACY\n", \
                             bg=bg_color,font=("Arial", 18, "bold"),
                                   fg="black",  width=20)
    accuracy_label.grid(row=0, column=1)

    accuracy_num = tkinter.Label(results_frame, text="", \
                             bg=bg_color,font=("Arial", 35, "bold"),
                                   fg="white",  width=20)
    accuracy_num.grid(row=1, column=1)


    timetaken_label = tkinter.Label(results_frame, text=f"\nTIME TAKEN\n", \
                             bg=bg_color,font=("Arial", 18, "bold"),
                                    fg="black",  width=20)
    timetaken_label.grid(row=0, column=2)

    timetaken_num = tkinter.Label(results_frame, text="", \
                             bg=bg_color,font=("Arial", 35, "bold"),
                                    fg="white",  width=20)
    timetaken_num.grid(row=1, column=2)



# MAIN WINDOW -----------------------------------------------------------------


# creating the window
window = tkinter.Tk()
window.title("✦ LIGHT TYPE ✦  by Aaisha")
window.config(bg=bg_color)

# declaring general width and height dimensions for the window
width = 1200
height = 700

# getting the user's screen dimesions 
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

# finding center coordinates
x = int((screenwidth/2) - (width/2))
y = int((screenheight/2) - (height/2))

# for screen to be in the center of user's screen
window.geometry(f"{width}x{height}+{x}+{y}")


# START WINDOW FRAME ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# creating the start frame (welcome window +  menu options)
start_frame = tkinter.Frame(window, bg=bg_color)
start_frame.grid(row=1, column=10)


# welcome message label
welcome_label = tkinter.Label(start_frame, text="\nWELCOME TO\n", fg="black", \
                            bg=bg_color, width=68, font=("Arial", 30, "bold"))
welcome_label.grid(row=1, pady=40)



# L I G H T  T Y P E label (main title of the program)
lighttype_label = tkinter.Label(start_frame, text="✦ L I G H T  T Y P E ✦\n", \
                                fg="black",
                                bg=bg_color,
                                font=("Times", 75, "bold"))
lighttype_label.grid(row=2, pady=15)


# instructions label
instructions_label = tkinter.Label(start_frame, text="Chose a time length to \
type. Then, press start when you are ready. Now type the given text as fast as\
 possible in the textbox until your time is up. Find out your tpying speed \
and accuracy! Enjoy :)", fg="black",
                         bg=bg_color, wraplength=1000,
                         font=("Arial", 17, "italic"))

instructions_label.grid(row=3, pady=5)


# asking about menu options label
menuoptions_label = tkinter.Label(start_frame, text="So what do you want to do?\
", fg="black", bg=bg_color, font="Arial, 20")
menuoptions_label.grid(row=4, pady=30)


# frame for menu options buttons
buttons_frame = tkinter.Frame(start_frame, bg=bg_color)
buttons_frame.grid()


# menu options buttons for typing tests (with different time lengths) 
seconds15_button = tkinter.Button(buttons_frame, text="Test ~ 15 secs"\
                                  , fg="black", font="Arial, 20", \
                                  command=lambda: menuchoice(15))
seconds15_button.grid(row=5, column=0, padx=15)


seconds30_button = tkinter.Button(buttons_frame, text="Test ~ 30 secs"\
                                  , fg="black", font="Arial, 20", \
                                  command=lambda: menuchoice(30))
seconds30_button.grid(row=5, column=1, padx=15)


seconds60_button = tkinter.Button(buttons_frame, text="Test ~ 60 secs"\
                                  , fg="black", font="Arial, 20", \
                                  command=lambda: menuchoice(60))
seconds60_button.grid(row=5, column=2, padx=15)


# exit button
exit_button = tkinter.Button(buttons_frame, text="Exit", fg="black",\
                             font="Arial, 20", command=window.destroy)
exit_button.grid(row=6, column=1, pady=20)


# displaying window
window.mainloop()
