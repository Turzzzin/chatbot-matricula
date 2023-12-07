from friday_orchestrator.aws.clients import lex
from friday_orchestrator.aws.transcribe.get_text import transcribe_audio
from friday_orchestrator.utils.env_class import EnvVariables

def get_lex_response(twilio_body, user_phone_number):

    if twilio_body['NumMedia'][0] == '0':
        user_input = twilio_body['Body'][0]
        lex_response = lex.recognize_text(botId=EnvVariables.bot_id,
                                        botAliasId=EnvVariables.bot_alias_id,
                                        localeId=EnvVariables.locale_id,
                                        sessionId=user_phone_number,
                                        text=user_input,)

    if twilio_body['NumMedia'][0] != '0':
        if twilio_body['MediaContentType0'][0] == 'image/jpeg' or twilio_body['MediaContentType0'][0] == 'image/png':
            # Enviar uma mensagem ao Lex indicando que o usuário enviou uma imagem
            lex_response = lex.recognize_text(botId=EnvVariables.bot_id,
                                        botAliasId=EnvVariables.bot_alias_id,
                                        localeId=EnvVariables.locale_id,
                                        sessionId=user_phone_number,
                                        text='Imagem enviada')
            
        if twilio_body['MediaContentType0'][0] == 'audio/ogg':
            # Enviar conteúdo do áudio como input
            message_id = twilio_body['MessageSid'][0]
            key = f'{user_phone_number}/user-audio/{message_id}'
            user_audio_input = transcribe_audio(message_id, f's3://{EnvVariables.audio_bucket}/{key}')
            lex_response = lex.recognize_text(botId=EnvVariables.bot_id,
                                        botAliasId=EnvVariables.bot_alias_id,
                                        localeId=EnvVariables.locale_id,
                                        sessionId=user_phone_number,
                                        text=user_audio_input)
    return lex_response