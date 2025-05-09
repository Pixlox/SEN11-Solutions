def recamanSequence(N):
    if N <= 0:
        return []

    sequence = [0] * N
    sequence[0] = 1
    seen = {1}

    for n in range(2, N + 1):
        A = sequence[n - 2] - n
        if A > 0 and A not in seen:
            sequence[n - 1] = A
        else:
            sequence[n - 1] = sequence[n - 2] + n
        seen.add(sequence[n - 1])

    return sequence

N = int(input("Enter an integer N: "))

sequence = recamanSequence(N)
print(f"The first {N} terms of Recaman's sequence are: {sequence}")