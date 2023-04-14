def chiffrement_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''
    for lettre in message:
        if lettre in alphabet:
            index = alphabet.index(lettre)
            nouvel_index = (index + decalage) % 26
            message_chiffre += alphabet[nouvel_index]
        else:
            message_chiffre += lettre
    return message_chiffre
