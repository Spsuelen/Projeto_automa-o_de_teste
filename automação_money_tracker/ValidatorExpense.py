class ExpenseValidator:
    @staticmethod
    def validate_price(price):
        if not price:
            print("Incorreto. O campo não deve estar vazio.")

        if not price.isdigit() or not (1 <= len(price) <= 13):
            print("Incorreto. Tamanho Incorreto.")

