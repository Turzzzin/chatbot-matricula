from src.aws.clients import rekognition

def compare_faces(phone_number):
    bucket_name = 'bucket-friday-matricula'
    key_rg = f'ingressantes/{phone_number}/picture-rg'
    key_selfie = f'ingressantes/{phone_number}/picture-selfie'

    rekognition_response = rekognition.compare_faces(
        SourceImage = {
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key_rg
            }
        },
        TargetImage = {
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key_selfie
            }
        }
    )
    
    if rekognition_response['FaceMatches']:
        similarity = rekognition_response['FaceMatches'][0]['Similarity']
    else:
        similarity = 0
        
    return similarity