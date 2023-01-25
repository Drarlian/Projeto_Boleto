"""
Simulador de Boleto.
"""
import datetime

def vencimento_boleto():
    data_atual = datetime.datetime.now()

    boleto_base = datetime.timedelta(days=3)
    boleto_caso_especial = datetime.timedelta(days=5)

    if 0 <= data_atual.weekday() <= 1:
        return data_atual + boleto_base
    elif 2 <= data_atual.weekday() <= 4:
        return data_atual + boleto_caso_especial


confirmacao = True

if confirmacao:
    print('O boleto foi gerado com sucesso!')
    print(f'Seu boleto vence no dia: {vencimento_boleto().strftime("%d/%m/%Y")}')
else:
    print('O boleto não foi gerado.')
