# Pyton Study ( CS50.dev )

## 1) Print; Input

```javascript 
print("Hello World") 'დაპრინტავს ჰელოუ ვორლდს'


print( input("What is your name")) `python test.py-ის დაწერის შემდეგ "ინფუთი" გამოვა რომელსაც პასუხად შოთას 
                                    თუ დავუწერ დაპრინტავს შოთას ეგრევე, რადგან "პრინტი" პრინტავს "ინფუთს"`


print("Hello", "Shota", "How are you today", sep="\n") `ეს სამივე პარამეტრს გამოპრინტავს ახალ აბზაცზე (sep="\n)`                                    
```

## 1) ცვლადი / Variable

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

print("Hello", fullname)   `დაპრინტავს: hello name surname-ში რასაც ჩავწერთ
2                                           
```

## 1) ცვლადი / Variable
```javascript
num1 = int(input("first: "))
num2 = int(input("second: "))

sum = num1 + num2

print("your number is: " , sum) `რიცხვად რომ აღიქვას პითონმა დაგვჭირდება Int ფუნქცია„
```

## 1) If Function

```javascript
num1 = int(input("first: "))
num2 = int(input("second: "))

if num1 > num2 :
    print("I is bigger")

if num2 > num1 :
    print("II is bigger")    `რასაც ჩავწერ იმის მიხედვით გამოპრინტავს`
```