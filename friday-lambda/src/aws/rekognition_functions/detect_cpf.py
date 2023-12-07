from src.aws.clients import rekognition
import re

def extract_cpf(text):
    cpf_template = re.findall(r'\b\d{9}/\d{2}\b', text) 
    return cpf_template

def format_cpf(cpf):
   # Remove o caractere '/'
   cpf = cpf.replace('/', '')
   # Junta todos os caracteres em uma única string
   cpf = ''.join(cpf)
   return cpf


def detect_cpf(phone_number, cpfIngressante):
    key_rg = f'ingressantes/{phone_number}/picture-rg'
    bucket_name = 'bucket-friday-matricula'
    
    response = rekognition.detect_text(
       Image = {
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key_rg
            }
        },
    )

    detected_cpf = [cpf for text in response['TextDetections'] if text['Type'] == 'WORD' for cpf in extract_cpf(text['DetectedText'])]
    cpf_string = detected_cpf[0]
    cpf_formated = format_cpf(cpf_string)
    print('******CPF FORMATED*******')
    print(cpf_formated)
    print('******CPF FORMATED*******')
    if cpfIngressante == cpf_formated:
        is_equal = True
    else:
        is_equal = False
    
    print(is_equal)
    return is_equal