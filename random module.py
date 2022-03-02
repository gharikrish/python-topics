Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
print(dir(random))
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
random.random() #float(0.00 to 1.0)
0.6112608932320236
random.uniform(10,20)#float(10 to 20)
17.89240762390636
random.randint(10,20)#int
13
random.randrange(1,10,2)# start= 1,end = 10-1,step = [1,3,5,7,9]
3
random.randrange(0,10,2)# start= 1,end = 10-1,step = [1,3,5,7,9]
0
#choice
res = ['win','lose','draw']
random.choice(res)
'lose'
random.choice(res)
'draw'

random.choice(res)
'win'
# coices (more than 1 value)
color = ['green','red','black']
res= random.choices(color,k=6)# k is key
print(res)
['green', 'green', 'red', 'black', 'red', 'red']
res= random.choices(color,weights=[2,3,1],k=6)# k is key
print(res)
['red', 'red', 'red', 'red', 'red', 'red']
print(res)
['red', 'red', 'red', 'red', 'red', 'red']
print(res)
['red', 'red', 'red', 'red', 'red', 'red']
deck = list(range(1,53))
print(deck)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
random.shuffle(deck)

print(deck)
[37, 15, 30, 38, 45, 33, 18, 26, 32, 10, 51, 3, 5, 4, 12, 16, 34, 46, 22, 13, 7, 43, 29, 2, 11, 36, 19, 40, 23, 50, 20, 35, 47, 6, 42, 24, 25, 52, 9, 1, 31, 21, 14, 8, 28, 27, 39, 41, 44, 48, 17, 49]
random.sample(deck,k =10)
[44, 8, 43, 1, 15, 45, 10, 29, 17, 7]
#getrandbits
#k = 3 min =000=>0  max= 111=>7
random.getrandbits(3)
0
random.getrandbits(3)
2
random.getrandbits(4)
1
