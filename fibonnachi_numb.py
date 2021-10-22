arr = []
n=70
def Fib(n):

  if arr[n] != -1:
    return arr[n]
  if n == 0:
    arr[0] = 0
    return 0 #base case 1
  elif n == 1:
    arr[1] = 1;
    return 1  #base case 2
  else:
    arr[n] = Fib(n-1) + Fib(n-2);
    return arr[n];

for i in range(n+1):
    arr.append(-1);
Fib(n)

def conditionalSum(value, condition):
    if condition == "even":
        return sum(i for i in arr if i % 2 == 0)
print(conditionalSum(arr, "even"))
