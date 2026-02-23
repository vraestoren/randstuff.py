# randstuff.py
Web-API for [randstuff](https://randstuff.ru) website to generate random stuff

![](https://i.postimg.cc/v8hSZRFb/a-OHLI4-V0-FI.jpg)

### Example
```py3
from randstuff import RandStuff

randstuff = RandStuff()
random_joke = randstuff.generate_random_joke()["joke"]["text"]
print(random_joke)
```
