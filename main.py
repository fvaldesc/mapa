import pprint
import os
import numpy as np
from zipfile import ZipFile
from secrets import token_bytes
import argparse
 
import clases  as c

import subprocess



import configparser
configuracion = configparser.ConfigParser()
 
archivoBase=" "
numeroMAK  =" "
archivoMapaMaquina=" "
directorio_Programa_Mapa=" "
directorio_Programa_Maquina=" "
datosFormulario=""
test="true"
checkformulario="" 
 
configuracion.read('main.cfg')
general = configuracion['General']
directorioProgramaMapa= general['directorio_Programa_Mapa']
directorioProgramaMaquina= general['directorio_Programa_Maquina']
numeroMAK=general['numeroMAK']
archivoMapaMaquina=general['archivoEjemplo']
datosFormulario=general['datosFormulario']
labelFormulario=general['labelFormulario']
IDactual=general['IDActual']
test=general['test']
sintomas=general['sintomas']
antecedentes=general['antecedentes']
tamanoVentana=general['tamanoVentana']
cliente=general['cliente']
checkformulario==general['checkformulario']



print("******************************************************************")
print (IDactual)
print(directorioProgramaMapa)
print(directorioProgramaMaquina)
print("******************************************************************")
mapa=c.Mapa(numeroMAK,directorioProgramaMapa,directorioProgramaMaquina,datosFormulario,labelFormulario,IDactual,sintomas,antecedentes,tamanoVentana,cliente,checkformulario)


if mapa.hayArchivosNuevos():
        mapa.leeDatosDeLaMaquina()
        mapa.ingresaDatosDelPaciente()
        mapa.ColocarDatosSegunFormatoMAPA()
        mapa.CrearInformacionDelArchivo() 
        mapa.preparaArchivo()
        if (test!="true"):
                mapa.moverArchivoProcesado()
        print("******************************************************************")
        mapa.ejecutarAplicacionMapa()
        print("******************************************************************")
        # save to a file
        config = configparser.ConfigParser()
        config.read('main.cfg')
        IDactual = str(int(IDactual)+1)
        config.set('General', 'IDActual', IDactual)
        with open('main.cfg', 'w') as configfile:
             config.write(configfile)

else:
        print("No hay archivo para el proceso")

