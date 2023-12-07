from src.aws.clients import dynamodb

def check_if_approved(cpfIngressante):
    table_name = 'approved-db'
    
    item = {
        'cpf': {'S': cpfIngressante}
    }

    approved_data = dynamodb.get_item(TableName=table_name, Key=item)
    
    if 'Item' in approved_data:
        return True
    else:
        return False
        
def get_approved_data(cpfIngressante):
    table_name = 'approved-db'
    
    item = {
        'cpf': {'S': cpfIngressante}
    }

    approved_data = dynamodb.get_item(TableName=table_name, Key=item)
    return approved_data