from tkinter import *
from tkinter import filedialog
from turtle import heading
from PIL import Image
import pytesseract #need to install pytesseract.exe from google
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from googletrans import Translator #googletrans==3.1.0a0
from gtts import gTTS
from playsound import playsound  #playsound==1.2.2
import docx
import os
from tkinter.filedialog import asksaveasfilename
from tktooltip import ToolTip
from tkinter import scrolledtext

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# import cv2
# from pytesseract import Output

pad = 3
root = Tk()
root.state('zoomed')
root.configure(background='#eddcd9')
root.title('Image Processing using OCR')
root.iconbitmap("icon.ico")

#heading
Title=Label(root, text='Image Processing Using OCR', background='#eddcd9',
                     font='poppins  20 bold',)
Title.place(x=30,y=10)


# functions
# select image function

def selectimg():
    global img
    textarea.delete(1.0, END)
    f_types = [('png Files', '*.png'), ('Jpg Files', '*.jpg'),
               ('Jpeg Files', '*.jpeg'), ('webp files', '*.webp')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    
    path = filename
    img = Image.open(path)
    image = img.convert('L')

    image.save('temp.png')
    text = pytesseract.image_to_string(Image.open('temp.png'),
            lang='eng+hin+kan')
    textarea.insert(END, text)

    # for count

    text = textarea.get('1.0', 'end-1c')

    word_count = len(text.split())
    letter_count = len([char for char in text if char.isalpha()])
    number_count = len([char for char in text if char.isnumeric()])
    sentence_count = len([char for char in text if char in ['.', '?',
                         '!']])

    w = 'Words:' + str(word_count) + '  Letters:' + str(letter_count) \
        + '  Numbers:' + str(number_count) + '  Sentenses :' \
        + str(sentence_count)

    heading = Label(root, text=w, background='#eddcd9',
                     font='poppins  10 bold',)
    heading.pack()
    heading.place(x=30, y=690)



# savefile dialogbox

def saveasdocx():
    text = textarea2.get('1.0', 'end-1c')
    if text == '':
        messagebox.showerror('Save Docx', 'there is no text to save')
    else:
        doc = docx.Document()
        doc.add_paragraph(text)
        file_path = asksaveasfilename(defaultextension='.docx',
                filetypes=[('Word Document', '*.docx')])
        
        doc.save(file_path)
        messagebox.showinfo('Save Docx', 'document saved')


# encoding='utf-8'

# translator

def translate():
    ta = textarea.get('1.0', 'end-1c')
    choosl = cl.get()

    if ta == '':
        messagebox.showerror('translator',
                             'there is no text to translate')
    else:
        textarea2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(ta, dest=choosl)
        textarea2.insert('end', output.text)

    # font count

    text = textarea2.get('1.0', 'end-1c')

    word_count = len(text.split())
    letter_count = len([char for char in text if char.isalpha()])
    number_count = len([char for char in text if char.isnumeric()])
    sentence_count = len([char for char in text if char in ['.', '?',
                         '!']])

    w = 'Words:' + str(word_count) + '  Letters:' + str(letter_count) \
        + '  Numbers:' + str(number_count) + '  Sentenses :' \
        + str(sentence_count)

    heading1 = Label(root, text=w, background='#eddcd9',
                      font='poppins  10 bold')
    heading1.pack()
    heading1.place(x=690, y=690)


# speak

def speak():
    text2 = textarea2.get('1.0', 'end-1c')
    if text2 == '':
        messagebox.showerror('Alert', 'There is nothing to speak')
    else:
        audio = gTTS(text2)
        audio.save('text.mp3')
        playsound('text.mp3')
        os.remove('text.mp3')


# uplde button

selimg = Button(
    root,
    text='Select Image',
    command=selectimg,
     font='poppins  10 bold',   
    width=12,
    height=2,
    background='#de5499',
    foreground='white',
    relief="flat"
    )
selimg.pack()
selimg.place(x=40, y=60)

# drop down list

l = tk.StringVar()
cl = ttk.Combobox(root, width=15, textvariable=l, state='randomly',
                   font='poppins  10',)
cl['values'] = (
    'english',
    'hindi',
    'kannada',
    'afrikaans',
    'albanian',
    'amharic',
    'arabic',
    'armenian',
    'azerbaijani',
    'basque',
    'belarusian',
    'bengali',
    'bosnian',
    'bulgarian',
    'catalan',
    'cebuano',
    'chichewa',
    'chinese (simplified)',
    'chinese (traditional)',
    'corsican',
    'croatian',
    'czech',
    'danish',
    'dutch',
    'esperanto',
    'estonian',
    'filipino',
    'finnish',
    'french',
    'frisian',
    'galician',
    'georgian',
    'german',
    'greek',
    'gujarati',
    'haitian creole',
    'hausa',
    'hawaiian',
    'hebrew',
    'hebrew',
    'hmong',
    'hungarian',
    'icelandic',
    'igbo',
    'indonesian',
    'irish',
    'italian',
    'japanese',
    'javanese',
    'kannada',
    'kazakh',
    'khmer',
    'korean',
    'kurdish (kurmanji)',
    'kyrgyz',
    'lao',
    'latin',
    'latvian',
    'lithuanian',
    'luxembourgish',
    'macedonian',
    'malagasy',
    'malay',
    'malayalam',
    'maltese',
    'maori',
    'marathi',
    'mongolian',
    'myanmar (burmese)',
    'nepali',
    'norwegian',
    'odia',
    'pashto',
    'persian',
    'polish',
    'portuguese',
    'punjabi',
    'romanian',
    'russian',
    'samoan',
    'scots gaelic',
    'serbian',
    'sesotho',
    'shona',
    'sindhi',
    'sinhala',
    'slovak',
    'slovenian',
    'somali',
    'spanish',
    'sundanese',
    'swahili',
    'swedish',
    'tajik',
    'tamil',
    'telugu',
    'thai',
    'turkish',
    'ukrainian',
    'urdu',
    'uyghur',
    'uzbek',
    'vietnamese',
    'welsh',
    'xhosa',
    'yiddish',
    'yoruba',
    'zulu',
    )
cl.current(0)
cl.pack()
cl.place(x=160, y=70)

# digital document

textarea = Text(root, width=80, height=34,relief="flat")
textarea = scrolledtext.ScrolledText(root, width=80, height=34,)
textarea.place(x=25, y=140)

textarea2 = Text(root, width=80, height=34,relief="flat")
textarea2 = scrolledtext.ScrolledText(root, width=80, height=34)
textarea2.place(x=695, y=140)

# speak button``

start = Button(
    root,
    text='Start',
    command=translate,
     font='poppins  10 bold',
    width=12,
    height=2,
    background='#48494d',
    foreground='white',
    relief="flat"
    )
start.pack()
start.place(x=330, y=60)

# start button

speak = Button(
    root,
    text='Speak',
    command=speak,
     font='poppins  10 bold',
    width=12,
    height=2,
    background='#48494d',
    foreground='white',
    relief="flat"
    )
speak.pack()
speak.place(x=450, y=60)

# save button

saveasdoc = Button(
    root,
    text='Save as DOCX',
    command=saveasdocx,
     font='poppins  10 bold',
    width=12,
    background='#e99f4c',
    foreground='#264143',
    relief="flat"
    )
saveasdoc.pack()

saveasdoc.place(x=570, y=65)


# clear

def clear():
 textarea.delete('1.0', 'end')
 textarea2.delete('1.0', 'end')


    
    

c = Button(
    root,
    text='Clear',
    command=clear,
     font='poppins  10 bold',
    width=12,
    background='#e99f4c',
    foreground='#264143',
    relief="flat"
    )
c.pack()
c.place(x=1040, y=65)


# replace

def find_replace():
    text = textarea2.get('1.0', 'end-1c')
    if text == '':
        messagebox.showerror('Alert', 'There is nothing to replace')
    else:

    # Perform find and replace

        find_word = find_entry.get()
        replace_word = replace_entry.get()
        replaced_text = text.replace(find_word, replace_word)

    # Update the text widget with the replaced text

        textarea2.delete('1.0', 'end')
        textarea2.insert('1.0', replaced_text)

        messagebox.showinfo('Replacement',
                            'Words replaced successfully.')


find_label = tk.Label(root, text='Find Word:')
find_label.pack()
find_label.place(x=690, y=55)
find_entry = tk.Entry(root,relief="flat")
find_entry.pack()
find_entry.place(x=780, y=55)

replace_label = tk.Label(root, text='Replace word:')
replace_label.pack()
replace_label.place(x=690, y=85)
replace_entry = tk.Entry(root,relief="flat")
replace_entry.pack()
replace_entry.place(x=780, y=85)

replace_button = Button(
    root,
    text='Replace',
    font='poppins  10 bold',
    width=12,
    background='#e99f4c',
    foreground='#264143',
    command=find_replace,
    relief="flat"
    )
replace_button.pack()
replace_button.place(x=920, y=65)






# button hoverhand
def on_enter(event):
    start.config(cursor='hand2')
    selimg.config(cursor='hand2')
    speak.config(cursor='hand2')
    saveasdoc.config(cursor='hand2')
    replace_button.config(cursor='hand2')
    c.config(cursor='hand2')
    #tooltips
    ToolTip(selimg,msg="select image to extract text",delay=1)
    ToolTip(start,msg="translate to selcted text language",delay=1)
    ToolTip(speak,msg="speak translated text",delay=1)
    ToolTip(saveasdoc,msg="save as docx to local storage",delay=1)
    ToolTip(replace_button,msg="replace the word from translated textbarea",delay=1)
    ToolTip(c,msg="clear the both textarea",delay=1)

def on_leave(event):
    start.config(cursor='')
    selimg.config(cursor='')
    speak.config(cursor='')
    saveasdoc.config(cursor='')
    replace_button.config(cursor='')
    c.config(cursor='')  # Restore the default cursor on mouse leave

start.bind("<Enter>", on_enter) 
start.bind("<Leave>", on_leave)
selimg.bind("<Enter>", on_enter) 
selimg.bind("<Leave>", on_leave)
speak.bind("<Enter>", on_enter) 
speak.bind("<Leave>", on_leave)
saveasdoc.bind("<Enter>", on_enter) 
saveasdoc.bind("<Leave>", on_leave)
replace_button.bind("<Enter>", on_enter) 
replace_button.bind("<Leave>", on_leave)
c.bind("<Enter>", on_enter) 
c.bind("<Leave>", on_leave)

# v=Scrollbar(root, orient='vertical')
# v.config(command=textarea.yview)
# textarea.pack()

root.mainloop()
