from selenium import webdriver

# Inicializar o driver do Safari
#Initialize the Safari driver
driver = webdriver.Safari()

# Open the Google About page
# Abrindo o Google About 
driver.get("https://about.google/")

# Locate the headline logo using different locators
# Localize o logotipo do título usando diferentes localizadores

# 1. Using XPath
# 1. Usando XPath
logo_xpath = driver.find_element_by_xpath('//div[@class="logo"]//a')
print("Locator 1 (XPath):", logo_xpath.get_attribute("href"))

# 2. Using CSS selector
# 2. Usando o seletor CSS
logo_css = driver.find_element_by_css_selector('.logo a')
print("Locator 2 (CSS):", logo_css.get_attribute("href"))

# 3. Using class name
# 3. Usando o nome da classe
logo_class = driver.find_element_by_class_name('logo')
print("Locator 3 (Class Name):", logo_class.find_element_by_tag_name('a').get_attribute("href"))

# 4. Using ID
# 4. Usando ID
logo_id = driver.find_element_by_id('logo')
print("Locator 4 (ID):", logo_id.find_element_by_tag_name('a').get_attribute("href"))

# 5. Using link text
# 5. Usando o texto do link
logo_link_text = driver.find_element_by_link_text('Google')
print("Locator 5 (Link Text):", logo_link_text.get_attribute("href"))

# Close the browser
# Feche o navegador
driver.quit()