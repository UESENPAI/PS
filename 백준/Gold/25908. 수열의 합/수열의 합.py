from sys import stdin
input = stdin.readline

def boj25908():
    S, T = map(int, input().split())

    tau = [0] * (T + 1)
    spf = [0] * (T + 1)
    power = [0] * (T + 1)

    tau[1] = 1
    primes = []

    for i in range(2, T + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            tau[i] = 2
            power[i] = 1

        for p in primes:
            if p * i > T:
                break

            spf[p * i] = p

            if i % p == 0:
                power[p * i] = power[i] + 1
                tau[p * i] = tau[i] // (power[i] + 1) * (power[i] + 2)
                break
            else:
                power[p * i] = 1
                tau[p * i] = tau[i]<<1

    ans = 0

    for t in range(S, T + 1):
        if t & 1:
            ans -= tau[t]
        else:
            k = (t & -t).bit_length() - 1
            tau_m = tau[t] // (k + 1)
            ans += (k - 1) * tau_m

    print(ans)

if __name__ == '__main__': boj25908()