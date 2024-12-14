def print_numbers(M, N, K):
    result = []
    if K == 0:
        return result
    if M <= N:
        i = M
        while i <= N:
            result.append(i)
            i += abs(K) + 1
    else:
        i = M
        while i >= N:
            result.append(i)
            i -= abs(K) + 1
    return result

inputs = [50, 100, 7]
M, N, K = inputs
print(print_numbers(M, N, K))

print(print_numbers(15, 5, 2))  
print(print_numbers(25, 50, 4)) 
print(print_numbers(15, 100, -2)) 
print(print_numbers(0, 0, 2))    
print(print_numbers(200, 200, 50))
