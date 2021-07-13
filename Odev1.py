liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_l = []
def flatten(l):
     
     for item in l:
        if isinstance(item, (list, tuple)): 
            flatten(item)
        else:
            new_l.append(item)
     return new_l

print(flatten(liste))