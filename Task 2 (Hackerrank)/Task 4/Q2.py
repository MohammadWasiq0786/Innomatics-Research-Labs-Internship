def split_and_join(sentence):
    return "-".join(sentence.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)