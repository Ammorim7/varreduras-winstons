import re

def extrair_emails(arquivo_entrada, arquivo_saida):
    padrao_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()

    emails = re.findall(padrao_email, conteudo)

    emails_unicos = set(emails)
    
    with open(arquivo_saida, 'w') as f:
        for email in emails_unicos:
            f.write(email + '\n')

extrair_emails('varreduras de emails/secretarias_obras_rj.txt', 'varreduras de emails/emails_obras_rj.txt')