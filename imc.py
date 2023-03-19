

def imc (estatura, peso):

    return peso / estatura ** 2

peso = float(input("Escriba su peso (kg): "))
estatura = float(input("Escriba su estarura (Mt): "))

indice = imc (estatura, peso)

print("Su indice de masa corpora (IMC): {}".format(indice))
 
