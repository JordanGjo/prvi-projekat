temperatura = int(input("Unesite temperaturu : "))
test_temperatura = -1
temperatura =  test_temperatura
poruka = "" 
if temperatura < 0:
    poruka = "oprez klizavo"

if temperatura > 0:
   poruka = "Temperatura iznad 0"
   if temperatura > 30:
      poruka = "Ukljucite klima uredjaj" 

test_temperatura = -1
ocekuvana_poruka = "Oprez klizavo"
if poruka == ocekuvana_poruka :
   print("Case - ispod nule , test prosao")