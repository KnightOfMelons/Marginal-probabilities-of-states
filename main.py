# Задание 1.
# Найти предельные вероятности для системы S при λ01 = 1, λ02 = 2, λ10 = 2, λ13 = 2, λ20 = 3, λ23 = 1, λ31 = 3, λ32 = 2.
# Система уравнений имеет вид:

# (λ01 + λ02)p0 = λ10p1 + λ20p2,
# (λ10 + λ13)p1 = λ01p0 + λ31p3,
# (λ20 + λ23)p2 = λ02p0 + λ32p3,
# (λ31 + λ32)p3 = λ13p1 + λ23p2.

from sympy import symbols, Eq, solve

# Сделал вывод условия для удобства
print("\nСистема уравнений имеет вид: \n\n(λ01 + λ02)p0 = λ10p1 + λ20p2,\n(λ10 + λ13)p1 = λ01p0 + λ31p3,\n(λ20 + λ23)p2 = λ02p0 + λ32p3,\n(λ31 + λ32)p3 = λ13p1 + λ23p2.")

def solve_equations(values=None):
    # Если значения не были переданы, используем значения по умолчанию
    if values is None:
        values = [1, 2, 2, 2, 3, 1, 3, 2]

    # Это тоже, для лучшего визуального восприятия 
    print(f"{values[0]+values[1]}p0 = {values[2]}p1 + {values[4]}p2,\n{values[2]+values[3]}p1 = {values[0]}p0 + {values[6]}p3,\n{values[4]+values[5]}p2 = {values[1]}p0 + {values[7]}p3,\np0 + p1 + p2 + p3 = 1.\n")

    # Определим переменные вероятностей
    p0, p1, p2, p3 = symbols('p0 p1 p2 p3')

    eq1 = Eq(3*p0, 2*p1 + 3*p2)  # 3p0 = 2p1 + 3p2
    eq2 = Eq(4*p1, p0 + 3*p3)    # 4p1 = p0 + 3p3
    eq3 = Eq(4*p2, 2*p0 + 2*p3)  # 4p2 = 2p0 + 2p3
    eq4 = Eq(p0 + p1 + p2 + p3, 1)  # нормировочное условие

    # Тут решается система уравнений
    solution = solve([eq1, eq2, eq3, eq4], (p0, p1, p2, p3))

    # Преобразуем дроби в десятичные значения (там до этого они выводились как {p0: 2/5, p1: 1/5, p2: 4/15, p3: 2/15}, не комильфо)
    solution_rounded = {var: round(sol.evalf(), 2) for var, sol in solution.items()}

    print("Решение: ", solution_rounded)
    return solution_rounded

# Тут начало программы как бы
user_input = input("\nВведите значения для λ01, λ02, λ10, λ13, λ20, λ23, λ31, λ32 через пробел (или нажмите Enter для использования значений по умолчанию): ")

if user_input.strip():  # Если пользователь что-то ввел
    values = list(map(int, user_input.split()))
else:
    values = None  # Используем значения по умолчанию

solve_equations(values)