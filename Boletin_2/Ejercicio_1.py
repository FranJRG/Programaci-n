dia=int(input("Que dia es"))
print("Es valido?", 1<=dia<=31)

print("-----------")

sueldo_bruto=int(input("Que sueldo tienes"))
sueldo_neto=int(input("Cuanto tenemos"))
retencion=(sueldo_bruto*22)/100
print(retencion<=sueldo_neto)

print("-----------")

num1=int(input("Que numero es"))
num2=int(input("Cual es el numero"))
print(num1%3==0 or num2%3==0)

print("-----------")

nota=int(input("Que calificacion obtenemos"))
print(5<=nota<=10)

print("---------------")

nota1=int(input("Que nota es"))
nota2=int(input("Que nota es"))
nota3=int(input("Que nota es"))
print(5>=(nota1+nota2+nota3)/3<=10)

print("----------------")

nota1=int(input("Que nota obtienes"))
nota2=int(input("Que nota obtienes"))
nota3=int(input("Que nota obtienes"))
print(5<=nota1 and 5<=nota2 and 5<=nota3)

print("------------")

Saldo=int(input("Cual es el saldo"))
Descubierto=int(input("Cuantas veces"))
print(Saldo>=1000 and Descubierto<5)

print("----------------")

asignaturasAprobadas=int(input("Cuantas hay aprobadas"))
asignaturasCurso=int(input("Cuantas materias hay"))
print(asignaturasAprobadas>= (asignaturasCurso*30)/100)

print("----------------")

mes=int(input("En que mes estamos"))
dia=int(input("Que dia es"))
print(0>=mes<12 and 0>=dia<31 )