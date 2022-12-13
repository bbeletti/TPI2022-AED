import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label,ttk,messagebox,TOP,LEFT,RIGHT
from pathlib import Path
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def mostrar_frame(frame):
    frame.tkraise()
def login(login_type):
    if login_type == "normal":
        login_state = 0
        userCidi = entry_f17_1.get()
        passCidi = entry_f17_2.get()
        try_credenciales = passCidi + ' ' + userCidi+ "\n"
        credenciales = open("archivos\Credenciales.txt","r")
        strcredenciales = credenciales.readlines()
        cant_user = int(strcredenciales[0])
        for u in range(1, cant_user):
            if try_credenciales == strcredenciales[u]:
                #inicio de session exitoso
                credenciales.close()
                login_state = 1
                mostrar_frame(frame8)
        if login_state == 0:
            credenciales.close()
            messagebox.showerror("inicio de sesion", "Las credenciales son incorrectas")
    if login_type == "admin":
        login_state = 0
        userAdmin = entry_f11_1.get()
        passAdmin = entry_f11_2.get()
        try_credenciales = passAdmin + ' ' + userAdmin+ "\n"
        credenciales = open("archivos\Credenciales.txt","r")
        strcredenciales = credenciales.readlines()
        cant_user = int(strcredenciales[0])
        cant_admin = int(strcredenciales[cant_user+1])
        for u in range(cant_user+2, cant_user+cant_admin+2): #2 param cidi, admin
            if try_credenciales == strcredenciales[u]:
                #inicio de session exitoso
                credenciales.close()
                login_state = 1
                mostrar_frame(frame0)
        if login_state == 0:
            credenciales.close()
            messagebox.showerror("inicio de sesion", "Las credenciales son incorrectas")


window=tk.Tk()

window.geometry("1280x700")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame0 = tk.Frame(window)
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window) 
frame6 = tk.Frame(window)
frame7 = tk.Frame(window)
frame8 = tk.Frame(window)
frame9 = tk.Frame(window)
frame10 = tk.Frame(window)
frame11 = tk.Frame(window)
frame12 = tk.Frame(window)
frame13 = tk.Frame(window)
frame14 = tk.Frame(window)
frame15 = tk.Frame(window)
frame16 = tk.Frame(window)
frame17 = tk.Frame(window)
frame18 = tk.Frame(window)

for frame in (frame0, frame1, frame2,frame3, frame4, frame5, frame6, frame7, frame8, 
frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16, frame17,frame18):
    frame.grid(row=0, column=0, sticky='nsew')
    
#===============================canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
def actualizarStats():
    graficos()
    mostrar_frame(frame6)
    return

#===============================frame 0
background_f0 = PhotoImage(
    file=Path(r"assets\frame0\image_1.png"))
label0 = Label( frame0, image = background_f0)
label0.place(x = 0, y = 0)  

button_f0_image_1 = PhotoImage(
    file=Path(r"assets\frame0\button_1.png"))
button_f0_1 = Button(
    frame0,
    image=button_f0_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f0_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

button_f0_image_2 = PhotoImage(
    file=Path(r"assets\frame0\button_2.png"))
button_2 = Button(
    frame0,
    image=button_f0_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame18),
    relief="flat"
)
button_2.place(
    x=236.0,
    y=195.0,
    width=221.0,
    height=86.0
)

button_f0_image_3 = PhotoImage(
    file=Path(r"assets\frame0\button_3.png"))
button_3 = Button(
    frame0,
    image=button_f0_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame4),
    relief="flat"
)
button_3.place(
    x=529.0,
    y=195.0,
    width=221.0,
    height=86.0
)

button_f0_image_4 = PhotoImage(
    file=Path(r"assets\frame0\button_4.png"))
button_4 = Button(
    frame0,
    image=button_f0_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame13),
    relief="flat"
)
button_4.place(
    x=822.0,
    y=195.0,
    width=221.0,
    height=86.0
)

button_f0_image_5 = PhotoImage(
    file=Path(r"assets\frame0\button_5.png"))
button_5 = Button(
    frame0,
    image=button_f0_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame12),
    relief="flat"
)
button_5.place(
    x=236.0,
    y=347.0,
    width=221.0,
    height=86.0
)

button_f0_image_6 = PhotoImage(
    file=Path(r"assets\frame0\button_6.png"))
button_f0_6 = Button(
    frame0,
    image=button_f0_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame14),
    relief="flat"
)
button_f0_6.place(
    x=529.0,
    y=347.0,
    width=221.0,
    height=86.0
)

button_f0_image_7 = PhotoImage(
    file=Path(r"assets\frame0\button_7.png"))
button_f0_7 = Button(
    frame0,
    image=button_f0_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: actualizarStats(),
    relief="flat"
)
button_f0_7.place(
    x=529.0,
    y=482.0,
    width=221.0,
    height=86.0
)

button_f0_image_8 = PhotoImage(
    file=Path(r"assets\frame0\button_8.png"))
button_f0_8 = Button(
    frame0,
    image=button_f0_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame15),
    relief="flat"
)
button_f0_8.place(
    x=822.0,
    y=347.0,
    width=221.0,
    height=86.0
)


#===============================frame 0

#===============================frame 1

def actualizartodo():
    entry_f1_2['values'] = puesto()
    entry_f1_3['values'] = localidad()
    entry_f1_5['values'] = depto()
    entry_f1_4['values'] = infraccion()
    return
def guardar():
    fileDenuncia=open(r'archivos/denunciacidi.txt','a+')
    fileUsuario=open(r'archivos/usuariocidi.txt', 'a+')
    cantidad = []
    auxiliar=''
    hoy=date.today()
    error1=True
    error2=True
    error3=True
    error4=True
    error5=True
    entry1D=entry_f1_1.get('1.0', 'end-1c') #deescripcion
    entry2D=entry_f1_2.get() #paraje
    entry3D=entry_f1_3.get() #localidad
    entry5D=entry_f1_5.get() #departamento
    entry4D=entry_f1_4.get() #subtipo
    entry6D=entry_f1_6.get() #nombre del denunciado
    entry7D=entry_f1_7.get() #mail
    entry8D=entry_f1_8.get() #numero de telefono del denunciante
    entry9D=entry_f1_9.get() #nombre del denunciante
    if len(entry8D)==10:
        try:
            int(entry8D)
        except:

            messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
            return
    else:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in depto():
        if i==entry5D:
            error3=False
    if error3==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in puesto():
        if i==entry2D:
            error4=False
    if error4==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in localidad():
        if i==entry3D:
            error5=False
    if error5==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in infraccion():
        if i==entry4D:
            error2=False
    if error2==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in range(len(entry7D)):
        if (entry7D[i:len(entry7D)]=='@gmail.com' or entry7D[i:len(entry7D)]=='@hotmail.com' or entry7D[i:len(entry7D)]=='@outlook.com'):
            error1=False
    if error1==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return

    cadenas = entry1D.split('\n')
    for i in cadenas:
        auxiliar+=i+' '
    entry1D=auxiliar

    fileDenuncia.seek(0)
    fileanoni=open('archivos/denunciaanon.txt','r')
    cantidad1=fileanoni.readlines()
    fileanoni.close()
    cantidad = fileDenuncia.readlines()
    number = len(cantidad)+len(cantidad1)
    numberaux = number
    if numberaux < 10:
        numberstr = str(number)
        ndenuncia = "0" + numberstr
    if numberaux < 100:
        ndenuncia = "0" + ndenuncia
    
    denuncia =''
    usuario =''
    denuncia+=ndenuncia+'|'+str(hoy)+'|'+entry4D+'|'+entry3D+'|'+entry1D+'|'+'programado'+'|'+entry5D+'|'+entry2D+'|'+entry6D
    fileDenuncia.write(denuncia+'\n')

    usuario+=entry7D+'|'+entry9D+'|'+entry8D+'|'+ndenuncia
    fileUsuario.write(usuario+'\n')
    fileUsuario.close()
    fileDenuncia.close()
    messagebox.showinfo('guardado','se ha guardado su denuncia')
    mostrar_frame(frame8)
    return 

def depto():
    depart=open('archivos/departamentos.txt','r')
    departamentos=[]
    for linea in depart:
        linea=str(linea)
        departamentos.append(linea[0:len(linea)-1])
    depart.close()
    return departamentos

def localidad():
    local=open('archivos/localidades.txt','r')
    localidades=[]
    for linea in local:
        linea=str(linea)
        localidades.append(linea[0:len(linea)-1])
    local.close()
    return localidades
#Devuelve un string con el contenido de infraccion.txt
def puesto():
    para=open('archivos/paraje.txt','r')
    parajes=[]
    for linea in para:
        linea=str(linea)
        parajes.append(linea[0:len(linea)-1])
    para.close()
    return parajes

#Devuelve un string con el contenido de infraccion.txt
def infraccion():
    infrac=open('archivos/infraccion.txt','r')
    infraccion=[]
    for linea in infrac:
        linea=str(linea)
        infraccion.append(linea[0:len(linea)-1])
    infrac.close()
    return infraccion


background_f1 = PhotoImage(
    file=Path(r"assets\frame1\image_1.png"))
label1 = Label( frame1, image = background_f1)
label1.place(x = 0, y = 0)  

button_f1_image_1 = PhotoImage(
    file=Path(r"assets\frame1\button_1.png"))
button_f1_1 = Button(
    frame1,
    image=button_f1_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=guardar,
    relief="flat"
)
button_f1_1.place(
    x=882.0,
    y=598.0,
    width=148.0,
    height=46.0
)

entry_f1_image_1 = PhotoImage(
    file=Path(r"assets\frame1\entry_1.png"))

