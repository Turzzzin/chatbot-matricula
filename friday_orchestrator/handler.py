import base64
import urllib
from friday_orchestrator.aws.s3.upload_image import upload_image_to_s3
from friday_orchestrator.aws.s3.upload_audio import upload_audio_to_s3
from friday_orchestrator.aws.lex.get_lex_response import get_lex_response
from friday_orchestrator.twilio.create_message import create_twilio_message
from friday_orchestrator.aws.lex.get_session import get_lex_session
    
def get_twilio_body(event):
   encoded_body = event['body']
   decoded_body = base64.b64decode(encoded_body)
   decoded_body = urllib.parse.unquote(decoded_body)
   message = urllib.parse.parse_qs(decoded_body)
   
   return message

def orchestrator(event, context):
   twilio_body = get_twilio_body(event)
   user_phone_number = twilio_body['WaId'][0]
   
   if twilio_body['NumMedia'][0] != '0':
      print('**CAIU NO NUMMEDIA != 0')
      lex_response = get_lex_session(user_phone_number)
      print('**LEX RESPONSE NO IF DA MEDIA**')
      print(lex_response)
      
      if twilio_body['MediaContentType0'][0] == 'image/jpeg' or twilio_body['MediaContentType0'][0] == 'image/png':
         print('**CAIU NO CONTENTTYPE = IMAGE')
         upload_image_to_s3(twilio_body, lex_response)
      if twilio_body['MediaContentType0'][0] == 'audio/ogg':
         upload_audio_to_s3(twilio_body)

   lex_response = get_lex_response(twilio_body, user_phone_number)
   create_twilio_message(lex_response, user_phone_number)