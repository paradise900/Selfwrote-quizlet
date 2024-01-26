def adding():
    global defenition
    global set_of_def

    while True:
        eng = input()
        if eng == '0':
            break
        rus = input()
        if rus == '0':
            break
        if not defenition.get(eng):
            defenition[eng] = rus
            set_of_def.append(eng)


def practice():
    from random import randint

    global defenition
    global set_of_def

    l = len(set_of_def) - 1
    ans = ''
    while ans != '0':
        n = randint(0, l)
        print(defenition[set_of_def[n]], end='')
        ans = input()
        if ans == set_of_def[n]:
            print('\n')
            continue
        else:
            print(f"Wrong! It's {set_of_def[n]}\n")
            

f = open('learn project/1.txt', 'r')
set_of_def = []
defenition = {}
for word in f:
    for x in range(len(word) - 1):
        if word[x:x + 2] != '--':
            continue
        else:
            defenition[word[:x - 1]] = word[x + 3:]
            set_of_def.append(word[:x - 1])
f.close()
while True:
    mes = input('"a" if you want to add new defenition \n"p" if you wanna practice\n"0" for exit\n')
    if mes == 'a':
        adding()
    elif mes == 'p':
        practice()
    elif mes == '0':
        break

f = open('itmo_study/1.txt', 'w')
for key, val in defenition.items():
    s = key + ' -- ' + val + '\n'
    f.writelines(s)

