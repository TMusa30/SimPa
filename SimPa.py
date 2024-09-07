import sys


stack = []

ulaz_string = ""

for line in sys.stdin:
  ulaz_string += line

lines = ulaz_string.splitlines()

pocetno_stanje = lines[5]
proba = stack.append(lines[6])

prihvatljivo_stanje = lines[4]
prijelazi = lines[7:]

ulazi = lines[0].split("|")

trenutno_stanja = [pocetno_stanje]
simbol_stanje = 0
izlaz = []

izlaz.append(pocetno_stanje + "#" + stack[0])
i = 0
for ulaz in ulazi:
  for trenutno_stanje in trenutno_stanja:
    for simbol in ulaz.split(","):
      zapamti = []
      nijeProsao = 0
      for prijelaz in prijelazi :
        epsilonPrijelaz = []

        
        pocetno, ulazni_simbol, znak = prijelaz.split("->")[0].split(",")
        if stack and stack[0]:
            if prihvatljivo_stanje != simbol_stanje:
                if pocetno == trenutno_stanje and ulazni_simbol == "$" and znak == stack[0][0]:
                    novo_stanje = prijelaz.split("->")[1].split(",")
                    simbol_stanje = novo_stanje[0]
                    znakZapamti = novo_stanje[1]

                    trenutno_stanje = simbol_stanje

                    cuvajPop = stack.pop()
                    prvoSlovoNaStogu = cuvajPop[0]

                    if len(cuvajPop) >1 :
                        stack.append(znakZapamti + cuvajPop[1:])
                
                    else :
                        stack.append(znakZapamti)
                    epsilonPrijelaz.append(simbol_stanje + "#" + "".join(stack))
                    izlaz.append("|".join(epsilonPrijelaz))
                
            if nijeProsao == 0 :    
                if pocetno == trenutno_stanje and ulazni_simbol == simbol and znak == stack[0][0]:
                    nijeProsao = 1
                    i = i + 1
                    novo_stanje = prijelaz.split("->")[1].split(",")
                    simbol_stanje = novo_stanje[0]
                    znakZapamti = novo_stanje[1]
               
                    trenutno_stanje = simbol_stanje
                    if znakZapamti == "$":
                       popaj = stack.pop()
                       stack.append(popaj[1:])
                    else:
                       cuvajPop = stack.pop()
                       prvoSlovoNaStogu = cuvajPop[0]
                       if len(cuvajPop) > 1:
                        stack.append(znakZapamti + cuvajPop[1:])

                       else : 
                        stack.append(znakZapamti)
                
                    zapamti.append(simbol_stanje + "#" + "".join((stack)))
                    izlaz.append("|".join(zapamti))
                

                
  if (i == 0) :
    izlaz.append("fail")
    izlaz.append("0")
  elif(simbol_stanje == prihvatljivo_stanje):
    izlaz.append("1")
  else :
    izlaz.append("0")
  print("|".join(izlaz))
  
      




    
