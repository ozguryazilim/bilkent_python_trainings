fibo = [0, 1]

n = 2
while n < 500:
	fibo.insert(n, fibo[n-1] + fibo[n-2])
	n += 1

print(fibo)