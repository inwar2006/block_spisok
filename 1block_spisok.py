#!/usr/bin/env python32

file_source = open('source_file.txt')
file_result = open('result_file.txt','w')

n = 1 # 
type = 1 # 
			# 1
			# 2 

while True:
	s = file_source.readline()
	if not s: break
	if s not in("\n") and type == 1: # 
		file_result.write("\n" + str(n) + "." + "\n") # 
		file_result.write(s) # 
		type = 2 # 
		n += 1 # 
		continue
	if s not in("\n") and type == 2 and "razdel" not in s: # 
		file_result.write(s) # 
		continue
	if "razdel" in s: # 
		type = 1 # 
		continue # 

file_result.write("\n" + "Total: " + str(n))

file_result.close()
file_source.close()
