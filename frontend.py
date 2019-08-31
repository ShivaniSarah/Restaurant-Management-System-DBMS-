from tkinter import *
import backend
from PIL import ImageTk,Image



def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]

    selected_tuple=list1.get(index)
""" e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
"""

def recipe():
    list1.delete(0,END)
    list1.insert(END,"Recipeid,name,Cooking-time")
    
    list1.insert(END,backend.viewrecipe1(day.get(),meal.get())[0])
    
    list1.insert(END,"Ingredient,Quantity")
    
    for row in backend.viewrecipe2(day.get(),meal.get()):
        list1.insert(END,row)


def nutrition():

    list1.delete(0,END)
    cal=0
    carb=0
    prot=0
    fat=0
    ingred=[]
    row=[]
    nut=[]
    q=[]
    row=backend.viewrecipe(day.get(),meal.get())
    for i in range(0,len(row)):

       ingred=row[i][1]
       q=row[i][2]
       nut=backend.nvalue(ingred)

       cal+=(nut[0][1])*q
       carb+=(nut[0][2])*q
       prot+=(nut[0][3])*q
       fat+=(nut[0][4])*q
    string="calories="+str(cal)+",carb="+str(carb)+",prot="+str(prot)+",fat="+str(fat)
    list1.insert(END,string)

def checkstock():

     s=0
     row=backend.viewrecipe(day.get(),meal.get())
     for i in range(0,len(row)):
       ing=row[i][1]
       ing_quantity_required=row[i][2]
       tuple=(backend.viewingredient(ing))
       ing_quantity_exist=tuple[0][1]
       if(ing_quantity_required*no.get() >ing_quantity_exist):
           list1.delete(0,END)
           list1.insert(END,"WARNING:Stock is less.Can't prepare the food.")
           list1.insert(END,"Please click on 'Shop Detail' button")
           s=1
           break
     if(s==0):
         list1.delete(0,END)
         list1.insert(END,"ALL GOOD:Proceed To Cook.")
         list1.insert(END,"Please click on 'Update Stock' Button")

def updatestock():
     list1.delete(0,END)
     row=backend.viewrecipe(day.get(),meal.get())
     for i in range(0,len(row)):
       ing=row[i][1]
       ing_quantity_required=row[i][2]
       tuple=(backend.viewingredient(ing))
       ing_quantity_exist=tuple[0][1]
       flag=backend.update(ing,ing_quantity_exist-(ing_quantity_required*no.get()))
       list1.insert(END,flag)
       if(flag=="Done"):
        list1.insert(END,backend.viewingredient(ing))
def shopdetail():
     list1.delete(0,END)
     d=backend.shopdetail(day.get(),meal.get())
     for i in d:
      list1.insert(END,i)

def noofingredients():
    list1.delete(0,END)
    list1.insert(END,"No of ingredients are"+str(backend.noofingredients()[0]))

def clear():
    list1.delete(0,END)

def new_winF1(): # new window definition
    newwin = Toplevel(window)
    newwin.geometry('500x500')
    newwin.configure(background='#59253A')

    l1=Label(newwin,text="Ingredient_Name",bg='#59253A',fg='white')
    l1.grid(row=0,column=0,pady=(200,5),padx=900)

    ing=StringVar()
    e1=Entry(newwin,textvariable=ing)
    e1.grid(row=1,column=0)

    l2=Label(newwin,text="Quantity",bg='#59253A',fg='white')
    l2.grid(row=2,column=0)

    quan=IntVar()
    e2=Entry(newwin,textvariable=quan)
    e2.grid(row=3,column=0)


    l3=Label(newwin,text="Buying_date",bg='#59253A',fg='white')
    l3.grid(row=4,column=0)

    date1=StringVar()
    e3=Entry(newwin,textvariable=date1)
    e3.grid(row=5,column=0)


    l4=Label(newwin,text="Expiry_date",bg='#59253A',fg='white')
    l4.grid(row=6,column=0)

    date2=StringVar()
    e4=Entry(newwin,textvariable=date2)
    e4.grid(row=7,column=0)


    l5=Label(newwin,text="Family of Ingredient",bg='#59253A',fg='white')
    l5.grid(row=8,column=0)

    family=StringVar()
    e5=Entry(newwin,textvariable=family)
    e5.grid(row=9,column=0)

    list1=Listbox(newwin, height=3,width=100)
    list1.grid(row=10,column=0,rowspan=2,columnspan=2,pady=20)


    def addingredient():
      flag=backend.updateingredientaftershopping(ing.get(),quan.get(),date1.get(),date2.get(),family.get())
      list1.insert(END,flag)
      if(flag=="Done"):
        out=backend.viewingredient(ing.get())
        list1.insert(END,out)

    b1=Button(newwin,text="Add", width=12,command=addingredient)
    b1.grid(row=11,column=0,pady=(130,10))



