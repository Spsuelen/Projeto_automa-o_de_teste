from datetime import datetime, timedelta


class TestData(object):
    #
    budget_type = 'usuario'
    # Representa o campo "nome" vazio
    new_budget_type = ""
    # Representa o campo "nome" com menos de 2 caracteres
    new_budget_type2 = "A"
    # Representa o campo "nome" com mais de 20 caracteres
    new_budget_type3 = "Testando um nome aleatorio"
    # Representa o campo "nome" com uma patualização para um  novo type
    update_budget_type = "Livraria"

    #
    budget_value = "600"
    # Representa o campo "valor" vazio
    new_budget_value = ""
    # Representa o campo "valor" com um numero inteiro
    new_budget_value2 = "1000"
    # Representa o campo "valor" com um numero decimal de ate duas casas
    new_budget_value3 = "1000.00003"
    # Representa o campo "valor" com uma atualização.
    update_budget_value = "1500.75"

    #
    budget_account = 'user01-'
    # Representa o campo "Account" vazio
    new_budget_account = ""
    # Representa o campo "Account" com menos de 3 caracteres
    new_budget_account2 = "ab"
    # Representa o campo "Account" com mais de 8 caracteres
    new_budget_account3 = "abcde1234"
    # Representa o campo "Account" para verifcar caracteres especiais
    new_budget_account4 = "user@01"
    # Representa o campo "account" com uma atualização .
    update_budget_account = "eu-01-"

    budget_note = "Testando as informações"
    # Representa o campo "Note" vazio
    new_budget_note = ""
    # Representa o campo "Account" com mais de 20 caracteres
    new_budget_note2 = "Testando Informacoes aleatorias aqui"
    # Representa o campo "Note" com uma atualização .
    update_budget_note = "Testando Novamente"
