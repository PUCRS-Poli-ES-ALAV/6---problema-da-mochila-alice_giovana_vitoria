import time
from itertools import combinations

def knapsack_brute_force(items, capacity):
    n = len(items)
    max_value = 0
    iterations = 0
    best_combination = []
    
    # Testa todas as combinações possíveis
    for r in range(1, n + 1):
        for combo in combinations(items, r):
            iterations += 1
            total_weight = sum(item[0] for item in combo)
            total_value = sum(item[1] for item in combo)
            
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = combo
    
    return max_value, iterations, best_combination

def knapsack_dp(items, capacity):
    n = len(items)
    # Cria tabela DP com (n+1) linhas e (capacity+1) colunas
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    iterations = 0
    
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for j in range(1, capacity + 1):
            iterations += 1
            if weight <= j:
                dp[i][j] = max(dp[i-1][j], value + dp[i-1][j - weight])
            else:
                dp[i][j] = dp[i-1][j]
    
    # Reconstrói a solução
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(i-1)  # Índice baseado em 0
            j -= items[i-1][0]
        i -= 1
    
    return dp[n][capacity], iterations, selected_items

def test_knapsack():
    # Casos de teste
    test_cases = [
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
    
    print("Testando implementações da Mochila:")
    print("=" * 80)
    
    for case in test_cases:
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
    test_knapsack() 