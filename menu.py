from win32com.client import *
 
directorio_Programa_Mapa='\"D:\\Program Files (x86)\\Sistemed\\MAPA\\bin\\sistemed_mapa\"'
 
 
sh = Dispatch("Wscript.Shell")
 
 
print(directorio_Programa_Mapa)
sh.Run(directorio_Programa_Mapa)
#sh.AppActivate("Untitled");
#sh.Sendkeys("Hello!")
#sh.SendKeys("{Enter}")