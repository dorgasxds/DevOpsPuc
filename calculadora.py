def calcular_tmb_homem(peso, altura, idade):
    return 10 * peso + 6.25 * altura - 5 * idade + 5

def calcular_tmb_mulher(peso, altura, idade):

    return 10 * peso + 6.25 * altura - 5 * idade - 161

def main():
    sexo = input("Digite seu sexo (M/F): ").strip().upper()
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em cm: "))
    idade = int(input("Digite sua idade em anos: "))
    
    if sexo == 'M':
        tmb = calcular_tmb_homem(peso, altura, idade)
    else:
        tmb = calcular_tmb_mulher(peso, altura, idade)
    
    print(f"Sua TMB é: {tmb:.2f} calorias por dia")

if __name__ == "__main__":
    main()
    
