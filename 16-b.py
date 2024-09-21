number = int(input("Enter number "))
prime_number = []
i_ = 1
while len(prime_number) < number:
    i_ += 1
    is_prime = True
    for i in range(2, int(i_ ** 0.5) + 1):
        if i_ % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_number.append(i_)
print(prime_number)