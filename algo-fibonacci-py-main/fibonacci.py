def fibonacci(n):
  fib = [0,1]
  if n <3 and n>0: return fib[n-1]
  if n <=0 : return False
  for x in range(2,n):
    fib.append(fib[x-1]+fib[x-2])
  return fib[-1] + fib[-2]


# print(fibonacci(11))
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(20))