nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print(f'A média entre {nota1} e {nota2} é: {media:.1f}')
#ou
print(f'A média entre {nota1} e {nota2} é: '
      f'{(nota1+nota2)/2:.1f}')