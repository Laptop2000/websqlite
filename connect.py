import sqlite3 as s

def getconnet():
    conn=s.connect('amitava.db')
    #conn=s.connect('d:\\sqlite\\moli.db')
    #conn=s.connect(':memory:')
    return conn

def talk():
    con=getconnet()
    cur=con.cursor()
    print('cur is ',type(cur))
    qry='''
    CREATE TABLE ALLPRODUCTS(PID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT(10),PRICE INTEGER);
    '''
    try:
        cur.execute(qry)    # SQL EXECUTED
        print('----done----')
    except Exception as q:
        print('problem ...',q)
    con.close()


def insert():
    con=getconnet()
    cur=con.cursor()
    qry="insert into ALLPRODUCTS values(21,'washing machine',28000)"
    try:
        cur.execute(qry)    # SQL EXECUTED
        con.commit()
        print('----INSERT done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()

def insert_dynamic(a,b,c):
    con=getconnet()
    cur=con.cursor()  
    
    try:
        cur.execute("insert into ALLPRODUCTS values(?,?,?)",(a,b,c))    # SQL EXECUTED
        con.commit()
        print('----INSERT done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()

def insert_dynamic_again(a,b,c):
    con=getconnet()
    cur=con.cursor()  
    
    try:
        cur.execute("insert into ALLPRODUCTS values(:m,:n,:o)",(a,b,c))    # SQL EXECUTED
        con.commit()
        print('----INSERT done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()


def insert_bulk():
    con=getconnet()
    cur=con.cursor()  
    qry="insert into products values(?,?,?)"

    prlist=[(22,'aa',1200),
            (222,'aaa',14200),
            (242,'aaw',15200),
            (212,'aae',13200),
            (262,'aad',18200)
            ]
    
    try:
        cur.executemany(qry,prlist)
        con.commit()
        print('----INSERT ALL.....done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()


def updateproduct(newpr,name):
    con=getconnet()
    cur=con.cursor()  
    qry="update products set price=? where name=?"

      
    try:
        cur.execute(qry,(newpr,name))
        con.commit()
        print('----updated price.....done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()


def deleteproduct(name):
    con=getconnet()
    cur=con.cursor()  
    qry="delete from products where name=?"

      
    try:
        cur.execute(qry,(name,))
        con.commit()
        print('----deleted price.....done----')
    except Exception as q:
        print('problem ...',q)
        con.rollback()
    con.close()



def showall():
    con=getconnet()
    cur=con.cursor()  
    qry="select * from products"

      
    try:
        cur.execute(qry)
        rows=cur.fetchall()
        for r in rows:
            print(r)

        
    except Exception as q:
        print('problem ...',q)
        
    con.close()


def showone(pname):
    con=getconnet()
    cur=con.cursor()  
    qry="select * from products where name=?"

      
    try:
        cur.execute(qry,(pname,))
        row=cur.fetchone()
        print(row)

        
    except Exception as q:
        print('problem ...',q)
        
    con.close()


def showweb(pname):
    try:
        con=getconnet()
        cur=con.cursor()  
        qry="select * from products where name=?"   
        cur.execute(qry,(pname,))
        row=cur.fetchone()      

        
    except Exception as q:
        print('problem ...',q)

    return row
        
    con.close()



