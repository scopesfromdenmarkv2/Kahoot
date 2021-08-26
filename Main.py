import random
from kahoot import client
import string

Kahoot = client()


def main():
    classid = input("Kahoot ID >")
    botamount = int(input("How Many Bots :? >"))
    for p in range(botamount):
        randname = string.ascii_uppercase + string.ascii_lowercase
        displayedname = ''.join(random.choice(randname)for p in range(5,5))
        Kahoot.join(f"{botamount}", displayedname)


if __name__ == "__main__":
    main()
