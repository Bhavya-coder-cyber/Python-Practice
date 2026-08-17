def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
for i in chai:
    print(i)
# print(next(chai)) gives error due to stopIteration

def infinite_chai():
    count = 1
    while True:
        yield f"Cup {count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for i in range(4):
    print(next(refill))

for i in range(3):
    print(next(user2))

