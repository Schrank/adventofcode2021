from Day1 import Day1

if __name__ == '__main__':
    day1 = Day1()
    with open('day1.txt') as file:
        day1Input = file.read()
    print("Day 1a " + str(day1.count(day1Input)) + "\n")
    print("Day 1b " + str(day1.count2(day1Input)) + "\n")
