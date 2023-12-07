from friday_orchestrator.utils.env_class import EnvVariables
from friday_orchestrator.aws.clients import lex

def get_lex_session(session_id):
    session = lex.get_session(
        botId=EnvVariables.bot_id,
        botAliasId=EnvVariables.bot_alias_id,
        localeId=EnvVariables.locale_id,
        sessionId=session_id
    )

    return session