# EXTRAÇÃO DE DOMÍNIO

# Recebe a entrada e armazena na variável "entrada"
entrada = "ana@example.com;bob@test.com"

# Função reponsável por extrair os domínios dos emails


def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')

    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = []
    for email in lista_emails:
        arroba = email.index("@") + 1
        dominio = dominios.append(email[arroba:])

    return dominios


# Imprime a lista de strings com os domínios
extrair_dominios(entrada)


# FORMATANDO DATA
entrada = "15-05-1999;23-11-2003"


def conversor_data(data):
    separador_entrada = data.split(";")
    array_datas = []

    for datas in separador_entrada:
        barras = datas.split("-")
        formato_certo = f"{barras[2]}/{barras[1]}/{barras[0]}"
        array_datas.append(formato_certo)

    return array_datas


conversor_data(entrada)


# CONVERTENDO °C PARA °F //°F = (°C × 9/5) + 32
entrada = "0,10,20,30,40"


def conversor_temp(temperaturas):
    array_temp = entrada.split(",")
    fahrenheit = []

    for temp in array_temp:
        temp = (int(temp)*(9/5) + 32)
        fahrenheit.append(temp)

    return fahrenheit


print(conversor_temp(entrada))
