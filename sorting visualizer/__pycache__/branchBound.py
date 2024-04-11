import sys

def branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    unassigned = list(range(n))
    assignment = [-1] * n
    min_cost = sys.maxsize

    def calculate_cost(assignment):
        total_cost = 0
        for club, student in enumerate(assignment):
            total_cost += cost_matrix[club][student]
        return total_cost

    def backtrack(assignment, current_cost):
        nonlocal min_cost
        if not unassigned:
            if current_cost < min_cost:
                min_cost = current_cost
            return
        for i in unassigned:
            assignment[len(assignment) - len(unassigned)] = i
            new_cost = calculate_cost(assignment)
            if new_cost < min_cost:
                unassigned.remove(i)
                backtrack(assignment, new_cost)
                unassigned.append(i)

    backtrack(assignment, 0)

    return min_cost, assignment


n = int(input("Enter the number of students/clubs: "))
cost_matrix = []
print("Enter the cost matrix (separated by space or comma):")
for i in range(n):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

min_cost, assignment = branch_and_bound(cost_matrix)
print(f"Minimum Cost: {min_cost}")
print("Assignment:")
for club, student in enumerate(assignment):
    print(f"Club {club + 1} -> Student {student + 1}")

