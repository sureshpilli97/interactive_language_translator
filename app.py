# Intractive Language Translator

# import web app flask packages

from flask import Flask,request,render_template,flash
from wtforms import SelectField
from flask_wtf import FlaskForm 

# import translate and language detection packages

from langdetect import detect
import googletrans

# import speech recognization and text to speech conversion packages

from gtts import gTTS
import speech_recognition as sr 

# voice recognization souce variable declaration

r=sr.Recognizer()

# translation variable declaration

translate_text=googletrans.Translator()

# getting languages languages
 
def languages():
    return list(googletrans.LANGUAGES.values())

# translate text to another language and convert to audio

def transalate_to(text,m):
    mytext=translate_text.translate(text=text,dest=m).text
    #print(mytext)
    voice = gTTS(text=mytext, slow=False)
    #voice.save("D:/mini project/templates/lang.mp3")
    return mytext

# speech recoginizatation and  convert to text

def take_speech():
    with sr.Microphone() as source:
        print("speek.......")
        a=r.listen(source)
        try:
            text=r.recognize_google(a)
            print(text)
            return text
        except sr.UnknownValueError:
            return "Not listened"
        except:
            return "Network Problem"
        
# web application 

text,s,f,m="","",1,""

# Flask form creation in HTML page

class Form(FlaskForm):
    languages=SelectField('languages',choices=languages())
web=Flask(__name__)
web.secret_key='1236547890'
@web.route("/home")
def home():
    global on,text
    text=""
    on=False
    form=Form()
    return render_template("index.html",form=form)
@web.route("/record",methods=['GET','POST'])
def record():
    global on 
    on=True
    global text,s,f,m
    m=request.form.to_dict()['languages']
    while on:
        s=take_speech()
        print(s)
        if s not in ["Not listened","Network Problem"]:
            text+=s
            f=0

# getting data from HTML page

@web.route("/result",methods=['GET','POST'])
def result():
    global text,s,f,m
    if f==0:
        d=detect(s) # language detection
        mytext=transalate_to(text,m)
        flash(text+"("+d+")")
        flash(mytext+" ("+m+")")
    else:
        flash(s)
    return home()