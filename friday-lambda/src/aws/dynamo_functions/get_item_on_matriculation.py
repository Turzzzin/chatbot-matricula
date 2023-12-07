from src.aws.clients import dynamodb

def check_if_registered(cpfIngressante):
    table_name = 'matriculation-db'
    
    item = {
        'cpf': {'S': cpfIngressante}
    }

    registered_user = dynamodb.get_item(TableName=table_name, Key=item)

    if 'Item' in registered_user:
        return True
    else:
        return False

def get_registered_data(cpfIngressante):
    table_name = 'matriculation-db'
    
    item = {
        'cpf': {'S': cpfIngressante}
    }

    registered_user = dynamodb.get_item(TableName=table_name, Key=item)
    return registered_user