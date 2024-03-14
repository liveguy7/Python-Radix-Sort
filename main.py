
def hold(a,pos):
  n = len(a)
  output = [0] * n
  count = [0] * 10
  for i in range(0,n):
    idx = a[i] // pos
    count[idx % 10] += 1
  for i in range(1,10):
    count[i] += count[i - 1]
  i = n - 1
  while(i >= 0):
    idx = a[i] // pos
    output[count[idx % 10] - 1] = a[i]
    count[idx % 10] -= 1
    i -= 1
  for i in range(0,n):
    a[i] = output[i]

def radixsort(a):
  maximum = max(a)
  pos = 1
  while(maximum // pos > 0):
    hold(a,pos)
    pos *= 10

col = [170, 45, 75, 90, 802, 24, 2, 66]
print(col)
radixsort(col)
print(col)




