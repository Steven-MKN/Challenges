#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum 
#of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def get_fibonacci(start: int, how_many: int):
    num_list = [start]
    num_list.append(start + 0)
    while len(num_list) < how_many:
        num_list.append(num_list[-1] + num_list[-2])
    return num_list

beg = input('Enter fibonacci starting number: ')
length = input('Enter length of fibonacci sequence: ')

print(get_fibonacci(int(beg), int(length)))
