from unittest import case

day = input("输入星期几1-7:")

match day:
    case "1" :
        print(f"星期{day}不休息")
    case "2" :
        print(f"星期{day}不休息")
    case "3":
        print(f"星期{day}不休息")
    case "4":
        print(f"星期{day}不休息")
    case "5":
        print(f"星期{day}不休息")
    case "6":
        print("星期六休息")
    case "7":
        print("星期天休息")
    case _ :
        print("输入1-7")