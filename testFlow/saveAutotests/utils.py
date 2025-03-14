def clean_code(raw_code):
    """
    Преобразует строку с escape-последовательностями в читаемый код.
    Заменяет \r\n и \n на символы новой строки.
    """
    # Заменяем \r\n на \n (унифицируем символы новой строки)
    cleaned_code = raw_code.replace('\r\n', '\n')
    return cleaned_code 