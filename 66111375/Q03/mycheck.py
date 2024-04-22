#66111375 กฤษดา ขันตรี


from checknumber.checkevenoddprime import CheckEvenOddPrime

num_int = int(input("ใส่ตัวเลข: "))

check_even_odd_prime = CheckEvenOddPrime(num_int)

print(f"{num_int} -> {check_even_odd_prime.result}")

check_even_odd_prime.is_even()
print(f"{num_int} -> {check_even_odd_prime.result}")

check_even_odd_prime.is_odd()
print(f"{num_int} -> {check_even_odd_prime.result}")

check_even_odd_prime.is_prime()
print(f"{num_int} -> {check_even_odd_prime.result}")
