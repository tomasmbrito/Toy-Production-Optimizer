from pulp import *

def max_profit():
    # Ler o input
    t, p, max_toys = map(int, input().split())
    toys = list(range(1, t+1))
    profits = {}
    limits = {}
    # Ler o lucro e a capacidade de produção de cada brinquedo
    for i in toys:
        li, ci = map(int, input().split())
        profits[i] = li
        limits[i] = ci
    packs = []
    pack_profits = {}
    # Ler o lucro de cada pacote especial
    for _ in range(p):
        i, j, k, lijk = map(int, input().split())
        packs.append((i, j, k))
        pack_profits[(i, j, k)] = lijk

    # Definir o problema de programação linear
    prob = LpProblem("Maximize_Profit", LpMaximize)
    toy_vars = LpVariable.dicts("Toy", toys, 0, None, LpInteger)
    pack_vars = LpVariable.dicts("Pack", packs, 0, None, LpInteger)

    # Função objetivo para maximizar o lucro
    prob += lpSum([profits[i]*toy_vars[i] for i in toys]) + lpSum([pack_profits[j]*pack_vars[j] for j in packs]), "Total Profit"

    # Restrições de produção
    prob += lpSum([toy_vars[i] for i in toys]) + 3*lpSum([pack_vars[j] for j in packs]) <= max_toys, "Max production limit"
    for i in toys:
        prob += toy_vars[i] <= limits[i], f"Max production limit for toy {i}"
        prob += toy_vars[i] + lpSum([pack_vars[j] for j in packs if i in j]) <= limits[i], f"Max production limit for toy {i} considering packs"

    # Resolver o problema
    prob.solve(PULP_CBC_CMD(msg=False))
    print(int(value(prob.objective)))

# Chamar a função
max_profit()
