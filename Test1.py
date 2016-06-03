#print("122222222")
#import sys

#sys.stdin.encodin


# print('kim')
# print(40 * 2)
# print(43 // 2)
# print(round(2.6))

# def p_pp():
# 	pass


# utf-8 인코딩 파일 출력
# def p_file_print():
# 	try:
# 		with open('test.txt', 'r', encoding='utf-8') as t_fo:
# 			for t_ls in t_fo.readlines():				
# 				print(t_ls)
# 	except Exception as e:
# 		print(e)


# p_file_print()



'''
class open2(object):
	def __init__(self, path):
		print('initialize')
		self.file = open(path)
		#print(self.file)

	def __enter__(self):
		print('entered')
		return 'self.file'

	def __exit__(self, ext, exv, trb):
		print('exited')
		self.file.close()
		return True

	def aaa(self):
		print('read')
		return '파일 읽기를 구현해 주세요.'


with open2('test.txt') as t_fo:
	#s = t_fo.xxx()
	print(t_fo)
	pass
'''


''' 예외를 발생을 안함
class CFileOpen(object):
	def __init__(self, fp, fo):
		self._f = open(fp, mode=fo, encoding="utf-8")

	def __enter__(self):
		return self

	def __exit__(self, ext, exv, trb):
		return True

	def print(self):
		print('print')

	def readline(self):
		return self._f.readline()



try:
	with CFileOpen('test.txt', 'r') as t_fo:
		t_fo.print()
		print(t_fo.readline())
except Exception as e:
	print(e)
'''



'''
class CFileOpen(object):
	def __init__(self, fp, fo):
		self._f = open(fp, mode=fo, encoding="utf-8")

	def __enter__(self):
		return self

	def __exit__(self, ext, exv, trb):
		return True

	def print(self):
		print('print')

	def readline(self):
		return self._f.readline()



try:
	with open('test.txt', mode='r', encoding='utf-8') as t_fo:
		for t_sl in t_fo.readlines():
			print(t_sl)
except Exception as e:
	print(e)
'''



class CFileOpen(object):
	def __init__(self):
		pass

	def __enter__(self):
		return self

	def __exit__(self, ext, exv, trb):
		return True

	def get_offer(self):
		print('get_offer22222')



with CFileOpen() as t_fo:
	#print('t_fo.get_offer()')
	t_fo.get_offer()













