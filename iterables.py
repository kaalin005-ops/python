#iterables=A object /collections that can return its elements one at a time,
#allowing it to be iterated over in a loop

numbers=[1,2,3,4,5,6]
for number in reversed(numbers):
    print(number, end="-")

fruits={"apple","orange","bananna","coconut"}
#for fruit in reversed(fruits):
  #  print(fruits)

'''**In Python, an *iterable* is any object that can return its elements one at a time, allowing it to be looped over using a `for` loop.** Common examples include lists, tuples, strings, dictionaries, and sets.

---

## 🔁 What Makes Something an Iterable?

An object is considered *iterable* if it implements the **`__iter__()`** method or has a **`__getitem__()`** method that can return items starting from index 0.

### ✅ Examples of Iterables:
- **List**: `["apple", "banana", "cherry"]`
- **Tuple**: `(1, 2, 3)`
- **String**: `"hello"`
- **Set**: `{10, 20, 30}`
- **Dictionary**: `{"name": "Alice", "age": 25}`

You can loop through all of these using a `for` loop:

```python
for char in "hello":
    print(char)
```

---

## 🔄 Iterable vs Iterator

- **Iterable**: An object that can be looped over (like a list or string).
- **Iterator**: An object that keeps state and produces the next value when you call `next()` on it.

You can convert an iterable into an iterator using the `iter()` function:

```python
nums = [1, 2, 3]
it = iter(nums)  # it is now an iterator
print(next(it))  # Output: 1
print(next(it))  # Output: 2
```

> **Every iterator is an iterable, but not every iterable is an iterator**.

---

## 🧠 Why Are Iterables Important?

- They allow looping with `for` loops.
- They are used in many Python features like list comprehensions, generators, and functions like `map()`, `filter()`, and `zip()`.

---

## 🧪 How to Check if Something Is Iterable

You can use the `collections.abc.Iterable` class:

```python
from collections.abc import Iterable

print(isinstance("hello", Iterable))  # True
print(isinstance(42, Iterable))       # False
```

---

If you'd like, I can show you how to create your own custom iterable class or explore how iterables work with generators. Want to dive into that?
'''

my_dictionary={"A":1,"B":2,"c":3}

for key,value in my_dictionary.items():
    print(key, value)