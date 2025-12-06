from posty import posts

def find_suspicious_ip(posts, time_threshold):
    ip_groups = {} #grupowanie postów po ip okej?
    for p in posts:
        ip_groups.setdefault(p["ip"], []).append(p)

    total_posts = len(posts)
    max_ip = None
    max_count = 0

    for ip, group in ip_groups.items():
        group.sort(key=lambda x: x["timestamp"]) #sortowanie postów po czasie spoko?

        current_chain = 1
        posts_count = 0

        for i in range(1, len(group)):
            if group[i]["timestamp"] - group[i-1]["timestamp"] < time_threshold:
                current_chain += 1
            else:
                if current_chain > 1:
                    posts_count += current_chain
                current_chain = 1

        if current_chain > 1:
            posts_count += current_chain

        if posts_count > max_count:
            max_count = posts_count
            max_ip = ip

    percent = (max_count / total_posts) * 100
    return max_ip, percent

time_threshold = 11 # próg czasowy jakby co?
ip, percent = find_suspicious_ip(posts, time_threshold)
#chyba wyniki?
print(find_suspicious_ip(posts, time_threshold))