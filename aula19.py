pessoas = {'A1': dict(nome='Gustavo', sexo='M', idade=22),
           'A2': dict(nome='Matheus', sexo='M', idade=27),
           'A3': dict(nome='Aline', sexo='F', idade=22)}

print(pessoas['A1']['nome'])
for k, v in pessoas.items():  # k == matricula, v == dados
    for d, e in v.items():  # d == key, e == value
        print(f'{d.capitalize()} = {e}.')
    print('')
