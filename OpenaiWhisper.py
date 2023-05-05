import os
import openai  # pip install openai
import tkinter as tk
import customtkinter as ctk
import ttkbootstrap as ttk
from tkinter import filedialog
from fpdf import FPDF
import re 
from dotenv import load_dotenv
load_dotenv()


#openai.api_key = os.getenv("OPENAI_KEY")

'''user_prompt = "cat wearing red cape"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

f = open('C:/Users/Dr/Downloads/FF audio/postBUp/Audio 2023/dg0324a$440_TGaS _ Global Commercial Operations Interview-20230322_090350-Meeting Recording [PART 1] Unit 1.mp3', "rb")
transcript = openai.Audio.transcribe("whisper-1", f)
#print(transcript["text"])'''

ziada = ctk.CTk()
ziada.title('Transcription App(Whisper)')
ziada.geometry('1280x720+300x200')
ziada.config(bg='orange')

frm_header = ctk.CTkFrame(ziada, bg_color='black')
frm_header.grid(row=0, column=0, columnspan=3)
frm_sidenav = ctk.CTkFrame(ziada, bg_color='white')
frm_sidenav.grid(row=1, column=0, )
frm_body = ctk.CTkFrame(ziada, bg_color='white')
frm_body.grid(row=1, column=1, columnspan=2)
#==========font variables=================================================
f_header = ('helvetica', 80, 'bold')
f_sidelbl = ('helvetica',10, 'normal')
bg_sidelbl = 'grey'

#================In frm_header============================================================================
lbl_header = ctk.CTkLabel(frm_header, text="Ziada Transcription Agency", text_color='indigo', bg_color='grey', font=f_header, padx=10)
lbl_header.grid()

#===============In frm_body==================================================================================
frm_bodytp = ctk.CTkFrame(frm_body, bg_color='grey')
frm_bodytp.grid(row=0,column=0, padx=4, pady=4)
frm_bodybt = ctk.CTkFrame(frm_body, bg_color='grey')
frm_bodybt.grid(row=1,column=0, pady=(2,2), padx=4)
frm_bodysv = ctk.CTkFrame(frm_body, bg_color='grey')
frm_bodysv.grid(row=2,column=0, pady=(2,2), padx=4) 

btn_bodytp1 = ctk.CTkButton(frm_bodytp, text="play.ico", text_color='indigo', bg_color='green')
btn_bodytp1.grid(row=0,column=0, padx=4)
btn_bodytp2 = ctk.CTkButton(frm_bodytp, text="rew.ico", text_color='indigo', bg_color='green')
btn_bodytp2.grid(row=0,column=1, padx=4)
btn_bodytp3 = ctk.CTkButton(frm_bodytp, text="pause.ico", text_color='indigo', bg_color='green')
btn_bodytp3.grid(row=0,column=2, padx=4)
btn_bodytp4 = ctk.CTkButton(frm_bodytp, text="fwd.ico", text_color='indigo', bg_color='green')
btn_bodytp4.grid(row=0,column=3, padx=4)

txt_body = ctk.CTkTextbox(frm_bodybt, width=700, height=500, bg_color='white')
txt_body.grid(row=0,column=0)

#==================In frm_sidenav==========================================================================
lbl_key = ctk.CTkLabel(frm_sidenav, text='Api Key: ', font=f_sidelbl,text_color='indigo')
lbl_key.grid(row=0, column=0, pady=(40,10), padx=(30,10))
ent_key = ctk.CTkEntry(frm_sidenav, textvariable='', placeholder_text='enter key here',bg_color='cyan', width=200)
ent_key.grid(row=0, column=1, pady=(40,10),padx=(0,30))
lbl_info = ctk.CTkLabel(frm_sidenav, text='To get your key go to: platform/openai', font=f_sidelbl, text_color='indigo')
lbl_info.grid(row=1, column=0, columnspan=2, pady=(40,10), padx=(30,10))

def selectFile():#Opens file directory for file selection
    path = filedialog.askopenfilename()
    print(path)
    s_path = re.split('/',path)
    file_name = s_path[-1]
    #Show file_name label
    lbl_name.configure(text=file_name)
    def transcribe():#Takes openai_key and transcribes selected file
        openai.api_key = ent_key.get()
        f = open(path, "rb")
        transcript = openai.Audio.transcribe("whisper-1", f)
        txt_body.insert(1.0,transcript["text"])
        btn_trs.grid_forget()

        def saveTranscript():#Saves the selected transcript as pdf format
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("times",size=12)
            pdf.text(10,10,txt=txt_body.get(1.0))
            pdf.output("pdf.pdf")
            ent_key.delete(0, 1)
            ent_key.focus()
            txt_body.delete(1.0,2.0)
            btn_save.grid_forget()


        btn_save = ctk.CTkButton(frm_bodysv, text='Save as PDF', text_color='yellow', bg_color='cyan',command=saveTranscript)
        btn_save.grid(row=0, column=0,columnspan=2, pady=(5,5))
    
    
    btn_trs = ctk.CTkButton(frm_sidenav, text='Transcribe Me', text_color='yellow', bg_color='cyan', command=transcribe)
    btn_trs.grid(row=4, column=0,columnspan=2, pady=(0,50))

lbl_name = ctk.CTkLabel(frm_sidenav, text='', font=f_sidelbl, text_color='indigo')
lbl_name.grid(row=3, column=0, columnspan=2, pady=(10,10), padx=(5,5))
btn_file = ctk.CTkButton(frm_sidenav, text='Select MP3 File', text_color='yellow', bg_color='cyan',command=selectFile)
btn_file.grid(row=2, column=0,columnspan=2, pady=(10,200))


ziada.columnconfigure(0, weight=1)
ziada.columnconfigure(1, weight=1)
ziada.rowconfigure(0, weight=1)
ziada.rowconfigure(1, weight=2)

ziada.mainloop()
