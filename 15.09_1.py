class Average:
    def average(self, *args):
        print(sum(args) / len(args) if len(args) else 0)

numbers = []
while True:
    a = input()
    if a == '':
        break
    numbers.append(float(a))

print(Average().average(*numbers))

