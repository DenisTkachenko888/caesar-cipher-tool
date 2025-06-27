eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Запрос направления
direction = input("Напишите 'Ш', если хотите зашифровать или 'Д', чтобы дешифровать текст: ").lower()
while direction not in ['ш', 'д']:  
    direction = input("Вы ввели неправильно. Напишите 'Ш', если хотите зашифровать или 'Д', чтобы дешифровать текст: ").lower()

# Запрос языка
language = input("Напишите 'ru', если хотите выбрать русский язык или 'en', чтобы выбрать английский язык: ").lower()
while language not in ['ru', 'en']:
    language = input("Вы ввели неправильно. Напишите 'ru', если хотите выбрать русский язык или 'en', чтобы выбрать английский язык: ").lower()

# Запрос шага сдвига
step = input("Выберите шаг сдвига (число): ")
while not step.isdigit():
    step = input("Вы ввели не число! Выберите шаг сдвига (число): ")
step = int(step)

# Запрос текста
text = input("Введите текст для шифрования/дешифрования: ")

def caesar(direction, language, step, text):
    if language == 'en':
        lower_alphabet = eng_lower_alphabet
        upper_alphabet = eng_upper_alphabet
    else:
        lower_alphabet = rus_lower_alphabet
        upper_alphabet = rus_upper_alphabet

    result = ""

    for char in text:
        if char in lower_alphabet:  # Работа с маленькими буквами
            alphabet = lower_alphabet
        elif char in upper_alphabet:  # Работа с большими буквами
            alphabet = upper_alphabet
        else:
            result += char  # Неалфавитные символы остаются без изменений
            continue

        index = alphabet.index(char)
        if direction == 'ш':  # Шифрование
            new_index = (index + step) % len(alphabet)
        else:  # Дешифрование
            new_index = (index - step) % len(alphabet)
        result += alphabet[new_index]

    return result

# Выполнение функции
output_text = caesar(direction, language, step, text)
print("Результат:", output_text)
