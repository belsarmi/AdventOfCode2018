zahlen = []

with open("AoC_Day1Input.txt") as f:
    for zeile in f:
        zahlen.append(int(zeile.strip()))

print(sum(zahlen))
