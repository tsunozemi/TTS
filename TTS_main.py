import sys
from numpy import *

print("enter the num of input data")
data_num = int(input())

print("enter the num of result data")
result_num = int(input())

print("enter the num of pattern")
data_pattern = int(input())

data_table = [[0 for i in range(data_pattern)] for j in range(data_num + result_num)]
names = [0 for i in range(data_num + result_num)]

print(data_table)
print(names)

print("enter the name of input data")
for count in range(0, data_num):
	print("enter {}'s input data name".format(count + 1))
	names[count] = input()

print("enter the name of result data")
for count in range(data_num, data_num + result_num):
	print("enter {}'s result data name".format(count - data_num + 1))
	names[count] = input()

for num in range(0, data_num):
	print("enter {}'s input data".format(names[num]))
	for enter_count in range(0, data_pattern):
		buf = int(input())
		if int(buf) == 1:
			data_table[num][enter_count] = 1
		elif buf == 0:
			data_table[num][enter_count] = 0
		else:
			data_table[num][enter_count] = 'n'

for num in range(data_num, data_num + result_num):
	print("enter {}'s result data".format(names[num]))
	for enter_count in range(0, data_pattern):
		buf = int(input())
		if buf == 1:
			data_table[num][enter_count] = 1
		elif buf == 0:
			data_table[num][enter_count] = 0
		else:
			data_table[num][enter_count] = 'n'

print(data_table)
print(names)

for i in range(0, data_num + result_num):
	if i == data_num:
		print(" ", end = "")
	if i == data_num + result_num - 1:
		print(" _")
	else:
		print(" _", end = "")

for i in range(0, data_num + result_num):
	print("|", end = "")
	if i == data_num:
		print("|", end = "")
	print(names[i], end = "")

print("|")

for num in range(0, data_pattern):
	"""
	for i in range(0, data_num + result_num):
		if i == data_num + result_num - 1:
			print(" _")
		else:
			print(" _", end = "")
	"""
	#print(data_num + result_num)
	for i in range(0, data_num + result_num):
		print("|", end = "")
		if i == data_num:
			print("|", end = "")
		print(data_table[i][num], end = "")
		
	print("|")

for i in range(0, data_num + result_num):
	if i == data_num:
		print(" ", end = "")
	if i == data_num + result_num - 1:
		print(" ¯")
	else:
		print(" ¯", end = "")

print(names)
