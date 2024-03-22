#pip install ortools

from ortools.linear_solver import pywraplp


def create_data_model():         #Funcion para crear nuestro modelo
    """Create the data for the example."""
    data = {}
    weights = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]   #Pesos
    data["weights"] = weights   #Creacion de distintas listas, para pesos, items, bins
    data["items"] = list(range(len(weights)))
    data["bins"] = data["items"]
    data["bin_capacity"] = 100   #Capacidad maxima
    return data



def main():   #Función principal
    data = create_data_model()   #Asignamos los datos

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:   #Verificación de creación del solver de manera correcta
        return

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data["items"]:
        for j in data["bins"]:
            x[(i, j)] = solver.IntVar(0, 1, "x_%i_%i" % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data["bins"]:
        y[j] = solver.IntVar(0, 1, "y[%i]" % j)

    # Constraints -> restricciones
    # Each item must be in exactly one bin.
    for i in data["items"]:
        solver.Add(sum(x[i, j] for j in data["bins"]) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data["bins"]:
        solver.Add(
            sum(x[(i, j)] * data["weights"][i] for i in data["items"])
            <= y[j] * data["bin_capacity"]
        )

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data["bins"]]))

    print(f"Solving with {solver.SolverVersion()}")   #Resolución del problema
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0
        for j in data["bins"]:  #Para mostrar los bins iterados en cada uno
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data["items"]:
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data["weights"][i]
                if bin_items:
                    num_bins += 1   #Mostrar los bins actuales
                    print("Bin number", j)
                    print("  Items packed:", bin_items)
                    print("  Total weight:", bin_weight)
                    print()
        print()
        print("Number of bins used:", num_bins)   #Numero de bins usados
        print("Time = ", solver.WallTime(), " milliseconds")   #Tiempo de ejecución
    else:
        print("The problem does not have an optimal solution.")  #Por si no hay solución optima


if __name__ == "__main__":   #Llamada de funcion principal
    main()
