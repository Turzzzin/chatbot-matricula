from src.aws.lex import fazer_matricula
from src.aws.lex import consultar_matricula

def lambda_handler(event, context):
    intent = event['sessionState']['intent']['name']
    invocation_source = event['invocationSource']
    phone_number = event['sessionId']
    
    if intent == 'fazerMatricula':
        response = fazer_matricula.handler(event)
    if intent == 'consultarMatricula':
        response = consultar_matricula.handler(event)
    
    return response