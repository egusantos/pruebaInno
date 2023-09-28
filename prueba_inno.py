import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import re

class use_unittest(unittest.TestCase):
    #Crear una instancia del navegador
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
    #Definir una función para esperar a que un elemento sea visible
    def wait_element(self,by, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((by, locator)))

    # Caso de prueba 1
    def test_case_1(self):
        driver=self.driver
        driver.get("https://www.innocv.com/")
        time.sleep(5)
        self.assertIn("INNOCV SOLUTIONS",driver.title)
        cookies = self.wait_element(By.XPATH,"//*[@id='rcc-confirm-button']")
        cookies.click()
        #Pulsar pestaña "Contacto"
        contacto = self.wait_element(By.XPATH, "//*[@id='root']/div/div[1]/header/div/div/div/div/div/nav/div/a[7]")
        contacto.click()
        #Guardar el número de teléfono
        telefono = self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/div/div/div/div/p[2]/span/span[2]")
        numero = str(telefono.text).replace("(+34)","")
        #Ir a "Aviso legal"
        """aviso_legal = self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div/div/div[2]/div[2]/nav/ul/div[3]/a/li")
        aviso_legal.click()"""
        driver.get("https://www.innocv.com/aviso-legal")
        #Comprobar que el teléfono es el mismo (obviando el +34)
        telefono_aviso = self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div/p[3]/span/span").text
        #numero_aviso = telefono_aviso.text.split()[-1]
        assert numero in telefono_aviso, "El número de teléfono no coincide"
        print("Caso de prueba 1: OK")
        
    # Caso de prueba 2
    def test_case_2(self):
        # Abrir URL https://www.innocv.com/
        driver=self.driver
        driver.get("https://www.innocv.com/")
        time.sleep(5)
        self.assertIn("INNOCV SOLUTIONS",driver.title)
        cookies = self.wait_element(By.XPATH,"//*[@id='rcc-confirm-button']")
        cookies.click()
        #Pulsar pestaña "Contacto"
        contacto = self.wait_element(By.XPATH, "//*[@id='root']/div/div[1]/header/div/div/div/div/div/nav/div/a[7]")
        contacto.click()
        # Contar cuantas veces aparece Faraday
        #dir=self.wait_element(By.XPATH, "//*[@id='maps']/div/ul/li[1]/div/p")
        #ubicacion=self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/p")
        footer=self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div/div/div[1]/div[2]/div[2]/div/div/p[5]")
        #mapa=self.wait_element(By.XPATH, "//*[@id='mapDiv']/div/div/div[4]/div/div/div/div/div[1]/div[2]")
        html_source = self.driver.page_source
        regex='Faraday'
        counter = len(re.findall(regex,html_source))
        print(f"Caso de prueba 2: Faraday aparece {counter} veces")
        assert counter==4, "La palabra Faraday no aparece las veces esperadas (4)"
    
    # Caso de prueba 3
    def test_case_3(self):
        # Abrir URL https://www.innocv.com/
        driver=self.driver
        driver.get("https://www.innocv.com/")
        time.sleep(5)
        self.assertIn("INNOCV SOLUTIONS",driver.title)
        cookies = self.wait_element(By.XPATH,"//*[@id='rcc-confirm-button']")
        cookies.click()
        #Pulsar pestaña "Contacto"
        contacto = self.wait_element(By.XPATH, "//*[@id='root']/div/div[1]/header/div/div/div/div/div/nav/div/a[7]")
        contacto.click()
        # Pulsar en "Enviar formulario"
        enviar = self.wait_element(By.XPATH, "//*[@id='maps']/div/div/form/button/span[1]") #//*[@id='maps']/div/div/form/button
        driver.execute_script("document.getElementsByClassName('MuiButton-label')[0].click()",enviar)
        # Comprobar que aparece el texto "Campo requerido" en rojo
        campos_requeridos = driver.find_elements(By.XPATH, "//p[text()='Campo requerido']")
        assert campos_requeridos,"No hay campos requeridos"
        for campo in campos_requeridos:
            color = campo.value_of_css_property("color")
            assert color == "rgba(244, 67, 54, 1)", "El texto no es rojo"
        print("Caso de prueba 3: OK")
    
    # Caso de prueba 4
    def test_case_4(self):
        # Abrir URL https://www.innocv.com/
        driver=self.driver
        driver.get("https://www.innocv.com/")
        time.sleep(5)
        self.assertIn("INNOCV SOLUTIONS",driver.title)
        cookies = self.wait_element(By.XPATH,"//*[@id='rcc-confirm-button']")
        cookies.click()
        #Pulsar pestaña "Contacto"
        contacto = self.wait_element(By.XPATH, "//*[@id='root']/div/div[1]/header/div/div/div/div/div/nav/div/a[7]")
        contacto.click()
        # Hacer scroll a la sección de "Noticias"
        noticias = self.wait_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[2]/div[1]/p[2]")
        noticias_visibles=self.wait_element(By.XPATH, f"//*[@id='root']/div/div/div[2]/div[2]/div[2]/article/section[1]/div[2]/div[1]/p[2]")
        driver.execute_script("arguments[0].scrollIntoView();", noticias)
        # Leer las fechas de todas las noticias
        my_dates=[]
        my_index=[i+1 for i in range(3)]
        for i in my_index:
            news_info=self.wait_element(By.XPATH, f"//*[@id='root']/div/div/div[2]/div[2]/div[2]/article/section[{i}]/div[2]/div[1]/p[2]").text
            my_dates.append(news_info)
        print(my_dates)
        #fechas = driver.find_elements(By.XPATH, "//div[@class='date']")
        # Comprobar que se corresponden con el mes actual o hasta dos meses antes
        today = datetime.date.today()
        print(today)
        limit = today - datetime.timedelta(days=60)
        for date in my_dates:
            day, month, year = date.split("-")
            news_date = datetime.date(int(year), int(month), int(day))
            assert news_date >= limit, f"Hay alguna noticia anterior a 2 meses"
            print(f"Caso de prueba 4: La noticia del {date} está dentro del rango")
            
    # Cerrar driver    
    def tearDown(self):
        self.driver.close()
        
if __name__=='__main__':
    unittest.main()        