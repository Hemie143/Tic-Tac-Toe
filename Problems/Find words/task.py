text = input()
print("_".join([w for w in text.split() if w.endswith("s")]))