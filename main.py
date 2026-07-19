while True :
    x = input("Enter the value of x: ").strip().lower()
    if x == "hello world":
        for _ in range(5):
            print(x)
        break
    else:
        print("Error")