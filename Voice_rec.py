import speech_recognition as sr
import smtplib
from textblob import TextBlob
#from newspaper import article


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

words=text.split()

finalSentence=' '.join(words)

blob=TextBlob(finalSentence)
sentiment=blob.sentiment.polarity

print(sentiment)
