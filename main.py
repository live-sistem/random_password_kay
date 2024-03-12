import random
list_a = ['0','1','2','3','4','5','6','7','8','9']
list_c = ['!','@','$','%','^','&','?','/','<','>','[',']','{','}','|','|',':',';','.',',','`']

list_b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list_d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password=[]
password_massiv = []

def main():
    while True:
        user_ID = input()
        if user_ID == 'run' :
            simvol = int(input('Минимум 4 символа: '))
            if simvol >=4:
                for i in range(simvol):
                    G = cheng(list_a, list_b, list_d, list_c, simvol)             
                    password.append(G)

                for i in range(len(password)): 
                    password_list = (list(password[random.randint(0,9)][random.randint(0,3)]))
                    password_massiv.append(password_list)
                result = [] 
                for sublist in password_massiv:
                    for item in sublist:
                        result.append(item)
                genir = ''
                for i in result:
                    genir+=i
                print(genir)
            
            else:
                print("Слишком короткий")
                continue
        elif user_ID == '-h':
            print('star program write - "ran" ')
        elif user_ID == '-e': 
            print("ok")
            break
            

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

if __name__ == '__main__':
    main()