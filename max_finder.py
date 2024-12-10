def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

if __name__ == "__main__":
    count = int(input("Введите количество элементов: "))
    numbers = []
    for _ in range(count):
        num = float(input("Введите число: "))
        numbers.append(num)
    
    print("Минимум:", find_min(numbers))

