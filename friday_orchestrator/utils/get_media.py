import base64
import requests
from friday_orchestrator.utils.env_class import EnvVariables

def get_media(media_url):
   account_sid = EnvVariables.account_sid
   auth_token = EnvVariables.auth_token

   headers = {
      'Authorization': f'Basic {base64.b64encode(f"{account_sid}:{auth_token}".encode()).decode()}'
   }
   media = requests.get(media_url, headers=headers)

   return media