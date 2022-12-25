#PYTHON PROJECT
#Name: Adhil Rumais
#Submission date : 4 September 2020
import pickle
import csv
import random
try:
    import imdb
except:
    f=open("Rules.txt",'r')
    for i in range(3):
        f.readline()
    for i in range(7):
        print(f.readline())
    print("For the program to perform all its functions, install imdbpy and run the program again.Else, continue")

def signin():
    while True:
        c=0
        nm=input("Enter username: ")
        pp=input("Enter password: ")
        with open('Signin.csv','r') as f:
            r=csv.reader(f)
            next(r)
            for i in r:
                if nm==i[0] and pp==i[1]:
                    c+=1
                    print("Successfully logged in. Welcome " + nm)
                    return c
                    break
            else:
                print("Data entered is incorrect")
                ch=input("Do you want to retry?(Y/N): ")
                if ch=='Y':
                    continue
                else:
                    break
            break
def signup():
    with open('Signin.csv','r') as f:
        r=csv.reader(f)
        next(r)
        while True:
            nm=input("Enter a username: ")
            for i in r:
                if nm==i[0]:
                    print("Username already taken. Try a different name.")
                    break
            else:
                break
    with open('Signin.csv','r') as f:
        r=csv.reader(f)
        next(r)
        while True:
            n=input("Enter a unique ID PIN: ")
            for i in r:
                if n==i[2]:
                    print("ID PIN already taken. Try a different one.")
                    break
            else:
                break
    f.close()
    while True:
        pp=input("Enter a password with a minimum of 4 characters: ")
        if len(pp)<4:
            print("Weak password. Try again")
            continue
        else:
            break
    with open("Signin.csv",'a',newline='') as f:
        w=csv.writer(f)
        w.writerow([nm,pp,n])
    print("Your account has been successfully created. Login with your new account\n")
def forgot_pass():
    
    with open('Signin.csv','r') as f:
        r=csv.reader(f)
        next(r)
        while True:
            idn=input("Enter user name: ")
            idp=input("Enter the ID PIN: ")
            for i in r:
                if idp==i[2] and idn==i[0]:
                    p=input("ID PIN is correct. Please enter a new password: ")
                    with open('Signin.csv','r') as l:
                        r=csv.reader(l)
                    
                        with open('Signin tempo.csv','w',newline='') as g:
                            w=csv.writer(g)
                            for k in r:
                                if idp==k[2]:
                                    k[1]=p
                                    w.writerow(k)
                                else:
                                    w.writerow(k)
                    with open('Signin tempo.csv','r') as h:
                        r=csv.reader(h)
                        with open('Signin.csv','w',newline='') as i:
                            w=csv.writer(i)
                            for j in r:
                                w.writerow(j)
                    print("Password reset successfully. Please login with your account\n")
                    break
            else:
                print("Incorrect ID PIN")
                cp=input("Do you want to try again(Y/N)?: ")
                if cp=='N':
                    break
            break
def case(x):
    x2=x.split(',')
    x1=''
    for j in x2:        
        x1+=j[0].upper()
        l=len(j)
        k=0
        for i in range(1,l):
            n=j[i]
            if k==1:
                x1+=n.upper()
            elif not n.isspace():
                x1+=n.lower()
            k=0
            if n.isspace():
                x1+=n
                k=1
            
            
        x1+=','
    ln=len(x1)
    x=x1[0:ln-1]
    return x
