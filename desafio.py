CONSTANTE_BONUS = 1000

# 1. Solicite que o funcionário informe seu nome

nome_usuario = str(input('Informe nome do funcionario: '))

# 2. Solicite que salário desse funcionário seja informado

salario_usuario = float(input('Informe o salário: '))

# 3. Insira o valor de bônus recebido

bonus_usuario = float(input('Informe o percentual do bônus: '))

# 4. Calcule valor do bônus final

calculo = CONSTANTE_BONUS + ( salario_usuario + (salario_usuario * bonus_usuario ))

# 5.Imprima o cálculo bônus final

print(calculo)

# 6. Imprima mensagem personalizada

print(f'Olá {nome_usuario}, o seu bônus final será de {calculo}')