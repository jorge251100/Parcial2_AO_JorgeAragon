#Código probado en colabs

#pip install ortools       -> Para instalar la libreria

from ortools.algorithms.python import knapsack_solver


def main():  #Funcion principal
    # Create the solver. -> Instancia de clase
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    values = [  #Valores muestra que pueden entrar en la mochila
        # fmt:off
      360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
      78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
      87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
      312
        # fmt:on
    ]
    weights = [  #Los pesos de esos valores muestra
        # fmt: off
      [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
       42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
       3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13],
        # fmt: on
    ]
    capacities = [850]   #Cuanto le cabe a la mochila

    solver.init(values, weights, capacities)  #Inicializamos solver con parametros de valores, pesos y capacidades
    computed_value = solver.solve()  #manda a aplicar el solve, la solución optima

    packed_items = []  #Listas vacias para almacenar los valores que se van a empaquetar y sus pesos
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)  #Imprime el resultado o ese valor total que le cabe a la mochila
    for i in range(len(values)):          #En un for vemos cada valor para ver si si está empaquetado, si si lo metemos a la lista de empaquetados
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print("Total weight:", total_weight)  #Imprimos peso total, indice de cada valor y sus respectivos pesos
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)


if __name__ == "__main__":    #Para mandar a llamar a la función principal
    main()