def analyze_user_activity(log_file_path: str) -> dict:
    actions = {}
    user_time = {} 
    users = set() 
    login_times = [] 

    with open(log_file_path, "r") as file: 
        for line in file:  
            data = line.split() 

            if len(data) != 4: 
                continue

            date, user, action, time = data 

            try: 
                time = float(time)
            except ValueError:
                continue

            actions[action] = actions.get(action, 0) + 1 
            users.add(user) 

            if action == "login": 
                login_times.append(time) 
                user_time[user] = time 
 
    average = sum(login_times) / len(login_times) if login_times else 0 
    most_active = max(user_time, key=user_time.get) if user_time else None 

    return { 
        "action_counts": actions,
        "average_session_time": average,
        "most_active_user": most_active,
        "total_users": len(users)
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
