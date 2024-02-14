import requests
import json

def consultar_cep(cep):
    # Monta requisição para API ViaCep
    url = f"https://viacep.com.br/ws/{cep}/json/"        
    try:
        # Envia requisição
        response = requests.get(url)
        # Valida retorno da requisição
        response.raise_for_status() 
        # Carrega json retornado
        localizacao = response.json()
        # Tratamento para CEP não encontrado
        if "erro" in localizacao:
            print("Não foi possível obter a localização. Verifique o CEP informado e tente novamente.")
            return None
        # Retorna localização encontrada
        return localizacao
    # Tratamento para Bad Request (status_code = 400)
    except requests.exceptions.RequestException as e:
        print(f"Falha ao consultar CEP informado. Erro: {e}")
        return None

def validar_cep():
    # Valida CEP informado - Somente números e deve conter 8 dígitos
    while True:
        cep = input("Informe o CEP (somente números): ")        
        if cep.isdigit() and len(cep) == 8:
            return cep
        else:
            print("CEP fornecido inválido. Informe um CEP válido com 8 dígitos.")

def exibir_localizacao(localizacao):
    # Mostra todas informações retornada pela API
    if localizacao:
        print(f"CEP         : {localizacao['cep']}\n"
              f"Logradouro  : {localizacao['logradouro']}\n"
              f"Complemento : {localizacao['complemento']}\n"
              f"Bairro      : {localizacao['bairro']}\n"
              f"Localidade  : {localizacao['localidade']}\n"
              f"UF          : {localizacao['uf']}\n"
              f"IBGE        : {localizacao['ibge']}\n"
              f"GIA         : {localizacao['gia']}\n"
              f"DDD         : {localizacao['ddd']}\n"
              f"SIAFI       : {localizacao['siafi']}\n"
              )