"""Gotowe zadanie zrobiłem przy sporej pomocy ChatGPT
Żeby to zrobić musiałem poszukać jak sprawić żeby czytał wyraz od końca, nie było tego w kursie więc szukałem po necie.

W moim oryginalnym kodzie chciałem tylko sparwdzić czy dobrze mam zapisany kod na spawrdzanie palindromu, ale nie wiedziałem jak przekonwertować str na bool

words=("woda")

for word in words:
    if words==words[::-1]:
        print("true")
    else:
        print("false")

"""
def palindrom(word: str) -> bool:
    return word == word[::-1]

word = "potop"
print(palindrom(word))

