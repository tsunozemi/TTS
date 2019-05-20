import re

class 7table(object):
	"""docstring for 7table"""
	def __init__(self, inputs = 0, results = 0, pattern = 0,input_names = "", \
		result_names = "", input_datas = "", results_datas = ""):

		self.inputs = inputs
		self.results = results
		self.pattern = pattern
		self.alldata = inputs + results
		
		self.input_names = re.split(",", input_names)
		self.result_names = re.split(",", result_names)
		self.names = self.input_names + self.results_names

		self.input_datas = re.split(",", input_names)
		self.result_datas = re.split(",", result_names)
		self.datas = [[self.input_datas] + [self.result_datas]


	def __del__(self):
		pass

	def tsbleplot(self):
		for i in range(0, self.alldata):
			if i == self.inputs:
				print(" ", end = "")
			if i == self.alldata - 1:
				print(" _")
			else:
				print(" _", end = "")

		for i in range(0, self.alldata):
			print("|", end = "")
			if i == self.inputs:
				print("|", end = "")
			print(self.names[i], end = "")

		print("|")

		for num in range(0, self.pattern):
			"""
			for i in range(0, data_num + result_num):
				if i == data_num + result_num - 1:
					print(" _")
				else:
					print(" _", end = "")
			"""
			#print(data_num + result_num)
			for i in range(0, self.alldata):
				print("|", end = "")
				if i == self.inputs:
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