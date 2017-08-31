#!/usr/bin/env python32
# В данном виде работает для кодировки ANCI
# Скрипт для компоновки блоков текста и последующей
# нумерацией данных блоков. Разделение блоков происходит
# по условной строке "раздел"

file_source = open('source_file.txt')
file_result = open('result_file.txt','w')

n = 1 # счетчик нумерации блоков текста по умолчанию
type = 1 # флаг типа строки в блоке
			# 1 - первая в блоке нумеруется
			# 2 - обычная, не нумеруется

while True:
	s = file_source.readline()
	if not s: break
	if s not in("\n") and type == 1: # блок нумеруется
		file_result.write("\n" + str(n) + "." + "\n") # нумерация блока
		file_result.write(s) # 
		type = 2 # перевод флага - следующая строка будет обычная 
		n += 1 # счетчик нумерации блоков текста
		continue
	if s not in("\n") and type == 2 and "раздел" not in s: # обычная строка
		file_result.write(s) # просто записываем строку, без нумерации блока
		continue
	if "раздел" in s: # условие окончания блока
		type = 1 # переводим флаг типа строки снова на 1 для нумерации
		continue # граница блока, начинаем заново

file_result.write("\n" + "Всего блоков: " + str(n) + "n\")

file_result.close()
file_source.close()
