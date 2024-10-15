import requests

# Lista de municípios do estado de Espirito Santo (você pode expandir ou ajustar conforme necessário)
municipios = [
  "afonsoclaudio",
  "aguadocedonorte",
  "aguiabranca",
  "alegre",
  "alfredochaves",
  "altorionovo",
  "anchieta",
  "apiaca",
  "aracruz",
  "atiliovivacqua",
  "baixaogrande",
  "barradesaofrancisco",
  "boaesperanca",
  "bomjesusdonorte",
  "brejetuba",
  "cachoeirodeitapemirim",
  "cariacica",
  "castelo",
  "colatina",
  "conceicaodabarra",
  "conceicaodocastelo",
  "divinodesaolourenco",
  "domingosmartins",
  "doresdoriopreto",
  "ecoporanga",
  "fundao",
  "governadorlindenberg",
  "guacui",
  "guarapari",
  "ibatiba",
  "ibiracu",
  "iconha",
  "irupi",
  "itaguaçu",
  "itapemirim",
  "itueta",
  "jaguare",
  "joaoneiva",
  "lajinha",
  "linhares",
  "mantenopolis",
  "marataizes",
  "marechalfloriano",
  "marilandia",
  "mimosodosul",
  "montanha",
  "mucurici",
  "munizfreire",
  "muqui",
  "novavenecia",
  "pancas",
  "pedrocanario",
  "pinheiros",
  "piuma",
  "pontobelo",
  "presidentekennedy",
  "riobananal",
"rionovodosul",       
  "santaleopoldina",
  "santamariadejetiba",
  "santateresa",
  "saodomingosdonorte",
  "saogabrieladapalha",
  "saomateus",
  "saorochodocanaa",
  "serra",
  "sooretama",
  "vargemalta",
  "vendaova",
  "viana",
  "vilavelha",
  "vitoria"
]



# Função para gerar URL com base no nome do município
def gerar_url_prefeitura(municipio):
    return f"https://www.{municipio}.es.gov.br"

# Função para verificar se a URL está ativa
def verificar_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Iterar sobre a lista de municípios e testar as URLs
urls_ativas = []
for municipio in municipios:
    url = gerar_url_prefeitura(municipio)
    if verificar_url(url):
        urls_ativas.append(url)
        print(url)

# Exibir as URLs que estão ativas
print("Codigo finalizado!")

print(urls_ativas)
