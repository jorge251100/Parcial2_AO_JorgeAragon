#Probado en colabs

#pip install ortools

"""Solve a multiple knapsack problem using a MIP solver."""
from ortools.linear_solver import pywraplp


def main():   #Función principal
    #Definimos lo que son los datos del problema con los que trabajaremos
    data = {}
    data["weights"] = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    data["values"] = [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25]
    assert len(data["weights"]) == len(data["values"])   #Verificamos que haya coincidencias en parametros de los datos
    data["num_items"] = len(data["weights"])
    data["all_items"] = range(data["num_items"])

    data["bin_capacities"] = [100, 100, 100, 100, 100]
    data["num_bins"] = len(data["bin_capacities"])
    data["all_bins"] = range(data["num_bins"])

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")  #Creación del solver
    if solver is None:
        print("SCIP solver unavailable.")
        return

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data["all_items"]:
        for b in data["all_bins"]:
            x[i, b] = solver.BoolVar(f"x_{i}_{b}")

    # Constraints. -> Las restricciones
    # Each item is assigned to at most one bin.
    for i in data["all_items"]:
        solver.Add(sum(x[i, b] for b in data["all_bins"]) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data["all_bins"]:
        solver.Add(
            sum(x[i, b] * data["weights"][i] for i in data["all_items"])
            <= data["bin_capacities"][b]
        )

    # Objective.
    # Maximize total value of packed items.
    objective = solver.Objective()
    for i in data["all_items"]:
        for b in data["all_bins"]:
            objective.SetCoefficient(x[i, b], data["values"][i])
    objective.SetMaximization()

    print(f"Solving with {solver.SolverVersion()}")  #Imprime info del solver
    status = solver.Solve()   #Resuelve problema

    if status == pywraplp.Solver.OPTIMAL:         #Si se encuentra una solución optima
        print(f"Total packed value: {objective.Value()}")   #Imprime total de valores empaquetados
        total_weight = 0
        for b in data["all_bins"]:
            print(f"Bin {b}")
            bin_weight = 0
            bin_value = 0
            for i in data["all_items"]:
                if x[i, b].solution_value() > 0:
                    print(         #Empaquetados de acuerdo al bin actual
                        f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                    )
                    bin_weight += data["weights"][i]
                    bin_value += data["values"][i]
            print(f"Packed bin weight: {bin_weight}")
            print(f"Packed bin value: {bin_value}\n")
            total_weight += bin_weight
        print(f"Total packed weight: {total_weight}")   #Total de empaquetados
    else:
        print("The problem does not have an optimal solution.")   #Si no hay solución optima


if __name__ == "__main__":    #LLamada a función principal
    main()