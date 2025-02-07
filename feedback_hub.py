# Importing Modules
from tkinter import *
from tkinter import messagebox
import os
import datetime
import smtplib
import threading
from email.message import EmailMessage
from enc_dec import decrypt


# Defining Functions

def hub():
    def sub_feed():
        # Connecting to feedback file
        demo = open("demo.txt", 'a')
        demo.write("Date: {}\n".format(datetime.datetime.now()))
        demo.write("Feedback for Raven\n")
        demo.write("Summary: {}".format(str(summarise_entry.get("1.0", END))))
        demo.write("Description: {}\n".format(str(desc_entry.get("1.0", END))))
        demo.close()

        decrypt("credentials.txt")
        credentials = open("decryptedcredentials.txt")
        email = credentials.readline()
        password = credentials.readline()

        credentials.close()

        msg = EmailMessage()
        msg['Subject'] = "Raven Feedback"
        msg['From'] = "divyam.mathur12042004@gmail.com"
        msg['To'] = "divyam.mathur12042004@gmail.com"
        msg.set_content("See the Attachment for Feedback")

        demo = open("demo.txt", 'rb')
        demo_data = demo.read()
        demo_name = demo.name

        msg.add_attachment(demo_data, maintype='application', subtype='octet-stream', filename=demo_name)
        demo.close()

        messagebox.showinfo("INFO", "Your feedback is being submitted to the server, please be patient.")

        root2.lift()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)

        messagebox.showinfo("INFO", "Thank You for your feedback.")

        os.remove("decryptedcredentials.txt")

        root2.destroy()

    root2 = Tk()
    root2.geometry('500x200')
    root2.title("Feedback Hub")
    root2.iconbitmap("raven.ico")
    root2.wm_resizable(0, 0)

    # Feedback Hub Interface
    summarise_entry = Text(root2, font="Ariel 14", height=1, width=28)
    summarise_entry.place(x=180, y=0)

    desc_entry = Text(root2, font="Ariel 14", height=5, width=28)
    desc_entry.place(x=180, y=40)

    summarise_label = Label(root2, text="Summarise your feedback", font=("Ariel Bold", 11))
    summarise_label.grid(column=0, row=0)

    desc_label = Label(root2, text="Explain in more detail", font=("Ariel Bold", 12))
    desc_label.place(x=0, y=40)

    empty_lbl = Label(root2)
    empty_lbl.grid(column=1, row=1)

    sub_fed = Button(root2, command=lambda: threading.Thread(target=sub_feed).start(), text="Submit", width=9, height=1)
    sub_fed.place(x=120, y=170)

    cancel_but = Button(root2, command=root2.destroy, text="Cancel", width=9, height=1)
    cancel_but.place(x=250, y=170)

    root2.mainloop()


if __name__ == "__main__":
    hub()
