import selenium
from selenium.webdriver.common.keys import Keys
navegador = webdriver.Chrome() #abrir navegador

navegador.get('https://www.google.com/')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
flo = (float(cotacao_dolar))
print(f'A cotação do dólar é {flo:.2f}')