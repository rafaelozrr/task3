def fib_number(num):
    first_fb = 1
    second_fb = 1

    for i in range(num - 2):
        sum = first_fb + second_fb
        first_fb = second_fb
        second_fb = sum
        i += 1
    print("Значение =", second_fb)
fib_number(6)