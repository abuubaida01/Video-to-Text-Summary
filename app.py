from flask import Flask, render_template, request

import dill as pickle
TextSummarizer = pickle.load(open("TextSummarizer.pkl",'rb'))


#-------------------Function----------------- 
from youtube_transcript_api import YouTubeTranscriptApi

from transformers import pipeline
summarizer = pipeline('summarization')

# ## let's make a function
def TakeOutText(link):
    #will get ID
    ID = link.split("=")[1]

    #will get caption 
    transcript = YouTubeTranscriptApi.get_transcript(ID)

    #let's gather text 
    text = " ".join([i['text'] for i in transcript])

    return text




#-----------------------Flask-----------------------
app = Flask(__name__)  # important
# server=app.server

@app.route('/')  # for pointing homepage
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():

    Input= request.form.get('input_T/V') 
    text = TextSummarizer(Input)
    RealText = TakeOutText(Input)

    
    return render_template('predict.html', summary = text, RealText=RealText)
if __name__ == "__main__":
    app.run(debug=True)
