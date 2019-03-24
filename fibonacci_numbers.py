def get_fibonacci(start: int, how_many: int):
    num_list = [start]
    num_list.append(start + 0)
    while len(num_list) < how_many:
        num_list.append(num_list[-1] + num_list[-2])
    return num_list

beg = input('Enter fibonacci starting number: ')
length = input('Enter length of fibonacci sequence: ')

print(get_fibonacci(int(beg), int(length)))