# # When you write a function first step is write the program
# # input
# numbers = [2,3,5,10] # 20

# # process
# total = sum(numbers) # 20
# count = len(numbers) # 4
# avg = total / count # 5.0

# # output
# print(avg)

# Second step: re-write the program as a function
def average(numbers: list[float]) -> float:
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

numbers = [5,6]
grades = [100,100,100,0]
avg_grade = average(grades)
print(f"Average of {grades} is {avg_grade}")

def test_average():
    numbers = [1,1,1,]
    expect = 1.0
    actual = average(numbers)
    assert expect == actual