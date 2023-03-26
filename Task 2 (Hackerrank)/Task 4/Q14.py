import textwrap
def merge_the_tools(string, k):
    for i in textwrap.wrap(string, k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in i if c not in d ]))
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)