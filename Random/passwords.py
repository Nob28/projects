import secrets
import string
from passlib.pwd import genword





#----المعلومات المتطلبة
#اسم المستخدم
#الطول
#هل بيها احرف كبيرة او صغيرة
#هل بيها رموز
#ارقام

#----الكود
#متغير = انبوت (اسم\او..)
#احتمالبيت الخطء









def generate_password( username , length, letters, upper, digits, symbols):

    characters = ''

    if letters:
        characters += string.ascii_lowercase
    if upper:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation


    if not characters:
        return ValueError('Es muss mindestens ein Zeichentyp angegeben werden.')

    password = ''.join(secrets.choice(characters) for _ in range(length))
    print(f'password: {password} ')
    save_to_file(username, password, length, letters, upper, digits, symbols)



def save_to_file(username, password, length, letters, upper, digits, symbols):
    with open("user_credentials.txt", "a", encoding="utf-8") as file:
        file.write(f'Benutzernme: {username}\n')
        file.write(f'Passwortlänge: {length}\n')
        file.write(f'Enthält Buchstaben: {"Ja" if letters else "Nein"}\n')
        file.write(f'Enthält Großbuchstaben: {"Ja" if upper else "Nein"}\n')
        file.write(f'Enthält Ziffern: {"Ja" if digits else "Nein"}\n')
        file.write(f'Enthält Symbole: {"Ja" if symbols else "Nein"}\n')
        file.write('-------------\n')
    print ('Die Informationen werden in der Datei user_credentials.txt gespeichert')

def main ():

    username = input('Wie heißen Sie ?')
    print(f'hallo {username}')

    length = int (input('Geben Sie die gewünschte Passwortlänge ein:'))

    letters = input('Soll Ihr Passwort Kleinbuchstaben enthalten? (J) (N): ').strip() .lower() == 'j'
    upper = input('Soll Ihr Passwort Großbuchstaben enthalten? (J) (N): ').strip() .lower() == 'j'
    digits = input('Soll Ihr Passwort Zahlen enthalten? (J) (N): ').strip() .lower() == 'j'
    symbols = input('Soll Ihr Passwort Symbole enthalten? (J) (N) :').strip() .lower() == 'j'


    try:

        generate_password(username, length, letters, upper, digits, symbols)

    except ValueError as e:
        print(f"Es gab ein Problem: {e}")


if __name__ == '__main__':
    main()

