list_to_sort = ["sunHacks","HackNotts","DurHack","HackQuarantine","CovHacks","HackSheffield","😀", "Hack😀"]
max_val = max([len(a) for a in list_to_sort])
def pad(word,num):
    word = word + " "*num
    return word
def value(a):
    if a == " ":
        return 0
    if str(a) in "0123456789":
        return int(a)+1
    if str(a) in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return 11 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(str(a))
    if str(a) in "abcdefghijklmnopqrstuvwxyz":
        return 37 + "abcdefghijklmnopqrstuvwxyz".find(str(a))
    if str(a) in "!.,/[]{};:'@#~?":
        return 63 + "!.,/[]{};:'@#~?".find(str(a))
    else:
        return 78 + ord(a)
def radix_sort(to_sort,index,max_len):
    if -index == max_len +1:
        return to_sort
    else:
        buckets = []
        for i in range(129759):
            buckets.append([])
        for thing in to_sort:
            if -index > len(thing):
                buckets[0].append(thing)
            else:
                let = thing[index]
                vl = value(let)
                buckets[value(let)].append(thing)
        new_list = []
        for b in buckets:
            new_list += b
        return radix_sort(new_list,index-1,max_len)

list_to_sort = [pad(a,max_val - len(a)) for a in list_to_sort]
sorted_list = radix_sort(list_to_sort,-1,max_val)
print(sorted_list)

