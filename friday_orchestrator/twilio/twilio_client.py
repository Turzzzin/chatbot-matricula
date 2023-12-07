from friday_orchestrator.utils.env_class import EnvVariables
from twilio.rest import Client

account_sid = EnvVariables.account_sid
auth_token = EnvVariables.auth_token

twilio_client = Client(account_sid, auth_token)