import re

def extrair_emails(arquivo_entrada, arquivo_saida):
    # Expressão regular para capturar emails
    padrao_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Abrir e ler o arquivo de entrada
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()

    # Encontrar todos os emails no conteúdo
    emails = re.findall(padrao_email, conteudo)

    # Remover duplicados convertendo a lista para um conjunto
    emails_unicos = set(emails)
    
    # Salvar os emails únicos encontrados no arquivo de saída
    with open(arquivo_saida, 'w') as f:
        for email in emails_unicos:
            f.write(email + '\n')

# Substitua 'entrada.txt' pelo caminho do arquivo original
# e 'saida.txt' pelo caminho do arquivo onde você quer salvar os emails
extrair_emails('varreduras de emails/secretarias_saude_mg.txt', 'varreduras de emails/emails_saude_mg.txt')