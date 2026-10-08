#comparison operator
# a = 10
# b = 15 
# print(a==b)

#not equal to
# a = 10
# b = 15
# print(a!=b)

#greater than
# a = 5 
# b = 10
# print(a>b)

#less than
# a = 5 
# b = 10
# print(a>b)

#greater than equal to
# a = 10
# print(a>=10)

#greater than
# a = 10
# b = 15
# print(a>b)

#int
# a = 10
# print(type(a))

#string
# name = 'hello'
# print(type(name))

#boolean
# c = True
# print(type(c))

#float
# d = 10.34
# print(type(d))


# a = 'hanan'
# print(a.capitalize())

# c = 'hanan'
# print(c.lower())

# lt = ['index',10,'python',10.90]
# print(lt[2])
# print(lt[3])
# print(lt[1])
# print(lt[0])
# print(lt[1:3])


# pt =['wasiq',12,15,20,30,40,50,70,80,'hanan','python',True,25,'python',35,45,'close',45,False,18]
# pt[0] = 'rubhan' #here we updated
# pt.remove(12)

# pt.pop(7)

# pt.insert(1,'himayun')



# print(pt)


# dt ={
#     "name":"rubhan",
#     "roll no" : 21,
#     "country" : "kashmir",

    




# }


# dt['pin-code'] = 190001

# del dt["roll no"]

# print(dt)

# lt=['python',12,True,20,'laptop','hp',50,'index']
# print(lt[1:])
# print(lt[:-1])
# print(lt[::2])
# print(lt[-1])
# print(lt[-2])
# print(lt[:-2])


# a = 10
# b = 15
# a,b=b,a
# print(a,b)

# a=10
# print(type(a))

# a='rubhan'
# print(type(a))

# a=10.20
# print(type(a))

# a=True
# print(type(a))

# a=10
# b=5
# c=a+b
# print(c)

# a=10
# b=5
# c=a-b
# print(c)

# a=10
# b=5
# c=a*b
# print(c)


# a=10
# b=2
# c=a/b
# print(c)

# lt=[['python',12,True],['index',15,True]]
# lt[1].insert(1,'himayun')
# del lt[0][1]
# lt[1].pop(1)

# print(lt)


# lt=[['python',10,True],['index',20,False]]
# del lt[0][1]



# lt=[[['rubhan',15,True],['hanan',20,False]],[['python',15,'dell'],['khan',30,]],[['himayun',25,'khan'],['core',35,'khan']]]

# print(lt[1][0][1])
# print(lt[2][0][0])
# print(lt[1][0][0])

# del lt[0][0][0]
# lt[0][0].insert(0,'Wasiq')


# print(lt)



# lt=[[['wasiq',10,True],['malik',20,False]], [['python',30,'case'],['umar',40,'khan']],[['asif',50,'index'],['abid',55,'term']]]
# print(lt[1][0][1])
# print(lt[2][0][1])
# print(lt[2][1][2])
# print(lt[0][1][2])
# print(lt[1][0][1])

# lt[1][0].append('ali')
# lt[0][0].insert(3,'salim')
# lt[1][1].append('abdul')
# lt[1][1].insert(1,'mary')
# lt[1][1].pop(1)
# lt[0][0].pop(0)
# lt[0][0][0]='hamza'




# print(lt)

# dt = {
#     '1':{'name':'wasiq','Roll_no':20},
#     '2':{'name':'hanan','Roll_no':30}

# }
# dt['1']['name']='Rubhan'
# dt['1']['roll_no']='40'






# print(dt)

# dt = {
#     '1':{'name':'rubhan','Roll_no':20},
#     '2':{'name':'wasiq','Roll_no':30}

# }
# dt['1']['name']='umer'
# dt['1']['Roll_no']=40




# print(dt)


# lt =[[['Rubhan',10,True],['Hanan',20,False]],[['Wasiq',30],['Khan',40,]],[['Khan,50'],['Malik',55,]]]



# print(lt[1][1][0])
# print(lt[1][1][1])
# print(lt[1][0][1])
# lt[1][0].append('ali')
# lt.pop(1)
# lt.pop(2)




# print(lt)

