#### Fonction secondaire


def ispalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def main():
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
