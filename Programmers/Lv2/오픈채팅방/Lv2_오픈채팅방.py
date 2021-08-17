def solution(record):
    user_info = {}
    actions = []
    answer = []

    for s in record:
        words = s.split()
        if words[0] != "Leave":
            user_info[words[1]] = words[2]
        if words[0] != "Change":
            actions.append((words[0], words[1]))

    for action in actions:
        if action[0] == "Enter":
            answer.append(user_info[action[1]] + "님이 들어왔습니다.")
        else:
            answer.append(user_info[action[1]] + "님이 나갔습니다.")

    return answer


def better_solution(record):
    answer = []
    user_info = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for r in record:
        words = r.split()
        if words[0] in ["Enter", "Change"]:
            user_info[words[1]] = words[2]

    for r in record:
        words = r.split()
        if words[0] != "Change":
            answer.append(user_info[words[1]] + printer[words[0]])

    return answer
