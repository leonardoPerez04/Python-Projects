travel_logs = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany" : ["Stuttgart","Berlin"]
}

for key in travel_logs:
    if key == "France":
        for char in travel_logs[key]:
            if char == "Lille":
                print(char)
nested_list = ["A","B",["C","D"]]

print(nested_list[2][0])