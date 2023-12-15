import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import re
import mysql.connector
from selenium import webdriver
import os

def compra_agil():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")  # Maximizar la ventana
    chrome_options.add_argument("--window-size=1920,1080") 
    chrome_options.add_experimental_option("prefs", {
        # Ruta de la carpeta de descarga
        "download.default_directory": "/Users/grupofirma/Desktop/Bot-compra-agil/Archivos",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })

    options = webdriver.ChromeOptions()


    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://www.mercadopublico.cl'
    driver.get(url)

    sleep(3)

    elemento = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="encabezado"]/nav/div[2]/div[1]/div/button'))
    )
    elemento.click()
    sleep(1)

    print('clave unica')
    clave_unica = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="zocial-oidc"]'))
    )
    clave_unica.click()
    sleep(1)

    input1=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,'uname')))

    input1.send_keys("181747919")
    sleep(1)

    input2=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,'pword')))
    input2.send_keys("Seba@2022")
    sleep(1)

    WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="login-submit"]')))
    sleep(1)

    click_login =WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,'login-submit')))
    click_login.click()
    sleep(2)

    modal = "#rdbOrg1556732"
    elemento2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, modal)))

    solanch=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rdbOrg1556732"]')))
    solanch.click()

    ingresar=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="myModal"]/div/div/div[3]/a')))
    ingresar.click()
    sleep(2)

    # Modulo Compra Agil
    compra_agil=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mnuPrincipaln6"]/table/tbody/tr/td/a')))
    compra_agil.click()
    sleep(2)
    print('entro a compra agil')

    wait = WebDriverWait(driver, 3)

    driver.switch_to.frame(wait.until(EC.visibility_of_element_located((By.ID,"fraDetalle"))))
    print('paso el ifram')
    check_box=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="panel2a-content"]/div/label[2]/span[1]/span/input')))
    check_box.click()
    sleep(2)
    print('ahcer click en el checbox')
    #Analizar la cantidad de filas existentes
    filas = driver.find_elements(By.CLASS_NAME, 'Cardstyles__Content-sc-ssikjk-2.larVNz')
    cantidad_elementos = len(filas)
    print("Cantidad de elementos con la clase especificada:", cantidad_elementos)
    sleep(2)

    contadorPagina=1
    contador = 1
    data = []

    totalBotonPagina = '(//*[@id="__root"]/div/main/div[2]/div[3]/div[3]/div/div/nav/ul/li/button)[last()-1]'

    try:
        try:
            pagina_nav=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,totalBotonPagina)))
            numeroPagina=int(pagina_nav.text)
            print('Total de paginas',numeroPagina)
            
        except:
            sleep(3)
            #Recorre Pagination

        for z in range(1,numeroPagina +1):
            
            if z == 1 :
                print('el Z es',z)
            else:
                paginaSiguiente = '(//*[@id="__root"]/div/main/div[2]/div[3]/div[3]/div/div/nav/ul/li/button)[last()]'
                identificador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,paginaSiguiente)))
                identificador.click()
            
            
            #Recorre las filas
            for i in range(1, cantidad_elementos +1):
                texto_archivos=''
                
                participar_contenido=f'//*[@id="__root"]/div/main/div[2]/div[3]/div[2]/div/div[{contador}]/div/div/div[2]/div[4]/a'

                participar=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,participar_contenido)))
                participar.click()
                sleep(2)
                
                try:
                    WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//body"))
                )
                    print("El body de la página se ha cargado completamente.")

                    
                except Exception as e:
                    print(f"Error al esperar la carga del body de la página: {e}")

                finally:
                

                    #Identificar datos Detalle de cotizacion
                    identificador = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__root"]/div/main/div[1]/div[2]/div/h2'))) #id
                    textoIdentificador = identificador.text
                    numero_cotizacion = re.search(r'\b(\d+-\d+-COT\d+)\b', textoIdentificador).group(1) if re.search(r'\b(\d+-\d+-COT\d+)\b', textoIdentificador) else None
                    print("Número de cotización:", numero_cotizacion) #numero
                    

                    nombre=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[1]/div[2]/p')))
                    textoNombre = nombre.text
                    print('Nombre de cotizacion:', textoNombre)


                    descripcion=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[2]/div[2]/p')))
                    textoDescripcion = descripcion.text
                    print('Descripcion:', textoDescripcion)


                    direccionEntrega=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[3]/div[2]/p')))
                    textoDireccion = direccionEntrega.text
                    print('Direccion de Entrega:', textoDireccion)
                    

                    plazoEntrega=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[4]/div[2]/p')))
                    textoPlazo = plazoEntrega.text
                    print('Plazo de Entrega:', textoPlazo)


                    presupuesto=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[5]/div[2]/p')))
                    textoPresupuesto = presupuesto.text
                    print('Presupuesto:', textoPresupuesto)


                    fechaPublicacion=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[6]/div[2]/p')))
                    textoFechaPublicacion = fechaPublicacion.text
                    print('Fecha de Publicacion:', textoFechaPublicacion)


                    fechaCierre=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[7]/div[2]/p')))
                    textoFechaCierre = fechaCierre.text
                    print('Fecha de Cierre:', textoFechaCierre)
                    #sleep(3)
                    try:
                        ruta= '/Users/grupofirma/Downloads'
                        destino= '/Users/grupofirma/Desktop/scrap con python/Archivos'
                        

                    #Descargas
                        archivo1=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[10]/div[2]/div/div[1]')))
                        enlaces_pdf1 = archivo1.find_elements(By.TAG_NAME, "a")
                        
                        if enlaces_pdf1:
                                for enlace_pdf in enlaces_pdf1:
                                    print('entro al enlace 1')
                                    archivo1_texto= "'"+enlace_pdf.text+"'"+","
                                    print(archivo1_texto)
                                    texto_archivos += archivo1_texto + '\n'
                                    enlace_pdf.click()
                                    sleep(2)
                                

                        else:
                            print("No hay archivos adjuntos en la página.")
                    except:
                        print('no hay archivos')
                        
                    try:
                        archivo2=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[10]/div[2]/div/div[2]')))
                        enlaces_pdf2 = archivo2.find_elements(By.TAG_NAME, "a")
                        
                        if enlaces_pdf2:
                                for enlace_pdf2 in enlaces_pdf2:
                                    print('entro al enlace 2')
                                    archivo2_texto= "'"+enlace_pdf2.text+"'" + ","
                                    print(archivo2_texto)
                                    texto_archivos += archivo2_texto + '\n'
                                    enlace_pdf2.click()
                        else:
                            print("No hay enlace 2")
                    except:
                        print('no hay archivo 2')
                        
                        
                    try:
                        archivo3=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[10]/div[2]/div/div[3]')))
                        enlaces_pdf3 = archivo3.find_elements(By.TAG_NAME, "a")
                        print('no hay archivos que descargar ')
                        
                        if enlaces_pdf3:
                                for enlace_pdf3 in enlaces_pdf3:
                                    print('entro al enlace 3')
                                    archivo3_texto= "'"+enlace_pdf3.text+"'"+","
                                    print(archivo3_texto)
                                    texto_archivos += archivo3_texto +'\n'
                                    enlace_pdf3.click()
                                    

                        else:
                            print("No hay enlace 3")
                    except:
                        print('no hay archivo 3')
                        
                        
                    try:
                        archivo4=WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[1]/div[5]/div[1]/div[10]/div[2]/div/div[4]')))
                        enlaces_pdf4 = archivo4.find_elements(By.TAG_NAME, "a")
                        print('no hay archivos que descargar ')
                        
                        if enlaces_pdf4:
                                for enlace_pdf4 in enlaces_pdf4:
                                    print('entro al enlace 4')
                                    archivo4_texto= "'"+enlace_pdf4.text+"'"+","
                                    print(archivo4_texto)
                                    texto_archivos += archivo4_texto + '\n'
                                    enlace_pdf4.click()
                        else:
                            print("No hay enlace 4")
                    except:
                        print('no hay archivo 4')

                    print('Archivos',texto_archivos)
                    
                    #Conexion con la base de datos
                    configuracion ={
                        'host':'localhost',
                        'user':'root',
                        'database':'compra_agil'
                    }

                    try:
                        conexion = mysql.connector.connect(**configuracion)
                        print("Conectado a la base de datos ","("+str(conexion.connection_id)+")")
                        sql= "compraAgil_insertarDatosNest"
                        cursor = conexion.cursor()
                        
                        NumeroCotizacion= numero_cotizacion
                        Nombre = textoNombre
                        Descripcion= textoDescripcion
                        Direccion= textoDireccion
                        PlazoEntrega= textoPlazo
                        Presupuesto= textoPresupuesto
                        Fecha=textoFechaPublicacion
                        FechaCierre= textoFechaCierre
                        Archivos= texto_archivos
                        
                        consulta = """
                            INSERT INTO datos_agil (NumeroCotizacion, Nombre, Descripcion, Direccion, PlazoEntrega, Presupuesto, Fecha, FechaCierre, Archivos)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        
                        cursor.callproc("compraAgil_insertarDatosNest", (NumeroCotizacion, Nombre, Descripcion, Direccion, PlazoEntrega, Presupuesto, Fecha, FechaCierre, Archivos))

                        conexion.commit()
                        
                    except mysql.connector.Error as e:
                        
                        print("Error en la conexión a la base de datos:",e)

                    finally:
                        if 'conexion' in locals() and conexion.is_connected():
                            cursor.close()

                            conexion.close()
                            print("Conexión cerrada.")

                            volver=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__root"]/div/main/div[2]/div[5]/div[1]/div[8]/div[1]/button')))
                            volver.click()
                            sleep(2)

                            contador+=1
                            print('CONTADOR',contador)
                            print('termino de',textoNombre)

                            if i == 20:
                                    contador=1
                            else:
                                print('Se Mantiene')

                            def eliminar_archivos_duplicados(ruta_especifica):
                                print('aqi entra la funcion')
                                # Obtener la lista de archivos en la ruta específica
                                archivos = os.listdir(ruta_especifica)

                                # Crear un diccionario para almacenar los archivos por tamaño
                                archivos_por_tamano = {}

                                for archivo in archivos:
                                    # Obtener la ruta completa del archivo
                                    ruta_completa = os.path.join(ruta_especifica, archivo)

                                    # Obtener el tamaño del archivo
                                    tamano = os.path.getsize(ruta_completa)

                                    # Agregar la ruta al diccionario
                                    if tamano not in archivos_por_tamano:
                                        archivos_por_tamano[tamano] = [ruta_completa]
                                    else:
                                        archivos_por_tamano[tamano].append(ruta_completa)

                                # Iterar sobre el diccionario y eliminar archivos duplicados
                                for rutas in archivos_por_tamano.values():
                                    if len(rutas) > 1:
                                        print(f"Archivos duplicados para tamaño {os.path.getsize(rutas[0])} bytes:")
                                        for ruta in rutas[1:]:
                                            print(f"  {ruta}")
                                            os.remove(ruta)
                                            print(f"Eliminando {ruta}")

                                print("Información extraida")

                            # Ruta específica donde se descargan los archivos
                            ruta_especifica = "/Users/grupofirma/Desktop/Bot-compra-agil/Archivos"

                            # Llamar a la función para eliminar archivos duplicados
                            eliminar_archivos_duplicados(ruta_especifica)
    except:


        print('finaliza el proceso')
        driver.quit() #fin de proceso
while True:
    compra_agil()
    time.sleep(3 * 60 * 60)