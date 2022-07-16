import clases2 as d
import clases3 as e
import pprint
import os
import numpy as np
from zipfile import ZipFile
from secrets import token_bytes
import argparse
import shutil 
from tkinter import *
import os
import tkinter as tk
import shutil

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        placement=3
        for pick in picks:
                var = IntVar()
                chk = Checkbutton(self, text=pick, variable=var,width=12,height=2)
                chk.pack(side=side, anchor=anchor, expand=YES)
                self.vars.append(var)
    def state(self):
                return map((lambda var: var.get()), self.vars)
 

class Comprimir:
    def __init__(self,_directorioProgramaMapa):
   #     print('Nombre Comprimir:') 
        self.nombre = ""
        self.directorioProgramaMapa=_directorioProgramaMapa

    def ejecutar(self,_nombre):
        self.nombre=_nombre
        self.__comprimeZIP()
        self.__crearArchivoZIPConXOR()
        salida=self.directorioProgramaMapa+"pendientes"+'\\'+_nombre+"XOR.tmp"
 
        shutil.copy(".\\temp\\"+_nombre+"XOR.tmp", salida)

    def __comprimeZIP(self):
        filenames = [self.nombre+".sal"]
        with ZipFile(".\\temp\\"+self.nombre+".zip", mode="w") as archive:
            for filename in filenames:
                archive.write(".\\temp\\"+filename)
        
    def __crearArchivoZIPConXOR(self):
 
        file = open(".\\temp\\"+self.nombre+".zip", "rb")
        fileSalida = open(".\\temp\\"+self.nombre+"XOR.tmp", "wb")
 
        key = bytes(token_bytes(1))
        fileSalida.write(key)
        byte=1
        while byte:
            byte = file.read(1)
            encrypted_text = self.__crypt_xor(byte, key)
            fileSalida.write(encrypted_text)
   #         print(byte,encrypted_text)
 
        fileSalida.close()
 
    def __crypt_xor(self,message, key):
        result = bytearray(message)
        for i, k in enumerate(self.__cycle(key, len(message))):
            result[i] ^= k
        return result

    def __cycle(self,s, max):
        n = len(s)
        return (s[i % n] for i in range(max))



class Archivo:
    def __init__(self,_mac):
     #   print('Nombre Archivo:') 
        self.persona        =e.Persona(_mac)
        self.clinicos       =e.Clinicos()
        self.medicotratante =e.Medicotratante()
        self.medicaciones   =e.Medicaciones()
        self.sueno          =e.Sueno()
        self.trabajo        =e.Trabajo()
        self.observaciones  =e.Observaciones()
        self.comidas        =e.Comidas()
        self.datos          =""

