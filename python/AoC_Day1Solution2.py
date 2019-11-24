zahlen = []

with open("AoC_Day1Input.txt") as f:
    for zeile in f:
        zahlen.append(int(zeile.strip()))

result = 0
results = {}
found = False
numberLoops = 0
while not found:
    numberLoops += 1
    print(f"Loop #:{numberLoops}")
    for zahl in zahlen:
        result += zahl
        if result in results:
            print(f"Frequncy: {result}")
            found = True
            break
        else:
            results[result] = False
print(f"Sum of the input: {sum(zahlen)}")
# number of loops 144
#frequency: 71961
