
# somme

def somme(n) : 
    somme = 0 
    for i in range(1,n+1) : 
        somme += i 
    return somme

# racine 

def suivant(n, a) : 
    n = (n + (a / n))/2
    return(n)

def racine(n) : 
    x0 = (1+n)/2
    while abs(((suivant(x0,n) - x0)) / x0) > 10**-5 :
        x0 = suivant(x0,n)
    return x0

# suites 

def suites(n) : 
    u0 = 0.25
    v0 = 0.5
    un_sv = v0 + u0
    vn_sv = un_sv - v0
    for _ in range(n - 1) : 
        un_sv = vn_sv + un_sv
        vn_sv = un_sv - vn_sv
    return un_sv

def fibonnacci(n) : 
    f0 = 0 
    f1 = 1
    for _ in range(n) : 
        (f1,f0) = (f1 + f0, f1)
    return f1

def triangles(n) :
    etoile = "*" 
    longeur = n * 2 - 1 
    for _ in range(1,n + 1) : 
        espace = " " * ((longeur - len(etoile)) // 2)
        print(f"{espace}{etoile}")
        etoile += "*" * 2

def triangles_point(n) :
    etoile = "*" 
    longeur = n * 2 - 1 
    for _ in range(1,n + 1) : 
        espace = " " * ((longeur - len(etoile)) // 2)
        point = "." * ((longeur - len(etoile)) // 2)
        print(f"{point}{etoile}{espace}")
        etoile += "*" * 2

def croix(n) : # pas fini 
    for i in range(n) :
        centre = "." * (i - 2) 
        cote = "." * (i - (2 + len(centre)))
        print(f"{cote}*{centre}*{cote}")


def sapins(n) : #pas fini 
    espace = " " * (n - 1)
    for i in range(n) : 
        print(f"{triangles(i)}")
    for i in range(1,n + 1) : 
        print(f"{espace}|")
    
def base_2(n) :
    nb = ""
    while n // 2 != 0 : 
        nb = str(n%2) + nb
        n = n // 2
    nb = str(n%2) + nb
    return nb



    