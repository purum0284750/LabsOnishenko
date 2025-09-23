a = input("a: ").replace(',', '.')
b = input("b: ").replace(',', '.')
c = float(a)
d = float(b)
sum_result = c + d
avg_result = (c + d) / 2
print(f"sum={sum_result:.2f}; avg={avg_result:.2f}")