import viacep_methods as ViaCep

# Entrada
cep = ViaCep.validar_cep()

# Consulta CEP
localizacao = ViaCep.consultar_cep(cep)

# Saída
ViaCep.exibir_localizacao(localizacao)