# storage_calc.py
# Вариант 23
bytes_value = 2560
kilobytes = bytes_value / 1024
megabytes = bytes_value / (1024 ** 2)
print(f"Байты (DEC): {bytes_value}")
print(f"Байты (BIN): {bin(bytes_value)}")
print(f"Байты (HEX): {hex(bytes_value)}")
print(f"Килобайты (KB): {kilobytes}")
print(f"Мегабайты (MB): {megabytes}")
