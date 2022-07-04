from tkinter import *


def create_label(tk_type, _text, pos:tuple):
    my_label = Label(tk_type, text=_text)
    place_x, place_y, offset = pos
    my_label.place(relx=place_x, rely=place_y, anchor=offset)
    return my_label


def create_entry(tk_type, _width, pos:tuple):
    my_label = Entry(tk_type, width=_width)
    place_x, place_y, offset = pos
    my_label.place(relx=place_x, rely=place_y, anchor=offset)
    return my_label


def create_text(tk_type: Tk(), text_: str, font_parameter:tuple, place_parameter:tuple):
    my_label = Label(tk_type, text=text_)
    my_label.configure(font=font_parameter)
    place_x, place_y, offset = place_parameter
    my_label.place(relx=place_x, rely=place_y, anchor=offset)
    return my_label


def create_button(tk_type, _text, pos:tuple, on_execute_command):
    my_button = Button(tk_type, text=_text, command=on_execute_command)
    place_x, place_y, offset = pos
    my_button.place(relx=place_x, rely=place_y, anchor=offset)
    return my_button
