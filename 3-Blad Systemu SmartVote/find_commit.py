from datetime import datetime


def find_log(date, branch, file):
    last_commit_id = -1
    last_date = None

    with open('commits.txt', "r") as f:
        for commit in f:
            data = commit.strip().split("|")


            if data[3] == file and data[4] == branch:
                commit_date = datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
                if last_date is None or (last_date < commit_date < date):
                    last_commit_id = data[0]
                    last_date = commit_date
    return last_commit_id