"""
Variables

Valor, tipo, identidad

a = 7

! En Python lo que ocurre al ejecutar la sentencia o instrucción a = 7 es que se crea 
! primero un objeto con el VALOR 7 de TIPO int y se ubica en un lugar de memoria. 
! Este lugar de memoria se denomina en Python IDENTIDAD del objeto. Luego, la acción 
! de asignar 7 a la variable a hará que este nombre o identificador se asocie o refiere 
! a la dirección de memoria del objeto 7, o sea, a tendrá la misma identidad que 7.

"""


###########################################################################################
###                                Tipo de variables simples                            ###
###########################################################################################


##############################   Entrada de datos  ########################################

var_Int = 1                     ###  esta linea representa una variable entero 1,2,3,4...n   no admite: 1.2, 1.5
var_Float = 2.5                 ###  Esta lina admite variables tipo racional 1.5, 1.6,..n    
var_bolena = 3 > 2              ### arroja o maneja dartos en falso y verdadero TRUE = 1 FALSE = 0
var_Char = "a"                  ### Esta es una vabriable de tipo simple pero con letras, y estas deben estar entre comillas

var_Char = "S"
var_String = "Hello World"

###############################  Operaciones         #######################################
suma1 = var_Int + var_Int  
suma2 = var_Int + var_Int 
suma3 = var_Int + var_Float 

mult = var_Int * var_Int

################################     Salidas     ###########################################
print("resutaldo de suma1", suma2)      # FUNCION   ==>> print()
print("resutaldo de suma2", suma3)
print("resutaldo de mult", mult)

print("###############################################################")

# Entdrada
# Operaciones
# Salida Muesrta de resultados

# Programacion estructurada  ###   UNO DE LOS PARADIFAMAS DE PROGRAMACION
print(var_Float)
print(var_bolena)
print(var_Char)

print(type(var_Int))       #  type(var_Int)  esta funcion nos va decir que tipo devariable es     
print(type(var_Float))
print(type(var_bolena))
print(type(var_Char))

###########################################################################################
###########################################################################################

"""
La acción de asignación se usa para darle a una variable un valor determinado. 
En Python la acción de asignación de valores a una variable quiere decir que 
la variable con su nombre determinado se va a asociar al valor de la derecha 
de la asignación:
"""
