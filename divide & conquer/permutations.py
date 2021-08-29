def permute(l,pos1,pos2):
    l=list(l)
    l[pos1],l[pos2]=l[pos2],l[pos1]
    return ''.join(l)

def permutations(string, step = 0):
    if step == len(string):
        print("".join(string))
    
    for i in range(step, len(string)):
        st_p=permute(string,step,i)
        permutations(st_p, step + 1)
