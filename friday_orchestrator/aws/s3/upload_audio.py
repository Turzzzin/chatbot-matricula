from friday_orchestrator.aws.clients import s3
from friday_orchestrator.utils.get_media import get_media
from friday_orchestrator.utils.env_class import EnvVariables

def upload_audio_to_s3(twilio_body):   
    user_phone_number = twilio_body['WaId'][0]
    audio_url = twilio_body['MediaUrl0'][0]
    message_sid = twilio_body['MessageSid'][0]

    audio_content = get_media(audio_url).content
    audio_bucket_name = EnvVariables.audio_bucket
    object_key = f'{user_phone_number}/user-audio/{message_sid}'

    s3.put_object(Body=audio_content, Bucket=audio_bucket_name, Key=object_key, ContentType='audio/ogg')
