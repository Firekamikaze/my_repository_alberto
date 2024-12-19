from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
import time 
import sys  

##################################################______________________________
nombre = input("Ingresa tu Nombre: ") 
apellido = input("Ingresa tu Apellido: ")
email = input("Ingresa tu Email: ")
rut = input("Ingresa tu Rut: ")
numero_telefono = input("Ingresa tu numero de Telefono: ")
####################################################_____________________________

try:  
    eleccion = int(input("Selecciona cargo Directivo (1) o Asistente (2): "))  # Asegúrate de que se ingresa un número entero  
except ValueError:  
    print("No has ingresado un número válido.")  
    sys.exit()  # Cierra el programa si la entrada no es válida  

# Verificar si x es diferente de 1 y 2  
if eleccion != 1 and eleccion != 2:  
    print("el numero seleccionado no es 1 ni 2. El programa se cerrará.")  
    sys.exit()  # Cierra el programa 

#####################################################_________________________________________________


########parte navegador

driver=webdriver.Chrome()
driver.get("https://app.horaciolabs.com/web-administracion/") 
driver.set_window_size(948, 824) 

#____________________________________________________________________________________________#inicio de sesion 

usuario= driver.find_element(By.ID,("registerEmail"))
clave=  driver.find_element(By.ID,("registerPassword"))
boton=  driver.find_element(By.XPATH,("//div[@id='mainContent']/div/div/form/ui5-button"))
usuario.send_keys("directive@gmail.com")
clave.send_keys("directive1234")
boton.click()
#____________________________________________________________________________________________#

time.sleep(2)#espera dos segundos que cargue la pagina
#____________________________________________________________________________________________# se ubica el elemento usuaros de directiva
side_nav_item= driver.find_element(By.CSS_SELECTOR, "ui5-side-navigation-item:nth-child(12)")
driver.execute_script("arguments[0].scrollIntoView(true);", side_nav_item) #scroll en la barra lateral para evitar errores 
side_nav_item.click()
time.sleep(2)
crear_button = driver.find_element(By.CSS_SELECTOR, ".mb-2 > ui5-button") 
crear_button.click()
#____________________________________________________________________________________________#
time.sleep(2)
#____________________________________________________________________________________________# formulario@@@@@
F_nombre = driver.find_element(By.ID, "firstName") 
F_apellido = driver.find_element(By.ID, "lastName") 
F_email = driver.find_element(By.ID, "email")
F_rut = driver.find_element(By.ID, "document")
F_numero_telefono = driver.find_element(By.NAME, "phone")
F_cargo = driver.find_element(By.ID, "role")
F_cargo_Directivo = driver.find_element(By.CSS_SELECTOR, "ui5-option:nth-child(2)")
F_cargo_Asistente = driver.find_element(By.CSS_SELECTOR, "ui5-option:nth-child(3)")
F_guardar = driver.find_element(By.CSS_SELECTOR, ".justify-end > ui5-button")

F_nombre.send_keys(nombre) 
F_apellido.send_keys(apellido) 
F_email.send_keys(email) 
F_rut.send_keys(rut) 
F_numero_telefono.send_keys(numero_telefono)
F_cargo.click()
time.sleep(1)
if eleccion == 1:  
    F_cargo_Directivo.click()  
elif eleccion == 2:  
    F_cargo_Asistente.click()  
time.sleep(1)
F_guardar.click()
#____________________________________________________________________________________________#@@@@

time.sleep(1000)

driver.close()