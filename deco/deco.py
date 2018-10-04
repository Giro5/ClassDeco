def another_functin(func):
    def other_function():
        val = "Result from %s equal %s" %(func(), eval(func()))
        return val
    return other_function

@another_functin
def a_function():
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)