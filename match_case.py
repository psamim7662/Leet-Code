marks = int(input("Enter marks (0-100): "))

match marks // 10:
    case 10 | 9:
        print("Grade: A")
    case 8:
        print("Grade: B")
    case 7:
        print("Grade: C")
    case 6:
        print("Grade: D")
    case _:
        if 0 <= marks < 60:
            print("Grade: F")
        else:
            print("Invalid Marks")