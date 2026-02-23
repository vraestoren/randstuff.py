# randstuff.py

> Web-API for [randstuff.ru](https://randstuff.ru) to generate random jokes, facts, passwords, cities, and more.

<p align="center">
  <img src="https://i.postimg.cc/v8hSZRFb/a-OHLI4-V0-FI.jpg" alt="RandStuff" width="300"/>
</p>

---

## Quick Start

```python
from randstuff import RandStuff

randstuff = RandStuff()

joke = randstuff.generate_random_joke()["joke"]["text"]
print(joke)
```

---

## Features

- 😂 **Jokes** — random jokes on demand
- 🔢 **Numbers** — random numbers with range, uniqueness, and list support
- 🧠 **Wisdom & Facts** — random sayings and interesting facts
- 🔑 **Passwords** — configurable random password generation
- ❓ **Questions** — random questions with answer support
- 🎭 **Nicknames** — random username/nickname generation
- 🎰 **Tickets** — random lottery-style tickets
- 🌍 **Cities** — random cities filtered by country
- 🔮 **Ask** — magic 8-ball style yes/no answers

---

## Usage

### Jokes, Facts & Wisdom

```python
randstuff.generate_random_joke()
randstuff.generate_random_fact()
randstuff.generate_random_wisdom()
```

### Numbers

```python
# Single random number between 1 and 100 (default)
randstuff.generate_random_number()

# 5 unique numbers between 1 and 50
randstuff.generate_random_number(count=5, start=1, end=50, unique=1)
```

### Passwords

```python
# Simple 8-character password (default)
randstuff.generate_random_password()

# 16-character password with numbers and symbols
randstuff.generate_random_password(length=16, numbers=1, symbols=1)
```

### Questions & Answers

```python
# Get a random question
question = randstuff.generate_random_question()
question_id = question["question"]["id"]

# Answer it (number = answer option index)
randstuff.answer_to_question(id=question_id, number=1)
```

### Ask (Magic 8-Ball)

```python
randstuff.get_random_ask(question="Will it rain tomorrow?")
```

### Nicknames

```python
# Without numbers
randstuff.generate_random_nickname(numbers=0)

# With numbers appended (default)
randstuff.generate_random_nickname(numbers=1)
```

### Cities

```python
# Random city from any country (default)
randstuff.generate_random_city()

# Random city from a specific country
randstuff.generate_random_city(country="ru")
```

### Miscellaneous

```python
randstuff.generate_random_ticket()
```

---

## API Reference

| Method                      | Description                                      |
|-----------------------------|--------------------------------------------------|
| `generate_random_joke`      | Random joke                                      |
| `generate_random_fact`      | Random fact                                      |
| `generate_random_wisdom`    | Random saying or wisdom quote                    |
| `generate_random_number`    | Random number(s) within a range                  |
| `generate_random_password`  | Random password (configurable length/complexity) |
| `generate_random_question`  | Random question                                  |
| `answer_to_question`        | Submit an answer to a question by ID             |
| `get_random_ask`            | Yes/no magic-8-ball style answer                 |
| `generate_random_nickname`  | Random nickname/username                         |
| `generate_random_city`      | Random city, optionally filtered by country      |
| `generate_random_ticket`    | Random lottery-style ticket                      |

---
