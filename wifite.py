import os
import subprocess
import time

comando=input("inserisci comando")
#os.popen("wifite")
result=subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE).stdout.read()
print(result)

print (time.strftime("%H:%M:%S") +" " + time.strftime("%d/%m/%Y"))
print (time.strftime("%d/%m/%Y"))