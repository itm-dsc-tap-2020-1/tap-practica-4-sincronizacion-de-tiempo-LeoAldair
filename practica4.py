import datetime
from time import ctime
import ntplib
import os

servidorT = "time-a-g.nist.gov"
t1 = datetime.datetime.now()
print("T1 : %s" % t1)
    
clienteNTP = ntplib.NTPClient()
respuesta = clienteNTP.request(servidorT)
hora_ser = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
print("\nTiempo de servidor : " + str(hora_ser))
t2 = datetime.datetime.now()
print("\nT2 : %s" % t2)

ajuste = (t2-t1)/2
print("\nAjuste : %s" % ajuste)

reloj = hora_ser + ajuste
print("\nReloj :  %s" % reloj)

minu = int(reloj.minute)
fecha = ""
if minu>9 :
    fecha = "0"+str(reloj.month)+""+str(reloj.day)+""+str(reloj.hour)+""+str(reloj.minute)+""+str(reloj.year)
else:
    fecha = "0"+str(reloj.month)+""+str(reloj.day)+""+str(reloj.hour)+"0"+str(reloj.minute)+""+str(reloj.year)
print(fecha)

os.system('date -u %s' % fecha)





