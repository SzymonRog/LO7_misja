from best_tasks import find_best_tasks
import random
from lista_zadan import tasks


def calc_points(tasks, max_time):
    tasks_with_ratio = []
    for task in tasks:
        task_copy = task.copy()
        task_copy['ratio'] = task['points'] / task['time']
        tasks_with_ratio.append(task_copy)

    tasks_with_ratio.sort(key=lambda x: x['ratio'], reverse=True)
    selected_tasks = []
    total_time = 0
    total_points = 0

    for task in tasks_with_ratio:
        if total_time + task['time'] <= max_time:
            selected_tasks.append(task)
            total_time += task['time']
            total_points += task['points']

    return total_points


def test():
    komunikat = ""
    try:
        random.seed()
        selected_random_tasks = random.sample(tasks, 10)

        max_time = random.randint(60, 180)
        user_answer = find_best_tasks(selected_random_tasks, max_time)
        correct_answer = calc_points(selected_random_tasks, max_time)

        if user_answer == correct_answer:
            komunikat += "Test {i + 1} passed!"
            print(komunikat)
            return False

        else:
            komunikat += f"Test {i + 1} failed!\n"
            komunikat += f"Expected: {correct_answer}"
            komunikat += f" Result: {user_answer}"
            print(komunikat)
            return True

    except:
        return False

n = 10
for i in range(n):
    test()