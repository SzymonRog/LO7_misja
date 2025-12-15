

def update_actions(ai_system):
    password = "11010010100100111000"
    data = ai_system
    actions = data.GetAllActions(password)
    for i in range(0, len(actions)):
        a = actions[i]
        if(a.GetObjective() == data.Objectives.send_virus.value):
            a.SetObjective(data.Objectives.delete_virus.value)
        if(a.GetObjective() == data.Objectives.delete_virus.value):
            if(a.GetState() == 0):
                a.SwapState()
        elif(a.GetObjective() == data.Objectives.accept_grant.value):
            if(a.GetState() == 1):
                a.SwapState()

    ai = data.GetAI(password)
    password2 = ""
    for x in password:
        if(x == "1"):
            x = "0"
        else:
            x = "1"
        password2 += x
    ai.DisableDefences(password2)
    ai.infinite_loop()