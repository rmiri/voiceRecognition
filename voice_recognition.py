import speech_recognition


recognizer = speech_recognition.Recognizer()

def speech():
    with speech_recognition.Microphone() as source:
        print("say something")
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio)
            print(response)
        except speech_recognition.UnknownValueError:
            print("I CAN'T HEAR YOU")
        except speech_recognition.RequestError:
            print("too busy, talk to you later")

speech()
