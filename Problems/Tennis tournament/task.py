lines = int(input())
entries = []
for _ in range(lines):
    entries.append(input())
wins = [e[:-4] for e in entries if e.endswith("win")]
print(wins)
print(len(wins))
