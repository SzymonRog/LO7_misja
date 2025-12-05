import random

random.seed()
selected_random_tasks = random.sample(tasks, 10)


max_time = random.randint(60, 180)

tasks_with_ratio = []
for task in selected_random_tasks:
    task_copy = task.copy()
    task_copy['ratio'] = task['points'] / task['time']
    tasks_with_ratio.append(task_copy)

tasks_with_ratio.sort(key=lambda x: x['ratio'], reverse=True)

max_time = 180
selected_tasks = []
total_time = 0
total_points = 0

for task in tasks_with_ratio:
    if total_time + task['time'] <= max_time:
        selected_tasks.append(task)
        total_time += task['time']
        total_points += task['points']


print(f"Punkty={total_points}")
