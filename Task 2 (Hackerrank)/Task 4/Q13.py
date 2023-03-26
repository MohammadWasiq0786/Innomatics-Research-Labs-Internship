def minion_game(string):
    vowels = 'AEIOU'
    k,s = 0,0
    l =len(string)
    for i in range(l):
        if string[i] in vowels:
            k += (l-i)
        else:
            s += (l-i)
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)