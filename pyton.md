# Pyton Study ( CS50.dev )

## 1) Print; Input

```javascript 
print("Hello World") 'დაპრინტავს ჰელოუ ვორლდს'


print( input("What is your name")) `python test.py-ის დაწერის შემდეგ "ინფუთი" გამოვა რომელსაც პასუხად შოთას 
                                    თუ დავუწერ დაპრინტავს შოთას ეგრევე, რადგან "პრინტი" პრინტავს "ინფუთს"`


print("Hello", "Shota", "How are you today", sep="\n") `ეს სამივე პარამეტრს გამოპრინტავს ახალ აბზაცზე (sep="\n)`                                    
```

## 2) ცვლადი / Variable

```javascript 
1
name = input("what is your name?")
print("hello", name, "How are you today", name) `ჯერ გკითხავს What is your name? და შოთას როჩავწერ, დაპრინტავს 
                                                  hello shota How are you today shota`
1

2
name = input("What is your name?")
surname = input("what is your surname?")
fullname = name + " " + surname

print("Hello", fullname)   `დაპრინტავს: hello name surname-ში რასაც ჩავწერთ`
2                                           
```

## 3) ცვლადი / Variable
```javascript
num1 = int(input("first: "))
num2 = int(input("second: "))

sum = num1 + num2

print("your number is: " , sum) `რიცხვად რომ აღიქვას პითონმა დაგვჭირდება Int ფუნქცია„
```

## 4) If Function

```javascript
num1 = int(input("first: "))
num2 = int(input("second: "))

if num1 > num2 :
    print("I is bigger")

if num2 > num1 :
    print("II is bigger")    `რასაც ჩავწერ იმის მიხედვით გამოპრინტავს`
```

## 5) AND / OR in Python

```javascript
`AND`
score = int(input("Score: "))

if score > 90 and score < 100 :
    print("A") `and-ის შემთხვევაში უნდა აკმაყოფილებდეს ორივე პირობას`

"OR"
score = int(input("Score: "))

if score < 20 or score < 10 :
    print("F") `or-ის შემთხვევაში ერთ ერთს უნდა აკმაყოფილებდეს მეორე კიდია`

if score not 20 :
    print("F")
```

## 5) Functions

```javascript
def sumXY (x, y):
    return x + y

x = int(input("x: "))
y = int(input("y: "))

result = sumXY(x,y)

print(result) `ეს დაბეჭდავს რასაც ჩავწერთ იმ რიცხვების ჯამს`
```

## 5) ციკლები (FOR)

```javascript
counter = 3

while counter >= 0 :
    print ("hello")
    counter = counter - 1 `სანამ ქაუნთერი 0-ზე მეტი იქნება, ეს პირობა შესრულდება`


for i in range(3):
    print("hello")  `ესეც დაბეჭდავს 3-ჯერ, მაგრამ უფრო მარტივად:::::::::ანუ ეს range(3) იგივეა რაც [1, 2, 3]`
```

## 5) While 
```javascript
while True:
    n = int(input("score: "))
    if n < 0 :
        print(n, " is negative")  
        continue                     `ეს continue ნიშნავს რომ ფუნქცია მაინც გაგრძელდეს თუ n ნაკლებია 0-ზე`
    else:
        print(n, " is positive")
        break                        `ეს break წყვიტავს ფუნქციას`
```


## 6) LIST
```javascript
students = ['shota', 'irkali', 'elene']

index = 0

for student in students:
    if(index % 2 == 0):
        print(student)   `ეს დაბეჭდავს ერთის გამოტოვებით ზემოთ სტუდენტების სიიდან, რადგან 1-ით ახტება index-ით`
    index += 1    
```

## 6) Exceptions in TRY

```javascript
try:
    number = int(input("number is: "))
    print(f"your number is {number}")
except ValueError:
    print("there is error") `except-ი გაეშვება მაშინ როდესაც ინფუთში რიცხვის მაგივრად ჩავწერთ ასოებს მაგალითად`


def main ():
    number = get_input()
    print(f"your input is {number}")


def get_input():
    while True:
        try:
            number = int(input("number: "))
        except ValueError:
            print("it is not number") `აქ იქამდე გკითხავს ამ კითხვას სანამ რიცხვს არ ჩაწერ`
        else:
            break
        
    return number
    
main()    
```