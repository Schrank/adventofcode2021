from Day1 import Day1

if __name__ == '__main__':
    day1 = Day1()
    file = open('day1.txt', mode='r')
    day1Input = file.read()
    print("Day 1a " + str(day1.count(day1Input)) + "\n")
    print("Day 1b " + str(day1.count2(day1Input)) + "\n")
    file.close()