# dt = {
#     1:{'name':{'rubhan'},'adress':{'sgr'}},
#     2:{'name':{'wasiq'},'adress':{'pul'}},
#     3:{'name':{'hanan'},'adress':{'kash'}},





# }

# print(dt)
# dt[1]['name']='asif'
# dt[2]['adress']="bud"
# del dt[1]

# print(dt)


# n1 = float(input("enter a number:-"))
# op = input('enter an operator:-(+,-,/)')
# n2 = float(input("enter a number:-"))

# if op == '+':
#     print(n1+n2)
# elif op == '-':
#     print(n1-n2)
# elif op == '/':
#     print(n1/n2)



# tab = int(input("enter a number:-"))

# for i in range(1,11):
#     res = tab*i
#     print(tab,'x',i,'=',res)



# b_age = int(input("enter your age:-"))
# g_age = int(input("enter your age:-"))

# if b_age>18 and g_age>21:
#     print("you are welcome")
# else:
#     print("you are not")



# prime number

\
# n = int(input('enter a number:-'))

# if n<=1:
#     print('not prime')
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print('not prime')
#             break
#     else:
#         print('prime number')

# try
#     a = 20
#     print type a)
# except SyntaxError:
#     print('incorrect Syntex')

# try:
#     a = 10
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print('cant be divided by zero')

# int error
# try:
#     age = int("twenty")
# except ValueError:
#     print('invalid value for int')

# dictionary error
# try:
#     dt={"name":'hanan', "Roll_no":20}
#     print(dt["adress"])
# except KeyError:
#     print('key not defined')

# try:
#     pt = (10,20)
#     pt[0] = 50
# except TypeError:
#     print('tuple cant be changed ')

# class ils:
#     def python(self):
#         print("this class is python")

#     def java(self):
#         print("this class is java")

#     def excel():
#         print("this class is excel")

# i=ils()
# i.python()
# i.java()



# class ils:
#     def aa(self):
#         print("this is from A")

#     def bb(self):
#         print("this is from B")

#     def cc(self):
#         print("this is from C")

# i=ils()
# i.aa()
# i.bb()

# class A:
#     def aa(self):
#         print("this is from A")
    
# class B(A):
#     def bb(self):
#         print("this is from B")

# i=B()
# i.aa()
# i.bb()

# class A:
#     def aa(self):
#         print("this is from A")

# class B(A):
#     def bb(self):
#         print("this is from B")

# class C(B):
#     def cc(self):
#         print("this is from C")

# i=C()
# i.aa()
# i.bb()
# i.cc()


# polymorphism

# class animal :
#     def speak(self):
#         print("an animal makes sounds")

# class cat:
#     def speak(self):
#         print("a cat meows")

# i=animal()
# f=cat()
# i.speak()
# f.speak()

# class ils:
#     def institute(self):
#         print('this is ils')

# class tech(ils):
#     def institute(self):
#         super().institute()
#         print("this is a branch")

# t=tech()
# t.institute()

# class ils:
#     def __init__(self):
#         print("this is from instructor")
#         self.__fee()

#     def hello(self):
#         print("this is from public")

#     def _bye(self):
#         print("this is from protected")

#     def __fee(self):
#         print("this is from private")

# i=ils()
# i.hello()
# i._bye()

# a = 250
# b = 250
# print(a is b)

# a = 302
# b = 302
# print(a is b)

# a =[1,2,3,4]
# b = 2
# print(b in a)

# class A:
#     def ok(self):
#         print("this is from A")

# class B:
#     def ok(self):
#         print("this is from B")

# class C(A,B):
#     pass

# c =C()
# print(C.mro())


# f = open('file.txt','w')
# f.write('Hello World')
# f.close()


# f = open('file.txt','r')
# dt = f.read()
# print(dt)


# f = open('file.txt','a')
# f.write(' im in file handling')
# f.close


# f = open(r'C:\Users\DELL\Desktop\file.txt',"w")
# f.write("Hello World")
# f.close()

# from index2 import add
# print(add(12,20))


# a=10
# b=15
# print(a+b)

# a=10
# b=15
# c= a.__add__(b)
# print(c)

































