import random
list_a = ['0','1','2','3','4','5','6','7','8','9']
list_c = ['!','@','$','%','^','&','?','/','<','>','[',']','{','}','|','|',':',';','.',',','`']

list_b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def fmain(offset):
    password=[]
    password_massiv = []
    result = []
    var = ''
    if offset >= 4:
        for i in range(offset):
            G = cheng(list_a, list_b, list_d, list_c, offset)             
            password.append(G)
        for i in range(len(password)): 
            password_list = (list(password[random.randint(0, offset-1)][random.randint(0,3)]))
            password_massiv.append(password_list)
        
        for sublist in password_massiv:
            for item in sublist:
                result.append(item)
        genir = ''
        for i in result:
            genir+=i
        return(genir)
    else:
        return False
            

def cheng(list_a, list_b, list_d, list_c, simvol):
    mas=[]
    for i in range(1):
        i=i+1
        a = random.choice(list_a)
        b = random.choice(list_b)
        d = random.choice(list_d)
        c = random.choice(list_c)
        mas.append(a)
        mas.append(b)
        mas.append(d)
        mas.append(c)
    return mas