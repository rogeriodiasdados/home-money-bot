from google import genai


# 1.conexão com a IA
Client = genai.Client(api_key='')

# 2.Dados dos sensores (Modulo 1 e 4:tipos e listas)
 
motores = [{'nome': 'motor 01 - esteira','temp':'82.5'},
           {'nome': 'motor 02 - compressorres', 'temp': '95.0'},
           {'nome': 'motor 03 - prensa','temp': 'dado_corrompido'},
           {'nome': 'motor 04 - refinador', 'temp':'45.0'}]

motores_criticos=[]
print ('---Iniciando ronda inteligente---\n')

# ronda de inspeção (modullo 4 : loop 'for')

for  item in motores:
    nome_motor = item["nome"]
    leitura_crua = item["temp"]

    # modulo 5: disjuntor (try except)
    try:
    
        # modulo 1 :convertendo o texto para numero decimal (foat)
        temperatura = float (leitura_crua)

        # tomada de decisão (if/ elif/else)

        if temperatura > 90.0:
            print (f" {nome_motor}|{temperatura}'°c -> alerta critico")
            motores_criticos.append(f"{nome_motor} ({temperatura}°c)")

        elif temperatura > 75.0:
            print (f"{nome_motor} | {temperatura}°c ->atenção temperatura elevada!")

        else:
            print (f"{nome_motor} | {temperatura}°c-> normal")
    except:
        print (f"{nome_motor} | leitura:'{leitura_crua}' -> FALHA NO SENSOR! verificara fiação.")

# 4 e 5. CHAMA A IA E SALVA NO arquivo(modulo 2)


            