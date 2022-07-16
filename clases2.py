class PatientData:
    def __init__(self):
        self.aBPMCount=""
        self.name=""
        self.id=""
        self.yearBegin=""
        self.monBegin=""
        self.dayBegin=""
        self.hourBegin=""
        self.minBegin=""
        self.secBegin=""
        self.maxPressValue=""
        self.awakeWarnOnOff=""
        self.awakeSysMaxValue=""
        self.awakeSysMinValue=""
        self.awakeDiaMaxValue=""
        self.awakeDiaMinValue=""
        self.asleepWarnOnOff=""
        self.asleepSysMaxValue=""
        self.asleepSysMinValue=""
        self.asleepDiaMaxValue=""
        self.asleepDiaMinValue=""
        self.display=""
        self.startKey=""
        self.awakeHour=""
        self.awakeMin=""
        self.awakeDuration=""
        self.asleepHour=""
        self.asleepMin=""
        self.asleepDuration=""
        self.apecialHourStart=""
        self.specialMinStart=""
        self.specialDuration=""
        self.specialHourEnd=""
        self.specialMinEnd=""
        self.addr=""
        self.gender=""
        self.birthday=""
        self.race=""
        self.height=""
        self.weight=""
        self.age=""
        self.phone=""
        self.medications=""
        self.referringPhys=""
        self.interprettingPhys=""
        self.comments=""
        self.clinicalInterp=""
        self.outpatientNo=""
        self.admissionNo=""
        self.bedNo=""
        self.departmentNo=""
        self.email=""


    def  getRut(self):
                return self.id
    def  getNombre(self):
                return self.name
    def  setABPMCount(self,_aBPMCount):
                self.aBPMCount=_aBPMCount
    def  setName(self,_name):
                self.name=_name
    def  setEnumDeviceType(self,_enumDeviceType):
                self.enumDeviceType=_enumDeviceType
    def  setId(self,_id):
                self.id=_id
    def  setYearBegin(self,_yearBegin):
                self.yearBegin=_yearBegin
    def  setMonBegin(self,_monBegin):
                self.monBegin=_monBegin

    def  setDayBegin(self,_dayBegin):
                self.dayBegin=_dayBegin
    def  setHourBegin(self,_hourBegin):
                self.hourBegin=_hourBegin
    def  setMinBegin(self,_minBegin):
                self.minBegin=_minBegin
    def  setSecBegin(self,_secBegin):
                self.secBegin=_secBegin
    def  setMaxPressValue(self,_maxPressValue):
                self.maxPressValue=_maxPressValue
    def  setAwakeWarnOnOff(self,_awakeWarnOnOff):
                self.awakeWarnOnOff=_awakeWarnOnOff
    def  setAwakeSysMaxValue(self,_awakeSysMaxValue):
                self.awakeSysMaxValue=_awakeSysMaxValue

    def  setAwakeSysMinValue(self,_awakeSysMinValue):
                self.awakeSysMinValue=_awakeSysMinValue
    def  setAwakeDiaMaxValue(self,_awakeDiaMaxValue):
                self.awakeDiaMaxValue=_awakeDiaMaxValue
    def  setAwakeDiaMinValue(self,_awakeDiaMinValue):
                self.awakeDiaMinValue=_awakeDiaMinValue
    def  setAsleepWarnOnOff(self,_asleepWarnOnOff):
                self.asleepWarnOnOff=_asleepWarnOnOff
    def  setAsleepSysMaxValue(self,_asleepSysMaxValue):
                self.asleepSysMaxValue=_asleepSysMaxValue
    def  setAsleepSysMinValue(self,_asleepSysMinValue):
                self.asleepSysMinValue=_asleepSysMinValue
    def  setAsleepDiaMaxValue(self,_asleepDiaMaxValue):
                self.asleepDiaMaxValue=_asleepDiaMaxValue


    def  setAsleepDiaMinValue(self,_asleepDiaMinValue):
                self.asleepDiaMinValue=_asleepDiaMinValue
    def  setDisplay(self,_display):
                self.display=_display
    def  setStartKey(self,_startKey):
                self.startKey=_startKey
    def  setAwakeHour(self,_awakeHour):
                self.awakeHour=_awakeHour
    def  setAwakeMin(self,_awakeMin):
                self.awakeMin=_awakeMin
    def  setAwakeDuration(self,_awakeDuration):
                self.awakeDuration=_awakeDuration
    def  setAsleepHour(self,_asleepHour):
                self.asleepHour=_asleepHour

    def  setAsleepMin(self,_asleepMin):
                self.asleepMin=_asleepMin
    def  setAsleepDuration(self,_asleepDuration):
                self.asleepDuration=_asleepDuration
    def  setSpecialHourStart(self,_specialHourStart):
                self.specialHourStart=_specialHourStart
    def  setSpecialMinStart(self,_specialMinStart):
                self.specialMinStart=_specialMinStart
    def  setSpecialDuration(self,_specialDuration):
                self.specialDuration=_specialDuration
    def  setSpecialHourEnd(self,_specialHourEnd):
                self.specialHourEnd=_specialHourEnd
    def  setSpecialMinEnd(self,_specialMinEnd):
                self.specialMinEnd=_specialMinEnd
    def  setAddr(self,_addr):
                self.addr=_addr
    def  setGender(self,_gender):
                self.gender=_gender

    def  setBirthday(self,_birthday):
                self.birthday=_birthday
    def  setRace(self,_race):
                self.race=_race
    def  setHeight(self,_height):
                self.height=_height
    def  setWeight(self,_weight):
                self.weight=_weight
    def  setAge(self,_age):
                self.age=_age
    def  setPhone(self,_phone):
                self.phone=_phone
    def  setMedications(self,_medications):
                self.medications=_medications
    def  setReferringPhys(self,_referringPhys):
                self.referringPhys=_referringPhys
    def  setInterprettingPhys(self,_interprettingPhys):
                self.interprettingPhys=_interprettingPhys
    def  setComments(self,_comments):
                self.comments=_comments
    def  setClinicalInterp(self,_clinicalInterp):
                self.clinicalInterp=_clinicalInterp
    def  setOutpatientNo(self,_outpatientNo):
                self.outpatientNo=_outpatientNo
    def  setAdmissionNo(self,_admissionNo):
                self.admissionNo=_admissionNo
    def  setBedNo(self,_bedNo):
                self.bedNo=_bedNo
    def  setDepartmentNo(self,_departmentNo):
                self.departmentNo=_departmentNo
    def  setEmail(self,_email):
                self.email=_email


    def print(self):
            print (self.patientData.aBPMCount)
            print (self.patientData.name)
            print (self.patientData.id)
            print (self.patientData.yearBegin)
            print (self.patientData.monBegin)
            print (self.patientData.dayBegin)
            print (self.patientData.hourBegin)
            print (self.patientData.minBegin)

            print (self.patientData.secBegin)
            print (self.patientData.maxPressValue)
            print (self.patientData.awakeWarnOnOff)
            print (self.patientData.awakeSysMaxValue)
            print (self.patientData.awakeSysMinValue)

            print (self.patientData.awakeDiaMaxValue)
            print (self.patientData.awakeDiaMinValue)
            print (self.patientData.asleepWarnOnOff)
            print (self.patientData.asleepSysMaxValue)
            print (self.patientData.asleepSysMinValue)

            print (self.patientData.asleepDiaMaxValue)
            print (self.patientData.asleepDiaMinValue)
            print (self.patientData.startKey)
            print (self.patientData.awakeHour)
            print (self.patientData.awakeMin)
            print (self.patientData.awakeDuration)
            print (self.patientData.asleepHour)
            print (self.patientData.asleepMin)
            print (self.patientData.asleepDuration)
            print (self.patientData.specialHourStart)
            print (self.patientData.specialMinStart)
            print (self.patientData.specialDuration)
            print (self.patientData.specialHourEnd)
            print (self.patientData.specialMinEnd)
            print (self.patientData.addr)
            print (self.patientData.gender)
            print (self.patientData.birthday)
            print (self.patientData.race)
            print (self.patientData.height)
            print (self.patientData.weight)
            print (self.patientData.age)
            print (self.patientData.phone)
            print (self.patientData.medications)
            print (self.patientData.referringPhys)
            print (self.patientData.interprettingPhys)
            print (self.patientData.comments)
            print (self.patientData.clinicalInterp)
            print (self.patientData.outpatientNo)
            print (self.patientData.admissionNo)
            print (self.patientData.bedNo)
            print (self.patientData.departmentNo)
            print (self.patientData.email)
 

