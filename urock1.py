def palindrome(s): 
        return s[::-1] == s 
while True: 
    s = input("введите слово: ") 
    print(f"{s} это слово является палиндромом" if 
    palindrome(s) else "это слово не является палиндромом")




def func(s):
    print(set(s))
    for syn in set(s):
        counter = 0
        for sub_s in s:
            if syn == sub_s:
                counter += 1
        print(syn, "-", counter)


#func("aabccd")


def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, "-", count)

strcounter("alekwsnkefleksnkfe ")
