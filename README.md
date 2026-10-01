# Python Functions

## Question 1: Why do we use functions?

Functions are used to avoid repeating code and make programs easier to read, maintain, and test. They allow us to group a block of code that performs a specific task and call it whenever needed.

```python
print("Bhagirathi")
print("Yati")
print("Gouthami")
```

Without functions, the same logic must be written again and again. Functions help with reuse and organization.

---

## Question 2: What exactly is a function?

A function is a reusable block of code that performs a specific task. It is defined once and can be called many times.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

A function can also take input and return output.

---

## Question 3: What problem did functions solve?

Functions solved several important programming problems:

- code reuse
- less repetition
- better organization
- easier maintenance
- easier testing

Instead of writing the same code multiple times, we can write a function once and reuse it.

---

## Question 4: What is the difference between defining and calling a function?

Defining a function creates the function structure, but it does not run the code inside it.

```python
def greet():
    print("Hello")
```

Calling the function executes its body:

```python
greet()
```

The definition tells Python what the function is; the call tells Python to run it.

---

## Question 5: What is a function without parameters?

A function without parameters does not take input values.

```python
def welcome():
    print("Welcome to Nighan2 Labs")

welcome()
```

This is the simplest type of function and is useful when the task does not need any input.

---

## Question 6: What is a function with parameters?

A parameter is a variable used in the function definition, while an argument is the actual value passed when calling the function.

```python
def welcome(name):
    print("Welcome", name)

welcome("Bhagirathi")
```

Here, `name` is the parameter and `"Bhagirathi"` is the argument.

---

## Question 7: What is a function with multiple parameters?

A function can accept more than one parameter.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

This allows the function to work with multiple values at the same time.

---

## Question 8: What is a return statement?

The `return` statement sends a value back to the caller. This is one of the most important concepts in functions.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Compare this with a function that only prints a value:

```python
def add(a, b):
    print(a + b)
```

`print()` displays output, while `return` sends the result back for further use.

---

## Question 9: What happens after a return statement?

When Python reaches a `return` statement, the function stops executing immediately.

```python
def test():
    return 10
    print("Hello")

print(test())
```

The line `print("Hello")` will never run because the function has already returned.

---

## Question 10: Can a function return multiple values?

Yes. In Python, a function can return multiple values as a tuple.

```python
def calculate(a, b):
    return a + b, a - b, a * b

x, y, z = calculate(10, 5)
print(x)
print(y)
print(z)
```

This function is effectively returning a tuple of values.

---

## Question 11: What are default parameters?

Default parameters allow a function to use a value when no argument is provided.

```python
def greet(name="Bhagirathi"):
    print("Hello", name)

greet()
greet("Yati")
```

Default parameters are useful when we want a function to work even if the user does not pass a value.

---

## Question 12: What are positional arguments?

Positional arguments are passed in the order in which the parameters are defined.

```python
def student(name, age):
    print(name, age)

student("Bhavana", 20)
```

The first value goes to `name` and the second value goes to `age`.

---

## Question 13: What are keyword arguments?

Keyword arguments are passed by parameter name, so the order does not matter.

```python
def students(name="Bhagirathi", age=21):
    print(name, age)

students(age=25, name="Bhagirathi")
```

This makes function calls clearer and easier to read.

---

## Question 14: What is the difference between positional and keyword arguments?

Positional arguments are matched by position, while keyword arguments are matched by name.

```python
def students(name, age, course):
    print(name, age, course)

students("Bhagirathi", age=22, course="BCA")
```

This works because the keyword arguments specify the parameter names clearly.

But this is invalid:

```python
students(name="Bhagirathi", 21, course="BCA")
```

A positional argument cannot appear after a keyword argument.

---

## Question 15: What is `*args`?

`*args` allows a function to accept any number of positional arguments.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

`*args` collects extra arguments into a tuple.

---

## Question 16: What is `**kwargs`?

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def student(**details):
    print(details)

student(name="Bhagirathi", age=21, course="BCA")
```

`kwargs` becomes a dictionary-like collection of keyword arguments.

---

## Question 17: How do we combine positional and keyword arguments?

A function can accept a normal parameter, a default parameter, `*args`, and `**kwargs` together.

```python
def example(a, b=10, *args, **kwargs):
    pass
```

This pattern is useful when writing flexible functions that accept many kinds of inputs.

---

## Question 18: What is the difference between local and global scope?

A local variable is created inside a function and is only available within that function.

```python
def test():
    x = 10
    print(x)

test()
```

A global variable is defined outside the function and can be accessed from inside it.

```python
x = 100

def test():
    print(x)

test()
```

Local variables stay inside the function; global variables are available across the program.

---

## Question 19: What is the `global` keyword?

The `global` keyword allows a function to modify a variable that exists outside the function.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

Using `global` is sometimes necessary, but it is better to prefer function parameters and return values when possible because global state can make code harder to maintain.

---

## Question 20: What happens when we try to use a local variable outside its function?

A variable created inside a function is local to that function and cannot be accessed outside it.

```python
def test():
    x = 10

test()
print(x)
```

This raises a `NameError` because `x` is local to `test()`.

---

## Question 21: Can functions call other functions?

Yes. A function can call another function to perform a part of the task.

```python
def add(a, b):
    return a + b

def display():
    result = add(10, 20)
    print(result)

display()
```

This structure is useful for organizing logic into smaller, reusable parts.

---

## Final Summary

Functions are important because they:

- reduce repetition
- make code clearer
- help with reuse
- support better structure
- allow modular programming

A well-designed function should do one clear job, use parameters when needed, and return values when the result is required by the caller.
