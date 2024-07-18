from datetime import date
from datetime import datetime
import time
from datetime import timedelta


class TestData(object):
    # primeira Inserção de informações
    expense_price = "300"
    expense_title = "Livros"
    expense_category = "Lazer"

    # segunda Inserção de Informações
    expense_price2 = "700"
    expense_title2 = "Supermercado"
    expense_category2 = "Alimentacao"

    # terceira Inserção de Informações
    expense_price3 = "780"
    expense_title3 = "Mensalidade do curso"
    expense_category3 = "Educacao"

    # quarta Inserção de Informações
    expense_price4 = "3500"
    expense_title4 = "Aluguel"
    expense_category4 = "Moradia"

    # quinta Inserção de Informações
    expense_price5 = "1000"
    expense_title5 = "financiamento moto"
    expense_category5 = "Locomocao"

    # atualizando o price
    expense_new_price = "1500"

    # Testando valores incorretos na Adição
    new_expense_price = "-5000"
    new_expense_title = "algo aleatorio para o teste verificar"
    new_expense_category = "algo aleatorio para o teste verificar a adição no aplicativo de valores incorretos"

    # Utilizando a data e hora atual do sistema

    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M')
