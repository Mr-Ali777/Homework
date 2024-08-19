# #1
letter = input("From keybord: ").lower()
match letter:
    case 'a' | 'e' | 'y' | 'u' | 'i' | 'o':
        print("Vowels")
    case 'e' | 'b' | 'c' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm'| 'n'| 'p'| 'q'| 'r' |'s'| 't'| 'v'| 'w'| 'x'| 'z':
        print("Consonant")


#2
day = input(" Day: ")
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Working day")
    case "Saturday" | "Sunday":
        print("Weekend")

#3
fruit = input(" Fruit: ")
match fruit:
    case "banana":
        print("Желтый")
    case "kiwi":
        print("зеленый")
    case "strawberry":
        print("Красный")

#4
estimation = int(input("From keybord: "))
match estimation:
    case 1:
        print("Плохо")
    case 2 :
        print("Удовлетворительно")
    case 3 :
        print("Удовлетворительно")
    case 4:
        print("Хорошо")
    case 5:
        print("Отлично")



