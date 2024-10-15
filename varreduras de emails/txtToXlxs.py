import pandas as pd

with open("contatos/emails 15-11.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Vamos separar as partes por "Contatos encontrados em"
blocos = texto.split("Contatos encontrados em ")

# Inicializar listas para armazenar os dados
urls = []
emails = []
telefones = []

# Iterar sobre os blocos de contatos
for bloco in blocos[1:]:  # O primeiro item será vazio, então começamos do índice 1
    linhas = bloco.splitlines()
    
    # Extrair URL (primeira linha sempre tem a URL)
    url = linhas[0].replace(":", "").strip()
    urls.append(url)
    
    # Variáveis para armazenar email e telefone temporariamente
    email_list = []
    telefone_list = []
    
    # Iterar sobre as linhas restantes para encontrar emails e telefones
    for linha in linhas[1:]:
        if "Emails" in linha:
            # Pegar as próximas linhas até encontrar algo que não seja email
            continue
        elif "Telefones" in linha:
            continue
        elif "@" in linha:
            email_list.append(linha.strip())
        elif "(" in linha or linha.startswith("Telefones") or linha.isdigit():
            telefone_list.append(linha.strip())
    
    # Adicionar os emails e telefones encontrados na lista principal
    emails.append(", ".join(email_list) if email_list else "Nenhum email encontrado")
    telefones.append(", ".join(telefone_list) if telefone_list else "Nenhum telefone encontrado")

# Criar um DataFrame com pandas
df = pd.DataFrame({
    "URL": urls,
    "Emails": emails,
    "Telefones": telefones
})

# Exibir os dados para verificação (opcional)
print(df)

# Salvar os dados em uma planilha Excel
df.to_excel("emails15-11.xlsx", index=False)
