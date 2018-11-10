from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
import threading

audioFileName = "question.mp3"
audioType = "audio/mp3"

# If service instance provides API key authentication
service = SpeechToTextV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway-syd.watsonplatform.net/speech-to-text/api',
    iam_apikey='')

models = service.list_models().get_result()
#print(json.dumps(models, indent=2))

model = service.get_model('en-US_BroadbandModel').get_result()
#print(json.dumps(model, indent=2))

#with open(join(dirname(__file__), audioFileName),
#          'rb') as audio_file:
#    print(json.dumps(
#        service.recognize(
#            audio=audio_file,
#            content_type=audioType,
#            timestamps=True,
#            word_confidence=True).get_result(),
#        indent=2))

# Example using websockets
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):
        print("transcript", type(transcript), transcript)

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        print('Service is listening')

    def on_hypothesis(self, hypothesis):
        print("hypothesis: ", type(hypothesis), hypothesis)

    def on_data(self, data):
        print("data: ", type(data), data)

# Example using threads in a non-blocking way
mycallback = MyRecognizeCallback()
audio_file = open(join(dirname(__file__), audioFileName), 'rb')
audio_source = AudioSource(audio_file)
service.recognize_using_websocket(audio_source, "%s; rate=44100" %audioType, mycallback)