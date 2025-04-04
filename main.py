#Definição de Métodos

def codificar_caracter(caracter):
    return chr(ord(caracter) + 1)

def decodificar_caracter(caracter):
    return chr(ord(caracter) - 1) 

def palavra_tamanho_valido(palavra):
    return len(palavra) > 0 and len(palavra) <= 5 

def extrair_letra(palavra,indice):
    return palavra[indice]

def codificar_palavra(palavra): 
     
    palavra_codificada = ''
    qtd_caracteres = len(palavra)
    caracter_atual = 0
    try:
      if caracter_atual < qtd_caracteres:
        palavra_codificada += codificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += codificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += codificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += codificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += codificar_caracter(extrair_letra(palavra,caracter_atual))
    except Exception:
      print("Ocorreu um erro!")    

    return palavra_codificada


def decodificar_palavra(palavra): 
     
    palavra_decodificada = ''
    qtd_caracteres = len(palavra)
    caracter_atual = 0
    try:
      if caracter_atual < qtd_caracteres:
        palavra_codificada += decodificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += decodificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += decodificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += decodificar_caracter(extrair_letra(palavra,caracter_atual))
        caracter_atual += 1
      if caracter_atual < qtd_caracteres:
        palavra_codificada += decodificar_caracter(extrair_letra(palavra,caracter_atual))
    except Exception:
      print("Ocorreu um erro!")    

    return palavra_decodificada

#ENTRADA

palavra_um = input("Digite a primeira palavra (até 5 letras): ")
palavra_dois = input("Digite a segunda palavra (até 5 letras): ")
palavra_tres = input("Digite a terceira palavra (até 5 letras): ")
palavra_codificada = input("Digite uma palavra codificada para decodificar (até 5 letras): ")


#PROCESSAMENTO

if not palavra_tamanho_valido(palavra_um) or not palavra_tamanho_valido(palavra_dois) or not palavra_tamanho_valido(palavra_tres) or not palavra_tamanho_valido(palavra_codificada):
    print("Cada palavra deve ter entre 1 e 5 letras!")
else:  
    print("Mensagem codificada: {} {} {}".format(codificar_palavra(palavra_um),codificar_palavra(palavra_dois), codificar_palavra(palavra_tres)));
    print("Palavra decodificada: {}".format(decodificar_palavra(palavra_codificada)))



