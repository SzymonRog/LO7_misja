from datetime import datetime

def find_log(date, branch, file):
    last_commit_id = -1
    last_date = None
    
    with open('commits.txt', "r") as f:  
        for commit in f:
            data = commit.strip().split("|")  
            
            if len(data) >= 5:  # sprawdzenie czy linia ma wszystkie potrzebne dane
                if data[3] == file:
                    if data[4] == branch:
                        commit_date = datetime.strptime(data[1], "%Y-%m-%d")  # parsowanie daty
                        
                        if last_date is None or (commit_date > last_date and commit_date < date):
                            last_commit_id = data[0]
                            last_date = commit_date
    
    return last_commit_id


find_log("2024-12-04 02:47:33","main","Borda.cpp")
