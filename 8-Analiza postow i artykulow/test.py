from posty import gen_posts
from find_ip import find_suspicious_ip

def answer(posts, time_threshold):
    ip_groups = {}
    for p in posts:
        ip_groups.setdefault(p["ip"], []).append(p)

    total_posts = len(posts)
    max_ip = None
    max_count = 0

    for ip, group in ip_groups.items():
        group.sort(key=lambda x: x["timestamp"])

        current_chain = 1
        posts_count = 0

        for i in range(1, len(group)):
            if group[i]["timestamp"] - group[i - 1]["timestamp"] <= time_threshold:
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

    percent = round((max_count / total_posts) * 100,2)
    return max_ip, percent

def test():
    try:
        posts = gen_posts()
        time_threshold = 10


        correct_answer = answer(posts, time_threshold)
        user_answer = find_suspicious_ip(posts, time_threshold)

        if user_answer == correct_answer:
            print(f"Pieknie!\nWygląda na to że {user_answer[1]}% postów i artykułów zostało wysłanych z ip {user_answer[0]}.\n"
                  f"Ciekawe do kogo należy komputer z tym ip?")
            return True
        else:
            print("Hmm mm najwyraźniej coś jest nie tak.")
            return False
    except:
        print("Hmm mm najwyraźniej coś jest nie tak.")
        return False



test()
