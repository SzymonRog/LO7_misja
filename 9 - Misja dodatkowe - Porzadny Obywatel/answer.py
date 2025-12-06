
def find_best_tasks(tasks, max_time):
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
