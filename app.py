import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        # clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)
        
        print("...")
        
        # capture the audio
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio, language='id')
            print("Speaker:", text)
            if text == 'berhenti':
                break
        except:
            print('Suara kurang jelas')