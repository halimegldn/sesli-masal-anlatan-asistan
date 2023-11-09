import playsound
import speech_recognition as sr
from gtts import gTTS
import random
import winsound
import time
import vlc
import os
from tkinter import *
#a=int(input())
def play(a):
    try:
        p.stop()
    except:
        b = 1
    p = vlc.MediaPlayer(os.getcwd() + a)
    p.play()
root = Tk()
buton1 = Button(root, text='music1',padx=25 ,pady=10,foreground="blue",background="black",command=lambda: play('\music1.mp3') )
buton1.pack()
buton2 = Button(root, text='music2',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music2.mp3') )
buton2.pack()
buton3 = Button(root, text='music3',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music3.mp3') )
buton3.pack()
buton4 = Button(root, text='music4',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music4.mp3') )
buton4.pack()
buton4 = Button(root, text='music5',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music5.mp3') )
buton4.pack()
buton6 = Button(root, text='music6',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music6.mp3') )
buton6.pack()
buton7 = Button(root, text='music7',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music7.mp3') )
buton7.pack()
buton8 = Button(root, text='music8',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music8.mp3') )
buton8.pack()
buton9 = Button(root, text='music9',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music9.mp3') )
buton9.pack()
buton10 = Button(root, text='music10',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music10.mp3') )
buton10.pack()
buton11 = Button(root, text='music11',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music11.mp3') )
buton11.pack()
buton12 = Button(root, text='music12',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music12.mp3') )
buton12.pack()
buton13= Button(root, text='music13',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music13.mp3') )
buton13.pack()
buton14 = Button(root, text='music14',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music14.mp3') )
buton14.pack()
buton15 = Button(root, text='music15',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music15.mp3') )
buton15.pack()
buton16 = Button(root, text='music16',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music16.mp3') )
buton15.pack()
buton17 = Button(root, text='music17',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music17.mp3') )
buton17.pack()
buton18 = Button(root, text='music18',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music18.mp3') )
buton18.pack()
buton19 = Button(root, text='music19',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music19.mp3') )
buton19.pack()
buton20 = Button(root, text='music20',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music20.mp3') )
buton20.pack()
buton21 = Button(root, text='music21',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music21.mp3') )
buton21.pack()
buton22 = Button(root, text='music22',padx=25, pady=10,foreground="blue",background="black",command=lambda: play('\music22.mp3') )
buton22.pack()
def konus(yazı):
    tts=gTTS(text=yazı,lang="tr")
    dosya_ismi="ses"+str(random.randint(0,100000000000000000000))+".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)
#konus("merhaba nasılsın")
def sesi_kaydet():
    global yazı
    print('Merhaba sizi dinliyorum')
    r=sr.Recognizer()
    with sr.Microphone() as kaynak:
        ses=r.listen(kaynak)
        soylenen_cumle=""
        try:
            soylenen_cumle=r.recognize_google(ses,language="Tr")
            print(soylenen_cumle)
            return soylenen_cumle
        except Exception:

            print("Söylediğin cümleyi anlayamadım.")
            return 'Tekrar söyler misin?'
c = 0
a = 1
p = vlc.MediaPlayer(os.getcwd()+'\music1.mp3')
while a == 1:
    yazı=sesi_kaydet()
    print(yazı)
    if "bir"==yazı or "1"==yazı:
        if c != 0:
            p.stop()
        print(yazı)
        p = vlc.MediaPlayer(os.getcwd()+'\music1.mp3')
        p.play()
    elif "2"==yazı or "2"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd()+'\music2.mp3')
        p.play()
    elif "üç"==yazı or "3"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music3.mp3')
        p.play()
    elif "dört"==yazı or "4"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music4.mp3')
        p.play()
    elif "beş"==yazı or "5"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music5.mp3')
        p.play()
    elif "altı"==yazı or "6"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music6.mp3')
        p.play()
    elif "yedi"==yazı or "7"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music7.mp3')
        p.play()
    elif "sekiz"==yazı or "8"==yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music8.mp3')
        p.play()
    elif "dokuz" == yazı or "9" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music9.mp3')
        p.play()
    elif "on" == yazı or "10" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music10.mp3')
        p.play()
    elif "on bir" == yazı or "11" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music11.mp3')
        p.play()
    elif "on iki" == yazı or "12" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music12.mp3')
        p.play()
    elif "on üç" == yazı or "13" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music13.mp3')
        p.play()
    elif "on dört" == yazı or "14" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music14.mp3')
        p.play()
    elif "on beş" == yazı or "15" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music15.mp3')
        p.play()
    elif "on altı" == yazı or "16" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music16.mp3')
        p.play()
    elif "on yedi" == yazı or "17" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music17.mp3')
        p.play()
    elif "on sekiz" == yazı or "18" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music18.mp3')
        p.play()
    elif "on dokuz" == yazı or "19" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music19.mp3')
        p.play()
    elif "yirmi" == yazı or "20" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music20.mp3')
        p.play()
    elif "yirmi bir" == yazı or "21" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music21.mp3')
        p.play()
    elif "yirmi iki" == yazı or "22" == yazı:
        if c != 0:
            p.stop()
        p = vlc.MediaPlayer(os.getcwd() + '\music22.mp3')
        p.play()
        #konus("iyiyim sen nasılsın")
    elif "tuşlar" in yazı:
        root.mainloop()
    elif "dur" in yazı:
        if c != 0:
            p.stop()
    c = 1
