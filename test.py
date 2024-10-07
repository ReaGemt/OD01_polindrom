import unicodedata


def is_palindrome(s):
    # 1. Преобразуем строку в нижний регистр, чтобы не учитывать регистр символов.
    s = s.lower()

    # 2. Нормализуем строку для поддержки символов Unicode.
    s = unicodedata.normalize('NFKD', s)

    # 3. Удаляем из строки все пробелы и специальные символы, оставляя только буквы и цифры.
    s = ''.join(char for char in s if char.isalnum())

    # 4. Проверяем, является ли строка пустой после удаления символов.
    if not s:
        return False

    # 5. Сравниваем строку с её перевёрнутым вариантом, используя цикл для поэтапной проверки.
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    # 6. Если все символы совпадают, возвращаем True (это палиндром).
    return True


# Пример использования
test_strings = [
    "A man, a plan, a canal, Panama",
    "Hello",
    "",
    "Казак",
    "А роза упала на лапу Азора"
]

# Выводим результаты для тестовых строк
for string in test_strings:
    result = is_palindrome(string)
    print(f"Строка '{string}' является палиндромом: {result}")
