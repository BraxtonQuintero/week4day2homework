# Exercise 1

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

new_places = list(filter(lambda x: x.strip(), places))
print(new_places)

# Exercise 2

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

new_authors = sorted(authors, key=lambda x: x.split()[-1].title())
print(new_authors)

# Exercise 3

places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

celsius = list(map(lambda x: (x[0],(x[1]*9/5)+32), places))
print(celsius)

# Exercise 4

def fib(num):
    if num in {0,1}:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


[fib(num) for num in range(7)]

n=7
for i in range(n):
    print(f"Iteration {i}: {fib(i)}")

# Exercise 5

def my_range(start, stop, step=-1):
    while start > stop:
        yield start
        start += step

for x in my_range(10, -1): 
    print(x**2)