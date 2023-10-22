# Intractive Language Translator

# import web app flask packages

from flask import Flask,request,render_template,flash,send_file
from wtforms import SelectField
from flask_wtf import FlaskForm 
from time import sleep

# import translate packages

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

def transalate_to(text,src_lang,dest_lang):
    translation=translate_text.translate(text=text,src=src_lang,dest=dest_lang)
    my_text=translation.text
    my_audio = "static/translate_lang.mp3"  # File path for saving the audio
    try:
        voice = gTTS(text=my_text, slow=False)
        voice.save(my_audio)
    except Exception as e:
        print("Error in audio conversion:", e)
        voice=False
    return my_text,voice

# speech recoginizatation and  convert to text

def take_speech():
    with sr.Microphone() as source: # accessing microphone 
 
        r.energy_threshold = 300  # Adjust this threshold for quality recoginization
        r.dynamic_energy_threshold = False
        r.pause_threshold = 0.8
        #print("Speek......")

        # noise reduction and listen voice

        r.adjust_for_ambient_noise(source) 
        a=r.listen(source,timeout=None)
        try:
            text=r.recognize_google(a) # voice to text
            return text
        except sr.UnknownValueError:
            return "Not listened"
        except sr.RequestError:
            return "Network Problem"
        except Exception:
            return "try after some time"
        
# web application 
# Flask form creation for web page

class Form(FlaskForm):
    l=languages()
    from_languages=SelectField('languages',choices=l)
    languages=SelectField('languages',choices=l)

# Flask app creation for web app

app = Flask(__name__, static_url_path='/static')
app.secret_key='1236547890'

# route home pagetext=""

get_speech,on=False,False
text,speek="",""

@app.route("/")
def home():
    return render_template("index.html",form=Form())
@app.route("/record",methods=['GET','POST'])
def record():
    global text,speek,get_speech,user_lang,required_lang,on
    text=""
    on=True
    get_speech=False

    # getting data from web page form

    on_mic=request.form.to_dict()['acess-phone']
    user_lang=request.form.to_dict()['from_languages']
    required_lang=request.form.to_dict()['languages']
    on_text=request.form.to_dict()['give_text']
    print(on_text)
    if on_text!="":
        text=on_text
        get_speech=True
        speek='Somethng Problem.....'
        return result()
    if on_mic=="True":
        while on:
            speek=take_speech()
            if speek not in ["Not listened","Network Problem","try after some time"]:
                text+=" "+speek
                get_speech=True
    return home()

# Result to web page

@app.route("/file_get",methods=['GET','POST'])
def file_get():
    global speek,text,user_lang,required_lang,get_speech
    file=request.files['file']
    if file.filename!='':
        text=file.read().decode('utf-8')
        get_speech=True
        user_lang=request.form.to_dict()['l']
        required_lang=request.form.to_dict()['f']
    else:
        speek='File not uploaded refresh and retry.....'
    return result()
@app.route("/result",methods=['GET','POST'])
def result():
    global text,on,user_lang,required_lang,get_speech,speek
    on=False
    if get_speech:
        sleep(4)
        text=text.lstrip(" ")
        my_text,voice=transalate_to(text,user_lang,required_lang)
        flag=text+" ("+user_lang+")"
        my_text=my_text+" ("+required_lang+")"
        text=""
        if voice:
            return render_template("index.html",message=flag,msg=my_text,form=Form(),my_audio="translate_lang.mp3")
        else:
            return home()
        
    flash(speek)
    text=""
    return home()

# Main function for the app

if __name__ == "__main__":
    app.run()