class Mapa:
    def __init__(self,_mac,_directorioProgramaMapa,_directorioProgramaMaquina,_datosFormulario,_labelFormulario,_IDActual,_sintomas,_antecedentes,_tamanoVentana,_cliente,_checkformulario):
        self.archivo = Archivo(_mac)
        self.maquina = d.Maquina()
        self.mac=_mac
        self.comprimir = Comprimir(_directorioProgramaMapa)
        self.directorioProgramaMapa=_directorioProgramaMapa
        self.directorioProgramaMaquina=_directorioProgramaMaquina
        self.archivoQueEstoyProcesando=""
        self.datosFormulario=_datosFormulario.split(",")
        self.labelFormulario=_labelFormulario.split(",")
        self.IDActual=_IDActual
        self.sintomas=_sintomas.split(",")
        self.antecedentes=_antecedentes.split(",")
        self.tamanoVentana = _tamanoVentana     
        self.cliente       = _cliente 
        self.checkformulario = _checkformulario.split(",")
        self.formularioOK    = TRUE
       

    def preparaArchivo(self):
        self.comprimir.ejecutar(self.archivoQueEstoyProcesando)

    def ejecutarAplicacionMapa(self):
        print(    self.directorioProgramaMapa+ "sistemed_mapa" )
 #       return_code = subprocess.call([  self.directorioProgramaMapa+"sistemed_mapa.exe", ""])  
        

 

    def llamaFormulario(self):
        fields = self.datosFormulario
        labels  = self.labelFormulario

 
        def fetch(entries,sintomas2,sintomas1,antecedentes,genero):
            sintomasList=list(sintomas1.state()) + list(sintomas2.state())
            antecedentesList=list(antecedentes.state())
            i=0
            sintomasSalida=""
            for s in sintomasList:
                if (s==1):
                    sintomasSalida=sintomasSalida+str(i+1)+","
                i=i+1
            antecedentesSalida=""
            i=0
            for s in antecedentesList:
                if (s==1):
                    antecedentesSalida=antecedentesSalida+str(i+1)+","
                i=i+1
            

            print("******************************************************************")
            self.archivo.persona.nombres        =  "" # entries[3][1].get()
            self.archivo.persona.apellidos      =  "" # entries[3][1].get()
            self.archivo.persona.altura         =  "" # entries[4][1].get()        
            self.archivo.persona.peso           =  "" # entries[13][1].get() 
            self.archivo.persona.cintura        =  "" # entries[5][1].get()       
            self.archivo.persona.rut            =  "" # entries[3][1].get()
            self.archivo.persona.kernel         =  "" # entries[6][1].get() 
            self.archivo.persona.telefono       =  "" # entries[8][1].get()
            self.archivo.persona.fax            =  "" # entries[9][1].get()        
            self.archivo.persona.mail           =  "" # entries[10][1].get()     
            self.archivo.persona.fechaNacimiento  = "" #  entries[11][1].get() 
            
            
            self.archivo.persona.mac            =  self.mac
            self.archivo.persona.id             =  self.IDActual
            self.archivo.persona.tipoId         =  "2"

            self.archivo.comidas.desayuno        =  "00:00" # entries[14][1].get()
            self.archivo.comidas.almuerzo        =  "00:00" # entries[15][1].get()
            self.archivo.comidas.once            =  "00:00" # entries[16][1].get()        
            self.archivo.comidas.cena            =  "00:00" # entries[17][1].get()   

            self.archivo.sueno.seAcosto          =  "00:00" # entries[18][1].get()
            self.archivo.sueno.seDurmio          =  "08:00" # entries[19][1].get()
            self.archivo.sueno.seDesperto        =  "00:00" # entries[20][1].get()
            self.archivo.sueno.seLevanto         =  "08:00" # entries[21][1].get()
            self.archivo.sueno.comoDurmio        =  "." # entries[22][1].get()

            self.archivo.trabajo.TrabajoInicio    =  "00:00" # entries[21][1].get()
            self.archivo.trabajo.TrabajoFin       =  "00:00" # entries[22][1].get()

            self.archivo.observaciones.Observaciones       =  "SIN OBSERVACIONES" # entries[22][1].get()

            self.archivo.medicotratante.medicoTratante    =  "" # entries[21][1].get()
            self.archivo.medicaciones.medicaciones       =  "" # entries[22][1].get()

            self.archivo.clinicos.sintomas              =  sintomasSalida
            self.archivo.clinicos.antecedente           =  antecedentesSalida
            
            self.archivo.persona.sexo           = "" #  entries[11][1].get() 
            self.archivo.persona.cliente        =  self.cliente # entries[7][1].get()

            if (genero == 0):
                self.archivo.persona.sexo           = "Masculino" #  entries[11][1].get() 
            

            j=0
            for entry in entries:
                field = entry[0]
                text  = entry[1].get()
                print('%s: "%s"' % (field, text)) 
                if (field=="Nombres"):
                    self.archivo.persona.nombres=text
                if (field=="Apellidos"):
                    self.archivo.persona.apellidos=text
                if (field=="Altura"):
                    self.archivo.persona.altura=text
                if (field=="Peso"):
                    self.archivo.persona.peso=text
                if (field=="Cintura"):
                    self.archivo.persona.cintura=text
                if (field=="Rut"):
                    self.archivo.persona.rut=text
                if (field=="Kernel"):
                    self.archivo.persona.kernel=text
                if (field=="Cliente"):
                    self.archivo.persona.cliente=text
                if (field=="Telefono"):
                    self.archivo.persona.telefono=text
                if (field=="Fax"):
                    self.archivo.persona.fax=text
                if (field=="Mail"):
                    self.archivo.persona.mail=text
                if (field=="FechaNacimiento"):
                    self.archivo.persona.fechaNacimiento=text
                if (field=="ID"):
                    self.archivo.persona.id=self.IDActual

                if (field=="Desayuno"):
                    self.archivo.comidas.desayuno=text
                if (field=="Almuerzo"):
                    self.archivo.comidas.almuerzo=text
                if (field=="Once"):
                    self.archivo.comidas.once=text
                if (field=="Cena"):
                    self.archivo.comidas.cena=text

                if (field=="seAcosto"):
                    self.archivo.sueno.seAcosto=text
                if (field=="seDurmio"):
                    self.archivo.sueno.seDurmio=text
                if (field=="seDesperto"):
                    self.archivo.sueno.seDesperto=text
                if (field=="seLevanto"):
                    self.archivo.sueno.seLevanto=text
                if (field=="comoDurmio"):
                    self.archivo.sueno.comoDurmio=text

                if (field=="TrabajoInicio"):
                    self.archivo.trabajo.TrabajoInicio   =text
                if (field=="TrabajoFin"):
                    self.archivo.trabajo.TrabajoFin      = text
                if (field=="Observaciones"):
                    self.archivo.observaciones.Observaciones      = text
 
                if (field=="MedicoTratante"):
                    self.archivo.medicotratante.medicoTratante      = text
                if (field=="Medicaciones"):
                    self.archivo.medicaciones.medicaciones      = text
                j=j+1
           

        def makeform(root, fields,labels):
            entries = []
            i=0;
            for field in fields:
                row = tk.Frame(root)
                if (field=="t1"):

                    label2 = Label(root,text=labels[i])
                    label2.place(x=20, y=20)
                    label2.pack(side=TOP,  fill=X)

                else:
                    lab = tk.Label(row, width=15, text=labels[i], anchor='nw',padx=20)
                    lab1 = tk.Label(row, width=4, text=" ", anchor="center")
                    ent = tk.Entry(row)
                    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                    lab.pack(side=tk.LEFT)
                    lab1.pack(side=tk.LEFT)
                    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
                    entries.append((field, ent))
                i=i+1
            return entries



        root = Tk()
        root.title("INGRESO DEL PACIENTE   Nº ["+self.IDActual+"]")
         
 

        root.geometry(self.tamanoVentana)
        ents = makeform(root, fields,labels)
      
  
        largo=int(len(self.sintomas)/2)
      
        label1 = Label(root,text="SINTOMAS")
        label1.place(x=20, y=20)
        label1.pack(side=TOP,  fill=X)
        
        sintomas = Checkbar(root, self.sintomas[largo:])
        sintomas.pack(side=TOP,  fill=X)
        sintomas.config(relief=GROOVE, bd=2)

        sintomas1 = Checkbar(root, self.sintomas[:largo])
        sintomas1.pack(side=TOP,  fill=X)
        sintomas1.config(relief=GROOVE, bd=2)

        label2 = Label(root,text="ANTECEDENTES")
        label2.place(x=20, y=20)
        label2.pack(side=TOP,  fill=X)

        antecedentes = Checkbar(root, self.antecedentes)
        antecedentes.pack(side=TOP,  fill=X)
        antecedentes.config(relief=GROOVE, bd=2)

        radioGrupo=LabelFrame(root,text="Selecciones Genero")
        radioGrupo.pack()
        genero=IntVar()
        masculino=Radiobutton(radioGrupo,text="Masculino",variable=genero,value=0)
        masculino.pack(anchor=W)
        femenino=Radiobutton(radioGrupo,text="Femenino",variable=genero,value=1)
        femenino.pack(anchor=W)

        root.bind('<Return>', (lambda event, e=ents: fetch(e,sintomas,sintomas1,antecedentes,genero)))   
        b1 = tk.Button(root, text='<< Procesar >>',command=(lambda e=ents: fetch(e,sintomas,sintomas1,antecedentes,genero.get())))
        b1.pack(side=tk.BOTTOM, padx=5, pady=5)

        
        self.formularioOK =True
        while (self.formularioOK ==True ):
            
            root.mainloop()
            self.CrearInformacionDelArchivo()

            if (len(self.archivo.persona.apellidos)) > 0 :
                self.formularioOK =False




        print("·····································································")
              

    def ColocarDatosSegunFormatoMAPA(self):
 
        self.llamaFormulario(  )

        self.archivo.persona.mac    =  self.mac
        self.archivo.datos          =  self.maquina.printDatosLeidosDeLaMaquina()   

    def CrearInformacionDelArchivo(self):
        archivoTexto=open(".\\temp\\"+self.archivoQueEstoyProcesando+".sal","w") 
        archivoTexto.write(self.archivo.persona.print())
        archivoTexto.write(self.archivo.clinicos.print())
        archivoTexto.write(self.archivo.medicotratante.print())
        archivoTexto.write(self.archivo.medicaciones.print())
        archivoTexto.write(self.archivo.sueno.print())
        archivoTexto.write(self.archivo.comidas.print())
        archivoTexto.write(self.archivo.trabajo.print())
        archivoTexto.write(self.archivo.observaciones.print())
        archivoTexto.write(self.archivo.datos)
        archivoTexto.close()

    def ingresaDatosDelPaciente(self):
        self.maquina.patientData.getRut()
        self.maquina.patientData.getNombre()
    
    def moverArchivoProcesado(self):
        source = self.directorioProgramaMaquina+self.archivoQueEstoyProcesando +".awp"
        destination = ".\\work\\"+self.archivoQueEstoyProcesando+".awp"
        print(source)
        print(destination)
        shutil.move(source,destination)

    def hayArchivosNuevos(self):
        directorio =   self.directorioProgramaMaquina
        contenido = os.listdir(directorio)
        archivos = []
        hay=False
        for fichero in contenido:
            if os.path.isfile(os.path.join(directorio, fichero)) and fichero.endswith('.awp'):
                archivos.append(fichero)
                hay=True
                nombre = archivos[0].split(".")
                self.archivoQueEstoyProcesando=nombre[0]
        return(hay)



    def leeDatosDeLaMaquina(self):
        fichero = open(self.directorioProgramaMaquina+self.archivoQueEstoyProcesando+".awp")
        lineasArchivos = []
 
        lineas = fichero.readlines()
        for linea in lineas:
            lineasArchivos.append(linea)
        for a in lineasArchivos:
            self.maquina.agregarExtraInfo(a)
            self.maquina.agregarPatientData(a)
            self.maquina.agregarAbpmdata(a)
            self.maquina.agregarDatosDeLaMaquina(a)
            self.maquina.agregarComentarioDeLaMaquina(a)
    
