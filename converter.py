# Файл: converter.py
# Автор: Иванов Илья, ИТ-12
# Конвертер систем счисления

print("КОНВЕРТЕР СИСТЕМ СЧИСЛЕНИЯ")

while True:
    print("\n" + "=" * 30)
    print("Выберите исходную систему:")
    print("1 - Десятичная (DEC)")
    print("2 - Двоичная (BIN)")
    print("3 - Шестнадцатеричная (HEX)")
    print("0 - Выход")
    
    try:
        mode_choice = int(input("Ваш выбор (0-3): "))
    except ValueError:
        print("Ошибка: введите число от 0 до 3")
        continue
    
    if mode_choice == 0:
        print("Завершение работы.")
        break
    
    if mode_choice not in [1, 2, 3]:
        print("Ошибка: введите число от 0 до 3")
        continue
    
    if mode_choice == 1:
        mode = 'dec'
    elif mode_choice == 2:
        mode = 'bin'
    else:
        mode = 'hex'
    
    number_str = input("Введите число: ").strip().upper()
    
    try:
        if mode == 'dec':
            dec_number = int(number_str)
            print(f"BIN: {bin(dec_number)[2:]}")
            print(f"HEX: {hex(dec_number)[2:].upper()}")
            
        elif mode == 'bin':
            if number_str.startswith('0B'):
                number_str = number_str[2:]
            dec_number = int(number_str, 2)
            print(f"DEC: {dec_number}")
            print(f"HEX: {hex(dec_number)[2:].upper()}")
            
        elif mode == 'hex':
            if number_str.startswith('0X'):
                number_str = number_str[2:]
            dec_number = int(number_str, 16)
            print(f"DEC: {dec_number}")
            print(f"BIN: {bin(dec_number)[2:]}")
            
    except ValueError:
        print(f"Ошибка: некорректное число для системы {mode}")
    except Exception as e:
        print(f"Ошибка: {e}")
