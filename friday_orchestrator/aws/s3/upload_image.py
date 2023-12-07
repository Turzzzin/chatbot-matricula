from friday_orchestrator.aws.clients import s3
from friday_orchestrator.utils.get_media import get_media
from friday_orchestrator.utils.env_class import EnvVariables

def upload_image_to_s3(twilio_body, lex_response):
    print('*********LEX RESPONSE NO UPLOAD S3**********')
    print(lex_response)
    user_phone_number = twilio_body['WaId'][0]
    dialogAction = lex_response['sessionState']['dialogAction']
    image_url = twilio_body['MediaUrl0'][0]
    media = get_media(image_url)
    image_content = media.content
    image_bucket_name = EnvVariables.image_bucket

    if 'slotToElicit' in dialogAction:
        slot_to_elicit = dialogAction['slotToElicit']
        print('**********SLOT TO ELICIT**************')
        print(slot_to_elicit)
        if slot_to_elicit == 'pictureRg':
            print("*************UPLOAD RG*****************")
            object_key = f'ingressantes/{user_phone_number}/picture-rg'
            s3.put_object(Body=image_content, Bucket=image_bucket_name, Key=object_key, ContentType='image/jpeg') 

        if slot_to_elicit == 'pictureSelfie':
            object_key = f'ingressantes/{user_phone_number}/picture-selfie'
            s3.put_object(Body=image_content, Bucket=image_bucket_name, Key=object_key, ContentType='image/jpeg')
            
        if slot_to_elicit == 'pictureScholarRecords':
            object_key = f'ingressantes/{user_phone_number}/picture-sr'
            s3.put_object(Body=image_content, Bucket=image_bucket_name, Key=object_key, ContentType='image/jpeg')