# Задание 1.
# Найти предельные вероятности для системы S при λ01 = 1, λ02 = 2, λ10 = 2, λ13 = 2, λ20 = 3, λ23 = 1, λ31 = 3, λ32 = 2.
# Система уравнений имеет вид:

# (λ01 + λ02)p0 = λ10p1 + λ20p2,
# (λ10 + λ13)p1 = λ01p0 + λ31p3,
# (λ20 + λ23)p2 = λ02p0 + λ32p3,
# (λ31 + λ32)p3 = λ13p1 + λ23p2.

from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt

# Эта функция для сравнений значений D и D1 в конце (сделал максимально просто).
def plot_comparison(D_values):
    labels = ['D', 'D_1']
    values = [D_values[0], D_values[1]]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['blue', 'green'])
    plt.ylabel('Значение')
    plt.title('Сравнение значений D и D_1')
    plt.show()

# Сделал вывод услови, которое чуть выше для удобства восприятия пользователю
print("\nСистема уравнений имеет вид: \n\n(λ01 + λ02)p0 = λ10p1 + λ20p2,\n(λ10 + λ13)p1 = λ01p0 + λ31p3,\n(λ20 + λ23)p2 = λ02p0 + λ32p3,\n(λ31 + λ32)p3 = λ13p1 + λ23p2.")

def first_task(values=None, print_text_hepler=False):
    # Если значения не были переданы, используем значения по умолчанию
    if values is None:
        values = [1, 2, 2, 2, 3, 1, 3, 2]

    if print_text_hepler == True:
        # Это тоже, для лучшего визуального восприятия 
        print(f"\n{values[0]+values[1]}p0 = {values[2]}p1 + {values[4]}p2,\n{values[2]+values[3]}p1 = {values[0]}p0 + {values[6]}p3,\n{values[4]+values[5]}p2 = {values[1]}p0 + {values[7]}p3,\np0 + p1 + p2 + p3 = 1.\n")

    # Определим переменные вероятностей
    p0, p1, p2, p3 = symbols('p0 p1 p2 p3')

    # На всякий случай записал сюда значения для лямбд (нужно ещё для задания 2)
    lmbd01 = values[0]
    lmbd02 = values[1]
    lmbd10 = values[2]
    lmbd13 = values[3]
    lmbd20 = values[4]
    lmbd23 = values[5]
    lmbd31 = values[6]
    lmbd32 = values[7]

    eq1 = Eq((values[0]+values[1])*p0, (values[2])*p1 + (values[4])*p2)  # 3p0 = 2p1 + 3p2
    eq2 = Eq((values[2]+values[3])*p1, (values[0])*p0 + (values[6])*p3)    # 4p1 = p0 + 3p3
    eq3 = Eq((values[4]+values[5])*p2, (values[1])*p0 + (values[7])*p3)  # 4p2 = 2p0 + 2p3
    eq4 = Eq(p0 + p1 + p2 + p3, 1)  # нормировочное условие


    # Тут решается система уравнений
    solution = solve([eq1, eq2, eq3, eq4], (p0, p1, p2, p3))


    # Преобразуем дроби в десятичные значения (там до этого они выводились как {p0: 2/5, p1: 1/5, p2: 4/15, p3: 2/15}, не комильфо)
    solution_rounded = {var: round(sol.evalf(), 2) for var, sol in solution.items()}

    # Сделал в таком виде, чтобы было удобнее. Почему-то через .get() не находились значения в словаре.
    p0 = solution_rounded[p0]
    p1 = solution_rounded[p1]
    p2 = solution_rounded[p2]
    p3 = solution_rounded[p3]

    # Лямбды нужны для задания 2
    return p0, p1, p2, p3, lmbd01, lmbd02, lmbd10, lmbd13, lmbd20, lmbd23, lmbd31, lmbd32

# Задание 2.
# Найти средний чистый доход от эксплуатации в стационарном режиме системы S в условиях предыдущего примера. Если известно, что
# в единицу времени исправная работа первого и второго узлов приносит доход соответственно в 10 и 6 ден. ед., а их ремонт требует
# затрат соответственно в 4 и 2 ден. ед. Оценить экономическую эффективность имеющейся возможности уменьшения вдвое среднего ремонта
# каждого из двух узлов, если при этом придется вдвое увеличить затраты на ремонт каждого узла (в единицу времени).

