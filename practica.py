#La nota del trimestre está basada en
#Nota hito individual = 30 %
#Nota hito grupal = 20 %
#Nota examen = 50 %

def Nota():
    nota_hitoIndividual=float(input('Digame su nota de hito individual '))
    hitoIndivudal=nota_hitoIndividual*0.3
    nota_hitoGrupal=float(input('Digame su nota de hito grupal '))
    hitoGrupal=nota_hitoGrupal*0.20
    nota_Examen=float(input('Digame su nota de examen '))
    notaExamen=nota_Examen*0.5
    NotaTrimestre=hitoIndivudal+hitoGrupal+notaExamen
    print (NotaTrimestre)
Nota()

#Se pide calcular la nota de tu examen tipo test.
#Serán 20 preguntas
#Las preguntas correctas sumarán 0,5
#Las preguntas incorrectas restarán 0,25
#Las preguntas sin contestar tendrán 0


def NotaTipotest():
    preguntas_Correctas=float(input('Digame sus respuestas correctas'))
    preguntaCorrecta=preguntas_Correctas*0.5
    preguntas_Incorrectas=float(input('Digame sus respuestas incorrectas'))
    preguntaIncorrecta=preguntas_Incorrectas*-0.25
    preguntas_NoContestadas=float(input('Digame sus respuestas no contestadas'))
    preguntaNoContestada=preguntas_NoContestadas*0
    Nota=preguntaCorrecta+preguntaIncorrecta+preguntaNoContestada
    print (Nota)
NotaTipotest()

#Diseña un algoritmo y un diagrama de flujo para:
#Con la base y la altura de un rectángulo, se nos pide calcular su perímetro y
#su área

#Datos de entrada 
#--Base y altura
#Datos de salida
#--Perímetro y área
#Algoritmo
#--Base*altura=area
#--2(base+altura)=perímetro

def rectangulo():
    base=float(input('Digame la base '))
    altura=float(input('Digame la altura '))
    area=base*altura
    perimetro=base*2+altura*2
    print (area)
    print (perimetro)
rectangulo()
