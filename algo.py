from pymongo import MongoClient

#client = MongoClient("mongodb+srv://Admin:horsebackriding@cluster0.mcaic.mongodb.net/info?retryWrites=true&w=majority")
#db = client["info"]
ans = [[[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]]

time_to_slots = { "9:00" : 0 , "10:40" : 1 , "12:40" : 2 , "14:20" : 3, "16:20" : 4}
days_to_slot = { "Mon" : 0 , "Tus" : 1 , "Wed" : 2 , "Thr" : 3 , "Fri" : 4 }
slot_to_time = {  0 : "9:00" , 1 :"10:40" , 2 : "12:40" , 3 : "14:20", 4 : "16:00"}
slot_to_day = { 0: "Mon", 1 : "Tus" , 2 : "Wed" , 3 : "Thr" , 4 : "Fri"}


classes = [["FSE", 0, 0], ["OS", 0, 0], ["Physics", 0, 0], ["PS", 0, 0], ["DE", 0, 0]]
instructors = [("Shilov", ["Fri", "9:00"], "DE", "prof"), ("Konyukhov", ["Fri", "10:40"], "DE", "tut"), ("Marat",
                ["Mon", "9:00"], "DE", "TA"), ("Kazorin", ["Mon", "9:00"], "DE", "TA"), ("Gorodetskiy", ["Fri", "9:00"],
                "PS", "prof"), ("Gorodetskiy", ["Thr", "10:40"], "PS", "tut"), ("Gorodetskiy", ["Thr", "9:00"],
                "PS", "TA"), ("Shikulin", ["Mon", "9:00"], "PS", "TA"), ("Gaponov", ["Wed", "9:00"], "Physics", "prof"),
               ("Kurkin", ["Wed", "10:40"], "Physics", "tut"), ("Ivanov", ["Wed", "9:00"], "Physics", "TA"), ("Nikiforov",
                ["Wed", "9:00"], "Physics", "TA"), ("Succi", ["Tus", "9:00"], "OS", "prof"), ("Lozhnikov", ["Mon", "9:00"],
                "OS", "tut"), ("Lozhnikov", ["Tus", "9:00"], "OS", "TA"), ("Vasquez", ["Tus", "9:00"], "OS", "TA"),
               ("Ergasheva", ["Tus", "9:00"], "OS", "TA"), ("Bobrov", ["Mon", "9:00"], "FSE", "prof"), ("Bobrov",
                ["Mon", "9:00"], "FSE", "tut"), ("Kolychev", ["Mon", "9:00"], "FSE", "TA"), ("Askarbekuly",
                ["Mon", "9:00"], "FSE", "TA"), ("Ignatov", ["Mon", "9:00"], "FSE", "TA")]


'''
for i in db["Instructor"]:
    instructors.append((i["Name"], i["prefTime"], i["Course"], i["Type"]))
for i in db["Classes"]:
    classes.append([i["CName"], 0, 0])
'''


def F(x, y):
    ans = 0
    #for i in db["Instructor"]:
    for i in instructors:
        ans += (x == i[3] and y == i[2])
    return ans




for i in range(len(ans)):
    for j in range(len(ans[i])):
        for k1 in classes:
            B = False
            for k2 in instructors:
                if k1[1] == 0 and k2[3] == "prof" and k2[2] == k1[0] and k2[1][0] == slot_to_day[i] and k2[1][1] == \
                        slot_to_time[j]:
                    ans[i][j] = "{0} lecture by {1}".format(k2[2], k2[0])
                    k1[1] += 1
                    B = True
                    break
                if k1[1] == 1 and k2[3] == "tut" and k2[2] == k1[0] and k2[1][0] == slot_to_day[i] and k2[1][1] == \
                        slot_to_time[j]:
                    ans[i][j] = "{0} tutorial by {1}".format(k2[2], k2[0])
                    k1[1] += 1
                    B = True
                    break
            if B:
                break


for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] != []:
            for k1 in classes:
                if "{0} lecture".format(k1[0]) in ans[i][j]:
                    k1[2] = 1
            continue
        for k1 in classes:
            B = False
            for k2 in instructors:
                if k1[1] == 0 and k2[3] == "prof" and k2[2] == k1[0]:
                    ans[i][j] = "{0} lecture by {1}".format(k2[2], k2[0])
                    k1[1] += 1
                    k1[2] = 1
                    B = True
                    break
                if k1[1] == 1 and k2[3] == "tut" and k2[2] == k1[0] and k1[2] == 1:
                    ans[i][j] = "{0} tutorial by {1}".format(k2[2], k2[0])
                    k1[1] += 1
                    k1[2] = 0
                    B = True
                    break
            if B:
                break

for i in classes:
    i[1] = 0
    i[2] = 0

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] != []:
            for k1 in classes:
                if k1[1] == 0 and "{0} lecture".format(k1[0]) in ans[i][j]:
                    k1[1] += 1
                if k1[1] == 1 and "{0} tutorial".format(k1[0]) in ans[i][j]:
                    k1[1] += 1
            continue
        for k1 in classes:
            B = False
            for k2 in instructors:
                if k1[1] == 2 and k2[3] == "TA" and k2[2] == k1[0] and k1[2] != 6:
                    ans[i][j] = "{0}-th set of labs for {1}".format(k1[2], k2[0])
                    k1[2] += F(k2[3], k2[2])
                    B = True
                    break
            if B:
                break


for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] != []:
            continue
        for k1 in classes:
            B = False
            for k2 in instructors:
                if k1[1] == 2 and k2[3] == "TA" and k2[2] == k1[0] and k1[2] != 6:
                    ans[i][j] = "{0}-th set of labs for {1}".format(k1[2], k2[0])
                    k1[2] += F(k2[3])
                    B = True
                    break
            if B:
                break

print(ans)