class ExtraInfo:
    def __init__(self):
        #        print('Nombre ExtraInfo:') 
                self.enumDeviceType=1
                self.enumRemote=1
                self.enumDevKey=1
                self.enumProtocol=1
                self.strDeviceType=1
                self.dataMode=1
                self.protocolVersion_Main=1
                self.protocolVersion_Sub=1
                self.deviceVersion_Main=1
                self.deviceVersion_Sub=1
                self.fileVersion_Main=1
                self.fileVersion_Sub=1
                self.softWareVersion_Main=1
                self.softWareVersion_Sub=1
            
    def setEnumDeviceType(self,_enumDeviceType):
                self.enumDeviceType=_enumDeviceType
    def setEnumRemote(self,_enumRemote):
                self.enumRemote=_enumRemote
    def setEnumDevKey(self,_enumDevKey):
                self.enumDevKey=_enumDevKey
    def setEnumProtocol(self,_enumProtocol):
                self.enumProtocol=_enumProtocol
    def setStrDeviceType(self,_strDeviceType):
                self.strDeviceType=_strDeviceType
    def setDataMode(self,_dataMode):
                self.dataMode=_dataMode
    def setProtocolVersion_Main(self,_protocolVersion_Main):
                self.protocolVersion_Main=_protocolVersion_Main
    def setProtocolVersion_Sub(self,_protocolVersion_Sub):
                self.protocolVersion_Sub=_protocolVersion_Sub
    def setDeviceVersion_Main(self,_deviceVersion_Main):
                self.deviceVersion_Main=_deviceVersion_Main
    def setDeviceVersion_Sub(self,_deviceVersion_Sub):
                self.deviceVersion_Sub=_deviceVersion_Sub
    def setFileVersion_Main(self,_fileVersion_Main):
                self.fileVersion_Main=_fileVersion_Main
    def setFileVersion_Sub(self,_fileVersion_Sub):
                self.fileVersion_Sub=_fileVersion_Sub
    def setSoftWareVersion_Main(self,_softWareVersion_Main):
                self.softWareVersion_Main=_softWareVersion_Main
    def setSoftWareVersion_Sub(self,_softWareVersion_Sub):
                self.softWareVersion_Sub=_softWareVersion_Sub

    def print(self):
            print (self.enumDeviceType)
            print (self.enumRemote)
            print (self.enumDevKey)
            print (self.enumProtocol)
            print (self.strDeviceType)
            print (self.dataMode)
            print (self.protocolVersion_Main)
            print (self.protocolVersion_Sub)
            print (self.deviceVersion_Main)
            print (self.deviceVersion_Sub)
            print (self.fileVersion_Main)
            print (self.fileVersion_Sub)
            print (self.softWareVersion_Main)
            print (self.softWareVersion_Sub)


