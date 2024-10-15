from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Função para capturar e-mails de uma página carregada pelo Selenium
def capturar_emails(driver):
    try:
        page_source = driver.page_source
        # Usar regex para encontrar todos os e-mails no corpo da página
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', page_source)
        return emails
    except Exception as e:
        print(f"Erro ao capturar e-mails: {e}")
        return []

# Configura o driver do Selenium usando WebDriver Manager
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa o Chrome em modo headless (sem interface gráfica)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abrir o Google e realizar a pesquisa
driver.get('https://www.google.com')
search_box = driver.find_element("name", 'q')
search_query = 'site:mg.gov.br "secretaria de saúde" e-mail'
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Espera para os resultados carregarem

# Captura os primeiros links de resultados da pesquisa
links = driver.find_elements("css selector", 'a')
result_urls = [link.get_attribute('href') for link in links if link.get_attribute('href') and 'mg.gov.br' in link.get_attribute('href')]

# Abrir o arquivo para salvar os resultados
with open('secretarias_saude_mg.txt', 'w') as f:
    for url in result_urls:
        try:
            driver.get(url)
            time.sleep(2)  # Espera para carregar o conteúdo da página
            emails = capturar_emails(driver)
            if emails:
                f.write(f"URL: {url}\n")
                f.write(f"E-mails: {', '.join(emails)}\n\n")
            else:
                f.write(f"URL: {url}\n")
                f.write("E-mails: Nenhum encontrado\n\n")
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")
            f.write(f"URL: {url}\n")
            f.write("E-mails: Erro ao acessar\n\n")

print("Captura de e-mails finalizada.")

# Fecha o navegador
driver.quit()
