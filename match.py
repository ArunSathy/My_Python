def h_error(s):
    match s:
        case 400:
            return "A"
        case 404:
            return "B"
        case 418:
            return "c"
        case _:
            return "some s"
y=int(input("enter an error : "))
x=h_error(y)
print(x)