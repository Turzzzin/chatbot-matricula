# import re

# def validate_slots(slots, intent):
    
#     if intent == 'fazerMatricula':
#         if not slots['cpfIngressante']:
#             print("Empty CPF")
#             return {
#                 'is_valid': False,
#                 'violated_slot': 'cpfIngressante',
#                 'message': 'Insira um CPF para continuar!'
#             }
            
#         if not re.match("^[0-9]{11}$", str(slots['cpfIngressante']['value']['originalValue'])):
#             print("Invalid CPF input")
#             return {
#                 'is_valid': False,
#                 'violated_slot': 'cpfIngressante',
#                 'message': 'Insira um CPF com 11 dígitos numéricos:'
#             }
            
#         if not slots['pictureRg']:
#             print("Empty RG picture")
#             return {
#                 'is_valid': False,
#                 'violated_slot': 'pictureRg',
#                 'message': 'Encaminhe uma foto de um documento com foto \r\n(OBS: deve conter seu CPF):'
#             }
            
#         if not slots['pictureSelfie']:
#             print("Empty selfie picture")
#             return {
#                 'is_valid': False,
#                 'violated_slot': 'pictureSelfie',
#                 'message': 'Encaminhe uma selfie sua, com o fundo branco:'
#             }
            
#         if not slots['pictureScholarRecords']:
#             print("Empty SR picture")
#             return {
#                 'is_valid': False,
#                 'violated_slot': 'pictureScholarRecords',
#                 'message': 'Encaminhe uma foto do seu histórico escolar:'
#             }
            
#     return {'is_valid': True}