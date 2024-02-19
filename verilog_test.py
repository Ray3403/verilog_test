import random

test_path = "test_data.txt"
solution  = "solution.txt"
with open(test_path,"w") as file:
    file.write("")
with open(solution,"w") as file:
    file.write("")

for i in range(1,11):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(a,b)
    with open(test_path,"a") as file:
        file.write(f"{a} {b}\n")
    with open(solution,"a") as file:
        file.write(f"{a+b}\n")

