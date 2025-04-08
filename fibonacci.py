import time

def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_dp(n):
    if n <= 1:
        return n
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def memoized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n)

def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n-1) + lookup_fibo(f, n-2)
    return f[n]

def test_fibonacci():
    # Valores para teste
    test_values = [4, 8, 16, 32, 128, 1000, 10000]
    
    print("Testando implementações de Fibonacci:")
    print("n\tRecursivo\tDP\t\tMemoizado")
    print("-" * 50)
    
    for n in test_values:
        # Teste recursivo
        start = time.time()
        try:
            if n <= 32:  # Recursivo é muito lento para valores maiores
                result_rec = fibo_rec(n)
                time_rec = time.time() - start
            else:
                result_rec = "N/A"
                time_rec = "N/A"
        except:
            result_rec = "Erro"
            time_rec = "N/A"
            
        # Teste DP
        start = time.time()
        try:
            result_dp = fibo_dp(n)
            time_dp = time.time() - start
        except:
            result_dp = "Erro"
            time_dp = "N/A"
            
        # Teste memoizado
        start = time.time()
        try:
            result_memo = memoized_fibo(n)
            time_memo = time.time() - start
        except:
            result_memo = "Erro"
            time_memo = "N/A"
            
        print(f"{n}\t{result_rec}\t\t{result_dp}\t\t{result_memo}")
        print(f"Tempo:\t{time_rec}\t{time_dp}\t{time_memo}")

if __name__ == "__main__":
    test_fibonacci() 