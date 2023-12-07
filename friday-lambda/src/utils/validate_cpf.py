import re

def validate_cpf(cpfIngressante):
    is_cpf_valid = re.match("^[0-9]{11}$", cpfIngressante)
    return is_cpf_valid