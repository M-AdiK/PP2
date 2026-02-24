import re

with open ("raw.txt" , "r" , encoding = "utf-8") as f:
    text = f.readlines()

for i in range(len(text)):
    if text[i].strip() == "ИТОГО:":
        total = text[i + 1].strip()
        print("TOTAL:", total)

pay = "Не найдено"

for line in text:
    if "Банковская карта" in line:
        pay = "Банковская карта"
print("Способ оплаты:", pay)

for line in text:
    if line.strip().startswith("Время:"):
        date = line.strip().replace("Время:", "").strip()
        print("Дата и время:", date)