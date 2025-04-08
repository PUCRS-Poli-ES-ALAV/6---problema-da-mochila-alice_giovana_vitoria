from fibonacci import fibo_rec, fibo_dp, memoized_fibo
from knapsack import knapsack_brute_force, knapsack_dp
import time

def generate_results_table():
    # Valores para teste de Fibonacci
    fib_values = [4, 8, 16, 32, 128, 1000, 10000]
    
    # Casos de teste da Mochila
    knapsack_cases = [
        {
            'name': 'Caso 1',
            'items': [
                (23, 92), (31, 57), (29, 49), (44, 68), (53, 60),
                (38, 43), (63, 67), (85, 84), (89, 87), (82, 72)
            ],
            'capacity': 165,
            'expected_selection': [0, 1, 2, 3, 5]  # Índices baseados em 0
        },
        {
            'name': 'Caso 2',
            'items': [
                (56, 50), (59, 50), (80, 64), (64, 46), (75, 50), (17, 5)
            ],
            'capacity': 190,
            'expected_selection': [0, 1, 4]  # Índices baseados em 0
        }
    ]
    
    print("TABELA DE COMPARAÇÃO DE RESULTADOS")
    print("=" * 80)
    
    # Resultados de Fibonacci
    print("\nIMPLEMENTAÇÕES DE FIBONACCI")
    print("-" * 80)
    print("n\tRecursivo\tDP\t\tMemoizado")
    print("-" * 80)
    
    for n in fib_values:
        # Recursivo
        start = time.time()
        try:
            if n <= 32:
                result_rec = fibo_rec(n)
                time_rec = time.time() - start
            else:
                result_rec = "N/A"
                time_rec = "N/A"
        except:
            result_rec = "Erro"
            time_rec = "N/A"
        
        # DP
        start = time.time()
        try:
            result_dp = fibo_dp(n)
            time_dp = time.time() - start
        except:
            result_dp = "Erro"
            time_dp = "N/A"
        
        # Memoizado
        start = time.time()
        try:
            result_memo = memoized_fibo(n)
            time_memo = time.time() - start
        except:
            result_memo = "Erro"
            time_memo = "N/A"
        
        print(f"{n}\t{result_rec}\t\t{result_dp}\t\t{result_memo}")
        print(f"Tempo:\t{time_rec}\t{time_dp}\t{time_memo}")
    
    # Resultados da Mochila
    print("\nIMPLEMENTAÇÕES DA MOCHILA")
    print("-" * 80)
    
    for case in knapsack_cases:
        print(f"\n{case['name']}")
        print("-" * 80)
        items = case['items']
        capacity = case['capacity']
        
        # Teste força bruta
        start = time.time()
        bf_value, bf_iterations, bf_selection = knapsack_brute_force(items, capacity)
        bf_time = time.time() - start
        
        # Teste programação dinâmica
        start = time.time()
        dp_value, dp_iterations, dp_selection = knapsack_dp(items, capacity)
        dp_time = time.time() - start
        
        print(f"Itens: {items}")
        print(f"Capacidade: {capacity}")
        print("\nForça Bruta:")
        print(f"Valor Máximo: {bf_value}")
        print(f"Itens Selecionados (índice 0): {sorted(bf_selection)}")
        print(f"Iterações: {bf_iterations}")
        print(f"Tempo: {bf_time:.6f} segundos")
        
        print("\nProgramação Dinâmica:")
        print(f"Valor Máximo: {dp_value}")
        print(f"Itens Selecionados (índice 0): {sorted(dp_selection)}")
        print(f"Iterações: {dp_iterations}")
        print(f"Tempo: {dp_time:.6f} segundos")
        
        print("\nSeleção Esperada (índice 0):", case['expected_selection'])
        print("-" * 80)

if __name__ == "__main__":
    generate_results_table() 