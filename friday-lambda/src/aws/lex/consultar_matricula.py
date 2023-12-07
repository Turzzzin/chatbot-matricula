from src.utils.validate_cpf import validate_cpf
from src.aws.dynamo_functions.get_item_on_matriculation import check_if_registered, get_registered_data

def handler(event):
    invocation_source = event['invocationSource']
    if invocation_source == 'DialogCodeHook':
        next_slot = event['proposedNextState']['dialogAction']['slotToElicit']
        
        if next_slot == 'goToFeedback':
            cpfIngressante = event['sessionState']['intent']['slots']['cpfIngressante']['value']['originalValue']
            cpf_is_valid = validate_cpf(cpfIngressante)
            is_registered = check_if_registered(cpfIngressante)
            
            if cpf_is_valid:
                if is_registered:
                    registered_data = get_registered_data(cpfIngressante)
                    user_name = registered_data['Item']['name']['S']
                    user_email = registered_data['Item']['email']['S'] 
                    analysis_required = registered_data['Item']['analysis-required']['S']
                    if analysis_required == 'rekognition':
                        response = {
                            "sessionState": event['proposedNextState'],
                            "messages": [
                                {
                                    'contentType': 'PlainText',
                                    'content': f'Opa *{user_name}*, localizei seu CPF no banco de dados!\r\nIsso significa que está *tudo certo* com a sua matrícula :)\r\nAguarde contato pelo email: {user_email}',
                                },
                                {
                                    'contentType': 'PlainText',
                                    'content': 'Você poderia responder um questionário de feedback para melhorarmos o nossos serviço?\r\n*1.* Sim\r\n*2.* Não'
                                }
                            ]
                        }
                    else:
                        response = {
                            "sessionState": event['proposedNextState'],
                            "messages": [
                                {
                                    'contentType': 'PlainText',
                                    'content': f'Opa *{user_name}*, localizei seu CPF no banco de dados! Porém, o reconhecimento facial não apresentou um resultado satisfatório.\r\nIsso significa que uma análise será feita manualmente por um funcionário do Centro Paula Souza.\r\nAguarde contato pelo email: {user_email}',
                                },
                                {
                                    'contentType': 'PlainText',
                                    'content': 'Você poderia responder um questionário de feedback para melhorarmos o nossos serviço?\r\n*1.* Sim\r\n*2.* Não'
                                }
                            ]
                        }
                else:
                    print(event['proposedNextState'])
                    response = {
                        "sessionState": event['proposedNextState'],
                        "messages": [
                            {
                              'contentType': 'PlainText',
                              'content': 'Não encontrei seu CPF no banco de dados!\r\nVocê não está matriculado :('
                            }
                        ]
                    }                    
                    
            else:
                event['proposedNextState']['dialogAction']['slotToElicit'] = 'cpfIngressante'
                response = {
                    "sessionState": event['proposedNextState'],
                    "messages": [
                            {
                                'contentType': 'PlainText',
                                'content': 'Insira um CPF com apenas 11 digitos numéricos:'
                            }
                        ]
                }
        else:
            response = {
              "sessionState": {
                  "dialogAction": {
                     "type": "Delegate"
                  }
              }
            }
            
    return response