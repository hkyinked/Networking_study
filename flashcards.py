from tkinter import *
from random import randint

root = Tk()
root.title ('Networking/Hardware Knowledge Flashcards')
root.geometry("550x310")


#question and terms along with the corresponding answers 
term = [
    (("Describe Single Mode Fiber"),("single strand of light")),
    (("What is a Vlan"),("logically segmented local area network")),
    (("What does the command Grep do"),("displays a matchs for given pattern")),
    (("What is the boot sequence"),("Bios,MBR,GRUB,KERNEL,INIT,Runlevel")),
    (("What is a process fork"),("When the system creates a copy of a process; they are identical in execution contents including execution thread, signal, handlers.")),
    (("Describe umnount"),("the command to unmount a previously mounted media(device, directory or file system)")),
    (("What is a Zombie Process"),("When a process has been killed but not fully terminated due to being blocked on resources; not harmful as it does not utilize any cpu or memory usage")),
    (("What are Inodes"),("Contain all info on a file and directory EXCEPT the actual data and filename (ex. file size, device id, user id, group id, timestamps)")),
    (("How would you check Load Averages"),("Cat /proc/loadavg; htop or top; uptime;(lower is better)")),
    
]

#Get count of our word list
count = len(term)

def next():
    answer_label.config(text="")

    # Create random selection
    global rando
    rando = randint(0, count-1)
    #update label with question
    question.config(text=term[rando][0])

def done ():
    #update label with answer
    answer_label.config(text=term[rando][1], wraplength=500)

#labels
question = Label(root, text="", font=("Helvetica", 18))
question.pack(pady=30)

answer_label = Label(root, text="", font=("Helvetica", 13))
answer_label.pack(pady=30)


# Create some buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=done)
answer_button.grid(row=0, column=2, padx=20)

forward_button = Button(button_frame, text="Next", command=next)
forward_button.grid(row=0, column=3, padx=20)

# Run next function when program starts
next()


root.mainloop()