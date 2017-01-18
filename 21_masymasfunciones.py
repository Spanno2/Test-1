def add(a, b):
    print "ADDING %d + %d" % (a, b)
    c = a + b
    return c

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

def calculo_imc (p,t):
	imc = p / (t*t)
	return imc

print "Ingresa tu peso y tu talla (en kg y en metros, para los decimales pone un punto) para calcular el IMC:\n",
peso = float(raw_input()) #el raw_input devuelve en forma string, lo que hay que añadir es el comando "float" que convierte esa string en float para poder operar matematicamente.
talla = float (raw_input())
imc = calculo_imc (peso, talla)
print "\nTu IMC es %f" % (imc)

# A puzzle for the extra credit, type it in anyway.
print "\nEsto es una cosa aparte, pero esta bueno comprenderlo"

what = add(30, subtract(1.82, multiply(78, divide(100, 2))))

print "\nThat becomes: ", what, "Can you do it by hand?"