entry_f1_1 = Text(
    master=frame1,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f1_1.place(
    x=712.0,
    y=490.0,
    width=318.0,
    height=98.0
)

entry_f1_image_2 = PhotoImage(
    file=Path(r"assets\frame1\entry_2.png"))

entry_f1_2 = ttk.Combobox( #paraje
    frame1,
    values=puesto()
)
entry_f1_2.place(
    x=712.0,
    y=404.0,
    width=318.0,
    height=48.0
)

entry_f1_image_3 = PhotoImage(
    file=Path(r"assets\frame1\entry_3.png"))

entry_f1_3 = ttk.Combobox( #localidad
    frame1,
    values=localidad()
)
entry_f1_3.place(
    x=712.0,
    y=312.0,
    width=318.0,
    height=48.0
)

entry_f1_image_5 = PhotoImage(
    file=Path(r"assets\frame1\entry_4.png"))

entry_f1_5 = ttk.Combobox( #departamento
    frame1,
    values=depto()
)
entry_f1_5.place(
    x=712.0,
    y=224.0,
    width=318.0,
    height=48.0
)

entry_f1_image_4 = PhotoImage(
    file=Path(r"assets\frame1\entry_5.png"))

entry_f1_4 = ttk.Combobox( #subtipo
    frame1,
    values=infraccion()
)
entry_f1_4.place(
    x=273.0,
    y=558.0,
    width=318.0,
    height=48.0
)

entry_f1_image_6 = PhotoImage(
    file=Path(r"assets\frame1\entry_6.png"))

entry_f1_6 = Entry(
    frame1,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f1_6.place(
    x=273.0,
    y=475.0,
    width=318.0,
    height=48.0
)

entry_f1_image_7 = PhotoImage(
    file=Path(r"assets\frame1\entry_7.png"))

entry_f1_7 = Entry( #correo del denunciante
    frame1,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f1_7.place(
    x=273.0,
    y=392.0,
    width=318.0,
    height=48.0
)

entry_f1_image_8 = PhotoImage(
    file=Path(r"assets\frame1\entry_8.png"))

entry_f1_8 = Entry( #numero de telefono del denunciante
    frame1,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f1_8.place(
    x=273.0,
    y=309.0,
    width=318.0,
    height=48.0
)

entry_f1_image_9 = PhotoImage(
    file=Path(r"assets\frame1\entry_9.png"))

entry_f1_9 = Entry( #nombre del denunciante
    frame1,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f1_9.place(
    x=273.0,
    y=226.0,
    width=318.0,
    height=48.0
)

button_f1_image_2 = PhotoImage(
    file=Path(r"assets\frame1\button_2.png"))
button_f1_2 = Button(
    frame1,
    image=button_f1_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame8),
    relief="flat"
)
button_f1_2.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
Atras = Button(
    borderwidth=0,
    highlightthickness=0,
    command=lambda:atras(),
    relief="flat",
    text='<',
)
Atras.place(
    x=882.0,
    y=598.0,
    width=35.0,
    height=35.0
)
siguiente = Button(
    borderwidth=0,
    highlightthickness=0,
    command=lambda:sig(),
    relief="flat",
    text='>',
)
siguiente.place(
    x=1102.0,
    y=598.0,
    width=35.0,
    height=35.0,
)
#===============================frame 1

#===============================frame 2
def actualizaranon():
    entry_f2_2['values']=puesto()
    entry_f2_3['values']=localidad()
    entry_f2_4['values']=depto()
    entry_f2_5['values']=infraccion()
    return

def guardar():
    fileDenunciaAnon=open('archivos/denunciaanon.txt','a+')
    fileUsuarioAnon=open('archivos/usuarioanon.txt', 'a+')
    cantidad = []
    auxiliar=''
    hoy=date.today()
    error1=True
    error2=True
    error3=True
    error4=True
    error5=True
    entry1D=entry_f2_1.get('1.0', 'end-1c')
    entry2D=entry_f2_2.get()
    entry3D=entry_f2_3.get()
    entry5D=entry_f2_5.get()
    entry4D=entry_f2_4.get()
    entry6D=entry_f2_6.get()
    entry7D=entry_f2_7.get()

    for i in depto():
        if i==entry4D:
            error3=False
    if error3==True:
        
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in puesto():
        if i==entry2D:
            error4=False
    if error4==True:
      
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in localidad():
        if i==entry3D:
            error5=False
    if error5==True:
       
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in infraccion():
        if i==entry5D:
            error2=False
    if error2==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    for i in range(len(entry7D)):
        if (entry7D[i:len(entry7D)]=='@gmail.com' or entry7D[i:len(entry7D)]=='@hotmail.com' or entry7D[i:len(entry7D)]=='@outlook.com'):
            error1=False
    if error1==True:
        messagebox.showinfo('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return

    cadenas = entry1D.split('\n')
    for i in cadenas:
        auxiliar+=i+' '
    entry1D=auxiliar

    fileDenunciaAnon.seek(0)
    filecidi=open('archivos/denunciacidi.txt','r')
    cantidad1=filecidi.readlines()
    filecidi.close()
    cantidad = fileDenunciaAnon.readlines()
    number = len(cantidad)+len(cantidad1)
    numberaux = number
    ndenunciaanon=''
    if numberaux < 10:
        numberstr = str(number)
        ndenunciaanon = "0" + numberstr
    if numberaux < 100:
        ndenunciaanon = "0" + ndenunciaanon
    
    
    denuncia =''
    usuario =''
    denuncia+=ndenunciaanon+'|'+str(hoy)+'|'+entry5D+'|'+entry3D+'|'+entry1D+'|'+'programado'+'|'+entry4D+'|'+entry2D+'|'+entry6D
    fileDenunciaAnon.write(denuncia+'\n')

    usuario+=entry7D+'|'+ndenunciaanon
    fileUsuarioAnon.write(usuario+'\n')
    fileUsuarioAnon.close()
    fileDenunciaAnon.close()
    messagebox.showinfo('guardado','se ha guardado su denuncia')
    mostrar_frame(frame7)
    return 
background_f2 = PhotoImage(
    file=Path(r"assets\frame2\image_1.png"))
label2 = Label( frame2, image = background_f2)
label2.place(x = 0, y = 0)  

button_f2_image_1 = PhotoImage(
    file=Path(r"assets\frame2\button_1.png"))
button_f2_1 = Button(
    frame2,
    image=button_f2_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame7),
    relief="flat"
)
button_f2_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

button_f2_image_2 = PhotoImage(
    file=Path(r"assets\frame2\button_2.png"))
button_f2_2 = Button(
    frame2,
    image=button_f2_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=guardar,
    relief="flat"
)
button_f2_2.place(
    x=875.0,
    y=583.0,
    width=148.0,
    height=46.0
)

entry_f2_image_1 = PhotoImage(
    file=Path(r"assets\frame2\entry_1.png"))
entry_f2_bg_1 = canvas.create_image(
    865.5,
    477.0434265136719,
    image=entry_f2_image_1
)
entry_f2_1 = Text( #descripcion
    frame2,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f2_1.place(
    x=708.0,
    y=410.0869140625,
    width=315.0,
    height=131.91302490234375
)

entry_f2_image_2 = PhotoImage(
    file=Path(r"assets\frame2\entry_2.png"))
entry_f2_bg_2 = canvas.create_image(
    864.0,
    353.0,
    image=entry_f2_image_2
)
entry_f2_2 = ttk.Combobox(#paraje
    frame2,
    values=puesto()
)
entry_f2_2.place(
    x=705.0,
    y=328.0,
    width=318.0,
    height=48.0
)

entry_f2_image_3 = PhotoImage(
    file=Path(r"assets\frame2\entry_3.png"))
entry_f2_bg_3 = canvas.create_image(
    864.0,
    270.0,
    image=entry_f2_image_3
)
entry_f2_3 = ttk.Combobox(#localidad
    frame2,
    values=localidad()
)
entry_f2_3.place(
    x=705.0,
    y=245.0,
    width=318.0,
    height=48.0
)

entry_f2_image_4 = PhotoImage(
    file=Path(r"assets\frame2\entry_4.png"))
entry_bg_4 = canvas.create_image(
    415.0,
    519.0,
    image=entry_f2_image_4
)
entry_f2_4 = ttk.Combobox(#depto
    frame2,
    values=depto()
)
entry_f2_4.place(
    x=256.0,
    y=494.0,
    width=318.0,
    height=48.0
)

entry_f2_image_5 = PhotoImage(
    file=Path(r"assets\frame2\entry_5.png"))
entry_bg_5 = canvas.create_image(
    415.0,
    436.0,
    image=entry_f2_image_5
)
entry_f2_5 = ttk.Combobox(#infraccion
    frame2,
    values=infraccion()
)
entry_f2_5.place(
    x=256.0,
    y=411.0,
    width=318.0,
    height=48.0
)

entry_f2_image_6 = PhotoImage(
    file=Path(r"assets\frame2\entry_6.png"))
entry_f2_bg_6 = canvas.create_image(
    415.0,
    353.0,
    image=entry_f2_image_6
)
entry_f2_6 = Entry(#nombre del denunciado
    frame2,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f2_6.place(
    x=256.0,
    y=328.0,
    width=318.0,
    height=48.0
)

entry_f2_image_7 = PhotoImage(
    file=Path(r"assets\frame2\entry_7.png"))
entry_bg_7 = canvas.create_image(
    415.0,
    270.0,
    image=entry_f2_image_7
)
entry_f2_7 = Entry(#correo del denunciante
    frame2,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f2_7.place(
    x=256.0,
    y=245.0,
    width=318.0,
    height=48.0
)
#===============================frame 2

def agarrar_mail():
    e_mail = entry_f16_1.get()
    mostrar_frame(frame3)
    return e_mail

#===============================frame 16
background_f16 = PhotoImage(
    file=Path(r"assets\frame16\image_1.png"))
label16 = Label( frame16, image = background_f16)
label16.place(x = 0, y = 0)
button_f16_image_1 = PhotoImage(
    file=Path(r"assets\frame16\button_1.png"))
button_f16_1 = Button(
    frame16,
    image=button_f16_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame7),
    relief="flat"
)
button_f16_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

entry_f16_image_1 = PhotoImage(
    file=Path(r"assets\frame16\entry_1.png"))
entry_16_bg_1 = canvas.create_image(
    653.0,
    386.0,
    image=entry_f16_image_1
)
entry_f16_1 = Entry(
    frame16,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f16_1.place(
    x=395.0,
    y=350.0,
    width=516.0,
    height=70.0
)

button_f16_image_2 = PhotoImage(
    file=Path(r"assets\frame16\button_2.png"))
button_f16_2 = Button(
    frame16,
    image=button_f16_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: agarrar_mail(),
    relief="flat"
)
button_f16_2.place(
    x=570.0,
    y=454.0,
    width=142.0,
    height=42.0
)
#===============================frame 16

#===============================frame 3

def sig():
    global opcionanon
    if opcionanon==limOpciones:
        grilla(limOpciones)
        return
    elif opcionanon<limOpciones:
        opcionanon+=1
        grilla(opcionanon)
        return
def atras():
    global opcionanon
    if opcionanon==0:
        grilla(0)
        return
    elif opcionanon>0:
        opcionanon-=1
        grilla(opcionanon)
        return
    
def abrir_f3():
    global limOpciones
    limOpciones=0
    e_mail=agarrar_mail()

    if e_mail!='':
        archivo=open('archivos/denunciaanon.txt')
        registros=archivo.readlines()
        contador=0
        limOpciones=len(registros)//8
        usuarios=open('archivos/usuarioanon.txt','r')
        user=usuarios.readlines()
        denuncias = []
        for i in user:
            i=i.split('|')
            if i[0] == e_mail:
                cadena=i[1]
                denuncias.append(cadena[0:3])
        nuevo=['']*len(denuncias)

        for i in registros:
            i=i.split('|')
            if contador<len(denuncias):
                if denuncias[contador] == i[0]:
                    nuevo[contador]=i
                    contador+=1
        return nuevo
    else:
        return[]

def matriz(dato):
    campos=abrir_f3()
    cont=0
    resultado=[[str(' ') for i in range(6)]for j in range(8)]
    if dato==limOpciones:
        for j in range(dato*8,len(campos)):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    elif dato<limOpciones:
        for j in range(dato*8,(dato+1)*8):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    return resultado

def grilla(dato):
    registros=matriz(dato)
    labelanon1.config(text=registros[0][0])
    labelanon2.config(text=registros[0][1])
    labelanon3.config(text=registros[0][2])
    labelanon4.config(text=registros[0][3])
    labelanon5.config(text=registros[0][4])
    labelanon6.config(text=registros[0][5])
    labelanon7.config(text=registros[1][0])
    labelanon8.config(text=registros[1][1])
    labelanon9.config(text=registros[1][2])
    labelanon10.config(text=registros[1][3])
    labelanon11.config(text=registros[1][4])
    labelanon12.config(text=registros[1][5])
    labelanon13.config(text=registros[2][0])
    labelanon14.config(text=registros[2][1])
    labelanon15.config(text=registros[2][2])
    labelanon16.config(text=registros[2][3])
    labelanon17.config(text=registros[2][4])
    labelanon18.config(text=registros[2][5])
    labelanon19.config(text=registros[3][0])
    labelanon20.config(text=registros[3][1])
    labelanon21.config(text=registros[3][2])
    labelanon22.config(text=registros[3][3])
    labelanon23.config(text=registros[3][4])
    labelanon24.config(text=registros[3][5])
    labelanon25.config(text=registros[4][0])
    labelanon26.config(text=registros[4][1])
    labelanon27.config(text=registros[4][2])
    labelanon28.config(text=registros[4][3])
    labelanon29.config(text=registros[4][4])
    labelanon30.config(text=registros[4][5])
    labelanon31.config(text=registros[5][0])
    labelanon32.config(text=registros[5][1])
    labelanon33.config(text=registros[5][2])
    labelanon34.config(text=registros[5][3])
    labelanon35.config(text=registros[5][4])
    labelanon36.config(text=registros[5][5])
    labelanon37.config(text=registros[6][0])
    labelanon38.config(text=registros[6][1])
    labelanon39.config(text=registros[6][2])
    labelanon40.config(text=registros[6][3])
    labelanon41.config(text=registros[6][4])
    labelanon42.config(text=registros[6][5])
    labelanon43.config(text=registros[7][0])
    labelanon44.config(text=registros[7][1])
    labelanon45.config(text=registros[7][2])
    labelanon46.config(text=registros[7][3])
    labelanon47.config(text=registros[7][4])
    labelanon48.config(text=registros[7][5])


opcionanon=0
registrosanon=matriz(0)

background_f3 = PhotoImage(
    file=Path(r"assets\frame3\image_1.png"))
label3 = Label( frame3, image = background_f3)
label3.place(x = 0, y = 0) 

button_f3_image_1 = PhotoImage(
    file=Path(r"assets\frame3\button_1.png"))
button_f3_1 = Button(
    frame3,
    image=button_f2_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame7),
    relief="flat"
)
button_f3_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
labelanon1=Label(
frame3,
anchor="nw",
text=registrosanon[0][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon1.place(
x=110.0,
y=233.0
)
labelanon2 = Label(
frame3,
anchor="nw",
text=registrosanon[0][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon2.place(
x=219.0,
y=233.0
)
labelanon3 = Label(
frame3,
anchor="nw",
text=registrosanon[0][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon3.place(
x=339.0,
y=233.0
)
labelanon4 = Label(
frame3,
anchor="nw",
text=registrosanon[0][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon4.place(
x=494.0,
y=233.0
)
labelanon5 = Label(
frame3,
anchor="nw",
text=registrosanon[0][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon5.place(
x=633.0,
y=233.0
)
labelanon6 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[0][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon6.place(
x=1074.0,
y=233.0
)
labelanon7 = Label(
frame3,
anchor="nw",
text=registrosanon[1][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon7.place(
x=110.00,
y=283.0
)
labelanon8 = Label(
frame3,
anchor="nw",
text=registrosanon[1][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon8.place(
x=219.0,
y=283.0
)
labelanon9 = Label(
frame3,
anchor="nw",
text=registrosanon[1][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon9.place(
x=339.0,
y=283.0
)
labelanon10 = Label(
frame3,
anchor="nw",
text=registrosanon[1][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon10.place(
x=494.0,
y=283.0
)
labelanon11 = Label(
frame3,
anchor="nw",
text=registrosanon[1][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon11.place(
x=633.0,
y=283.0
)
labelanon12 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[1][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon12.place(
x=1074.0,
y=283.0
)
labelanon13 = Label(
frame3,
anchor="nw",
text=registrosanon[2][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon13.place(
x= 110.00,
y=333.0
)
labelanon14 = Label(
frame3,
anchor="nw",
text=registrosanon[2][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon14.place(
x=219.0,
y=333.0
)
labelanon15 = Label(
frame3,
anchor="nw",
text=registrosanon[2][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon15.place(
x=339.0,
y=333.0
)
labelanon16 = Label(
frame3,
anchor="nw",
text=registrosanon[2][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon16.place(
x=494.0,
y=333.0
)
labelanon17 = Label(
frame3,
anchor="nw",
text=registrosanon[2][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon17.place(
x=633.0,
y=333.0
)
labelanon18 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[2][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon18.place(
x=1074.0,
y=333.0
)
labelanon19 = Label(
frame3,
anchor="nw",
text=registrosanon[3][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon19.place(
x= 110.00,
y=383.0
)
labelanon20 = Label(
frame3,
anchor="nw",
text=registrosanon[3][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon20.place(
x=219.0,
y=383.0
)
labelanon21 = Label(
frame3,
anchor="nw",
text=registrosanon[3][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon21.place(
x=339.0,
y=383.0
)
labelanon22 = Label(
frame3,
anchor="nw",
text=registrosanon[3][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon22.place(
x=494.0,
y=383.0
)
labelanon23 = Label(
frame3,
anchor="nw",
text=registrosanon[3][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon23.place(
x=633.0,
y=383.0
)
labelanon24 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[3][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon24.place(
x=1074.0,
y=383.0
)
labelanon25 = Label(
frame3,
anchor="nw",
text=registrosanon[4][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon25.place(
x= 110.00,
y=433.0
)
labelanon26 = Label(
frame3,
anchor="nw",
text=registrosanon[4][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon26.place(
x=219.0,
y=433.0
)
labelanon27 = Label(
frame3,
anchor="nw",
text=registrosanon[4][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon27.place(
x=339.0,
y=433.0
)
labelanon28 = Label(
frame3,
anchor="nw",
text=registrosanon[4][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon28.place(
x=494.0,
y=433.0
)
labelanon29 = Label(
frame3,
anchor="nw",
text=registrosanon[4][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon29.place(
x=633.0,
y=433.0
)
labelanon30 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[4][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon30.place(
x=1074.0,
y=433.0
)
labelanon31 = Label(
frame3,
anchor="nw",
text=registrosanon[5][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon31.place(
x=110.00,
y=483.0
)
labelanon32 = Label(
frame3,
anchor="nw",
text=registrosanon[5][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon32.place(
x=219.0,
y=483.0
)
labelanon33 = Label(
frame3,
anchor="nw",
text=registrosanon[5][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon33.place(
x=339.0,
y=483.0
)
labelanon34 = Label(
frame3,
anchor="nw",
text=registrosanon[5][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon34.place(
x=494.0,
y=483.0
)
labelanon35 = Label(
frame3,
anchor="nw",
text=registrosanon[5][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon35.place(
x=633.0,
y=483.0
)
labelanon36 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[5][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon36.place(
x=1074.0,
y=483.0
)
labelanon37 = Label(
frame3,
anchor="nw",
text=registrosanon[6][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon37.place(
x=110.00,
y=533.0
)
labelanon38 = Label(
frame3,
anchor="nw",
text=registrosanon[6][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon38.place(
x=219.0,
y=533.0
)
labelanon39 = Label(
frame3,
anchor="nw",
text=registrosanon[6][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon39.place(
x=339.0,
y=533.0
)
labelanon40 = Label(
frame3,
anchor="nw",
text=registrosanon[6][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon40.place(
x=494.0,
y=533.0
)
labelanon41 = Label(
frame3,
anchor="nw",
text=registrosanon[6][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon41.place(
x=633.0,
y=533.0
)
labelanon42 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[6][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon42.place(
x=1074.0,
y=533.0
)
labelanon43 = Label(
frame3,
anchor="nw",
text=registrosanon[7][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon43.place(
x= 110.00,
y=583.0
)
labelanon44 = Label(
frame3,
anchor="nw",
text=registrosanon[7][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
labelanon44.place(
x=219.0,
y=583.0
)
labelanon45 = Label(
frame3,
anchor="nw",
text=registrosanon[7][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon45.place(
x=339.0,
y=583.0
)
labelanon46 = Label(
frame3,
anchor="nw",
text=registrosanon[7][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon46.place(
x=494.0,
y=583.0
)
labelanon47 = Label(
frame3,
anchor="nw",
text=registrosanon[7][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon47.place(
x=633.0,
y=583.0
)
labelanon48 = Label(
frame3,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registrosanon[7][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
labelanon48.place(
x=1074.0,
y=583.0
)

Atrasanon = Button(
    frame3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:atras(),
    relief="flat",
    text='<',
)
Atrasanon.place(
    x=882.0,
    y=598.0,
    width=35.0,
    height=35.0
)
siguienteanon = Button(
    frame3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:sig(),
    relief="flat",
    text='>',
)
siguienteanon.place(
    x=1102.0,
    y=598.0,
    width=35.0,
    height=35.0,
)
#===============================frame 3

#===============================func f4
def grilla_f4(registro):
    label_f4_1.config(text=registro[0])
    label_f4_2.config(text=registro[1])
    label_f4_3.config(text=registro[2])
    label_f4_4.config(text=registro[3])
    label_f4_5.config(text=registro[4])
    entry_f4_1.insert(0, registro[5])
def cambiar_f4(vector,posicion):
    linea=vector[posicion]
    linea=linea.split('|')
    linea[5]=entry_f4_1.get()
    remplazo=''
    for i in range(len(linea)-1):
        remplazo+=linea[i]+'|'
    remplazo+=linea[len(linea)-1]
    vector[posicion]=remplazo
    return vector

def guardar_f4():
    archivocidi=open('archivos/denunciacidi.txt','r+')
    archivoanon=open('archivos/denunciaanon.txt','r+')
    cidi=archivocidi.readlines()
    anonima=archivoanon.readlines()
    #anoni flag para indicar si la denuncia se encuentra en
    #denuncias anonimas
    anoni=True
    posicion=0
    for i in range(len(cidi)):
        if cidi[i]==registro_f4:
            anoni=False
            posicion=i
    for i in range(len(anonima)):
        if anonima[i]==registro_f4:
            posicion=i
    if anoni==True:
        anonima[posicion]=registro_f4
        anonima = cambiar_f4(anonima,posicion)
        archivoanon.close()
        archivoanon=open('archivos/denunciaanon.txt','w')
        archivoanon.writelines(anonima)
        archivoanon.close()
    else:
        cidi[posicion]=registro_f4
        cidi=cambiar_f4(cidi,posicion)
        archivocidi.close()
        archivocidi=open('archivos/denunciacidi.txt','w')
        archivocidi.writelines(cidi)
        archivocidi.close()
    mostrar_frame(frame0)
    return
def buscar_f4():
    entry1D=entry_f4_2.get()
    if len(entry1D)!=3:
        messagebox.showerror('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    try:
        int(entry1D)
    except:
        messagebox.showerror('error','usted ha ingresado un dato de manera erronea verifique nuevamente')
        return
    existe=False
    archivocidi=open('archivos/denunciacidi.txt','r')
    archivoanon=open('archivos/denunciaanon.txt','r')
    global registro_f4
    for linea in archivoanon:
        if linea[0:3]==entry1D:
            existe=True
            registro_f4=linea
    archivoanon.close()
    for linea in archivocidi:
        if linea[0:3]==entry1D:
            existe=True
            registro_f4=linea
    archivocidi.close()
    if existe==False:
        messagebox.showinfo('error','no se ha encontrado la denuncia')#poner alarma
        return
    registro=registro_f4.split('|')
    grilla_f4(registro)
    return
#===============================func f4

#===============================frame 4
background_f4 = PhotoImage(
    file=Path(r"assets/frame4/image_1.png"))
label4 = Label( frame4, image = background_f4)
label4.place(x = 0, y = 0) 

entry_f4_image_1 = PhotoImage(
    file=Path(r"assets/frame4/entry_1.png"))
entry_f4_bg_1 = canvas.create_image(
    1124.5,
    464.0,
    image=entry_f4_image_1
)
entry_f4_1 = Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f4_1.place(
    x=1057.0,
    y=451.0,
    width=135.0,
    height=24.0
)

entry_f4_image_2 = PhotoImage(
    file=Path(r"assets/frame4/entry_2.png"))
entry_f4_bg_2 = canvas.create_image(
    766.0,
    231.5,
    image=entry_f4_image_2
)
entry_f4_2 = Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f4_2.place(
    x=695.0,
    y=217.0,
    width=142.0,
    height=27.0
)

button_f4_image_1 = PhotoImage(
    file=Path(r"assets/frame4/button_1.png"))
button_f4_2 = Button(
    frame4,
    borderwidth=0,
    image = button_f4_image_1,
    highlightthickness=0,
    command=buscar_f4,
    relief="flat"
)
button_f4_2.place(
    x=330.0,
    y=185.0,
    width=215.0,
    height=64.0
)

button_f4_image_2 = PhotoImage(
    file=Path(r"assets/frame4/button_2.png"))
button_f4_2 = Button(
    frame4,
    image=button_f4_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f4_2.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

button_f4_image_3 = PhotoImage(
    file=Path(r"assets/frame4/button_3.png"))
button_f4_3 = Button(
    frame4,
    image=button_f4_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: guardar_f4(),
    relief="flat"
)
button_f4_3.place(
    x=576.0,
    y=537.0,
    width=127.0,
    height=47.0
)
label_f4_1=Label(
master=frame4,
anchor="nw",
text='',
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f4_1.place(
x=110.0,
y=451.0
)
label_f4_2 = Label(
master=frame4,
anchor="nw",
text='',
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f4_2.place(
x=219.0,
y=451.0
)
label_f4_3 = Label(
master=frame4,
anchor="nw",
text='',
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f4_3.place(
x=339.0,
y=451.0
)
label_f4_4 = Label(
master=frame4,
anchor="nw",
text='',
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f4_4.place(
x=494.0,
y=451.0
)
label_f4_5 = Label(
master=frame4,
anchor="nw",
text='',
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f4_5.place(
x=640.0,
y=451.0
)
#===============================frame 4

#===============================frame 5
def agarrar_mail_f5():
    e_mail = entry_f17_2.get()
    mostrar_frame(frame5)
    return e_mail
def sig_f5():
    global opcion
    limOpciones_f5=0
    if opcion==limOpciones_f5:
        grilla_f5(limOpciones_f5)
        return
    elif opcion<limOpciones_f5:
        opcion+=1
        grilla_f5(opcion)
        return
def atras_f5():
    global opcion
    if opcion==0:
        grilla_f5(0)
        return
    elif opcion>0:
        opcion-=1
        grilla_f5(opcion)
        return
def abrir_f5():
    e_mail=agarrar_mail_f5()
    global limOpciones_f5
    if e_mail!='':
        archivo=open('archivos/denunciacidi.txt','r')
        registros=archivo.readlines()
        contador=0
        limOpciones_f5=len(registros)//8
        usuarios=open('archivos/usuariocidi.txt','r')
        user=usuarios.readlines()
        denuncias = []
        for i in user:
            i=i.split('|')
            if i[0] == e_mail:
                cadena=i[3]
                denuncias.append(cadena[0:3])
        nuevo=['']*len(denuncias)

        for i in registros:
            i=i.split('|')
            if contador<len(denuncias):
                if denuncias[contador] == i[0]:
                    nuevo[contador]=i
                    contador+=1
        return nuevo
    else:
        return[]
def matriz_f5(dato):
    campos=abrir_f5()
    cont=0
    resultado=[[str(' ') for i in range(6)]for j in range(8)]
    if dato==limOpciones_f5:
        for j in range(dato*8,len(campos)):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    elif dato<limOpciones_f5:
        for j in range(dato*8,(dato+1)*8):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    return resultado
def grilla_f5(dato):
    registros_f5=matriz_f5(dato)
    label_f5_1.config(text=registros_f5[0][0])
    label_f5_2.config(text=registros_f5[0][1])
    label_f5_3.config(text=registros_f5[0][2])
    label_f5_4.config(text=registros_f5[0][3])
    label_f5_5.config(text=registros_f5[0][4])
    label_f5_6.config(text=registros_f5[0][5])
    label_f5_7.config(text=registros_f5[1][0])
    label_f5_8.config(text=registros_f5[1][1])
    label_f5_9.config(text=registros_f5[1][2])
    label_f5_10.config(text=registros_f5[1][3])
    label_f5_11.config(text=registros_f5[1][4])
    label_f5_12.config(text=registros_f5[1][5])
    label_f5_13.config(text=registros_f5[2][0])
    label_f5_14.config(text=registros_f5[2][1])
    label_f5_15.config(text=registros_f5[2][2])
    label_f5_16.config(text=registros_f5[2][3])
    label_f5_17.config(text=registros_f5[2][4])
    label_f5_18.config(text=registros_f5[2][5])
    label_f5_19.config(text=registros_f5[3][0])
    label_f5_20.config(text=registros_f5[3][1])
    label_f5_21.config(text=registros_f5[3][2])
    label_f5_22.config(text=registros_f5[3][3])
    label_f5_23.config(text=registros_f5[3][4])
    label_f5_24.config(text=registros_f5[3][5])
    label_f5_25.config(text=registros_f5[4][0])
    label_f5_26.config(text=registros_f5[4][1])
    label_f5_27.config(text=registros_f5[4][2])
    label_f5_28.config(text=registros_f5[4][3])
    label_f5_29.config(text=registros_f5[4][4])
    label_f5_30.config(text=registros_f5[4][5])
    label_f5_31.config(text=registros_f5[5][0])
    label_f5_32.config(text=registros_f5[5][1])
    label_f5_33.config(text=registros_f5[5][2])
    label_f5_34.config(text=registros_f5[5][3])
    label_f5_35.config(text=registros_f5[5][4])
    label_f5_36.config(text=registros_f5[5][5])
    label_f5_37.config(text=registros_f5[6][0])
    label_f5_38.config(text=registros_f5[6][1])
    label_f5_39.config(text=registros_f5[6][2])
    label_f5_40.config(text=registros_f5[6][3])
    label_f5_41.config(text=registros_f5[6][4])
    label_f5_42.config(text=registros_f5[6][5])
    label_f5_43.config(text=registros_f5[7][0])
    label_f5_44.config(text=registros_f5[7][1])
    label_f5_45.config(text=registros_f5[7][2])
    label_f5_46.config(text=registros_f5[7][3])
    label_f5_47.config(text=registros_f5[7][4])
    label_f5_48.config(text=registros_f5[7][5])

opcion=0
registros_f5=matriz(0)

background_f5 = PhotoImage(
    file=Path(r"assets\frame5\image_1.png"))
label5 = Label( frame5, image = background_f5)
label5.place(x = 0, y = 0)  

button_f5_image_1 = PhotoImage(
    file=Path(r"assets\frame5\button_1.png"))
button_f5_1 = Button(
    frame5,
    image=button_f5_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame8),
    relief="flat"
)
button_f5_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
label_f5_1=Label(
master=frame5,
anchor="nw",
text=registros_f5[0][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_1.place(
x=110.0,
y=233.0
)
label_f5_2 = Label(
master=frame5,
anchor="nw",
text=registros_f5[0][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_2.place(
x=219.0,
y=233.0
)
label_f5_3 = Label(
master=frame5,
anchor="nw",
text=registros_f5[0][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_3.place(
x=339.0,
y=233.0
)
label_f5_4 = Label(
master=frame5,
anchor="nw",
text=registros_f5[0][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_4.place(
x=494.0,
y=233.0
)
label_f5_5 = Label(
master=frame5,
anchor="nw",
text=registros_f5[0][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_5.place(
x=633.0,
y=233.0
)
label_f5_6 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[0][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_6.place(
x=1074.0,
y=233.0
)
label_f5_7 = Label(
master=frame5,
anchor="nw",
text=registros_f5[1][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_7.place(
x=110.00,
y=283.0
)
label_f5_8 = Label(
master=frame5,
anchor="nw",
text=registros_f5[1][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_8.place(
x=219.0,
y=283.0
)
label_f5_9 = Label(
master=frame5,
anchor="nw",
text=registros_f5[1][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_9.place(
x=339.0,
y=283.0
)
label_f5_10 = Label(
master=frame5,
anchor="nw",
text=registros_f5[1][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_10.place(
x=494.0,
y=283.0
)
label_f5_11 = Label(
master=frame5,
anchor="nw",
text=registros_f5[1][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_11.place(
x=633.0,
y=283.0
)
label_f5_12 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[1][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_12.place(
x=1074.0,
y=283.0
)
label_f5_13 = Label(
master=frame5,
anchor="nw",
text=registros_f5[2][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_13.place(
x= 110.00,
y=333.0
)
label_f5_14 = Label(
master=frame5,
anchor="nw",
text=registros_f5[2][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_14.place(
x=219.0,
y=333.0
)
label_f5_15 = Label(
master=frame5,
anchor="nw",
text=registros_f5[2][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_15.place(
x=339.0,
y=333.0
)
label_f5_16 = Label(
master=frame5,
anchor="nw",
text=registros_f5[2][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_16.place(
x=494.0,
y=333.0
)
label_f5_17 = Label(
master=frame5,
anchor="nw",
text=registros_f5[2][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_17.place(
x=633.0,
y=333.0
)
label_f5_18 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[2][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_18.place(
x=1074.0,
y=333.0
)
label_f5_19 = Label(
master=frame5,
anchor="nw",
text=registros_f5[3][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_19.place(
x= 110.00,
y=383.0
)
label_f5_20 = Label(
master=frame5,
anchor="nw",
text=registros_f5[3][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_20.place(
x=219.0,
y=383.0
)
label_f5_21 = Label(
master=frame5,
anchor="nw",
text=registros_f5[3][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_21.place(
x=339.0,
y=383.0
)
label_f5_22 = Label(
master=frame5,
anchor="nw",
text=registros_f5[3][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_22.place(
x=494.0,
y=383.0
)
label_f5_23 = Label(
master=frame5,
anchor="nw",
text=registros_f5[3][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_23.place(
x=633.0,
y=383.0
)
label_f5_24 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[3][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_24.place(
x=1074.0,
y=383.0
)
label_f5_25 = Label(
master=frame5,
anchor="nw",
text=registros_f5[4][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_25.place(
x= 110.00,
y=433.0
)
label_f5_26 = Label(
master=frame5,
anchor="nw",
text=registros_f5[4][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_26.place(
x=219.0,
y=433.0
)
label_f5_27 = Label(
master=frame5,
anchor="nw",
text=registros_f5[4][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_27.place(
x=339.0,
y=433.0
)
label_f5_28 = Label(
master=frame5,
anchor="nw",
text=registros_f5[4][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_28.place(
x=494.0,
y=433.0
)
label_f5_29 = Label(
master=frame5,
anchor="nw",
text=registros_f5[4][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_29.place(
x=633.0,
y=433.0
)
label_f5_30 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[4][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_30.place(
x=1074.0,
y=433.0
)
label_f5_31 = Label(
master=frame5,
anchor="nw",
text=registros_f5[5][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_31.place(
x=110.00,
y=483.0
)
label_f5_32 = Label(
master=frame5,
anchor="nw",
text=registros_f5[5][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_32.place(
x=219.0,
y=483.0
)
label_f5_33 = Label(
master=frame5,
anchor="nw",
text=registros_f5[5][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_33.place(
x=339.0,
y=483.0
)
label_f5_34 = Label(
master=frame5,
anchor="nw",
text=registros_f5[5][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_34.place(
x=494.0,
y=483.0
)
label_f5_35 = Label(
master=frame5,
anchor="nw",
text=registros_f5[5][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_35.place(
x=633.0,
y=483.0
)
label_f5_36 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[5][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_36.place(
x=1074.0,
y=483.0
)
label_f5_37 = Label(
master=frame5,
anchor="nw",
text=registros_f5[6][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_37.place(
x=110.00,
y=533.0
)
label_f5_38 = Label(
master=frame5,
anchor="nw",
text=registros_f5[6][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_38.place(
x=219.0,
y=533.0
)
label_f5_39 = Label(
master=frame5,
anchor="nw",
text=registros_f5[6][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_39.place(
x=339.0,
y=533.0
)
label_f5_40 = Label(
master=frame5,
anchor="nw",
text=registros_f5[6][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_40.place(
x=494.0,
y=533.0
)
label_f5_41 = Label(
master=frame5,
anchor="nw",
text=registros_f5[6][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_41.place(
x=633.0,
y=533.0
)
label_f5_42 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[6][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_42.place(
x=1074.0,
y=533.0
)
label_f5_43 = Label(
master=frame5,
anchor="nw",
text=registros_f5[7][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_43.place(
x= 110.00,
y=583.0
)
label_f5_44 = Label(
master=frame5,
anchor="nw",
text=registros_f5[7][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f5_44.place(
x=219.0,
y=583.0
)
label_f5_45 = Label(
master=frame5,
anchor="nw",
text=registros_f5[7][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_45.place(
x=339.0,
y=583.0
)
label_f5_46 = Label(
master=frame5,
anchor="nw",
text=registros_f5[7][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_46.place(
x=494.0,
y=583.0
)
label_f5_47 = Label(
master=frame5,
anchor="nw",
text=registros_f5[7][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_47.place(
x=633.0,
y=583.0
)
label_f5_48 = Label(
master=frame5,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f5[7][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f5_48.place(
x=1074.0,
y=583.0
)

Atras = Button(
    frame5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:atras_f5(),
    relief="flat",
    text='<',
)
Atras.place(
    x=882.0,
    y=598.0,
    width=35.0,
    height=35.0
)
siguiente = Button(
    frame5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:sig_f5(),
    relief="flat",
    text='>',
)
siguiente.place(
    x=1102.0,
    y=598.0,
    width=35.0,
    height=35.0,
)
#===============================frame 5
def porcentajes():
    cidi=open(r'archivos/denunciacidi.txt')
    anonim=open(r'archivos/denunciaanon.txt')
    denunciasanonim=anonim.readlines()
    denunciascidi=cidi.readlines()
    infrac=infraccion()
    local=localidad()
    fechas=['2018','2019','2020','2021','2022']
    estadistica1=[0]*len(infrac)
    estadistica2=[0]*len(local)
    estadistica3=[0]*len(fechas)
    for i in range(len(denunciasanonim)):
        denunciasanonim[i]=denunciasanonim[i].split('|')
    for i in range(len(denunciascidi)):
        denunciascidi[i]=denunciascidi[i].split('|')
    for i in range(len(infrac)):
        for j in denunciascidi:
            if infrac[i]==j[2]:
                estadistica1[i]+=1
        for j in denunciasanonim:
            if infrac[i]==j[2]:       
                estadistica1[i]+=1
    for i in range(len(local)):
        for j in denunciascidi:
            if local[i]==j[3]:
                estadistica2[i]+=1
        for j in denunciasanonim:
            if local[i]==j[3]:       
                estadistica2[i]+=1
    for i in range(len(fechas)):
        for j in denunciascidi:
            if fechas[i]==j[1][0:4]:
                estadistica3[i]+=1
        for j in denunciasanonim:
            if fechas[i]==j[1][0:4]:       
                estadistica3[i]+=1
    return infrac,estadistica1,local,estadistica2,fechas,estadistica3
def graficos():
    tiposInfraccion,porcentaje,ciudades,denunciasf6,anios,denunciasf62= porcentajes()
    # grafico circular
    
    circulo, ax1 =plt.subplots(facecolor='gray', figsize=(4,3.5), dpi=100)
    plt.title('Denuncias por sub-tipos',color='white')
    ax1.pie(porcentaje,labels=tiposInfraccion, autopct='%1.2f%%')   #cambiar datos
    ax1.axis('equal')
    cuadroPie=FigureCanvasTkAgg(circulo, master=frame6)
    cuadroPie.draw()
    cuadroPie.get_tk_widget().pack(side=LEFT,padx=10)
    
    barras, ax2=plt.subplots(facecolor='gray', figsize=(3.5,3.5), dpi=100)
    plt.title('denuncias por ciudades',color='white')
    ax2.bar(ciudades, height=denunciasf6, width=0.1)
    ax2.grid(linestyle ='--',alpha=0.5)
    cuadroBar=FigureCanvasTkAgg(barras, master=frame6)
    cuadroBar.draw()
    cuadroBar.get_tk_widget().pack(side=RIGHT,padx=20)

    grafica=plt.figure(facecolor='gray', figsize=(4,3.5),dpi=100)
    ax3=grafica.add_subplot(111)
    plt.title('Denuncias anuales',color='white')
    ax3.plot(anios,denunciasf62, marker='o')
    ax3.grid(linestyle ='--',alpha=0.5)
    cuadroGrafico=FigureCanvasTkAgg(grafica,master=frame6)
    cuadroGrafico.draw()
    cuadroGrafico.get_tk_widget().pack(side=TOP,pady=175)
    return
#===============================frame 6
background_f6 = PhotoImage(
    file=Path(r"assets\frame6\image_1.png"))
label6 = Label( frame6, image = background_f6)
label6.place(x = 0, y = 0) 

button_image_1 = PhotoImage(
    file=Path(r"assets\frame6\button_1.png"))
button_1 = Button(
    frame6,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

#===============================frame 6
def actualizar2():
    actualizaranon()
    mostrar_frame(frame2)
    return
#===============================frame 7
background_f7 = PhotoImage(
    file=Path(r"assets\frame7\image_1.png"))
label7 = Label( frame7, image = background_f7)
label7.place(x = 0, y = 0)

button_f7_image_1 = PhotoImage(
    file=Path(r"assets\frame7\button_1.png"))
button_f7_1 = Button(
    frame7,
    image=button_f7_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f7_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

button_f7_image_2 = PhotoImage(
    file=Path(r"assets\frame7\button_2.png"))
button_2 = Button(
    frame7,
    image=button_f7_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: actualizar2(),
    relief="flat"
)
button_2.place(
    x=323.0,
    y=332.0,
    width=221.0,
    height=86.0
)

button_f7_image_3 = PhotoImage(
    file=Path(r"assets\frame7\button_3.png"))
button_f7_3 = Button(
    frame7,
    image=button_f7_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame16),
    relief="flat"
)
button_f7_3.place(
    x=774.0,
    y=332.0,
    width=221.0,
    height=86.0
)
#===============================frame 7
def actualizar():
    actualizartodo()
    mostrar_frame(frame1)
    return
#===============================frame 8


background_f8 = PhotoImage(
    file=Path(r"assets\frame8\image_1.png"))
label8 = Label( frame8, image = background_f8)
label8.place(x = 0, y = 0)

button_f8_image_1 = PhotoImage(
    file=Path(r"assets\frame8\button_1.png"))
button_f8_1 = Button(
    frame8,
    image=button_f8_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f8_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

button_f8_image_2 = PhotoImage(
    file=Path(r"assets\frame8\button_2.png"))
button_f8_2 = Button(
    frame8,
    image=button_f8_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame1),
    relief="flat"
)
button_f8_2.place(
    x=323.0,
    y=332.0,
    width=221.0,
    height=86.0
)

button_f8_image_3 = PhotoImage(
    file=Path(r"assets\frame8\button_3.png"))
button_f8_3 = Button(
    frame8,
    image=button_f8_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: agarrar_mail_f5(),
    relief="flat"
)
button_f8_3.place(
    x=774.0,
    y=332.0,
    width=221.0,
    height=86.0
)

#===============================frame 8
#===============================frame 9
background_f9 = PhotoImage(
    file=Path(r"assets\frame9\image_1.png"))
label9 = Label( frame9, image = background_f9)
label9.place(x = 0, y = 0)  

button_f9_image_1 = PhotoImage(
    file=Path(r"assets\frame9\button_1.png"))
button_f9_1 = Button(
    frame9,
    image=button_f9_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f9_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)


#===============================frame 9
#===============================frame 10
background_f10 = PhotoImage(
    file=Path(r"assets\frame10\image_1.png"))
label10 = Label( frame10, image = background_f10)
label10.place(x = 0, y = 0)

button_f10_image_1 = PhotoImage(
    file=Path(r"assets\frame10\button_1.png"))
button_f10_1 = Button(
    frame10,
    image=button_f10_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame11),
    relief="flat"
)
button_f10_1.place(
    x=529.0,
    y=492.0,
    width=229.16650390625,
    height=56.0
)

button_f10_image_2 = PhotoImage(
    file=Path(r"assets\frame10\button_2.png"))
button_f10_2 = Button(
    frame10,
    image=button_f10_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame7),
    relief="flat"
)
button_f10_2.place(
    x=529.0,
    y=399.0,
    width=229.16650390625,
    height=56.0
)

button_f10_image_3 = PhotoImage(
    file=Path(r"assets\frame10\button_3.png"))
button_f10_3 = Button(
    frame10,
    image=button_f10_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame9),
    relief="flat"
)
button_f10_3.place(
    x=127.0,
    y=67.0,
    width=182.0,
    height=30.0
)

button_f10_image_4 = PhotoImage(
    file=Path(r"assets\frame10\button_4.png"))
button_f10_4 = Button(
    frame10,
    image=button_f10_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame17),
    relief="flat"
)
button_f10_4.place(
    x=529.0,
    y=306.0,
    width=229.16650390625,
    height=56.0
)
#===============================frame 10

#===============================frame 11
background_f11 = PhotoImage(
    file=Path(r"assets\frame11\image_1.png"))
label11 = Label( frame11, image = background_f11)
label11.place(x = 0, y = 0) 
entry_f11_image_1 = PhotoImage(
    file=Path(r"assets\frame11\entry_1.png"))
entry_f11_bg_1 = canvas.create_image(
    641.0,
    383.6922607421875,
    image=entry_f11_image_1
)
entry_f11_1 = Entry(
    frame11,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f11_1.place(
    x=542.0,
    y=363.384521484375,
    width=198.0,
    height=38.615478515625
)

entry_f11_image_2 = PhotoImage(
    file=Path(r"assets\frame11\entry_2.png"))
entry_f11_bg_2 = canvas.create_image(
    641.0,
    298.4193115234375,
    image=entry_f11_image_2
)
entry_f11_2 = Entry(
    frame11,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)

entry_f11_2.place(
    x=542.0,
    y=277.838623046875,
    width=198.0,
    height=39.161376953125
)

button_f11_image_1 = PhotoImage(
    file=Path(r"assets\frame11\button_1.png"))
button_f11_1 = Button(
    frame11,
    image=button_f11_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login("admin"),
    relief="flat"
)
button_f11_1.place(
    x=570.0,
    y=477.0,
    width=142.0,
    height=42.0
)

button_f11_image_2 = PhotoImage(
    file=Path(r"assets\frame11\button_2.png"))
button_f11_2 = Button(
    frame11,
    image=button_f11_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f11_2.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

#===============================frame 11
def altaDpto():
    archivo=open('archivos/departamentos.txt','a')
    data=entry_f12_2.get()
    archivo.write(data+'\n')
    archivo.close()
    actualizarDpto()
    return
def actualizarDpto():
    entry_f12_1['values'] = depto()
    return

def bajaDpto():
    archivo=open(r'archivos/departamentos.txt','r+')
    lineas=archivo.readlines()
    nuevo=['']*(len(lineas)-1)
    cont=0
    error=True
    for i in depto():
        if i ==entry_f12_1.get():
            error=False
    if error==True:
        messagebox.showerror('error','no se ha encontrado el elemento')
        return
    for i in range(len(lineas)):
        if lineas[i]!=entry_f12_1.get():
            nuevo[cont]=lineas[i]
            cont+=1
    archivo.close()
    archivo2=open(r'archivos/departamentos.txt','w')
    archivo2.writelines(nuevo)
    archivo2.close()
    actualizarDpto()
    return
#===============================frame 12
background_f12 = PhotoImage(
    file=Path(r"assets\frame12\image_1.png"))
label12 = Label( frame12, image = background_f12)
label12.place(x = 0, y = 0)  
entry_f12_image_1 = PhotoImage(
    file=Path(r"assets\frame12\entry_1.png"))
entry_f12_bg_1 = canvas.create_image(
    942.5,
    350.0,
    image=entry_f12_image_1
)
entry_f12_1 = ttk.Combobox(
    frame12,
    values=depto(),
)
entry_f12_1.place(
    x=758.0,
    y=308.0,
    width=369.0,
    height=82.0
)

entry_f12_image_2 = PhotoImage(
    file=Path(r"assets\frame12\entry_2.png"))
entry_f12_bg_2 = canvas.create_image(
    346.5,
    350.0,
    image=entry_f12_image_2
)
entry_f12_2 = Entry(
    frame12,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f12_2.place(
    x=162.0,
    y=308.0,
    width=369.0,
    height=82.0
)

button_f12_image_1 = PhotoImage(
    file=Path(r"assets\frame12\button_1.png"))
button_f12_1 = Button(
    frame12,
    image=button_f12_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=altaDpto,
    relief="flat"
)
button_f12_1.place(
    x=236.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f12_image_2 = PhotoImage(
    file=Path(r"assets\frame12\button_2.png"))
button_f12_2 = Button(
    frame12,
    image=button_f12_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=bajaDpto,
    relief="flat"
)
button_f12_2.place(
    x=832.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f12_image_3 = PhotoImage(
    file=Path(r"assets\frame12\button_3.png"))
button_f12_3 = Button(
    frame12,
    image=button_f12_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f12_3.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
#===============================frame 12
def altaInfrac():
    archivo=open('archivos/infraccion.txt','a')
    data=entry_f13_2.get()
    archivo.write(data+'\n')
    archivo.close()
    actualizarInfrac()
    return
def actualizarInfrac():
    entry_f13_1['values'] = infraccion()
    return
def bajaInfrac():
    archivo=open('archivos/infraccion.txt','r+')
    lineas=archivo.readlines()
    nuevo=['']*(len(lineas))
    cont=0
    error=True
    for i in infraccion():
        if i ==entry_f13_1.get():
            error=False
    if error==True:
        messagebox.showerror('error','no se ha encontrado el elemento')
        return
    for i in range(len(lineas)):
        if lineas[i]!=entry_f13_1.get() + "\n":
            nuevo[cont]=lineas[i]
            cont+=1
    archivo.close()
    archivo2=open(r'archivos/infraccion.txt','w+')
    archivo2.writelines(nuevo)
    archivo2.close()
    actualizarInfrac()
    return
#===============================frame 13
background_f13 = PhotoImage(
    file=Path(r"assets\frame13\image_1.png"))
label13 = Label( frame13, image = background_f13)
label13.place(x = 0, y = 0)
button_f13_image_1 = PhotoImage(
    file=Path(r"assets\frame12\button_3.png"))
button_f13_1 = Button(
    frame13,
    image=button_f13_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f13_1.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)

entry_f13_image_1 = PhotoImage(
    file=Path(r"assets\frame12\entry_1.png"))
entry_f13_bg_1 = canvas.create_image(
    942.5,
    350.0,
    image=entry_f13_image_1
)
entry_f13_1 = ttk.Combobox(
    frame13,
    values=infraccion()
)
entry_f13_1.place(
    x=758.0,
    y=308.0,
    width=369.0,
    height=82.0
)

entry_f13_image_2 = PhotoImage(
    file=Path(r"assets\frame12\entry_2.png"))

entry_f13_2 = Entry(
    frame13,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f13_2.place(
    x=162.0,
    y=308.0,
    width=369.0,
    height=82.0
)

button_f13_image_2 = PhotoImage(
    file=Path(r"assets\frame12\button_1.png"))
button_f13_2 = Button(
    frame13,
    image=button_f13_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: altaInfrac(),
    relief="flat"
)
button_f13_2.place(
    x=236.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f13_image_3 = PhotoImage(
    file=Path(r"assets\frame12\button_2.png"))
button_f13_3 = Button(
    frame13,
    image=button_f13_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: bajaInfrac(),
    relief="flat"
)
button_f13_3.place(
    x=832.0,
    y=453.0,
    width=221.0,
    height=86.0
)
#===============================frame 13
def altaLocal():
    archivo=open('archivos/localidades.txt','a')
    data=entry_f14_2.get()
    archivo.write(data+'\n')
    archivo.close()
    actualizarLocal()
    return
def actualizarLocal():
    entry_f14_1['values'] = localidad()
    return
def bajaLocal():
    archivo=open(r'archivos/localidades.txt','r+')
    lineas=archivo.readlines()
    nuevo=['']*(len(lineas)-1)
    cont=0
    error=True
    for i in localidad():
        if i ==entry_f14_1.get():
            error=False
    if error==True:
        messagebox.showerror('error','no se ha encontrado el elemento')
        return
    for i in range(len(lineas)-1):
        if lineas[i]!=entry_f14_1.get():
            nuevo[cont]=lineas[i]
            cont+=1
    archivo.close()
    archivo2=open(r'archivos/localidades.txt','w')
    archivo2.writelines(nuevo)
    archivo2.close()
    actualizarLocal()
    return
#===============================frame 14
background_f14 = PhotoImage(
    file=Path(r"assets\frame14\image_1.png"))
label14 = Label( frame14, image = background_f14)
label14.place(x = 0, y = 0)
entry_f14_image_1 = PhotoImage(
    file=Path(r"assets\frame14\entry_1.png"))
entry_f14_bg_1 = canvas.create_image(
    942.5,
    350.0,
    image=entry_f14_image_1
)
entry_f14_1 = ttk.Combobox(
    frame14,
    values=localidad()
)
entry_f14_1.place(
    x=758.0,
    y=308.0,
    width=369.0,
    height=82.0
)

entry_f14_image_2 = PhotoImage(
    file=Path(r"assets\frame14\entry_2.png"))
entry_f14_bg_2 = canvas.create_image(
    346.5,
    350.0,
    image=entry_f14_image_2
)
entry_f14_2 = Entry(
    frame14,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f14_2.place(
    x=162.0,
    y=308.0,
    width=369.0,
    height=82.0
)

button_f14_image_1 = PhotoImage(
    file=Path(r"assets\frame14\button_1.png"))
button_f14_1 = Button(
    frame14,
    image=button_f14_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: altaLocal(),
    relief="flat"
)
button_f14_1.place(
    x=236.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f14_image_2 = PhotoImage(
    file=Path(r"assets\frame14\button_2.png"))
button_f14_2 = Button(
    frame14,
    image=button_f14_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: bajaLocal(),
    relief="flat"
)
button_f14_2.place(
    x=832.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f14_image_3 = PhotoImage(
    file=Path(r"assets\frame14\button_3.png"))
button_f14_3 = Button(
    frame14,
    image=button_f14_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f14_3.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
#===============================frame 14
def altaParaje():
    archivo=open('archivos/paraje.txt','a')
    data=entry_f15_2.get()
    archivo.write(data+'\n')
    archivo.close()
    actualizarParaje()
    return
def actualizarParaje():
    entry_f15_1['values'] = puesto()
    return
def bajaParaje():
    archivo=open(r'archivos/paraje.txt','r+')
    lineas=archivo.readlines()
    nuevo=['']*(len(lineas)-1)
    cont=0
    error=True
    for i in puesto():
        if i ==entry_f15_1.get():
            error=False
    if error==True:
        messagebox.showerror('error','no se ha encontrado el elemento')
        return
    for i in range(len(lineas)):
        if lineas[i]!=entry_f15_1.get():
            nuevo[cont]=lineas[i]
            cont+=1
    archivo.close()
    archivo2=open(r'archivos/paraje.txt','w')
    archivo2.writelines(nuevo)
    archivo2.close()
    actualizarParaje()
    return
#===============================frame 15
background_f15 = PhotoImage(
    file=Path(r"assets\frame15\image_1.png"))
label15 = Label( frame15, image = background_f15)
label15.place(x = 0, y = 0)
button_f15_image_1 = PhotoImage(
    file=Path(r"assets\frame15\button_1.png"))
button_f15_1 = Button(
    frame15,
    image=button_f15_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: altaParaje(),
    relief="flat"
)
button_f15_1.place(
    x=236.0,
    y=453.0,
    width=221.0,
    height=86.0
)

button_f15_image_2 = PhotoImage(
    file=Path(r"assets\frame15\button_2.png"))
button_f15_2 = Button(
    frame15,
    image=button_f15_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: bajaParaje(),
    relief="flat"
)
button_f15_2.place(
    x=832.0,
    y=453.0,
    width=221.0,
    height=86.0
)

entry_f15_image_1 = PhotoImage(
    file=Path(r"assets\frame15\entry_1.png"))
entry_f15_bg_1 = canvas.create_image(
    942.5,
    350.0,
    image=entry_f15_image_1
)
entry_f15_1 = ttk.Combobox(
    frame15,
    values=puesto()
)
entry_f15_1.place(
    x=758.0,
    y=308.0,
    width=369.0,
    height=82.0
)

entry_f15_image_2 = PhotoImage(
    file=Path(r"assets\frame15\entry_2.png"))
entry_f15_bg_2 = canvas.create_image(
    346.5,
    350.0,
    image=entry_f15_image_2
)
entry_f15_2 = Entry(
    frame15,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f15_2.place(
    x=162.0,
    y=308.0,
    width=369.0,
    height=82.0
)

button_f15_image_3 = PhotoImage(
    file=Path(r"assets\frame15\button_3.png"))
button_f15_3 = Button(
    frame15,
    image=button_f15_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f15_3.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
#===============================frame 15

#===============================frame 17
background_f17 = PhotoImage(
    file=Path(r"assets\frame17\image_1.png"))
label17 = Label( frame17, image = background_f17)
label17.place(x = 0, y = 0)
entry_f17_image_1 = PhotoImage(
    file=Path(r"assets\frame17\entry_1.png"))
entry_f17_bg_1 = canvas.create_image(
    639.0,
    429.30767822265625,
    image=entry_f17_image_1
)
entry_f17_1 = Entry(
    frame17,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f17_1.place(
    x=524.0,
    y=409.0,
    width=230.0,
    height=38.6153564453125
)

entry_f17_image_2 = PhotoImage(
    file=Path(r"assets\frame17\entry_2.png"))
entry_f17_bg_2 = canvas.create_image(
    639.0,
    329.5806884765625,
    image=entry_f17_image_2
)
entry_f17_2 = Entry(
    frame17,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f17_2.place(
    x=524.0,
    y=309.0,
    width=230.0,
    height=39.161376953125
)

button_f17_image_1 = PhotoImage(
    file=Path(r"assets\frame17\button_1.png"))
button_f17_1 = Button(
    frame17,
    image=button_f17_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login("normal"),
    relief="flat"
)
button_f17_1.place(
    x=568.0,
    y=508.0,
    width=142.0,
    height=42.0
)

button_f17_image_2 = PhotoImage(
    file=Path(r"assets\frame17\button_2.png"))
button_f17_2 = Button(
    frame17,
    image=button_f17_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame10),
    relief="flat"
)
button_f17_2.place(
    x=124.0,
    y=43.0,
    width=171.0,
    height=51.0
)
#===============================frame 17
#===============================frame 18
opcion_f18=0
filtrof18=False
def sig_f18():
    global opcion_f18
    if opcion_f18==limOpcion_f18es:
        
        grilla_f18(limOpcion_f18es)
        return
    elif opcion_f18<limOpcion_f18es:
        opcion_f18+=1
        
        grilla_f18(opcion_f18)
        return
def atras_f18():
    global opcion_f18
    if opcion_f18==0:
        grilla_f18(0)
        
        return
    elif opcion_f18>0:
        opcion_f18-=1
        grilla_f18(opcion_f18)
        
        return
def grilla_f18(dato):
    registros_f18=matriz_f18(dato)
    label_f18_1.config(text=registros_f18[0][0])
    label_f18_2.config(text=registros_f18[0][1])
    label_f18_3.config(text=registros_f18[0][2])
    label_f18_4.config(text=registros_f18[0][3])
    label_f18_5.config(text=registros_f18[0][4])
    label_f18_6.config(text=registros_f18[0][5])
    label_f18_7.config(text=registros_f18[1][0])
    label_f18_8.config(text=registros_f18[1][1])
    label_f18_9.config(text=registros_f18[1][2])
    label_f18_10.config(text=registros_f18[1][3])
    label_f18_11.config(text=registros_f18[1][4])
    label_f18_12.config(text=registros_f18[1][5])
    label_f18_13.config(text=registros_f18[2][0])
    label_f18_14.config(text=registros_f18[2][1])
    label_f18_15.config(text=registros_f18[2][2])
    label_f18_16.config(text=registros_f18[2][3])
    label_f18_17.config(text=registros_f18[2][4])
    label_f18_18.config(text=registros_f18[2][5])
    label_f18_19.config(text=registros_f18[3][0])
    label_f18_20.config(text=registros_f18[3][1])
    label_f18_21.config(text=registros_f18[3][2])
    label_f18_22.config(text=registros_f18[3][3])
    label_f18_23.config(text=registros_f18[3][4])
    label_f18_24.config(text=registros_f18[3][5])
    label_f18_25.config(text=registros_f18[4][0])
    label_f18_26.config(text=registros_f18[4][1])
    label_f18_27.config(text=registros_f18[4][2])
    label_f18_28.config(text=registros_f18[4][3])
    label_f18_29.config(text=registros_f18[4][4])
    label_f18_30.config(text=registros_f18[4][5])
    label_f18_31.config(text=registros_f18[5][0])
    label_f18_32.config(text=registros_f18[5][1])
    label_f18_33.config(text=registros_f18[5][2])
    label_f18_34.config(text=registros_f18[5][3])
    label_f18_35.config(text=registros_f18[5][4])
    label_f18_36.config(text=registros_f18[5][5])
    label_f18_37.config(text=registros_f18[6][0])
    label_f18_38.config(text=registros_f18[6][1])
    label_f18_39.config(text=registros_f18[6][2])
    label_f18_40.config(text=registros_f18[6][3])
    label_f18_41.config(text=registros_f18[6][4])
    label_f18_42.config(text=registros_f18[6][5])

def matriz_f18(dato):
    campos=abrir_f18()
    cont=0
    resultado=[[str(' ') for i in range(6)]for j in range(8)]
    if dato==limOpcion_f18es:
        for j in range(dato*7,len(campos)):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    elif dato<limOpcion_f18es:
        for j in range(dato*7,(dato+1)*7):
            for i in range(6):
                resultado[cont][i]=campos[j][i]
            cont+=1
    return resultado
def abrir_f18():
    global filtrof18
    if filtrof18==False:
        archivo=open('archivos/denunciacidi.txt','r')
        archivoanoni=open('archivos/denunciaanon.txt','r')
        registros_f18=archivo.readlines()
        registros_2_f18=archivoanoni.readlines()
        resultante=['']*(len(registros_2_f18)+len(registros_f18))
        contador=0
        global limOpcion_f18es
        limOpcion_f18es=(len(registros_f18)+len(registros_2_f18))//7
        for i in registros_f18:
            resultante[contador]=i.split('|')
            contador+=1
        for i in registros_2_f18:
            resultante[contador]=i.split('|')
            contador+=1
    else:
        resultante=busqueda()
        if resultante==[]:
            messagebox.showinfo('no hay denuncias','no se ha encontrado una denuncia')
            filtrof18=False
            return abrir_f18()
        limOpcion_f18es=len(resultante)//7

    return resultante
def busqueda():
    global filtrof18
    entry_1D=entry_f18_1.get()
    entry_2D=entry_f18_2.get()
    entry_3D=entry_f18_4.get()
    entry_4D=entry_f18_3.get()
    if entry_1D=='' and entry_2D=='' and entry_4D=='' and entry_3D=='':
        filtrof18==False
        return[]
    else:
        filtrof18=True
    registros=[]
    denunciasA=open('archivos/denunciaanon.txt','r')
    for linea in denunciasA:
        linea=linea.split('|')
        if entry_1D==linea[0] or entry_2D==linea[1] or entry_3D==linea[2] or entry_4D==linea[3]:
            registros.append(linea)
    denunciasA.close()
    denunciasC=open('archivos/denunciacidi.txt','r')
    for linea in denunciasC:
        linea=linea.split('|')
        if entry_1D==linea[0] or entry_2D==linea[1] or entry_3D==linea[2] or entry_4D==linea[3]:
            registros.append(linea)
    denunciasC.close()
    
    return registros

def botonf18():
    busqueda()
    grilla_f18(0)


background_f18 = PhotoImage(
    file=Path(r"assets/frame18/image_1.png"))
label18 = Label( frame18, image = background_f18)
label18.place(x = 0, y = 0)

registros_f18=matriz_f18(0)


button_f18_image_1 = PhotoImage(
    file=Path(r"assets/frame18/button_1.png"))
button_f18_1 = Button(
    frame18,
    image=button_f18_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_frame(frame0),
    relief="flat"
)
button_f18_1.place(
    x=122.0,
    y=34.0,
    width=171.0,
    height=51.0
)

entry_f18_image_1 = PhotoImage(
    file=Path(r"assets/frame18/entry_1.png"))
entry_f18_bg_1 = canvas.create_image(
    440.0,
    186.5,
    image=entry_f18_image_1
)
entry_f18_1 = Entry(
    frame18,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f18_1.place(
    x=379.0,
    y=172.0,
    width=122.0,
    height=27.0
)

entry_f18_image_2 = PhotoImage(
    file=Path(r"assets/frame18/entry_2.png"))
entry_f18_bg_2 = canvas.create_image(
    647.0,
    186.5,
    image=entry_f18_image_2
)
entry_f18_2 = Entry(
    frame18,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_f18_2.place(
    x=586.0,
    y=172.0,
    width=122.0,
    height=27.0
)

entry_f18_image_3 = PhotoImage(
    file=Path(r"assets/frame18/entry_3.png"))
entry_f18_bg_3 = canvas.create_image(
    1054.0,
    186.5,
    image=entry_f18_image_3
)
entry_f18_3 = ttk.Combobox(
    frame18,
values=localidad()
)
entry_f18_3.place(
    x=993.0,
    y=172.0,
    width=122.0,
    height=27.0
)

entry_f18_image_4 = PhotoImage(
    file=Path(r"assets/frame18/entry_4.png"))
entry_f18_bg_4 = canvas.create_image(
    853.0,
    186.5,
    image=entry_f18_image_4
)
entry_f18_4 = ttk.Combobox(
    frame18,
    values=infraccion()
)
entry_f18_4.place(
    x=792.0,
    y=172.0,
    width=122.0,
    height=27.0
)

button_f18_image_2 = PhotoImage(
    file=Path(r"assets/frame18/button_2.png"))
button_f18_2 = Button(
    frame18,
    image=button_f18_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: botonf18(),
    relief="flat"
)
button_f18_2.place(
    x=100.0,
    y=140.0,
    width=215.0,
    height=64.0
)


label_f18_1=Label(
master=frame18,
anchor="nw",
text=registros_f18[0][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_1.place(
x=110.0,
y=298.0
)
label_f18_2 = Label(
master=frame18,
anchor="nw",
text=registros_f18[0][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_2.place(
x=219.0,
y=298.0
)
label_f18_3 = Label(
master=frame18,
anchor="nw",
text=registros_f18[0][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_3.place(
x=339.0,
y=298.0
)
label_f18_4 = Label(
master=frame18,
anchor="nw",
text=registros_f18[0][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_4.place(
x=494.0,
y=298.0
)
label_f18_5 = Label(
master=frame18,
anchor="nw",
text=registros_f18[0][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_5.place(
x=633.0,
y=298.0
)
label_f18_6 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[0][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_6.place(
x=1074.0,
y=298.0
)
label_f18_7 = Label(
master=frame18,
anchor="nw",
text=registros_f18[1][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_7.place(
x=110.00,
y=348.0
)
label_f18_8 = Label(
master=frame18,
anchor="nw",
text=registros_f18[1][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_8.place(
x=219.0,
y=348.0
)
label_f18_9 = Label(
master=frame18,
anchor="nw",
text=registros_f18[1][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_9.place(
x=339.0,
y=348.0
)
label_f18_10 = Label(
master=frame18,
anchor="nw",
text=registros_f18[1][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_10.place(
x=494.0,
y=348.0
)
label_f18_11 = Label(
master=frame18,
anchor="nw",
text=registros_f18[1][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_11.place(
x=633.0,
y=348.0
)
label_f18_12 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[1][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_12.place(
x=1074.0,
y=348.0
)
label_f18_13 = Label(
master=frame18,
anchor="nw",
text=registros_f18[2][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_13.place(
x= 110.00,
y=398.0
)
label_f18_14 = Label(
master=frame18,
anchor="nw",
text=registros_f18[2][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_14.place(
x=219.0,
y=398.0
)
label_f18_15 = Label(
master=frame18,
anchor="nw",
text=registros_f18[2][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_15.place(
x=339.0,
y=398.0
)
label_f18_16 = Label(
master=frame18,
anchor="nw",
text=registros_f18[2][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_16.place(
x=494.0,
y=398.0
)
label_f18_17 = Label(
master=frame18,
anchor="nw",
text=registros_f18[2][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_17.place(
x=633.0,
y=398.0
)
label_f18_18 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[2][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_18.place(
x=1074.0,
y=398.0
)
label_f18_19 = Label(
master=frame18,
anchor="nw",
text=registros_f18[3][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_19.place(
x= 110.00,
y=448.0
)
label_f18_20 = Label(
master=frame18,
anchor="nw",
text=registros_f18[3][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_20.place(
x=219.0,
y=448.0
)
label_f18_21 = Label(
master=frame18,
anchor="nw",
text=registros_f18[3][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_21.place(
x=339.0,
y=448.0
)
label_f18_22 = Label(
master=frame18,
anchor="nw",
text=registros_f18[3][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_22.place(
x=494.0,
y=448.0
)
label_f18_23 = Label(
master=frame18,
anchor="nw",
text=registros_f18[3][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_23.place(
x=633.0,
y=448.0
)
label_f18_24 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[3][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_24.place(
x=1074.0,
y=448.0
)
label_f18_25 = Label(
master=frame18,
anchor="nw",
text=registros_f18[4][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_25.place(
x= 110.00,
y=498.0
)
label_f18_26 = Label(
master=frame18,
anchor="nw",
text=registros_f18[4][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_26.place(
x=219.0,
y=498.0
)
label_f18_27 = Label(
master=frame18,
anchor="nw",
text=registros_f18[4][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_27.place(
x=339.0,
y=498.0
)
label_f18_28 = Label(
master=frame18,
anchor="nw",
text=registros_f18[4][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_28.place(
x=494.0,
y=498.0
)
label_f18_29 = Label(
master=frame18,
anchor="nw",
text=registros_f18[4][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_29.place(
x=633.0,
y=498.0
)
label_f18_30 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[4][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_30.place(
x=1074.0,
y=498.0
)
label_f18_31 = Label(
master=frame18,
anchor="nw",
text=registros_f18[5][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_31.place(
x=110.00,
y=548.0
)
label_f18_32 = Label(
master=frame18,
anchor="nw",
text=registros_f18[5][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_32.place(
x=219.0,
y=548.0
)
label_f18_33 = Label(
master=frame18,
anchor="nw",
text=registros_f18[5][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_33.place(
x=339.0,
y=548.0
)
label_f18_34 = Label(
master=frame18,
anchor="nw",
text=registros_f18[5][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_34.place(
x=494.0,
y=548.0
)
label_f18_35 = Label(
master=frame18,
anchor="nw",
text=registros_f18[5][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_35.place(
x=633.0,
y=548.0
)
label_f18_36 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[5][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_36.place(
x=1074.0,
y=548.0
)
label_f18_37 = Label(
master=frame18,
anchor="nw",
text=registros_f18[6][0],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_37.place(
x=110.00,
y=588.0
)
label_f18_38 = Label(
master=frame18,
anchor="nw",
text=registros_f18[6][1],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 14 * -1)
)
label_f18_38.place(
x=219.0,
y=588.0
)
label_f18_39 = Label(
master=frame18,
anchor="nw",
text=registros_f18[6][2],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_39.place(
x=339.0,
y=588.0
)
label_f18_40 = Label(
master=frame18,
anchor="nw",
text=registros_f18[6][3],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_40.place(
x=494.0,
y=588.0
)
label_f18_41 = Label(
master=frame18,
anchor="nw",
text=registros_f18[6][4],
fg='#FFFFFF',
bg='#81bee6',
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_41.place(
x=633.0,
y=588.0
)
label_f18_42 = Label(
master=frame18,
anchor="nw",
fg='#FFFFFF',
bg='#81bee6',
text=registros_f18[6][5],
font=("OpenSansRoman ExtraBold", 16 * -1)
)
label_f18_42.place(
x=1074.0,
y=588.0
)

Atras_f18 = Button(
    frame18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:atras_f18(),
    relief="flat",
    text='<',
)
Atras_f18.place(
    x=882.0,
    y=623.0,
    width=30.0,
    height=30.0
)
Siguiente_f18 = Button(
    frame18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:sig_f18(),
    relief="flat",
    text='>',
)
Siguiente_f18.place(
    x=1102.0,
    y=623.0,
    width=30.0,
    height=30.0,
)

#===============================frame 18
window.resizable(False,False)
mostrar_frame(frame10)
window.mainloop()

