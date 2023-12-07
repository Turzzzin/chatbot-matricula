from friday_orchestrator.twilio.twilio_client import twilio_client

def create_twilio_message(lex_response, user_phone_number):
    if 'messages' in lex_response:   
        messages_lex = lex_response['messages']

        for message in messages_lex:
            message_content = message['content']
            message = twilio_client.messages.create(from_='whatsapp:+14155238886',
                                            body=message_content,
                                            to=f'whatsapp:+{user_phone_number}')