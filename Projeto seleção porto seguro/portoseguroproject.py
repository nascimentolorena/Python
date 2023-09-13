carrinhos = ("Digite abaixo, a quantidade de carrinhos que cada setor precisa guardar.")
print(carrinhos)

soroteca = 4
print(f'Soroteca =  {soroteca}')
hormonio = input("Hormônio - ")
bioquimica = input("Bioquímica - ")
hematologia = input("Hematologia -  ")

try:
    hormonio_int = int(hormonio)
    bioquimica_int = int(bioquimica)
    hematologia_int = int(hematologia)
    soma = hormonio_int + bioquimica_int + hematologia_int + soroteca

    if hormonio_int > 3:
        print("Hormônio excedeu o número de carrinhos.")
    else:
        print("Hormônio = OK")
    if bioquimica_int > 1:
        print("Bioquímica excedeu o número de carrinhos.")
    else:
        print("Bioquímica = OK")
    if hematologia_int > 1:
        print("Hematologia excedeu o número de carrinhos.")
    else:
        print("Hematologia = OK")
    if hormonio_int > 3 or bioquimica_int > 1 or hematologia_int > 1:
        print ("Por favor, coloque as amostras dos carrinhos excedentes em uma caixa organizadora e as disponha, no chão dos corredores da câmara.")
    elif hormonio_int + bioquimica_int + hematologia_int == 5:
        print("A câmara está completa.")
    elif hormonio_int + bioquimica_int + hematologia_int < 5:
        print(f'A câmara comporta até 9 carrinhos e no momento tem {soma}. Ainda cabe mais {9 - soma}.')
except:
    print('Uma ou mais opções não são válidas. Por favor, digite apenas números.')





