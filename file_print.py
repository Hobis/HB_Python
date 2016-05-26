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
def p_file_print():
	try:
		with open('test.txt', 'r', encoding='utf-8') as t_fo:
			for t_ls in t_fo.readlines():				
				print(t_ls)
	except Exception as e:
		print(e)


p_file_print()





