import time
from friday_orchestrator.aws.clients import transcribe
import json
import requests

def transcribe_audio(job_name, audio_uri):

    transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': audio_uri},
    MediaFormat='ogg',
    LanguageCode='pt-BR')

    while True:
        response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        status = response['TranscriptionJob']['TranscriptionJobStatus']

        if status in ['COMPLETED', 'FAILED']:
            break
        time.sleep(2)


    if status == 'COMPLETED':
        transcript_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        print(f"Transcript URI: {transcript_uri}")
        transcribe_file = requests.get(transcript_uri).content
        transcribe_file = json.loads(transcribe_file)
        print(transcribe_file)
        text = transcribe_file['results']['transcripts'][0]['transcript']
        print(text)
        text.replace('.','').replace(',','')
        return text
    else:
       print(f"Job {job_name} failed.")
       return None