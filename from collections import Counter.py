from collections import Counter

c = Counter()
c['red'] += 1
print(c)

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter()
for car in cars:
    c[car] += 1
 
print(c)
c = Counter(cars)
print(c)
print(c['black'])


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)

print(counter_moscow + counter_spb)

print(counter_moscow)
print(counter_spb)
counter_moscow.subtract(counter_spb)
print(counter_moscow)