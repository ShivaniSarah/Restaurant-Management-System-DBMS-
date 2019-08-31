import psycopg2


def viewrecipe1(day,meal):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT name,cooking_time from recipe WHERE name=(SELECT name from recipecatalog rc,schedule s WHERE rc.recipeid=s.recipeid AND day=%s AND meal=%s)",(day,meal,))
    rows=cur.fetchall()
    conn.close()
    return rows

def viewrecipe2(day,meal):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT ingredient,quantity FROM recipe WHERE name=(SELECT name from recipecatalog rc,schedule s WHERE rc.recipeid=s.recipeid AND day=%s AND meal=%s)",(day,meal,))
    rows=cur.fetchall()
    conn.close()
    return rows

def viewrecipe(day,meal):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM recipe WHERE name=(SELECT name from recipecatalog rc,schedule s WHERE rc.recipeid=s.recipeid AND day=%s AND meal=%s)",(day,meal,))
    rows=cur.fetchall()
    conn.close()
    return rows

def nvalue(ing):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM nutrition WHERE ingredient=%s", (ing,))
    rows=cur.fetchall()
    conn.close()
    return rows

def viewingredient(ingred):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ingredients WHERE name=%s ",(ingred,))
    rows=cur.fetchall()
    conn.close()
    return rows

def update(name,quantity):
    try:
     conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
     cur=conn.cursor()
     cur.execute("UPDATE ingredients SET quantity=%s WHERE name=%s",(quantity,name,))
     conn.commit()
     conn.close()
    except:
     return "Not Done"
    return "Done"

def shopdetail(day,meal):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT shopid,s.name,address,phone from shop s,ingredients i WHERE s.family=i.family AND i.name IN(SELECT ingredient from recipe WHERE name=(SELECT name from recipecatalog rc,schedule s WHERE rc.recipeid=s.recipeid AND day=%s AND meal=%s))",(day,meal,))
    rows=cur.fetchall()
    conn.close()
    return rows

def updateingredientaftershopping(name,quantity,buying_date ,expiry_date,family):
    try:
     conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
     cur=conn.cursor()
     cur.execute("UPDATE ingredients SET quantity=quantity+%s, buying_date=%s ,expiry_date=%s ,family=%s  WHERE name=%s",(quantity,buying_date ,expiry_date,family,name,))
     conn.commit()
     conn.close()
    except:
     return "Not Done"
    return "Done"

def schedulechange(name,day,meal):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    try:
     cur.execute("UPDATE schedule set recipeid=(SELECT recipeid from recipecatalog WHERE name=%s) WHERE day=%s AND meal=%s",(name,day,meal,))
     conn.commit()
     conn.close()
    except:
     return "Not Done"
    return "Done"

def expiryreminder(date1,date2):
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('SELECT name FROM ingredients WHERE expiry_date BETWEEN (%s) AND (%s)',(date1,date2,))
    rows=cur.fetchall()
    conn.close()
    return rows

def noofingredients():
    conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('SELECT * FROM noofingredients();')           
    rows=cur.fetchall()
    conn.close()
    return rows

def show1():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM ingredients")
  rows=cur.fetchall()
  conn.close()
  return rows

def show2():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM recipe")
  rows=cur.fetchall()
  conn.close()
  return rows

def show3():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM schedule")
  rows=cur.fetchall()
  conn.close()
  return rows

def show4():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM nutrition")
  rows=cur.fetchall()
  conn.close()
  return rows

def show5():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM shop")
  rows=cur.fetchall()
  conn.close()
  return rows

def show6():
  conn=psycopg2.connect("dbname='restaurant' user='postgres' password ='postgres123' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM recipecatalog")
  rows=cur.fetchall()
  conn.close()
  return rows





'''
print(viewrecipe1("mon","breakfast"))
print(viewrecipe2("mon","breakfast"))
print(viewrecipe("mon","breakfast"))
print(nvalue("Paneer"))
print(viewingredient("Paneer"))
print(update("Paneer",250))
print(shopdetail("mon","breakfast"))
print(updateingredientaftershopping("Paneer",200,"2018-01-01","2018-02-01","dairy"))
print(schedulechange("mon",2,"breakfast"))
print(expiryreminder("2018-01-01","2018-11-01"))
print(noofingredients())
print(show1())
print(show2())
print(show3())
print(show4())
print(show5())
print(show6())
'''