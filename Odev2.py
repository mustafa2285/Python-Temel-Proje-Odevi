liste = [[1, 2], [3, 4], [5, 6, 7]]

def tersliste(l):
       
    for item in l: 
        if isinstance(item, (list, tuple)):
            tersliste(item)

    l.reverse()       
        
    return l

print(tersliste(liste))