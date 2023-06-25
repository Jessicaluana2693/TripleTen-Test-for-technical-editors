import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o driver do Selenium
driver = webdriver.Chrome()

# 1. Abrir https://www.google.com/search?q=1
driver.get("https://www.google.com/search?q=1")

# 2. Localizar o logo e verificar a visibilidade
logo = driver.find_element(By.ID, "hplogo")
if logo.is_displayed():
    print("O logo está visível.")
else:
    print("O logo não está visível.")

# 3. Localizar a área de texto de pesquisa e verificar a visibilidade
search_box = driver.find_element(By.NAME, "q")
if search_box.is_displayed():
    print("A área de texto de pesquisa está visível.")
else:
    print("A área de texto de pesquisa não está visível.")

# 4. Inserir uma nova consulta de pesquisa
new_search_query = "Teste de automação"
search_box.clear()
search_box.send_keys(new_search_query)
search_box.submit()

# Aguardar um curto período de tempo para a página carregar
time.sleep(2)

# 5. Verificar se a consulta de pesquisa inserida está presente e se não há um placeholder presente
search_results = driver.find_element(By.XPATH, f"//div[@class='s']//span[text()='{new_search_query}']")
if search_results.is_displayed():
    print(f"A consulta de pesquisa '{new_search_query}' está presente nos resultados.")
else:
    print(f"A consulta de pesquisa '{new_search_query}' não está presente nos resultados.")

placeholder = search_box.get_attribute("placeholder")
if not placeholder:
    print("Não há um placeholder presente na área de texto de pesquisa.")
else:
    print(f"O placeholder '{placeholder}' está presente na área de texto de pesquisa.")

# Fechar o navegador
driver.quit()
