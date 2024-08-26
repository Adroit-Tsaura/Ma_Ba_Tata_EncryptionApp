# CeaserCipher class
class CeaserCipher:

    @staticmethod
    def encrypt(key, message):
        LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num + key
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)

                translated = translated + LETTERS[int(num)]
            else:
                translated = translated + symbol
        return translated

    @staticmethod
    def decrypt(key, message):
        LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key

                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)

                translated = translated + LETTERS[int(num)]
            else:
                translated = translated + symbol
        return translated