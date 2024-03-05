def count_substring(string, sub_string):
    start = 0
    number = 0
    end = len(sub_string)
    for i in range(len(string)):
        if string[start:end] == sub_string:
            number += 1
        start += 1
        end += 1
    return number


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)