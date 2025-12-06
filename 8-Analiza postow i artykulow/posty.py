posts = []

import random

num_posts = 1024
main_ip_count = int(num_posts * 0.95)  
other_ip_count = num_posts - main_ip_count  

#losowy time stamp jakby co
current_time = 1700000000

# 95% głównego IP jakby co
for i in range(1, main_ip_count + 1):
    current_time += random.randint(1, 10)  # odstępy czasowe jakby co
    posts.append({"id": i, "ip": "10.47.83.12", "timestamp": current_time})

# inne ip jakby co
other_ips = ["192.168.1.55", "172.16.0.1", "10.0.0.5", "52.10.67.4"]
for i in range(main_ip_count + 1, num_posts + 1):
    current_time += random.randint(50, 500)  # większe odstępy dla innych ip żeby nie były obok siebie jakby co
    ip = random.choice(other_ips)
    posts.append({"id": i, "ip": ip, "timestamp": current_time})
