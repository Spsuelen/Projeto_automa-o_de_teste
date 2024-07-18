class TitleValidator:
    @staticmethod
    def validate_title(title):
        if not title:
            print("Incorreto. O campo não deve estar vazio.")

        if not title.isalnum() or not (1 <= len(title) <= 20):
            print("Incorreto. Tamanho Incorreto.")

