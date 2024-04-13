
from datetime import datetime


def validar_tipos(Tipo_de_Acordo, Contrato, Inicio_da_Vigência, Fim_da_Vigência, SKU,
                   Descrição_do_Item, Mecânica, Pack_Size, Código_Brinde, Descrição_Brinde, Bandeira,
                   Abrangência_C, Mês_de_Competência_Contrato, Fornecedor, CNPJ, Categoria_Nível_2,  Valor_Total_do_Subsídio):
    
        # Verifica se 'Tipo_de_Acordo' é uma instância de str (string)
    if not isinstance(Tipo_de_Acordo, str):
        return False
        # Verifica se 'Contrato' é uma instância de str (string)
    if not isinstance(Contrato, str):
        return False
        # Verifica se 'Inicio_da_Vigência' é uma instância de str (datetime)
    if not isinstance(Inicio_da_Vigência, datetime):
        return False
        # Verifica se 'Fim_da_Vigência' é uma instância de str (datetime)
    if not isinstance(Fim_da_Vigência, datetime):
        return False
        # Verifica se 'SKU' é uma instância de str (int)
    if not isinstance(SKU, int):
        return False
        # Verifica se 'Descrição_do_Item' é uma instância de str (str)
    if not isinstance(Descrição_do_Item, str):
        return False
        # Verifica se 'Mecânica' é uma instância de str (str)
    if not isinstance(Mecânica, str):
        return False
        # Verifica se 'Pack_Size' é uma instância de str (int)
    if not isinstance(Pack_Size, int):
        return False
        # Verifica se 'Código_Brinde' é uma instância de str (int)
    if not isinstance(Código_Brinde, int):
        return False
        # Verifica se 'Descrição_Brinde' é uma instância de str (str)
    if not isinstance(Descrição_Brinde, str):
        return False
        # Verifica se 'Bandeira' é uma instância de str (str)
    if not isinstance(Bandeira, str):
        return False
        # Verifica se 'Abrangência_C' é uma instância de str (str)
    if not isinstance(Abrangência_C, str):
        return False
        # Verifica se 'Mês_de_Competência_Contrato' é uma instância de str (str)
    if not isinstance(Mês_de_Competência_Contrato, str):
        return False
        # Verifica se 'Fornecedor' é uma instância de str (str)
    if not isinstance(Fornecedor, str):
        return False
        # Verifica se 'CNPJ' é uma instância de str (int)
    if not isinstance(CNPJ, int):
        return False
        # Verifica se 'Categoria_Nível_2' é uma instância de str (str)
    if not isinstance(Categoria_Nível_2, str):
        return False
        # Verifica se 'Valor_Total_do_Subsídio' é uma instância de str (float)
    if not isinstance(Valor_Total_do_Subsídio, float):
        return False
        # Se todas as verificações passaram, retorna True
    return True