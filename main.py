import pandas as pd
from twilio.rest import Client

# Envio de SMS
# Configurar com SID e Token do Twilio
# Your Account SID from twilio.com/console
account_sid = "ACDe82967e5dbd72d3a8162bfd2ada08165"
# Your Auth Token from twilio.com/console
auth_token  = "09D3c9729028fc33463b78043865c6aa1"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta!')
        print(f'Vendedor: {vendedor} | Vendas: R${vendas}')

        # Mensagem da SMS
        # Configurar número que recebe e que envia SMS
        message = client.messages.create(
            to="+15558675309", 
            from_="+15017250604",
            body=f'Parabéns {Vendedor}!! Você bateu a meta e ganhou o bônus viagem.')

        print(message.sid)