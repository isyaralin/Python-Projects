# Custom Hash Map & Word Frequency Counter

## Overview
In this project, I built a **Hash Map** (essentially Python's built-in `dict`) completely from scratch. The goal was to understand how dictionaries actually work under the hood, so I was not allowed to use any of Python's native `dict` or `set` structures. 

After building the data structure, I used it to power a text-parsing application that reads a large block of text, cleans it up, and counts the frequency of every word.

---

## How the Hash Map Works

### 1. Handling Collisions (Separate Chaining)
When two different keys hash to the same index (a collision), the hash table handles it using a Linked List. I created a custom `Node` class so that multiple key-value pairs can chain together in the same bucket.

### 2. Custom Hash Function
Instead of using Python's built-in `hash()` function—which randomizes its output every time you run the script for security reasons—I wrote a custom 32-bit polynomial rolling hash function. This made the memory layout predictable and much easier to debug across different runs.

### 3. Dynamic Resizing
To keep the search and insertion times at $O(1)$, the hash map automatically grows. 
* It starts small, with just 5 buckets. 
* It constantly checks its **load factor** (the average number of items per bucket). 
* Once the load factor exceeds 4.0, the table dynamically doubles its bucket count and automatically re-hashes all the existing nodes into the new array.

---

## The Application (Text Parsing)
The second part of the script uses the custom Hash Map to process standard input (`sys.stdin`):
* **Cleaning the Text:** It uses Regular Expressions (`re`) to strip out all punctuation and isolate purely alphabetical words, converting everything to lowercase so that "Pizza" and "pizza" count as the same word.
* **Answering Queries:** After parsing the text, the script takes a list of words to query. It prints out how many times that word appeared in the text. 
* **State Management:** To handle duplicate queries, once a word's count is successfully looked up, I actively remove its node from the Hash Map. Any future queries for that same word will just return `None`.
