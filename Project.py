import swiftclient
import os
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename

fnam = ''
user = 'satyateja27'
key = 'satya@27'
container_name = 'my-new-container'
top = tkinter.Tk()
file_var = tkinter.StringVar(top, name='file_var')
command = lambda: open_file_handler(file_var)
comm=lambda: list_containers()

def open_file_handler(file_var):
    file_name = askopenfilename()
    file_var.set(file_name)
    helloCallBack(file_name)
    fn=file_name


def setup_connection():
    try:
        conn = swiftclient.Connection(
            user=user,
            key=key,
            authurl='http://52.53.194.27/auth/v1.0',
        )
    except Exception as e:
        print ("Authorization error.")
    return conn

def list_containers():
    res=""
    conn = setup_connection()
    try:
        for container in conn.get_account()[1]:
            res = res +  container['name'] + "\n"
    except Exception as e:
        res = e
    messagebox.showinfo("containers", res)


def helloCallBack(abc):
    upload(abc)
    messagebox.showinfo("abc",abc)


def upload(fnam):
    (head, tail)=os.path.split(fnam)
    print(tail)
    conn=setup_connection()
    try:
        fp = open(fnam, "r")
    except Exception as r:
        print ("couldn't open file")
    try:
        container_name = 'container3'
        with open(tail, 'r') as hello_file:
            conn.put_object(container_name, 'helo.txt',
                            contents= hello_file.read(),
                            content_type='text/plain')
        result="cont"
    except Exception as e:
        print (e)
        result = e
    print (result)


def main():
    title = Label(top, text="Welcome to the Swift Object Store")
    title.pack(fill=X)
    title = Label(top, text=" ")
    title.pack(fill=X)
    footer = Label(top, text="(Connected to server)")
    footer.pack(fill=X)
    title = Label(top, text=" ")
    title.pack(fill=X)
    title = Label(top, text="1. Select the files to be uploaded into Swift Object Store")
    title.pack(fill=X)
    conn=setup_connection()
    open_file = tkinter.Button(top, command=command,
                               padx=100, text="Upload")

    open_file.pack()
    title = Label(top, text=" ")
    title.pack(fill=X)
    title = Label(top, text="2. Click the button to view the Containers present in the Object Store")
    title.pack(fill=X)
    list_containers = tkinter.Button(top, command=comm,
                                     padx=100, text="List Containers")
    list_containers.pack()
    file_name = file_var.get()
    top.mainloop()

if __name__ == "__main__":
    main()