def calcular_salario(hora, valor):
    return hora * valor

def calcular_imposto_renda(salario):
    return (11/100)*salario

def calcular_inss(salario):
    return (8/100)*salario

def calcular_sindicato(salario):
    return (5/100)*salario

def calcular_salario_liquido(salario, desc_IR, desc_inss, desc_sindicato):
    descontos = desc_IR  + desc_inss + desc_sindicato
    return salario - descontos


def calcular_descontos(salario):
    desc_IR = calcular_imposto_renda(salario)
    desc_inss =  calcular_inss(salario)
    desc_sindicato = calcular_sindicato(salario)
    salario_liquido = calcular_salario_liquido(
        salario, desc_IR, desc_inss, desc_sindicato
    )
    return salario_liquido, desc_IR, desc_inss, desc_sindicato
    
   


primeira_entrada = "Quanto você ganha por hora: "
segunda_entrada = "Quanto você trabalhou por hora: "

valor = float(input(primeira_entrada))
hora = int(input(segunda_entrada))

salario = calcular_salario(valor, hora)

salario_liquido, desc_IR, desc_inss, desc_sindicato = calcular_descontos(
    salario
)
print(

    "+ Salário Bruto : R$ {:.2f}\n".format(salario),
    "- IR (11%) : R$ {:.2f}\n".format(desc_IR),
    "- INSS (8%) : R$ {:.2f}\n".format(desc_inss),
    "- Sindicato ( 5%) : R$ {:.2f}\n".format(desc_sindicato),
    "= Salário Liquido : R$ {:.2f}\n".format(salario_liquido)
)