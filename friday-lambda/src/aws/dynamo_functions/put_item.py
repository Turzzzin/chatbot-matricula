from src.aws.clients import dynamodb

def put_item_on_matriculation(phone_number, cpf, user_name, user_email, face_similarity):
    table_name = 'matriculation-db'
    key_rg = f'ingressantes/{phone_number}/picture-rg'
    key_selfie = f'ingressantes/{phone_number}/picture-selfie'
    key_sr = f'ingressantes/{phone_number}/picture-sr'
    
    # Check if manual analiysis is necessary
    if face_similarity < 98:
        analysis_required = 'human'
    else:
        analysis_required = 'rekognition'
        
    item = {
        'cpf': {'S': cpf},
        'phone-number': {'S': phone_number},
        'name': {'S': user_name},
        's3-picture-rg': {'S': key_rg},
        's3-picture-selfie': {'S': key_selfie},
        's3-picture-sr': {'S': key_sr},
        'email': {'S': user_email},
        'face-similarity': {'N': str(face_similarity)},
        'analysis-required': {'S': analysis_required}
    }
    
    dynamodb.put_item(TableName=table_name, Item=item)