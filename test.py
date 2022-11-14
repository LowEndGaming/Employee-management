from datetime import date
import mysql.connector as msql
cn=msql.connect(host='localhost',user='root',passwd='lowend')
if cn.is_connected():
    print('Connection has been established between Python and Mysql')
    print('Welcome to Employee Data Management System')
cur=cn.cursor()
cur.execute('create database if not exists emp')
cur.execute('use emp')
cur.execute('create table if not exists empl(eid integer primary key,ename varchar(20) not null,sal integer not null,Job varchar(20) not null,date date)')
cur.execute('create table if not exists perd(eid integer primary key,ename varchar(20) not null,Pno int8 not null,addr varchar(50),gen char(1))')
def addemp():
    cur.execute("select * from empl")
    d=cur.fetchall()
    print('*'*20,'ADD EMPLOYEEE','*'*20)
    f=0
    while True:
        fg=1
        n=int(input('Enter Employee ID(integer values):'))
        for i in range(len(d)):
            if d[i][0]==n:
                fg=0
                print('Employee ID already exists.Try again.')
        if fg==1:
            break
    e=input('Enter Employee Name:')
    s=int(input('Enter Employee Salary:'))
    j=input("Enter the Employee's Job:")
    m=int(input("Enter Employee's Phone number:"))
    while True:
        o=input("Enter Employee's Gender(m/f):")
        if o.lower() in 'MmFf':
            break
        print('Not valid data. Gender should be m or f. Try again')
    t=input('Enter Employee Address(Nearest city):')
    g=date.today()
    if f==0:
        cur.execute("insert into empl values(%s,%s,%s,%s,%s)",(n,e,s,j,g))
        cur.execute("insert into perd values(%s,%s,%s,%s,%s)",(n,e,m,t,o))
        cn.commit()
        print('Data on Employee:',e,' has been added succefully.')
        print('The Employee ID of Employee',e,'is',n)
        print('')
def delemp():
    print('*'*20,'DELETE EMPLOYEEE','*'*20)
    f=0
    n=int(input('Enter the Employee ID of Employee Data You Want to Delete:'))
    cur.execute("select * from empl")
    d=cur.fetchall()
    for i in range(len(d)):
        if d[i][0]==n:
            f=1
            cur.execute('delete from empl where eid=%s',(n,))
            cur.execute('delete from perd where eid=%s',(n,))
            cn.commit()
            print('Employee data has been Deleted')
    if f==0:
        print('Data on Employee ID',n,'does not Exist')
    print('')
def altemp():
    f=0
    n=int(input('Enter Employee ID whose data You Want to Change:'))
    cur.execute("select * from empl")
    d=cur.fetchall()
    for i in range(len(d)):
        if d[i][0]==n:
            f=1
    if f==0:
        print('No Data on given Employee ID exist.')
    if f==1:
        while True:
            print('*'*20,'ALTER EMPLOYEEE','*'*20)
            print('1.Change Employee Name'.center(57))
            print('2.Change Employee Salary'.center(57))
            print('3.Change Employee Job:'.center(57))
            print('4.Change Employee Address:'.center(57))
            print('5.Change Employee Phone Number:'.center(57))
            print('6.Change Employee Gender:'.center(57))
            print('7.Exit from Altering data'.center(57))
            print('*'*57)
            h=int(input('Enter your Choice:'))
            if h==1:
                na=input('Enter New Employee Name:')
                cur.execute('update empl set ename=%s where eid=%s',(na,n))
                cur.execute('update perd set ename=%s where eid=%s',(na,n))
                print('The Employee name has been changed to',na)
                cn.commit()
            elif h==2:
                s=int(input('Enter New Employee Salary:'))
                cur.execute('update empl set sal=%s where eid=%s',(s,n))
                print('The Employee salary has been changed to',s)
                cn.commit()
            elif h==3:
                k=input('Enter New Employee Job:')
                cur.execute('update empl set Job=%s where eid=%s',(k,n))
                print('The Employee Job has been changed to',k)
                cn.commit()
            elif h==4:
                l=input('Enter New Employee Address:')
                cur.execute('update perd set addr=%s where eid=%s',(l,n))
                print('The Employee Address has been changed to',l)
                cn.commit()
            elif h==5:
                d=int(input('Enter New Employee Phone Number:'))
                cur.execute('update perd set Pno=%s where eid=%s',(d,n))
                print('The Employee Phone number has been changed to',d)
                cn.commit()
            elif h==6:
                while True:
                    m=input("Enter Employee's Gender(m/f):")
                    if m.lower() in 'MmFf':
                        break
                    print('Not valid data. Gender should be m or f. Try again')
                cur.execute('update perd set Gen=%s where eid=%s',(m,n))
                print('The Employee Gender has been changed to',m)
                cn.commit()
            elif h==7:
                return
            else:
                print('Choice not found. Try again')
    print('')
