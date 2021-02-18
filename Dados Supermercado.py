#-*- coding:utf-8 -*-

nome_prod = [0]*9999
cod_prod = [0]*9999
prec_prod = [0]*9999
preçototal = 0.00

i = 0
z = int ( input("Digite 1 para continuar ou 0 para sair. "))
while (z !=0 and i<9999):
    nome_prod[i] =  input ("Digite o nome do produto: ")
    cod_prod[i] =  input ("Digite o código do produto: ")
    prec_prod[i] = float ( input ("Digite o preço do produto: "))
    preçototal = preçototal + prec_prod[i]
    print ("")
    i = i + 1
    z = int ( input("Digite 1 para continuar ou 0 para sair. "))

print ("")
print ("")

k = 0
while (k<i):
    print ("Nome do produto: ",nome_prod[k])
    print ("Código do produto: ",cod_prod[k])
    print ("Preço do produto: R$%.2f " % prec_prod[k])
    print ("")
    k = k + 1

print ("")
print ("Preço Total: R$%.2f " % preçototal)

print("Digite o valor a pagar: ")
val_pag = float (input()) 

print("")
if(val_pag>preçototal):
    troco = val_pag - preçototal
    print("Troco: R$ %.2f" % troco)


ex = input ("Digite qualquer tecla para sair: ")


