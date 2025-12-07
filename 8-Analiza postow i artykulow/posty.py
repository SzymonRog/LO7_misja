import random

def gen_posts():
    posts = []

    num_posts = 1024
    main_ip_count = int(num_posts * 0.95)
    other_ip_count = num_posts - main_ip_count


    current_time = 1765078020

    # 95% głównego IP
    for i in range(1, main_ip_count + 1):
        current_time += random.randint(1, 11)
        posts.append({"id": i, "ip": "89.74.152.23", "timestamp": current_time})

    # inne ip
    other_ips = [
        "148.23.91.204",
        "54.118.33.77",
        "89.201.14.66",
        "23.17.144.92",
        "133.51.72.10",
        "204.66.190.8",
        "77.34.199.152",
        "162.44.18.203",
        "91.130.47.221",
        "185.72.11.94",
        "64.199.120.33",
        "139.167.45.188",
        "82.14.200.57",
        "34.76.91.210",
        "201.33.17.145",
        "157.190.72.44",
        "45.12.98.200",
        "118.54.7.101",
        "216.77.22.19",
        "67.143.210.88",
        "104.55.19.166",
        "92.47.188.131",
        "142.33.77.210",
        "38.11.249.60",
        "120.67.188.29"
    ]
    for i in range(main_ip_count + 1, num_posts + 1):
        current_time += random.randint(-36000, 36000)
        ip = random.choice(other_ips)
        posts.append({"id": i, "ip": ip, "timestamp": current_time})

    return posts
