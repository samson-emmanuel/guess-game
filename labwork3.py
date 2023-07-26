n = 22
if n % 2 != 0:
    print('First Weird')
elif n % 2 == 0 and n in range(2,6):
    print('First Not Weird')
elif n % 2 ==0 and n in range (6,21):
    print('Second Weird')
elif n % 2 == 0 and n > 20:
    print('Second Not Weird')