def new_winF2(): # new window definition
    newwin = Toplevel(window)
    newwin.geometry('800x500')
    newwin.configure(background='light blue')


    l1=Label(newwin,text="INGREDIENTS",bg='#05386B',fg='white')
    l1.grid(row=0,column=0,padx=(50,0))

    l1=Label(newwin,text="RECIPIES",bg='#05386B',fg='white')
    l1.grid(row=0,column=6,padx=(50,0))

    l1=Label(newwin,text="SCHEDULE",bg='#05386B',fg='white')
    l1.grid(row=0,column=12,padx=(50,0))

    l1=Label(newwin,text="NUTRITION",bg='#05386B',fg='white')
    l1.grid(row=0,column=18,padx=(50,0))

    l1=Label(newwin,text="SHOPS",bg='#05386B',fg='white')
    l1.grid(row=3,column=18,padx=(50,0))

    l1=Label(newwin,text="RECIPE CATALOG",bg='#05386B',fg='white')
    l1.grid(row=0,column=24,padx=(50,0))





    list1=Listbox(newwin, height=70,width=60)
    list1.grid(row=1,column=0,rowspan=5,columnspan=5)
    sb1=Scrollbar(newwin)
    sb1.grid(row=1,column=5,rowspan=5)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list2=Listbox(newwin, height=70,width=60)
    list2.grid(row=1,column=6,rowspan=5,columnspan=5)
    sb2=Scrollbar(newwin)
    sb2.grid(row=1,column=11,rowspan=5)
    list2.configure(yscrollcommand=sb2.set)
    sb2.configure(command=list2.yview)

    list3=Listbox(newwin, height=70,width=60)
    list3.grid(row=1,column=12,rowspan=5,columnspan=5)
    sb3=Scrollbar(newwin)
    sb3.grid(row=1,column=17,rowspan=5)
    list3.configure(yscrollcommand=sb3.set)
    sb3.configure(command=list3.yview)

    list4=Listbox(newwin, height=35,width=60)
    list4.grid(row=1,column=18,rowspan=2,columnspan=5)
    sb4=Scrollbar(newwin)
    sb4.grid(row=1,column=23,rowspan=2)
    list4.configure(yscrollcommand=sb4.set)
    sb4.configure(command=list4.yview)

    list5=Listbox(newwin, height=35,width=60)
    list5.grid(row=4,column=18,rowspan=2,columnspan=5)
    sb5=Scrollbar(newwin)
    sb5.grid(row=4,column=23,rowspan=5)
    list5.configure(yscrollcommand=sb5.set)
    sb5.configure(command=list5.yview)


    list6=Listbox(newwin, height=70,width=50)
    list6.grid(row=1,column=24,rowspan=5,columnspan=5)
    sb6=Scrollbar(newwin)
    sb6.grid(row=1,column=29,rowspan=5)
    list3.configure(yscrollcommand=sb6.set)
    sb6.configure(command=list6.yview)

    list1.insert(END,"INCREDIENT QUANTITY B.DATE E.DATE FAMILY")
    for row in backend.show1():
     list1.insert(END,row)
     list1.insert(END,"\n")

    list2.insert(END,"NAME INGREDIENT QUANTITY COOKING_TIME")
    for row in backend.show2():
     list2.insert(END,row)
     list2.insert(END,"\n")

    list3.insert(END,"DAY RECIPIE_ID MEAL")
    for row in backend.show3():
     list3.insert(END,row)
     list3.insert(END,"\n")

    list4.insert(END,"INGREDIENT CALORIE CARBS PROTIEN FAT")
    for row in backend.show4():
     list4.insert(END,row)
     list4.insert(END,"\n")

    list5.insert(END,"SHOP_NO NAME ADDR PHONE FAMILY")
    for row in backend.show5():
     list5.insert(END,row)
     list5.insert(END,"\n")

    list6.insert(END,"RECIPE_ID NAME")
    for row in backend.show6():
     list6.insert(END,row)
     list6.insert(END,"\n")





def new_winF3(): # new window definition
    newwin = Toplevel(window)
    newwin.geometry('500x500')
    newwin.configure(background='#C96567')

    l1=Label(newwin,text="From date",bg='#C96567')
    l1.grid(row=0,column=0,pady=(200,20),padx=(750,2))
    l2=Label(newwin,text="To date",bg='#C96567')
    l2.grid(row=1,column=0,pady=(25,25),padx=(750,2))

    date1=StringVar()
    e1=Entry(newwin,textvariable=date1)
    e1.grid(row=0,column=1,pady=(200,20),padx=(0,5))

    date2=StringVar()
    e2=Entry(newwin,textvariable=date2)
    e2.grid(row=1,column=1,pady=(25,20))

    list1=Listbox(newwin, height=6,width=50)
    list1.grid(row=4,column=1,rowspan=8,columnspan=2,padx=(00,5),pady=50)

    sb1=Scrollbar(newwin)
    sb1.grid(row=4,column=3,rowspan=8)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    def expiryreminder():
       row= backend.expiryreminder(date1.get(),date2.get())
       for i in row:
           list1.insert(END,i)

    b1=Button(newwin,text="Remind", width=12,command=expiryreminder)
    b1.grid(row=3,column=1,)




