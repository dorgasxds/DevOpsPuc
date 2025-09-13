def calcular_tmb_homem(peso, altura, idade):
    return 10 * peso + 6.25 * altura - 5 * idade + 5

def calcular_tmb_mulher(peso, altura, idade):

    return 10 * peso + 6.25 * altura - 5 * idade - 161

def main():
    try:
        sexo = input("Digite seu sexo (M/F): ").strip().upper()
        if sexo not in ['M', 'F']:
            raise ValueError("Sexo deve ser M ou F")
            
        peso = float(input("Digite seu peso em kg: "))
        if peso <= 0:
            raise ValueError("Peso deve ser positivo")
            
        altura = float(input("Digite sua altura em cm: "))
        if altura <= 0:
            raise ValueError("Altura deve ser positiva")
            
        idade = int(input("Digite sua idade em anos: "))
        if idade <= 0:
            raise ValueError("Idade deve ser positiva")
        
        if sexo == 'M':
            tmb = calcular_tmb_homem(peso, altura, idade)
        else:
            tmb = calcular_tmb_mulher(peso, altura, idade)
        
        print(f"Sua TMB é: {tmb:.2f} calorias por dia")
            
    except ValueError as e:
        print(f"Erro: {e}")
    

