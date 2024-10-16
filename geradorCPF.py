# Gerador de CPF

import random

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9)) # Gera nove números aleatórios

# Sistema de validação de cpf                         
contador1 = 10
contador2 = 11
resultado1 = 0
resultado2 = 0

for digito in nove_digitos:
    resultado1 += (int(digito) * contador1)
    contador1 -= 1

primeiro_digito = (resultado1 * 10) % 11

if primeiro_digito > 9:
    print('O primeiro digito do CPF é 0')
else:
    print(f'O primeiro digito do CPF é {primeiro_digito}')

dez_digitos = nove_digitos + str(primeiro_digito)

for digito2 in dez_digitos:
    resultado2 += (int(digito2) * contador2)
    contador2 -= 1

segundo_digito = (resultado2 * 10) % 11

if segundo_digito > 9:
    print('O segundo digito do CPF é 0')
else:
    print(f'O segundo digito do CPF é {segundo_digito}')

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado) # Exibe o cpf gerado