class ValidadorExpense:
    @staticmethod
    def validate_duplicate_expense(new_expense_price, new_expense_title, new_expense_category):
        if (new_expense_price == new_expense_price and
                new_expense_title == new_expense_title and
                new_expense_category == new_expense_category):
            print("Não pode duplicar expenses já inseridos no aplicativo.")
        else:
            pass
