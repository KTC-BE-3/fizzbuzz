for i in range(1, 21):
    if i % 15 == 0:
        print('fizz buzz')
    elif i % 3 == 0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
