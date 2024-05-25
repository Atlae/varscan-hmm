import math

def parse_input(input: str) -> tuple[str, list[str], list[str], 
        dict[str, dict[str, float]], dict[str, dict[str, float]]]:
    """Parses a file into the path, alphabet, possible states, transition 
    matrix, and emission matrix.

    Args:
        input (str): file with each section partitioned by "--------"

    Returns: tuple[
            str,                            (Path)                  \n
            list[str],                      (Alphabet)              \n
            list[str],                      (States)                \n
            dict[str, dict[str, float]],    (Transmission Matrix)   \n
            dict[str, dict[str, float]]     (Emission Matrix)        ]
    """
    
    path: str
    alphabet: str
    states: str
    matrix1: str
    matrix2: str

    # splitting up the input file into their own sections
    path, alphabet, states, matrix1, matrix2 = [
        x.strip() for x in input.split("--------\n")
    ]

    # initializing the transmission matrix with the states
    transmission_matrix: dict[str, dict[str, float]] = {
        key: {} for key in states.split()
    }
    
    # parsing matrix1 and populating the transmission matrix with probabilities
    for row in matrix1.split("\n")[1:]:
        cells = row.split("\t")
        for i, key in enumerate(states.split(), 1):
            transmission_matrix[cells[0]][key] = float(cells[i])
    
    # initializing the emission matrix with the states
    emission_matrix: dict[str, dict[str, float]] = {
        key: {} for key in states.split()
    }

    # parsing matrix2 and populating the emission matrix with probabilities 
    for row in matrix2.split("\n")[1:]:
        cells = row.split("\t")
        for i, key in enumerate(alphabet.split(), 1):
            emission_matrix[cells[0]][key] = float(cells[i])
    
    return (path, alphabet.split(), states.split(), 
            transmission_matrix,  emission_matrix)

def viterbi(input: str) -> str:
    """Runs the Viterbi Algorithm

    Args:
        input (str): File containing the path, alphabet, states, transition
        matrix, and emission matrix.

    Returns:
        str: The most probable sequence of states given the path.
    """
    path, alphabet, states, transmission_matrix, emission_matrix = parse_input(input)
    n: int = len(states) # 2
    T: int = len(path) # 5
    table: list[list[float]] = [[] * T] * n
    backpointer: list[list[int]] = [[] * T] * n

    # fill in first column with log(1/n * b_i0)
    for i in range(n):
        table[i] = [
            math.log(emission_matrix[states[i]][path[0]]) - math.log(n)
            if emission_matrix[states[i]][path[0]] != 0 else float("-inf")
        ]
        backpointer[i] = []

    # fill in the rest of the table with
    # max_i{table[i][t-1] + log(a_ij)} + log(b_{j,o_t})
    for t in range(1, T):
        for j in range(n):
            prev_column = [
                table[i][t-1] + math.log(transmission_matrix[states[i]][states[j]])
                if transmission_matrix[states[i]][states[j]] != 0 else float("-inf")
                for i in range(n)
            ]
            max_prob = max(prev_column)
            max_prob_index = prev_column.index(max_prob)
            table[j].append(
                max_prob + math.log(emission_matrix[states[j]][path[t]])
                if emission_matrix[states[j]][path[t]] != 0 else float("-inf")
            )
            backpointer[j].append(max_prob_index)

    # find the max probability in the last column
    max_prob = max(table[i][-1] for i in range(n))
    max_prob_index = [table[i][-1] for i in range(n)].index(max_prob)

    # backtrack to find the most likely sequence of hidden states
    hidden_states = [max_prob_index]
    for t in range(T-2, -1, -1):
        hidden_states.append(backpointer[hidden_states[-1]][t])
    hidden_states.reverse()
    return "".join(states[i] for i in hidden_states)

if __name__ == "__main__":
    with open(r"example/dataset_34596_7.txt") as f:
        print(viterbi(f.read()))
