import requests
from bs4 import BeautifulSoup

url = 'http://www.transparencia.rn.gov.br/orgaos-do-governo'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    divs_tab_content = soup.find_all('div', class_='tab-content')

    with open('informacoes_tab_content.txt', 'w', encoding='utf-8') as file:
        if divs_tab_content:
            for index, div in enumerate(divs_tab_content):
                # Substituir os <br> por '\n' antes de pegar o texto
                for br in div.find_all('br'):
                    br.replace_with('\n')
                
                # Pegar o texto da div com a formatação de quebra de linha respeitada
                lines = div.get_text().splitlines()  # Splitlines respeita as quebras de linha
                
                file.write(f"Div {index + 1}:\n")  # Adicionar um título para cada div
                for line in lines:
                    file.write(f"    {line.strip()}\n")  # Indentar e salvar a linha
                file.write("\n")  # Quebra de linha entre as divs
            print("Informações salvas em 'informacoes_tab_content.txt'")
        else:
            print("Não foram encontradas divs com a classe 'tab-content'.")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")
