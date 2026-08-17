def chai_customer():
    print("Welcome!")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall)
stall.send("chai")

def local_chai():
    yield "Masala Chai"
    yield "Green Chai"
    yield "Black Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def chai():
    yield from local_chai() 
    yield from imported_chai()

for i in chai():
    print(i)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for order"
    except:
        print("Chai stall closed")

stall = chai_stall()
print(next(stall))
stall.close() #cleanup