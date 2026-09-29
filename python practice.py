"""
Python Variables and Memory Management
====================================


1. What is a variable in Python?
--------------------------------
A variable is a name that refers to an object in memory.

Example:
x = 10
# x refers to the integer object 10

Important: Python does not work like a box that directly stores a value.
Instead, variables point to objects.


2. Everything in Python is an object
-----------------------------------
This is an important interview concept.

x = 10
name = "Mahi"
marks = 85.5
numbers = [10, 20, 30]

# x -> integer object
# name -> string object
# marks -> float object
# numbers -> list object

Every object has:
- identity
- type
- value

Example:
x = 10
print(id(x))
print(type(x))
print(x)

Here:
- id() gives the identity
- type() gives the type
- value is the actual data stored in the object


3. Python built-in data types
-----------------------------
Python has several built-in data types:

- Numeric: int, float, complex
- Boolean: bool
- Text: str
- Sequence: list, tuple, range
- Set: set, frozenset
- Mapping: dict
- Binary: bytes, bytearray, memoryview
- Special: NaN type


4. Numeric types
----------------
int:
age = 25
count = -10

float:
price = 99.34
percentage = 85.75

complex:
z = 3 + 4j


5. Boolean
-----------
is_active = True
is_locked = False

Examples:
print(bool(0))
print(bool(1))
print(bool("HELLO"))


6. Strings
----------
name = "MAHI"
A string is an immutable sequence of characters.

Example:
print(name[0])
print(name[1])


7. Lists
--------
numbers = [10, 20, 30]

Properties:
- Ordered
- Mutable
- Allows duplicates
- Can contain different data types

Example:
data = [10, "python", 25.5, True]


8. Tuples
---------
point = (10, 20)

Properties:
- Ordered
- Immutable
- Allows duplicates


9. Sets
-------
numbers = {10, 20, 20, 30}

Properties:
- Unique elements
- Mutable
- Not used for positional indexing like lists


10. Dictionary
---------------
student = {
    "ID": 101,
    "NAME": "MAHI",
    "MARKS": 85.5,
}

A dictionary stores data in key-value pairs.


11. NaN
-------
result = float('nan')

NaN represents the absence of a value.
Do not confuse NaN with 0, False, or [] because they are different values with different meanings.


12. Mutable vs Immutable
------------------------
Immutable objects cannot be changed after creation.
Examples: int, float, bool, tuple, frozenset, str

Mutable objects can be changed after creation.
Examples: list, dict, set, bytearray


13. Variable rebinding
----------------------
x = 10
x = 20

This looks like x changed from 10 to 20.
But in reality, x was rebound to a different object.
The integer object 10 was not modified.


14. Memory example
------------------
a = 10
b = a

Conceptually:
- a -> 10
- b -> 10

Both names refer to the same object.

If later we do:
a = 20

Then:
- a -> 20
- b -> 10

So b remains 10.


15. Mutable object example
--------------------------
a = [10, 20]
b = a
b.append(30)
print(a)

Output:
[10, 20, 30]

Why?
Because a and b both refer to the same list object.
The append() method modifies that list in place.


16. == vs is
------------
== checks whether two values are equal.

Example:
a == b

is checks whether two references point to the same object.

Example:
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False


17. Where is memory used?
------------------------
At a conceptual level, Python programs use memory for:
- program code
- objects
- integers
- strings
- lists
- dictionaries
- functions

In CPython, objects are managed by Python's memory system.
Memory is obtained from the underlying operating system and allocated through Python's internal mechanisms.

Python variables reference objects, and CPython manages this memory dynamically.
The exact implementation details can vary with the Python version and interpreter.


18. Reference counting in CPython
---------------------------------
CPython mainly uses reference counting.

Example:
a = [1, 2, 3]
b = a

Conceptually:
- a -> [1, 2, 3]
- b -> [1, 2, 3]

There are two references to the same object.

If we do:
del b

Then the reference count decreases.
The object still exists if another reference is still pointing to it.


19. What is garbage collection?
------------------------------
Garbage collection means identifying objects that are no longer reachable or needed and reclaiming their memory.

Python has automatic memory management.
You do not normally need to call free() or delete memory manually, as in some lower-level languages.


20. Reference counting + garbage collector
------------------------------------------
Reference counting:
- Immediately tracks references to objects in CPython

Garbage collector:
- Handles cyclic garbage that reference counting alone cannot reclaim

Example:
a = []
a.append(a)

Now the list refers to itself, creating a reference cycle.
Python's cyclic garbage collector can detect and handle such cycles.


21. del does not necessarily delete the object
--------------------------------------------
numbers = [1, 2, 3]
del numbers

This removes the name or reference numbers.
It does not necessarily immediately destroy the object.

Example:
numbers = [1, 2, 3]
b = numbers
del numbers
print(b)  # [1, 2, 3]

The object still exists because b still references it.


22. When can an object become garbage?
-------------------------------------
a = [1, 2, 3]
b = a
del a
del b

Now there are no remaining references to that list.
The object becomes eligible for memory reclamation.

The exact time when memory is actually returned to the system may depend on the Python implementation.


23. Summary
-----------
Variable -> Object -> Memory -> Garbage Collector

- A variable is a name that references an object
- Objects have identity, type, and value
- Memory is managed automatically by Python
- Reference counting and garbage collection help reclaim unused memory

"""


# 1. Simple variable example
x = 10
print("x =", x)
print("id(x) =", id(x))
print("type(x) =", type(x))


# 2. Mutable object example
a = [10, 20]
b = a
b.append(30)
print("a =", a)


# 3. Equality check vs identity check
a = [1, 2]
b = [1, 2]
print("a == b:", a == b)
print("a is b:", a is b)


# 4. Boolean conversion
print(bool(0))
print(bool(1))
print(bool("HELLO"))
