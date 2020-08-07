import random
start = input('請輸入起始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
ans = random.randint(start, end)
x = 0
while True:
	x += 1
	input_ans = input('請輸入數字: ')
	input_ans = int(input_ans)
	if input_ans == ans:
		print('恭喜!你猜對了!', '(你一共猜了', x, '次)')
		break
	elif input_ans > ans:
		print('比答案大喔!', '(你目前猜了', x, '次)')
	elif input_ans < ans:
		print('比答案小喔!', '(你目前猜了', x, '次)')
	#else:
		#if input_ans > ans:
			#print('你猜得比答案大喔!', '(你目前猜了', x, '次)')
		#else:
			#print('你猜得比答案小喔!', '(你目前猜了', x, '次)')