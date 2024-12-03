temperatura = int(input("Unesite temperaturu : "))
test_temperatura = -1
test_temperatura = 35
temperatura = test_temperatura
poruka = "" 
if temperatura < 0:
    poruka = "oprez klizavo"

if temperatura > 0:
   poruka = "Temperatura iznad 0"
   if temperatura > 30:
      poruka = "Ukljucite klima uredjaj" 

test_temperatura = -1
ocekuvana_poruka = "Ukljucite klima uregjaj"
if poruka == ocekuvana_poruka:
    print ("Case - ispod nule , test prosao")