class Abpm:
    def __init__(self):
   #             print('Nombre Abpm:') 
                self.yearBegin=1
                self.monBegin=1
                self.dayBegin=1
                self.hourBegin=1
                self.minBegin=1
                self:secBegin=1
    def setYearBegin(self,_yearBegin):
        self.yearBegin=_yearBegin
    def setMonBegin(self,_monBegin):
        self.monBegin=_monBegin
    def setDayBegin(self,_dayBegin):
        self.dayBegin=_dayBegin
    def setHourBegin(self,_hourBegin):
        self.hourBegin=_hourBegin
    def setMinBegin(self,_minBegin):
        self._minBegin=_minBegin
    def setSecBegin(self,_secBegin):
        self.secBegin=_secBegin

class Maquina:
    def __init__(self):
       #       print('Nombre Maquina:') 
        self.patientData = PatientData()
        self.extraInfo   = ExtraInfo()
        self.abpmdata    = Abpm()
        self.datosLeidoDeLaMaquina=[]
        self.comentarioLeidoDeLaMaquina=[]
    
    def agregarDatosDeLaMaquina(self,s):
            if s[1:2]== "=" and  s[0:1].isdigit():
                aux=s.split("=")
                self.datosLeidoDeLaMaquina.append(aux[1])
            if s[2:3]== "=" and  s[0:2].isdigit():
                aux=s.split("=")
                self.datosLeidoDeLaMaquina.append(aux[1])
    def agregarComentarioDeLaMaquina(self,s):
                if s[0:1]== "C" and s[2:3]== "="  :
                    aux=s.split("=")
                    ss = s.split("=")
                    sss=ss[1]
               
                    self.comentarioLeidoDeLaMaquina.append(sss)
                if s[0:1]== "C" and s[3:4]== "="  :
                    ss = s.split("=")
                    sss=ss[1]
            
                    self.comentarioLeidoDeLaMaquina.append(sss)

    def printDatosLeidosDeLaMaquina(self):
        i=0
        ss="[data]\nvalor1 = "
        while i < len(self.datosLeidoDeLaMaquina):
          
            cc=self.comentarioLeidoDeLaMaquina[i]

            systole     = ""
            diastole    = ""
            fr          = ""
            pam         = ""
            dia         = ""
            ano         = ""
            mes         = ""
            diaActual   = ""
            hora        =""
            if (len(self.datosLeidoDeLaMaquina[i]) >43 ):
                systole     = str(int(self.datosLeidoDeLaMaquina[i][16:18],16)) 
                diastole    = str(int(self.datosLeidoDeLaMaquina[i][20:22],16))
                fr          = str(int(self.datosLeidoDeLaMaquina[i][28:30],16))
                pam         = str(int(self.datosLeidoDeLaMaquina[i][24:26],16))
                ano = str(int(self.datosLeidoDeLaMaquina[i][0:4],16))
                mes = "0"+ str(int(self.datosLeidoDeLaMaquina[i][4:6],16))
                dia = "0"+ str(int(self.datosLeidoDeLaMaquina[i][6:8],16))
                minutoString   = "0" + str(int(self.datosLeidoDeLaMaquina[i][10:12],16))
                if (len(minutoString) > 2):
                    minutoString   = str(int(self.datosLeidoDeLaMaquina[i][10:12],16))

                horaString     = "0" + str(int(self.datosLeidoDeLaMaquina[i][8:10],16))
                if ( len(horaString) > 2):
                    horaString     =  str(int(self.datosLeidoDeLaMaquina[i][8:10],16))
                hora        = horaString +":"+ minutoString
                print(hora)
                diaActual   = ano+"-"+mes[0:2]+"-"+dia[0:2]

            else:
                systole     = str(int(ss[8:10],16)) 
                diastole    = str(int(ss[10:12],16))
                fr          = str(int(ss[4:6],16))
                pam         = str(int(ss[6:8],16))
            a = diaActual + " " + hora + "," + systole + "," + diastole + "," + fr + "," +"0,0,"+"'"+ cc[0:len(cc)-1] +"'\n"+ '##'
            print(a)
            ss=ss+a
            i =i+ 1
            print(i)
            print(ss)
            a=len(ss)
            sss=ss[0:len(ss)-2] 
        return sss

    def agregarAbpmdata(self,s):
            if s.find("YearBegin") != -1:
                self.abpmdata.setYearBegin(s)
            if s.find("MonBegin") != -1:
                self.abpmdata.setMonBegin(s)
            if s.find("DayBegin") != -1:
                self.abpmdata.setDayBegin(s)
            if s.find("HourBegin") != -1:
                self.abpmdata.setHourBegin(s)
            if s.find("MinBegin") != -1:
                self.abpmdata.setMinBegin(s)
            if s.find("SecBegin") != -1:
                self.abpmdata.setSecBegin(s)
    def agregarPatientData(self,s):
            aux=s.split("=")
            if s.find("ABPMCount") != -1:
                self.patientData.setABPMCount(aux[1])
            if s.find("Name") != -1:
                self.patientData.setName(aux[1])
            if s.find("ID") != -1:
                self.patientData.setId(aux[1])
            if s.find("YearBegin") != -1:
                self.patientData.setYearBegin(aux[1])
            if s.find("DayBegin") != -1:
                self.patientData.setDayBegin(aux[1])
            if s.find("HourBegin") != -1:
                self.patientData.setHourBegin(aux[1])
            if s.find("MinBegin") != -1:
                self.patientData.setMinBegin(aux[1])
            if s.find("SecBegin") != -1:
                self.patientData.setSecBegin(aux[1])
 
            if s.find("MaxPressValue") != -1:
                self.patientData.setMaxPressValue(aux[1])
            if s.find("AwakeWarnOnOff") != -1:
                self.patientData.setAwakeWarnOnOff(aux[1])
            if s.find("AwakeSysMaxValue") != -1:
                self.patientData.setAwakeSysMaxValue(aux[1])
            if s.find("AwakeSysMinValue") != -1:
                self.patientData.setAwakeSysMinValue(aux[1])
            if s.find("AwakeDiaMaxValue") != -1:
                self.patientData.setAwakeDiaMaxValue(aux[1])
            if s.find("AwakeDiaMinValue") != -1:
                self.patientData.setAwakeDiaMinValue(aux[1])
            if s.find("AsleepWarnOnOff") != -1:
                self.patientData.setAsleepWarnOnOff(aux[1])
            if s.find("AsleepSysMaxValue") != -1:
                self.patientData.setAsleepSysMaxValue(aux[1])
 
            if s.find("AsleepSysMinValue") != -1:
                self.patientData.setAsleepSysMinValue(aux[1])
            if s.find("AsleepDiaMaxValue") != -1:
                self.patientData.setAsleepDiaMaxValue(aux[1])
            if s.find("AsleepDiaMinValue") != -1:
                self.patientData.setAsleepDiaMinValue(aux[1])
            if s.find("Display") != -1:
                self.patientData.setDisplay(aux[1])
            if s.find("StartKey") != -1:
                self.patientData.setStartKey(aux[1])
            if s.find("AwakeHour") != -1:
                self.patientData.setAwakeHour(aux[1])
            if s.find("AwakeMin") != -1:
                self.patientData.setAwakeMin(aux[1])
            if s.find("AwakeDuration") != -1:
                self.patientData.setAwakeDuration(aux[1])
            if s.find("AsleepHour") != -1:
                self.patientData.setAsleepHour(aux[1])
            if s.find("AsleepMin") != -1:
                self.patientData.setAsleepMin(aux[1])
            if s.find("AsleepDuration") != -1:
                self.patientData.setAsleepDuration(aux[1])
            if s.find("SpecialHourStart") != -1:
                self.patientData.setSpecialHourStart(aux[1])
            if s.find("SpecialDuration") != -1:
                self.patientData.setSpecialDuration(aux[1])
            if s.find("SpecialDuration") != -1:
                self.patientData.setSpecialDuration(aux[1])
            if s.find("SpecialHourEnd") != -1:
                self.patientData.setSpecialHourEnd(aux[1])
            if s.find("SpecialMinEnd") != -1:
                self.patientData.setSpecialMinEnd(aux[1])
            if s.find("Addr") != -1:
                self.patientData.setAddr(aux[1])
            if s.find("Gender") != -1:
                self.patientData.setGender(aux[1])
            if s.find("Birthday") != -1:
                self.patientData.setBirthday(aux[1])
            if s.find("Race") != -1:
                self.patientData.setRace(aux[1])
            if s.find("Height") != -1:
                self.patientData.setHeight(aux[1])
            if s.find("Weight") != -1:
                self.patientData.setWeight(aux[1])
            if s.find("Age") != -1:
                self.patientData.setAge(aux[1])
            if s.find("Phone") != -1:
                self.patientData.setPhone(aux[1])
            if s.find("Medications") != -1:
                self.patientData.setMedications(aux[1])
            if s.find("ReferringPhys") != -1:
                self.patientData.setReferringPhys(aux[1])
            if s.find("InterprettingPhys") != -1:
                self.patientData.setInterprettingPhys(aux[1])
            if s.find("Comments") != -1:
                self.patientData.setComments(aux[1])
            if s.find("ClinicalInterp") != -1:
                self.patientData.setClinicalInterp(aux[1])
 
            if s.find("OutpatientNo") != -1:
                self.patientData.setOutpatientNo(aux[1])
            if s.find("AdmissionNo") != -1:
                self.patientData.setAdmissionNo(aux[1])
            if s.find("BedNo") != -1:
                self.patientData.setBedNo(aux[1])
            if s.find("DepartmentNo") != -1:
                self.patientData.setDepartmentNo(aux[1])
            if s.find("Email") != -1:
                self.patientData.setEmail(aux[1])
    def agregarExtraInfo(self,s):
            if s.find("enumDeviceType") != -1:
                self.extraInfo.setEnumDeviceType(s)
            if s.find("enumRemote") != -1:
                self.extraInfo.setEnumRemote(s)
            if s.find("enumDevKey") != -1:
                self.extraInfo.setEnumDevKey(s)
            if s.find("enumProtocol") != -1:
                self.extraInfo.setEnumProtocol(s)
            if s.find("strDeviceType") != -1:
                self.extraInfo.setStrDeviceType(s)
            if s.find("DataMode") != -1:
                self.extraInfo.setDataMode(s)
            if s.find("ProtocolVersion_Main") != -1:
                self.extraInfo.setProtocolVersion_Main(s)
            if s.find("ProtocolVersion_Sub") != -1:
                self.extraInfo.setProtocolVersion_Sub(s)
            if s.find("DeviceVersion_Main") != -1:
                self.extraInfo.setDeviceVersion_Main(s)
            if s.find("DeviceVersion_Sub") != -1:
                self.extraInfo.setDeviceVersion_Sub(s)
            if s.find("FileVersion_Main") != -1:
                self.extraInfo.setFileVersion_Main(s)
            if s.find("strDeviFileVersion_SubceType") != -1:
                self.extraInfo.setStrDeviFileVersion_SubceType(s)
            if s.find("SoftWareVersion_Main") != -1:
                self.extraInfo.setSoftWareVersion_Main(s)
            if s.find("SoftWareVersion_Sub") != -1:
                self.extraInfo.setSoftWareVersion_Sub(s)