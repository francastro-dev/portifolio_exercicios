print("Calcule seu IMC")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kg:  "))
altura = float(input("Digite sua Altura: "))

imc = (peso / (altura*altura))
print(f'Ola {nome}: \n')
print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print("Seu IMC indica Magreza, procure orientação médica!")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu peso está normal")
elif imc > 24.9 and imc <= 29.9:
    print("Voce está em Sobrepeso,")
elif imc > 29.9 and imc <= 39.9:
    print("Você está em obesidade, É importante buscar orientação médica")
else:
    print("Voce está com Obesidade Grave, É fundamental buscar orientação médica")