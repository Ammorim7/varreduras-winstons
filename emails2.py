import requests
from bs4 import BeautifulSoup
import re

# Função para decodificar e-mails protegidos pelo Cloudflare
def decodificar_cf_email(cf_email):
    r = int(cf_email[:2], 16)
    email = ''.join([chr(int(cf_email[i:i+2], 16) ^ r) for i in range(2, len(cf_email), 2)])
    return email

# Função para extrair emails e telefones de toda a página, incluindo o rodapé
def extrair_contatos(url):
    try:
        # Realiza a requisição à URL
        response = requests.get(url)
        response.raise_for_status()

        # Faz o parsing do HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Conjunto para armazenar os emails e telefones encontrados
        emails = set()
        telefones = set()

        # Regex para encontrar emails normais
        email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        # Regex específica para encontrar apenas números de telefone nos formatos (XX) XXXX-XXXX e (XX) XXXXX-XXXX
        telefone_regex = r"\(\d{2}\)\s?\d{4,5}[-]?\d{4}"

        # Busca e-mails e telefones em toda a página (texto visível)
        emails.update(re.findall(email_regex, soup.get_text()))
        telefones.update(re.findall(telefone_regex, soup.get_text()))

        # Busca e-mails protegidos pelo Cloudflare em toda a página
        cf_email_tags = soup.find_all('a', class_='__cf_email__')
        for tag in cf_email_tags:
            cf_email = tag.get('data-cfemail')
            if cf_email:
                decoded_email = decodificar_cf_email(cf_email)
                emails.add(decoded_email)

        # Busca também em links e atributos de todas as tags
        for tag in soup.find_all(True):  # True para pegar todas as tags
            for attr in tag.attrs:
                attr_value = tag.attrs[attr]
                if isinstance(attr_value, str):
                    # Busca e-mails e telefones nos atributos
                    emails.update(re.findall(email_regex, attr_value))
                    telefones.update(re.findall(telefone_regex, attr_value))

        return emails, telefones

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return set(), set()

# Função para salvar os emails e telefones no arquivo à medida que são encontrados
def salvar_contatos(municipio, emails, telefones, arquivo="contatos.es.txt"):
    with open(arquivo, 'a') as f:
        f.write(f"\nContatos encontrados em {municipio}:\n")
        if emails:
            f.write("Emails:\n")
            for email in emails:
                f.write(f"{email}\n")
        else:
            f.write("Nenhum email encontrado.\n")

        if telefones:
            f.write("Telefones:\n")
            for telefone in telefones:
                f.write(f"{telefone}\n")
        else:
            f.write("Nenhum telefone encontrado.\n")

# Função principal para processar todos os municípios
def coletar_contatos():
    for url in municipios_urls:
        print(f"Coletando contatos de: {url}")
        emails, telefones = extrair_contatos(url)
        salvar_contatos(url, emails, telefones)

# Exemplo: Adicionar URLs das prefeituras para a lista
municipios_urls = ['https://www.afonsoclaudio.es.gov.br', 'https://www.aguadocedonorte.es.gov.br', 'https://www.alegre.es.gov.br', 'https://www.alfredochaves.es.gov.br', 'https://www.altorionovo.es.gov.br', 'https://www.anchieta.es.gov.br', 'https://www.apiaca.es.gov.br', 'https://www.aracruz.es.gov.br', 'https://www.boaesperanca.es.gov.br', 'https://www.brejetuba.es.gov.br', 'https://www.cariacica.es.gov.br', 'https://www.colatina.es.gov.br', 'https://www.conceicaodocastelo.es.gov.br', 'https://www.domingosmartins.es.gov.br', 'https://www.ecoporanga.es.gov.br', 'https://www.fundao.es.gov.br', 'https://www.governadorlindenberg.es.gov.br', 'https://www.guacui.es.gov.br', 'https://www.guarapari.es.gov.br', 'https://www.ibatiba.es.gov.br', 'https://www.ibiracu.es.gov.br', 'https://www.iconha.es.gov.br', 'https://www.irupi.es.gov.br', 'https://www.itapemirim.es.gov.br', 'https://www.jaguare.es.gov.br', 'https://www.joaoneiva.es.gov.br', 'https://www.linhares.es.gov.br', 'https://www.mantenopolis.es.gov.br', 'https://www.marataizes.es.gov.br', 'https://www.marechalfloriano.es.gov.br', 'https://www.marilandia.es.gov.br', 'https://www.munizfreire.es.gov.br', 'https://www.muqui.es.gov.br', 'https://www.novavenecia.es.gov.br', 'https://www.pancas.es.gov.br', 'https://www.pedrocanario.es.gov.br', 'https://www.pinheiros.es.gov.br', 'https://www.piuma.es.gov.br', 'https://www.presidentekennedy.es.gov.br', 'https://www.rionovodosul.es.gov.br', 'https://www.santaleopoldina.es.gov.br', 'https://www.santateresa.es.gov.br', 'https://www.saodomingosdonorte.es.gov.br', 'https://www.saomateus.es.gov.br', 'https://www.serra.es.gov.br', 'https://www.sooretama.es.gov.br', 'https://www.vargemalta.es.gov.br', 'https://www.vilavelha.es.gov.br', 'https://www.vitoria.es.gov.br']



# Coleta os emails e telefones de todas as URLs fornecidas
coletar_contatos()

print(f"Contatos salvos em 'contatos_coletados.txt'.")
