x = "a-a-a|"

a = x.split("|")
a.pop(1)
print(a)

carritoprod = [["Pizza1", 2, 3], ["Pizza2", 3, 4]]

print(len(carritoprod))

if len(carritoprod) == 1:
    constxt = ""
    for i in range(len(carritoprod[0]) - 1):
        constxt += str(carritoprod[0][i])
    constxt += str(carritoprod[0][len(carritoprod) - 1])
else:
    constxt = ""
    for i in range(len(carritoprod) - 1):
        txt = ""
        for j in range(len(carritoprod[0]) - 1):
            txt += str(carritoprod[i][j]) + "-"
        txt += str(carritoprod[i][len(carritoprod) - 1])
        constxt += txt + "|"
    constxt += txt

print(constxt)
