# Importing Modules

from tkinter import *
from tkinter import messagebox
from database import *
from feedback_hub import hub
import mysql.connector
import subprocess
import threading
from win10toast import *
from basic_func import *

toast = ToastNotifier()

# Connecting to the database

mycursor = mydb.cursor()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    charset="utf8",
    password="12345", 
    port = 3307
)

# Creating tkinter window

root = Tk()
root.title("Raven")
root.geometry("450x500")
root.wm_resizable(0, 0)
root.configure(background="white")
root.iconbitmap("raven.ico")

# Frames

# frame1 = Frame(root)
frame1 = Frame(root, highlightbackground="red", highlightthickness=5)
frame2 = Frame(root, highlightbackground="yellow", highlightthickness=5)
frame3 = Frame(root, highlightbackground="blue", highlightthickness=5)

msg_window = Entry(frame3, font="JetBrainsMono 14")
frame1.config(bg="White")
frame2.config(bg="White")

# Variables
x = StringVar()
y = StringVar()
status = StringVar()
bot_label = ""
running = True
spotify_url = "https://open.spotify.com/"
edge_dir = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
youtube_url = "https://youtube.com/"
msg_user_coordinates = [10, 10]
suggestion_label = []
spotify_found = False


# Functions

def debug():
    def motion(event):
        global x, y, status
        x, y = event.x, event.y
        status = Label(frame3, text="x: {}, y: {}".format(x, y))
        status.place(x=300, y=20)

    root.bind('<Motion>', motion)


def all_programs():
    import subprocess

    # traverse the software list
    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)

    # try block
    try:

        # arrange the string
        for i in range(len(a)):
            print(a.split("\\r\\r\\n")[6:][i])
            file = open('programs_installed', 'a')
            file.write(a.split("\\r\\r\\n")[6:][i])
            file.close()
    except IndexError as e:
        print("All Done")


def pre_run():
    thread1 = threading.Thread(target=all_programs, daemon=True)
    thread1.start()

    if find("spotify", "programs_installed"):
        global spotify_found
        spotify_found = True


pre_run()
submit()


def sub_btn_command(*args):
    global bot_label
    global suggestion_label
    global reply
    global repID
    global queID
    current_org = str(msg_window.get())
    current_new = current_org.lower()
    msg_window.delete(0, END)
    mycursor.execute('select * from questions;')
    output = mycursor.fetchall()
    for i in output:
        que_input = i[0]
        if que_input in current_new:

            que_label = Label(frame1, font="Ariel 12", text='You: ' + current_new, bg="white")
            que_label.place(x=msg_user_coordinates[0], y=msg_user_coordinates[1])
            msg_user_coordinates[1] += 30

            mycursor.execute('select queID from questions where que = "{}";'.format(que_input))
            output2 = mycursor.fetchall()

            for j in output2:
                queID = j[0]

            mycursor.execute('select reply from replies where repID = "{}";'.format(queID))

            output3 = mycursor.fetchall()
            for k in output3:
                reply = k[0]

            bot_label = Label(frame1, bg="white", font="Ariel 12", text="Chatbot: " + reply)
            bot_label.place(x=msg_user_coordinates[0], y=msg_user_coordinates[1])
            msg_user_coordinates[1] += 40

            mycursor.execute('select repID from replies where reply = "{}";'.format(reply))

            output4 = mycursor.fetchall()
            for l in output4:
                repID = l[0]

            mycursor.execute(
                'select suggestion, suggestion2, suggestion3, suggestion4 from suggestions where repID = "{}";'.format(
                    repID))

            output5 = mycursor.fetchall()
            # this for loop is active second time onwards when the submit button is pressed.
            for suggestion in suggestion_label:
                suggestion.pack_forget()
            suggestion_label.clear()
            # this runs first time submit button is pressed
            for suggestions in output5:
                for m in (suggestions[0:]):
                    label = Label(frame2, bg="white", text=m)
                    suggestion_label.append(label)
                    label.pack()

            if reply == "Sure!" or "Sure! You will be reminded after 5 minutes.":
                if "chrome" in current_new:
                    subprocess.call('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
                if not spotify_found:
                    if "spotify" in current_new:
                        subprocess.Popen((edge_dir, spotify_url))
                if "youtube" in current_new:
                    subprocess.Popen((edge_dir, youtube_url))
                if "suggest" in current_new:
                    # continue
                    hub()  # from feedback_hub
                if "reminder" in current_new:
                    reminder_text = current_new[9:]
                    t1 = threading.Timer(300,
                                         lambda: toast.show_toast("Reminder", "{}".format(reminder_text), duration=5))
                    t1.daemon = True
                    t1.start()


msg_window.bind("<Return>", sub_btn_command)

sub_button = Button(frame3, text="SUBMIT", font=("Ariel", 20), command=sub_btn_command, relief=GROOVE)

# MENU

menu_bar = Menu(root)
menu1 = Menu(menu_bar, tearoff=0)
menu2 = Menu(menu_bar, tearoff=0)
menu3 = Menu(menu_bar, tearoff=0)
menu2.add_command(label="About Us", command=lambda: messagebox.showinfo("About Us",
                                                                        "This is a Chat Bot made by Divyam Mathur. If you liked his effort go Appreciate him."))
menu2.add_command(label="Version", command=lambda: messagebox.showinfo("Version", "V 1.0"))
menu1.add_command(label="Exit", command=quit)
menu3.add_command(label="Co-ordinates", command=debug)
menu_bar.add_cascade(label="File", menu=menu1)
menu_bar.add_cascade(label="About", menu=menu2)
menu_bar.add_cascade(label="Debug", menu=menu3)

# Placing objects

# frame1.pack()
frame1.place(x=0, y=0, width=450, height=340)
frame2.place(x=0, y=340, width=450)
frame3.place(x=0, y=415, width=450)
frame3.configure(width=500)
sub_button.grid(columnspan=1, column=0, row=0)
msg_window.grid(columnspan=2, ipadx=43, ipady=11, column=1, row=0)

root.config(menu=menu_bar)

root.mainloop()
