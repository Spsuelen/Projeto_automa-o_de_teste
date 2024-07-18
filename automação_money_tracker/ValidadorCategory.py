class CategoryValidator:
    @staticmethod
    def validate_category(category):
        if not category:
            print("Incorreto. O campo não deve estar vazio.")

        if not category.isalnum() or not (1 <= len(category) <= 30):
            print("Incorreto. Tamanho Incorreto.")

