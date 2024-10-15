import requests
from bs4 import BeautifulSoup
import re

# Lista de URLs das prefeituras
municipios_urls = ['https://www.adamantina.sp.gov.br', 'https://www.aguai.sp.gov.br', 'https://www.agudos.sp.gov.br', 'https://www.alambari.sp.gov.br', 'https://www.altair.sp.gov.br', 'https://www.altinopolis.sp.gov.br', 'https://www.alvinlandia.sp.gov.br', 'https://www.amparo.sp.gov.br', 'https://www.analandia.sp.gov.br', 'https://www.angatuba.sp.gov.br', 'https://www.apiai.sp.gov.br', 'https://www.aracatuba.sp.gov.br', 'https://www.arandu.sp.gov.br', 'https://www.arapei.sp.gov.br', 'https://www.araraquara.sp.gov.br', 'https://www.araras.sp.gov.br', 'https://www.ariranha.sp.gov.br', 'https://www.assis.sp.gov.br', 'https://www.atibaia.sp.gov.br', 'https://www.auriflama.sp.gov.br', 'https://www.avare.sp.gov.br', 'https://www.balbinos.sp.gov.br', 'https://www.balsamo.sp.gov.br', 'https://www.barretos.sp.gov.br', 'https://www.barrinha.sp.gov.br', 'https://www.barueri.sp.gov.br', 'https://www.bastos.sp.gov.br', 'https://www.batatais.sp.gov.br', 'https://www.bauru.sp.gov.br', 'https://www.bebedouro.sp.gov.br', 'https://www.bertioga.sp.gov.br', 'https://www.bocaina.sp.gov.br', 'https://www.borborema.sp.gov.br', 'https://www.botucatu.sp.gov.br', 'https://www.brauna.sp.gov.br', 'https://www.brodowski.sp.gov.br', 'https://www.brotas.sp.gov.br', 'https://www.buri.sp.gov.br', 'https://www.buritama.sp.gov.br', 'https://www.buritizal.sp.gov.br', 'https://www.cabreuva.sp.gov.br', 'https://www.caieiras.sp.gov.br', 'https://www.cajati.sp.gov.br', 'https://www.cajobi.sp.gov.br', 'https://www.cajuru.sp.gov.br', 'https://www.campinas.sp.gov.br', 'https://www.cananeia.sp.gov.br', 'https://www.canitar.sp.gov.br', 'https://www.capivari.sp.gov.br', 'https://www.caraguatatuba.sp.gov.br', 'https://www.carapicuiba.sp.gov.br', 'https://www.cardoso.sp.gov.br', 'https://www.catigua.sp.gov.br', 'https://www.cedral.sp.gov.br', 'https://www.cerquilho.sp.gov.br', 'https://www.charqueada.sp.gov.br', 'https://www.chavantes.sp.gov.br', 'https://www.colina.sp.gov.br', 'https://www.colombia.sp.gov.br', 'https://www.conchal.sp.gov.br', 'https://www.cosmorama.sp.gov.br', 'https://www.cotia.sp.gov.br', 'https://www.cravinhos.sp.gov.br', 'https://www.cruzeiro.sp.gov.br', 'https://www.cubatao.sp.gov.br', 'https://www.descalvado.sp.gov.br', 'https://www.divinolandia.sp.gov.br', 'https://www.dourado.sp.gov.br', 'https://www.dumont.sp.gov.br', 'https://www.echapora.sp.gov.br', 'https://www.fartura.sp.gov.br', 'https://www.fernandopolis.sp.gov.br', 'https://www.fernao.sp.gov.br', 'https://www.franca.sp.gov.br', 'https://www.garca.sp.gov.br', 'https://www.guaira.sp.gov.br', 'https://www.guapiara.sp.gov.br', 'https://www.guara.sp.gov.br', 'https://www.guaraci.sp.gov.br', 'https://www.guararema.sp.gov.br', 'https://www.guarulhos.sp.gov.br', 'https://www.guatapara.sp.gov.br', 'https://www.guzolandia.sp.gov.br', 'https://www.hortolandia.sp.gov.br', 'https://www.iacri.sp.gov.br', 'https://www.ibitinga.sp.gov.br', 'https://www.icem.sp.gov.br', 'https://www.igarapava.sp.gov.br', 'https://www.igarata.sp.gov.br', 'https://www.indaiatuba.sp.gov.br', 'https://www.ipero.sp.gov.br', 'https://www.itai.sp.gov.br', 'https://www.itanhaem.sp.gov.br', 'https://www.itaoca.sp.gov.br', 'https://www.itatiba.sp.gov.br', 'https://www.itatiba.sp.gov.br', 'https://www.itapetininga.sp.gov.br', 'https://www.itapeva.sp.gov.br', 'https://www.itapevi.sp.gov.br', 'https://www.itapira.sp.gov.br', 'https://www.itaquaquecetuba.sp.gov.br', 'https://www.itarare.sp.gov.br', 'https://www.itatiba.sp.gov.br', 'https://www.itu.sp.gov.br', 'https://www.itupeva.sp.gov.br', 'https://www.jaborandi.sp.gov.br', 'https://www.jaci.sp.gov.br', 'https://www.jacupiranga.sp.gov.br', 'https://www.jales.sp.gov.br', 'https://www.jambeiro.sp.gov.br', 'https://www.jandira.sp.gov.br', 'https://www.jarinu.sp.gov.br', 'https://www.jau.sp.gov.br', 'https://www.jeriquara.sp.gov.br', 'https://www.jumirim.sp.gov.br', 'https://www.jundiai.sp.gov.br', 'https://www.juquitiba.sp.gov.br', 'https://www.lavrinhas.sp.gov.br', 'https://www.leme.sp.gov.br', 'https://www.lindoia.sp.gov.br', 'https://www.limeira.sp.gov.br', 'https://www.lucelia.sp.gov.br', 'https://www.macaubal.sp.gov.br', 'https://www.macedonia.sp.gov.br', 'https://www.magda.sp.gov.br', 'https://www.manduri.sp.gov.br', 'https://www.marilia.sp.gov.br', 'https://www.maua.sp.gov.br', 'https://www.mesopolis.sp.gov.br', 'https://www.miguelopolis.sp.gov.br', 'https://www.miracatu.sp.gov.br', 'https://www.mirandopolis.sp.gov.br', 'https://www.mirassol.sp.gov.br', 'https://www.mirassolandia.sp.gov.br', 'https://www.mococa.sp.gov.br', 'https://www.morungaba.sp.gov.br', 'https://www.motuca.sp.gov.br', 'https://www.novais.sp.gov.br', 'https://www.ocaucu.sp.gov.br', 'https://www.osasco.sp.gov.br', 'https://www.palestina.sp.gov.br', 'https://www.paraibuna.sp.gov.br', 'https://www.pedranopolis.sp.gov.br', 'https://www.pedregulho.sp.gov.br', 'https://www.pedreira.sp.gov.br', 'https://www.piedade.sp.gov.br', 'https://www.pindamonhangaba.sp.gov.br', 'https://www.pinhalzinho.sp.gov.br', 'https://www.piracaia.sp.gov.br', 'https://www.piracicaba.sp.gov.br', 'https://www.pirajui.sp.gov.br', 'https://www.pirangi.sp.gov.br', 'https://www.pirassununga.sp.gov.br', 'https://www.platina.sp.gov.br', 'https://www.poa.sp.gov.br', 'https://www.pompeia.sp.gov.br', 'https://www.pontal.sp.gov.br', 'https://www.pontalinda.sp.gov.br', 'https://www.porangaba.sp.gov.br', 'https://www.pradopolis.sp.gov.br', 'https://www.quadra.sp.gov.br', 'https://www.rafard.sp.gov.br', 'https://www.rancharia.sp.gov.br', 'https://www.restinga.sp.gov.br', 'https://www.rosana.sp.gov.br', 'https://www.roseira.sp.gov.br', 'https://www.rubineia.sp.gov.br', 'https://www.sagres.sp.gov.br', 'https://www.sales.sp.gov.br', 'https://www.salesopolis.sp.gov.br', 'https://www.salmourao.sp.gov.br', 'https://www.saltinho.sp.gov.br', 'https://www.salto.sp.gov.br', 'https://www.sandovalina.sp.gov.br', 'https://www.santos.sp.gov.br', 'https://www.sarapui.sp.gov.br', 'https://www.sertaozinho.sp.gov.br', 'https://www.tabapua.sp.gov.br', 'https://www.tabatinga.sp.gov.br', 'https://www.taciba.sp.gov.br', 'https://www.taiacu.sp.gov.br', 'https://www.taiuva.sp.gov.br', 'https://www.tanabi.sp.gov.br', 'https://www.tapiratiba.sp.gov.br', 'https://www.taquaritinga.sp.gov.br', 'https://www.taquarituba.sp.gov.br', 'https://www.taruma.sp.gov.br', 'https://www.tatui.sp.gov.br', 'https://www.taubate.sp.gov.br', 'https://www.timburi.sp.gov.br', 'https://www.trabiju.sp.gov.br', 'https://www.tremembe.sp.gov.br', 'https://www.tupa.sp.gov.br', 'https://www.turmalina.sp.gov.br', 'https://www.ubarana.sp.gov.br', 'https://www.ubatuba.sp.gov.br', 'https://www.ubirajara.sp.gov.br', 'https://www.urania.sp.gov.br', 'https://www.urupes.sp.gov.br', 'https://www.viradouro.sp.gov.br']


# Função para extrair emails e telefones de uma URL
def extrair_contatos(url):
    try:
        # Realiza a requisição à URL
        response = requests.get(url)
        response.raise_for_status()

        # Faz o parsing do HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Regex para encontrar emails
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))

        # Regex para encontrar telefones (formatos mais comuns)
        telefones = set(re.findall(r"\(?\d{2}\)?\s?\d{4,5}[-.\s]?\d{4}", soup.text))

        # Retorna os emails e telefones encontrados
        return emails, telefones

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return set(), set()

# Função para salvar os emails e telefones no arquivo à medida que são encontrados
def salvar_contatos(municipio, emails, telefones, arquivo="contatos_coletados.txt"):
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

# Coleta os emails e telefones de todas as URLs fornecidas
coletar_contatos()

print(f"Contatos salvos em 'contatos_coletados.txt'.")