chh=input("Do you want data unedited by previous users?(y/n)")
if chh=='y':
    with open('Film data.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['Film name','Year','Language','Genre','Main actors'])
        w.writerow(['Lucifer','2019','Malayalam','Action','Mohanlal,Prithviraj,Tovino',])
        w.writerow(['Mayavi','2007','Malayalam','Action,Thriller','Mammootty,Salim Kumar'])
        w.writerow(['Inception','2003','English','Thriller,Mystery','Leonardo Dicaprio'])
        w.writerow(['Interstellar','2010','English','Thriller,Mystery','Matthew McConaughey,Anne Hatheway'])
        w.writerow(['Trance','2020','Malayalam','Drama,Thriller','Fahad Fazil,Soubin Shahir'])
        w.writerow(['Chotta Mumbai','2006','Malayalam','Comedy,Drama','Mohanlal,Bhavana'])
        w.writerow(['Rajamanikyam','2007','Malayalam','Comedy,Drama','Mammootty,Rahman'])
        w.writerow(['Varathan','2015','Malayalam','Action,Thriller','Fahad Fazil,Aiswarya Lakshmi'])
        w.writerow(['Njan Prakashan','2018','Malayalam','Comedy','Fahad Fazil,Srinivaasan'])
        w.writerow(['Amen','2010','Malayalam','Comedy,Drama','Fahad Fazil'])
    with open('Signin.csv','w',newline='') as f:
        r=csv.writer(f)
        r.writerow(['USERNAME','PASSWORD','ID PIN'])
        w=(['Adhil','1234','9999'],['Allen','1235','0002'],['John','1236','0003'])
        for i in range(2):
            r.writerow(w[i])
    f=open("English.dat",'wb')
    dict1={'High budget':170000000,'Medium budget':80000000,'Low budget':30000000}
    dict2={'High budget':200000000,'Medium budget':110000000,'Low budget':20000000}
    dict3={'High budget':200000000,'Medium budget':130000000,'Low budget':18000000}
    dict4={'Simple':1000000,'Complex':3500000}
    list1=['Cinematography',2700000,'Junior artists',1500000,'Songs',167000]
    pickle.dump(dict1,f)
    pickle.dump(dict2,f)
    pickle.dump(dict3,f)
    pickle.dump(dict4,f)
    pickle.dump(list1,f)
    f.close()
    f=open("Malayalam.dat",'wb')
    dict1={'High budget':10000000,'Medium budget':7500000,'Low budget':5000000}
    dict2={'High budget':20000000,'Medium budget':10000000,'Low budget':5000000}
    dict3={'High budget':10000000,'Medium budget':7500000,'Low budget':6000000}
    dict4={'Simple':25000,'Complex':50000}
    list1=['Cinematography',100000,'Junior artists',100000,'Songs',10000]
    pickle.dump(dict1,f)
    pickle.dump(dict2,f)
    pickle.dump(dict3,f)
    pickle.dump(dict4,f)
    pickle.dump(list1,f)
    f.close()
    f=open("Tamil.dat",'wb')
    dict1={'High budget':8000000,'Medium budget':7500000,'Low budget':4500000}
    dict2={'High budget':20000000,'Medium budget':3000000,'Low budget':900000}
    dict3={'High budget':10000000,'Medium budget':5000000,'Low budget':3000000}
    dict4={'Simple':10000,'Complex':30000}
    list1=['Cinematography',75000,'Junior artists',35000,'Songs',7500]
    pickle.dump(dict1,f)
    pickle.dump(dict2,f)
    pickle.dump(dict3,f)
    pickle.dump(dict4,f)
    pickle.dump(list1,f)
    f.close()
    f=open("Hindi.dat",'wb')
    dict1={'High budget':50000000,'Medium budget':25000000,'Low budget':5000000}
    dict2={'High budget':45000000,'Medium budget':20000000,'Low budget':7000000}
    dict3={'High budget':40000000,'Medium budget':15000000,'Low budget':6500000}
    dict4={'Simple':37000,'Complex':65000}
    list1=['Cinematography',250000,'Junior artists',170000,'Songs',30000]
    pickle.dump(dict1,f)
    pickle.dump(dict2,f)
    pickle.dump(dict3,f)
    pickle.dump(dict4,f)
    pickle.dump(list1,f)
    f.close()
#main


print("*"*70+"WELCOME TO FILM DIRECTORY 2020"+"*"*67)
f=open("Rules.txt",'r')
f.seek(0)
for i in range(3):
    print(f.readline(),end='')
print("\n1. Sign in")
print("2.Forgot Password")
print("3. New Member")
ch=int(input("Enter the number corresponding to your choice: "))
if ch==1:
    c=signin()
elif ch==2:
    forgot_pass()
    '\n'
    c=signin()
elif ch==3:
    signup()
    c=signin()
if c>=1:
    while True:
        print("\nWhat action among those given below would you like to perform?")
        print('\t1.Search for a film')
        print('\t2.Modify the directory')
        print('\t3.To display films of a particular category')
        print('\t4.Basic calculator for production cost')
        print('\t5.Find the rating of any film')
        print('\t6.Test your knowledge')
        print("\t7.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            while True:
                n=input("\nEnter film name: ")
                n=case(n)
                with open("Film data.csv",'r') as f:
                    r=csv.reader(f)
                    next(r)
                    for i in r:
                        if n in i[0]:
                            lst1=['Film name','Year','Language','Genre','Main actors']
                            print("\nFilm is present in the directory")
                            for j in range(5):
                                print(lst1[j]+' : '+i[j])
                            break
                    else:
                        print("\nFilm not present in the directory")
                ch1=input("Do you want to search for another film(y/n)?")
                if ch1=='n':
                    break
        elif ch==2:
            while True:
                print("1.Add details of a film")
                print("2.Delete a film")
                print("3.Modify the details of a film")
                print("4.Go to main menu")
                ch2=int(input("Enter the number corresponding to your choice: "))
                if ch2==1:
                    while True:
                        with open("Film data.csv",'a',newline='') as f:
                            w=csv.writer(f)
                            nf=input("Enter name of film: ")
                            nf=case(nf)
                            ny=input("Enter year: ")
                            ny=case(ny)
                            nd=input("Enter language: ")
                            nd=case(nd)
                            ng=input("Enter genre: ")
                            ng=case(ng)
                            na=input("Enter the names of main actor(s): ")
                            na=case(na)
                            l=[nf,ny,nd,ng,na]
                            w.writerow(l)
                        print("\nFilm succesfully entered")
                        ch3=input("\nDo you want to add another film(y/n)?")
                        if ch3=='n':
                            break
                    continue
                elif ch2==2:
                    while True:
                        with open('Film data.csv','r') as f:
                            r=csv.reader(f)
                            with open('Film data tempo.csv','w',newline='') as g:
                                w=csv.writer(g)
                                nf=input("Enter film name to be deleted: ")
                                nf=case(nf)
                                for k in r:
                                    if nf==k[0]:
                                        continue
                                    else:
                                        w.writerow(k)
                        with open('Film data tempo.csv','r') as h:
                                r=csv.reader(h)
                                with open('Film data.csv','w',newline='') as i:
                                    w=csv.writer(i)
                                    for j in r:
                                        w.writerow(j)
                        print("\nFilm succesfully deleted from the directory")
                        ch4=input("\nDo you want to delete another film(y/n)? ")
                        if ch4=='n':
                            break
                elif ch2==3:
                    while True:
                        with open('Film data.csv','r') as f:
                            r=csv.reader(f)
                            with open('Film data tempo.csv','w',newline='') as g:
                                w=csv.writer(g)
                                nf=input("Enter name of film whose details are to be modified: ")
                                nf=case(nf)
                                d=input("Enter which detail(s) you want to change: ")
                                d=case(d)
                                dn=input("Enter the new detail(s) seperated by comma(If there are more than 1 details for a category,enclose it in brackets): ")
                                dn=case(dn)
                                d1=d.split(',')
                                dn1=dn.split(',')
                                lst1=['Film name','Year','Language','Genre','Main actors']
                                c=0
                                for k in r:
                                    if nf==k[0]:
                                        for p in range(len(d1)):
                                            for i in range(5):
                                                if c>=1:
                                                    n=p+1
                                                else:
                                                    n=p
                                                if d1[p]==lst1[i]:
                                                    if '(' in dn1[n] or ')' in dn1[n]:
                                                        ss=dn1[n]+','+dn1[n+1]
                                                        k[i]=ss
                                                        c+=1
                                                    else:    
                                                        k[i]=dn1[n]
                                                    if '(' in k[i] or ')' in k[i]:
                                                        s=ss[1:len(ss)-1]
                                                        k[i]=s[0].upper()+s[1:len(s)]
                                                    break
                                        w.writerow(k)
                                    else:
                                        w.writerow(k)
                        with open('Film data tempo.csv','r') as h:
                                r=csv.reader(h)
                                with open('Film data.csv','w',newline='') as i:
                                    w=csv.writer(i)
                                    for j in r:
                                        w.writerow(j)
                        print("\nFilm details successfully modified")
                        ch4=input("\nDo you want to modify another film(y/n)? ")
                        if ch4=='n':
                            break
                    continue
                else:
                    break
        elif ch==3:
            while True:
                c=input("Enter the category under which you want the data to be sorted: ")
                c=case(c)
                cn=input("Specify the " + c)
                cn=case(cn)
                lst1=['Film name','Year','Language','Genre','Main actors']
                with open('Film data.csv','r',) as f:
                    r=csv.reader(f)
                    for i in range(5):
                        if c==lst1[i]:
                            print('The films with '+ c +' ' + cn +' ' + 'are: \n')
                            with open('Film data.csv','r',) as g:
                                r1=csv.reader(g)
                                for j in r1:
                                    if cn in j[i]:
                                         print('  '+j[0])
                                break
                    ch4=input("\nDo you want to sort films again?(y/n) ")
                    if ch4=='n':
                        break
        elif ch==4:
            while True:
                s=0
                c=input("Specify the language of the industry: ")
                c=case(c)
                cn=c+'.dat'
                f=open(cn,'rb')
                l=['Director','Actor(s)','Actress(s)']
                st='\nCategory\t\t|Cost\n'
                st=st+'.'*35+"\n\n"
                ch=input("Enter your range of budget(High/Medium/Low): ")
                ch=case(ch)
                for i in range(3):
                    st=st+l[i]
                    dict1=pickle.load(f)
                    for k in dict1:
                        if k==(ch+" budget"):
                            n=dict1[k]
                            break
                    if i>0:
                        c=int(input("Number of "+l[i]))
                        n=n*c
                    s+=n
                    st=st+'\t\t|'+str(n)+'\n'
                ch=input('VFX(Y/N)')
                if ch=='Y':
                    dict2=pickle.load(f)
                    print("1.Simple VFX work")
                    print("2.Complex VFX work")
                    ch1=input("Enter the number corresponding to your choice: ")
                    for i in dict2:
                        if ch1=='1':
                            ch1='Simple'
                        else:
                            ch1='Complex'
                        if i==ch1:
                            st=st+ch1+' VFX work'+' '*8+'|'+str(dict2[i])+'\n'
                            s+=dict2[i]
                            break
                elif ch=='N':
                    dict2=pickle.load(f)
                list1=pickle.load(f)
                for i in range(0,len(list1),2):
                    if i!=4:
                        st=st+str(list1[i])+'\t\t|'+str(list1[i+1])+'\n'
                        s+=list1[i+1]
                    elif i==4:
                        ns=int(input("Number of songs: "))
                        nn=list1[i+1]
                        st=st+"Songs"+'\t\t        |'+str(nn*ns)+'\n'
                        s+=nn*ns
                st+='\nTOTAL\t\t\t|'+str(s)
                print(st)
                '\n'
                ch5=input("Do you want to calculate the budget again?(y/n): ")
                if ch5=='n':
                    break
        elif ch==5:
            c=0
            try:
                moviesDB=imdb.IMDb()
            except:
                print("imdbpy module is not installed.So this feature is not available")
                c+=1
            if c==0:
                while True:
                    try:
                        print("An interent connection is required")
                        moviesDB=imdb.IMDb()
                        n=input("\nEnter name of film: ")
                        n=case(n)
                        l=input("Enter language: ")
                        l=case(l)
                        movies=moviesDB.search_movie(n)
                        c=0
                        print("Searhing for the rating.....\n"
                              "Please wait for a few seconds")
                        for i in movies:
                            title=i['title']
                            id = movies[c].getID()
                            movie=moviesDB.get_movie(id)
                            if movie['languages']==[l]:
                                print(n+'('+str(movie['year'])+')'+' : '+str(movie['rating']))
                                break
                            else:
                                c+=1
                    except:
                        print("\nRating not registered")
                    ch4=input("\nDo you want to continue(y/n)?: ")
                    if ch4=='n':
                        break
        elif ch==6:
            print("\nClues will be given in a few rounds")
            print("If the guess is correct, number of choices won't be deducted\n")
            while True:
                with open("Film data.csv",'r') as f:
                    w=csv.reader(f)
                    next(w)
                    l=0
                    for i in w:
                        l+=1
                n=random.randint(0,l-1)
                c=''
                with open("Film data.csv",'r') as g:
                    w1=csv.reader(g)
                    next(w1)
                    for j1 in w1:
                        if n>=0:
                            c=j1[0]
                            ln=[j1[1],j1[2],j1[3],j1[4]]
                            n=n-1
                    cn=len(c)
                    if ' ' in c:
                        cn=cn-1
                        r=cn+1
                    else:
                        r=cn
                    a=[]
                    print("\t",end='')
                    for i in range(r):
                        if c[i] in "AEIOUaeiou ":
                            s=c[i]
                            s1=s.upper()
                        else:
                            s1="__"
                        a.append(s1)
                    '\n'
                    if r>8:
                        ran=9
                        constant=9
                    else:
                        ran=5
                        constant=5
                    p=20*ran
                    while ran!=1:
                        t=0
                        for j in a: 
                            print("\t"+j+"  ",end='')
                        for j in a:
                            if j.isalpha():
                                t+=1
                        if t==cn:
                            break
                        print("\nChoices left: "+str(ran-1))
                        if ran==constant-1:
                            print("Clue: Language is "+ln[1])
                        if ran==constant-3:
                            print("Clue: Main actors are "+ln[3])     
                        ans=input("\nEnter an alphabet:")
                        k=0
                        for j in range(r):
                            a1=c[j]
                            if ans.lower()==a1.lower():
                                k+=1
                                a.insert(j,ans.upper())
                                a.pop(j+1)
                            if j==(r-1):
                                break
                        if k>=1:
                            print("Correct choice")
                            print("Points available=",p)
                        else:
                            print("Incorrect answer")
                            p=p-20
                            print("Points available=",p)
                            ran=ran-1
                    if '__' not in a:
                        print("\nYou win. The name of the movie is "+c)
                        print("You got"+str(p)+"points")
                    else:
                        print("\nYou lose")
                        print("The name of the movie was "+c)

                ch4=input("\nDo you want to continue(y/n)?: ")
                if ch4=='n':
                    break
        elif ch==7:
            break
    
                
        

    
