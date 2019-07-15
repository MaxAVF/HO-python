def prime_factors(n):
  factors=[]
  i=2
  while i*i<=n:
   #print(i,n)
   if (n%i==0):
    n=n//i
    factors.append(i)
    i=2
   else:
    i+=1
  factors.append(n) 
  return sorted(list(set(factors)))[-1]

print(prime_factors(600851475143))