def viemp():
    print('*'*20,'VIEW EMPLOYEEE','*'*20)
    print('1.View All Employee Data'.center(56))
    print('2.View Employee Based on ID'.center(56))
    print('3.View Employee Based on Name'.center(56))
    print('4.View Employee Based on Salary'.center(56))
    print('5.View Employee Based on Address'.center(56))
    print('6.View Employee Based on Job'.center(56))
    print('7.View Employee Based on Data of entry'.center(56))
    print('8.View Employee Based on Phone number'.center(56))
    print('9.View Employee Based on Gender'.center(56))
    print('10.Exit after Viewing Data'.center(56))
    print('*'*56)
    j=int(input('Enter your choice:'))
    if j==1:
        cur.execute("select * from empl")
        d1=cur.fetchall()
        cur.execute("select * from perd")
        d2=cur.fetchall()
        if len(d1)==0:print('No Employee Data Exist')
        for i in range(len(d1)):
            print('**********Employee ID:',d1[i][0],'**********')
            print("Employee's ID:",str(d1[i][0])+(" "*(30-len(str(d1[i][0])))),"Employee's Name:",d1[i][1])
            print("Employee's Salary:",str(d1[i][2])+(" "*(26-len(str(d1[i][2])))),"Employee's Date of entry:",d1[i][4])
            print("Employee's Job:",d1[i][3]+(" "*(29-len(str(d1[i][3])))),"Employee Address:",d2[i][3])
            print("Employee Phone number:",str(d2[i][2])+(" "*(23-len(str(d2[i][2])))),end='')
            if d2[i][4] in 'Mm':
                print('Employee Gender:Male')
            if d2[i][4] in 'Ff':
                print('Employee Gender:Female')
        print('')
        return
    elif j==2:
        k=int(input('Enter ID of Employee Data You Want To View:'))
        cur.execute("select * from empl where eid=%s",(k,))
        d1=cur.fetchall()
        cur.execute("select * from perd where eid=%s",(k,))
        d2=cur.fetchall()
    elif j==3:
        d2=[]
        k=input('Enter Name of Employee Data You Want To View:')
        cur.execute("select * from empl where ename=%s",(k,))
        d1=cur.fetchall()
        for i in range(len(d1)):
            cur.execute("select * from perd where eid=%s",(d1[i][0],))
            d3=cur.fetchall()
            d2.extend(d3)
    elif j==4:
        k=int(input('Enter Salary of Employee Data You Want To View:'))
        d2=[]
        cur.execute("select * from empl where sal=%s",(k,))
        d1=cur.fetchall()
        for i in range(len(d1)):
            cur.execute("select * from perd where eid=%s",(d1[i][0],))
            d3=cur.fetchall()
            d2.extend(d3)
    elif j==5:
        k=input('Enter Address of Employee Data You Want To View:')
        d1=[]
        cur.execute("select * from perd where addr=%s",(k,))
        d2=cur.fetchall()
        for i in range(len(d2)):
            cur.execute("select * from empl where eid=%s",(d2[i][0],))
            d3=cur.fetchall()
            d1.extend(d3)
    elif j==6:
        k=input('Enter Job of Employee Data You Want To View:')
        d2=[]
        cur.execute("select * from empl where Job=%s",(k,))
        d1=cur.fetchall()
        for i in range(len(d1)):
            cur.execute("select * from perd where eid=%s",(d1[i][0],))
            d3=cur.fetchall()
            d2.extend(d3)
    elif j==7:
        k=input('Enter Date of Entry of Employee Data You Want To View(yyyy-mm-dd):')
        d2=[]
        cur.execute("select * from empl where date=%s",(k,))
        d1=cur.fetchall()
        for i in range(len(d1)):
            cur.execute("select * from perd where eid=%s",(d1[i][0],))
            d3=cur.fetchall()
            d2.extend(d3)
    elif j==8:
        k=int(input('Enter Phone number of Employee Data You Want To View:'))
        d1=[]
        cur.execute("select * from perd where Pno=%s",(k,))
        d2=cur.fetchall()
        for i in range(len(d2)):
            cur.execute("select * from empl where eid=%s",(d2[i][0],))
            d3=cur.fetchall()
            d1.extend(d3)
    elif j==9:
        k=input('Enter Gender of Employee Data You Want To View:')
        d1=[]
        cur.execute("select * from perd where gen=%s",(k,))
        d2=cur.fetchall()
        for i in range(len(d2)):
            cur.execute("select * from empl where eid=%s",(d2[i][0],))
            d3=cur.fetchall()
            d1.extend(d3)
    elif j==10:
        return
    else:
        print('No such Choice exist')
    if len(d1)==0:print('No Employee Data Exist')
    for i in range(len(d1)):
        print('*******Employee ID:',d1[i][0],'*******')
        print("Employee's ID:",str(d1[i][0])+(" "*(30-len(str(d1[i][0])))),"Employee's Name:",d1[i][1])
        print("Employee's Salary:",str(d1[i][2])+(" "*(26-len(str(d1[i][2])))),"Employee's Date of entry:",d1[i][4])
        print("Employee's Job:",d1[i][3]+(" "*(29-len(str(d1[i][3])))),"Employee Address:",d2[i][3])
        print("Employee Phone number:",str(d2[i][2])+(" "*(23-len(str(d2[i][2])))),end='')
        if d2[i][4] in 'Mm':
            print('Employee Gender:Male')
        if d2[i][4] in 'Ff':
            print('Employee Gender:Female')
    print('')
while True:
    print('*'*20,'MENU','*'*20)
    print('1.Add new employee data'.center(46))
    print('2.Delete employee id'.center(46))
    print('3.Alter employee data'.center(46))
    print('4.View employee data'.center(46))
    print('5.Exit'.center(46))
    print('*'*46)
    ch=int(input('Enter your choice:'))
    if ch==1:
        addemp()
    elif ch==2:
        delemp()
    elif ch==3:
        altemp()
    elif ch==4:
        viemp()
    elif ch==5:
        break
    else:
        print('Choice not found.Try again!')
