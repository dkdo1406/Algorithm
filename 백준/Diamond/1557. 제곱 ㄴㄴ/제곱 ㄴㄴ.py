import math
K = int(input())

def find_prime(K):
    global curr_cnt
    prime = []
    bef_cnt = 0
    curr_cnt = 0
    move = int(math.sqrt(K))
    prime_arr = [True] * (move + 1)
    for i in range(2, move + 1):
        if prime_arr[i]:
            prime.append(i)
            for j in range(i * i, move + 1, i):
                prime_arr[j] = False

    def fact(result, r, count):
        global curr_cnt
        if count % 2 == 0:
            curr_cnt -= (K // result)
        else:
            curr_cnt += (K // result)

        for i in range(r+1, len(prime)):
            if result * (prime[i] ** 2) > K:
                return
            fact(result * (prime[i] ** 2), i, count + 1)

    while True:
        k_prime = int(math.sqrt(K))
        move = k_prime - move
        prime_arr += [True] * (move + 1)
        bef_prime = k_prime - move
        
        for i in prime:
            for j in range(i + bef_prime - (bef_prime % i), k_prime + 1, i):
                prime_arr[j] = False
        for i in range(bef_prime+1, k_prime + 1):
            if prime_arr[i]:
                prime.append(i)
                for j in range(i * i, k_prime + 1, i):
                    prime_arr[j] = False

        curr_cnt = 0
        for i in range(len(prime)):
            fact(prime[i] ** 2, i, 1)

        if curr_cnt != bef_cnt:
            move = k_prime
            K += curr_cnt - bef_cnt
            bef_cnt = curr_cnt
        else:
            return K
print(find_prime(K))


