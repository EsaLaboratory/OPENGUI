class Object:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

object = Object(1,2,3)

print(object.__dict__.items())

newValue = 5

# for parameter, value in object.__dict__.items():
#     code = f"object.{parameter} = newValue"
#     exec(code)

for i, (parameter, value) in enumerate(object.__dict__.items()):
    print(i, parameter, value)
    object.__setattr__(parameter, newValue)

print(object.__dict__.items())