from src.utils.validate_cpf import validate_cpf
from src.aws.dynamo_functions.get_item_on_approved import check_if_approved, get_approved_data
from src.aws.dynamo_functions.put_item import put_item_on_matriculation
from src.aws.rekognition_functions.compare_faces import compare_faces
from src.aws.rekognition_functions.detect_cpf import detect_cpf

def handler(event):
    invocation_source = event['invocationSource']
    
    if invocation_source == 'DialogCodeHook':
        next_slot = event['proposedNextState']['dialogAction']['slotToElicit']
        
        if next_slot == 'pictureRg':
            cpfIngressante = event['sessionState']['intent']['slots']['cpfIngressante']['value']['originalValue']
            print(cpfIngressante)
            cpf_is_valid = validate_cpf(cpfIngressante)
            is_approved = check_if_approved(cpfIngressante)
            
            if cpf_is_valid:
                if is_approved:
                    response = {
                        "sessionState": event['proposedNextState']
                    }
                else:
                    response = {
                        "sessionState": {
                            "dialogAction": {
                                "type": "Close"
                            },
                            "intent": {
                                "name": "fazerMatricula",
                                "state": "Fulfilled"
                            }
                        },
                        "messages": [
                            {
                              'contentType': 'PlainText',
                              'content': 'Você não está no banco de dados de aprovados :( \r\nInfelizmente não posso continuar com o processo de matricula'
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
        elif next_slot == 'pictureSelfie':
            cpfIngressante = event['sessionState']['intent']['slots']['cpfIngressante']['value']['originalValue']
            phone_number = event['sessionId']
            cpf_is_equal = detect_cpf(phone_number, cpfIngressante)
            print(cpf_is_equal)
            if cpf_is_equal:
                response = {
                    "sessionState": event['proposedNextState']
                }
            else:
                response = {
                    "sessionState": {
                        "dialogAction": {
                            "type": "Close"
                        },
                        "intent": {
                            "name": "fazerMatricula",
                            "state": "Fulfilled"
                        }
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": "O CPF digitado é diferente do detectado na foto do documento.\r\nInfelizmente não posso continuar com o processo de matricula"
                        }
                    ]
                }
            
        elif next_slot == 'goToFeedback':
            cpfIngressante = event['sessionState']['intent']['slots']['cpfIngressante']['value']['originalValue']
            approved_data = get_approved_data(cpfIngressante)
            
            user_name = approved_data['Item']['name']['S']
            user_phone_number = approved_data['Item']['phone-number']['S']
            user_email = approved_data['Item']['email']['S']
            face_similarity = compare_faces(user_phone_number)
            
            put_item_on_matriculation(user_phone_number, cpfIngressante, user_name, user_email, face_similarity)
            
            response = {
              "sessionState": event['proposedNextState'],
              "messages": [
                  {
                      'contentType': 'PlainText',
                      'content': f'Beleza *{user_name}*, seus dados foram enviados para o banco de dados!\r\nAguarde contato pelo email: *{user_email}*'
                  },
                  {
                      'contentType': 'PlainText',
                      'content': 'Você poderia responder um questionário de feedback para melhorarmos o nossos serviço?\r\n*1.* Sim\r\n*2.* Não'
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