def second_task(solution_rounded_values, print_text_hepler=False, first_node_income = 10, second_node_income = 6, first_node_repairing = 4, second_node_repairing = 2):
    # Чуть выше в аргументах функции я передал значения по умолчанию для first_node_income, second_node_income, first_node_repairing, second_node_repairing.
    # Там в лекционных материалах были указаны именно эти числа. Это которые: "Если известно, что в единицу времени исправная
    # работа первого и второго узлов приносит доход соответственно в 10 (это у меня first_node_income) и 6 (это second_node_income) ден. ед., а их ремонт
    # требует затрат соответственно в 4 (это first_node_repairing) и 2 (second_node_repairing) ден. ед."
    # Если нужно, то можно и сделать эти параметры запрашиваемыми от пользователя, но я пока что оставил так. 
    
    # p0 = 0.40, p1 = 0.20, p2 = 0.27, p3 = 0.13.
    first_node = solution_rounded_values[0] + solution_rounded_values[2]
    second_node = solution_rounded_values[0] + solution_rounded_values[1]
    first_node_in_repair = solution_rounded_values[1] + solution_rounded_values[3]
    second_node_in_repair = solution_rounded_values[2] + solution_rounded_values[3]

    # Д = 8.18 ден. ед.
    D = (first_node * first_node_income) + (second_node * second_node_income) - (first_node_in_repair * first_node_repairing) - (second_node_in_repair * second_node_repairing)
    
    if print_text_hepler == True:
        print(f"Д = {first_node} * {first_node_income} + {second_node} * {second_node_income} - {first_node_in_repair} * {first_node_repairing} - {second_node_in_repair} * {second_node_repairing} = {D} ден. ед.")

    # Интенсивности потоков событий равны (λ10 = 4, λ20 = 6, λ31 = 6, λ32 = 4):
    lmbd10 = solution_rounded_values[6] * 2
    lmbd20 = solution_rounded_values[8] * 2
    lmbd31 = solution_rounded_values[10] * 2
    lmbd32 = solution_rounded_values[11] * 2

    # Остальные остаются прежними
    lmbd01 = solution_rounded_values[4]
    lmbd02 = solution_rounded_values[5]
    lmbd13 = solution_rounded_values[7]
    lmbd23 = solution_rounded_values[9]

    if print_text_hepler == True:
        # Это тоже, для лучшего визуального восприятия 
        print(f"\n{lmbd01 + lmbd02}p0 = {lmbd10}p1 + {lmbd20}p2,\n{lmbd10 + lmbd13}p1 = {lmbd01}p0 + {lmbd31}p3,\n{lmbd20 + lmbd23}p2 = {lmbd02}p0 + {lmbd32}p3,\np0 + p1 + p2 + p3 = 1.")


    # Тут также, как и в прошлой функции first_task решается
    p0, p1, p2, p3 = symbols('p0 p1 p2 p3')

    eq1 = Eq((lmbd01 + lmbd02)*p0, (lmbd10)*p1 + (lmbd20)*p2) # 3p0 = 4p1 + 6p2, 
    eq2 = Eq((lmbd10 + lmbd13)*p1, (lmbd01)*p0 + (lmbd31)*p3) # 6p1 = p0 + 6p3,   
    eq3 = Eq((lmbd20 + lmbd23)*p2, (lmbd02)*p0 + (lmbd32)*p3) # 7p2 = 2p0 + 4p3, 
    eq4 = Eq(p0 + p1 + p2 + p3, 1)  # нормировочное условие

    # Тут решается система уравнений
    solution = solve([eq1, eq2, eq3, eq4], (p0, p1, p2, p3))

    solution_rounded = {var: round(sol.evalf(), 2) for var, sol in solution.items()}

    # Решив систему, получим вероятность сост.
    p0 = solution_rounded[p0] # p0 = 0.6
    p1 = solution_rounded[p1] # p1 = 0.15
    p2 = solution_rounded[p2] # p2 = 0.12
    p3 = solution_rounded[p3] # p3 = 0.05

    first_node_2 = p0 + p2
    second_node_2 = p0 + p1
    first_node_in_repair_2 = p1 + p3
    second_node_in_repair_2 = p2 + p3

    first_node_repairing = first_node_repairing * 2 # Затраты на ремонт первого = 8
    second_node_repairing = second_node_repairing * 2 # Затраты на ремонт второго = 4

    D_1 = (first_node_2 * first_node_income) + (second_node_2 * second_node_income) - (first_node_in_repair_2 * first_node_repairing) - (second_node_in_repair_2 * second_node_repairing)

    if print_text_hepler == True:
        print(f"\nД1 = {first_node_2} * {first_node_income} + {second_node_2} * {second_node_income} - {first_node_in_repair_2} * {first_node_repairing} - {second_node_in_repair_2} * {second_node_repairing} = {D_1} ден. ед.")

    return D, D_1



# Тут начало программы как бы. Значения по умолчанию - 1 2 2 2 3 1 3 2
user_input = input("\nВведите значения для λ01, λ02, λ10, λ13, λ20, λ23, λ31, λ32 через пробел (или нажмите Enter для использования значений по умолчанию): ")

if user_input.strip():  # Если пользователь что-то ввел
    values = list(map(int, user_input.split()))
else:
    values = None  # Используем значения по умолчанию

# Запоминаю все значения из Задания 1 для использования их в Задании 2.

values_for_tasks = first_task(values, print_text_hepler=True)


print(f"==== Решение 1 задания ====\n\np0 = {values_for_tasks[0]}, p1 = {values_for_tasks[1]}, p2 = {values_for_tasks[2]}, p3 = {values_for_tasks[3]}.\n") 

print("==== Решение 2 задания ====\n")

D_values = second_task(values_for_tasks, print_text_hepler=True)

if D_values[1] > D_values[0]:
    print(f"\nТак как Д1 больше Д примерно на {((D_values[1] - D_values[0])/D_values[0]) * 100} %, то экономическая целесообразность ускорения ремонтов узлов очевидна.\n")
elif D_values[0] > D_values[1]:
    print(f"\nТак как Д больше Д1 примерно на {((D_values[0] - D_values[1])/D_values[1]) * 100} %, то экономическая целесообразность ускорения ремонтов узлов НЕ ОЧЕВИДНА.")
else:
    print('Д1 и Д равны друг другу, либо что-то пошло не так...')

choose = int(input("\nНужно ли рисовать диаграмму для сравнения?\n1 - Нарисовать\n2 - Нет\nВаш выбор: "))
if choose == 1:
    # Функция, которая вызывает отрисовку диаграммы 
    plot_comparison(D_values)
else:
    pass   
