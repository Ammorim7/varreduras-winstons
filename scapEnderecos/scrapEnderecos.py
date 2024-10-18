import requests
from bs4 import BeautifulSoup

# URL da página
url = 'http://www.transparencia.rn.gov.br/orgaos-do-governo'

# Realizar a requisição para pegar o conteúdo da página
response = requests.get(url)

# Checar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todas as divs com a classe "tab-content"
    divs_tab_content = soup.find_all('div', class_='tab-content')

    # Abrir um arquivo .txt para salvar as informações
    with open('informacoes_tab_content.txt', 'w', encoding='utf-8') as file:
        if divs_tab_content:
            # Iterar sobre todas as divs encontradas e salvar o texto de cada uma
            for div in divs_tab_content:
                file.write(div.get_text(strip=True) + '\n\n')  # Adicionar uma quebra de linha entre cada div
            print("Informações salvas em 'informacoes_tab_content.txt'")
        else:
            print("Não foram encontradas divs com a classe 'tab-content'.")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")