def new_winF4(): # new window definition
    newwin = Toplevel(window)
    newwin.geometry('500x500')

    newwin.configure(background='#5D001E')

    l1=Label(newwin,text="Day",bg='#5D001E',fg='white')
    l1.grid(row=0,column=0,pady=(250,20),padx=(600,5))

    l2=Label(newwin,text="Meal",bg='#5D001E',fg='white')
    l2.grid(row=0,column=2,pady=(250,20),padx=(10,5))

    l3=Label(newwin,text="Recipe name",bg='#5D001E',fg='white')
    l3.grid(row=0,column=4,pady=(250,20),padx=(10,5))

    day=StringVar()
    e1=Entry(newwin,textvariable=day)
    e1.grid(row=0,column=1,pady=(250,20))

    meal=StringVar()
    e2=Entry(newwin,textvariable=meal)
    e2.grid(row=0,column=3,pady=(250,20))

    recipename=StringVar()
    e2=Entry(newwin,textvariable=recipename)
    e2.grid(row=0,column=5,pady=(250,20))

    def schedulechange():
      str=backend.schedulechange(recipename.get(),day.get(),meal.get())
      l4 = Label(newwin,text=str)
      l4.grid(row=3,column=3)

    b1=Button(newwin,text="Change", width=12,command=schedulechange)
    b1.grid(row=1,column=3)


window=Tk()

window.wm_title("Restaurant Inventory Management")
window.geometry('500x500')
window.configure(background='#5CDB95')
 
C=Canvas(window,bg="blue",height=1000,width=500) 

background_image=PhotoImage(file="food.png")
background_label = Label(window,image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


l1=Label(window,text="Day",bg='#05386B',fg='white')
l1.grid(row=0,column=0,pady=(50,0),padx=(650,10),ipady=3)

l2=Label(window,text="Meal",bg='#05386B',fg='white')
l2.grid(row=0,column=2,pady=(50,0),padx=(0,10),ipady=3)

day=StringVar()
e1=Entry(window,textvariable=day)
e1.grid(row=1,column=0,padx=(650,10),ipady=3)

meal=StringVar()
e2=Entry(window,textvariable=meal)
e2.grid(row=1,column=2,padx=(0,10),ipady=3)

l3=Label(window,text="No of people",bg='#05386B',fg='white')
l3.grid(row=0,column=4,pady=(50,0),ipady=3)

no=IntVar()
e3=Entry(window,textvariable=no)
e3.grid(row=1,column=4,ipady=3)

list1=Listbox(window, height=6,width=50)
list1.grid(row=2,column=0,rowspan=8,columnspan=5,padx=(650,0))

sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="Recipe", width=18,command=recipe,bg='#05386B',fg='white')

b1.grid(row=1,column=100,padx=(250,0),pady=(0,10))

b2=Button(window,text="Nutrition", width=18,command=nutrition,bg='#05386B',fg='white')
b2.grid(row=2,column=100,padx=(250,0),pady=(0,10))

b3=Button(window,text="Check Stock", width=18,command=checkstock,bg='#05386B',fg='white')
b3.grid(row=3,column=100,padx=(250,0),pady=(0,10))

b4=Button(window,text="Update Stock", width=18,command=updatestock,bg='#05386B',fg='white')
b4.grid(row=4,column=100,padx=(250,0),pady=(0,10))

b5=Button(window,text="Shop Detail", width=18,command=shopdetail,bg='#05386B',fg='white')
b5.grid(row=5,column=100,padx=(250,0),pady=(0,10))

b7=Button(window, text ="Add Ingredient", width=18, command =new_winF1,bg='#05386B',fg='white') #command linked
b7.grid(row=6,column=100,padx=(250,0),pady=(0,10))

b8=Button(window,text="View Database", width=18,command=new_winF2,bg='#05386B',fg='white')
b8.grid(row=7,column=100,padx=(250,0),pady=(0,10))

b9=Button(window,text="Expiry Reminder", width=18,command=new_winF3,bg='#05386B',fg='white')
b9.grid(row=8,column=100,padx=(250,0),pady=(0,10))

b10=Button(window,text="Change schedule", width=18,command=new_winF4,bg='#05386B',fg='white')
b10.grid(row=9,column=100,padx=(250,0),pady=(0,10))

b12=Button(window,text="No of ingredients", width=18,command=noofingredients,bg='#05386B',fg='white')
b12.grid(row=10,column=100,padx=(250,0),pady=(0,10))

b6=Button(window,text="Clear", width=18,command=clear,bg='#05386B',fg='white')
b6.grid(row=11,column=100,padx=(250,0),pady=(0,10))

b11=Button(window,text="Close", width=18,command=window.destroy,bg='#05386B',fg='white')
b11.grid(row=12,column=100,padx=(250,0),pady=(0,10))

C.grid()

window.mainloop()
