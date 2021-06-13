from pywebio.input import *
from pywebio.output import *
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='My5ql', database='testdb')

mycursor = mydb.cursor()

def vote():

    name = input("Contestant name: ", type=TEXT)
    number = input("Contestant number: ", type=NUMBER)

    if number >= 0:
        put_text('Is this correct?')
        put_table([['NAME','NUMBER'], [name, number]])
        check = checkbox(options = ['Confirm'])

        if check:
            talent1 = radio('Rate the talent', [8, 9, 10])
            charisma1 = radio('Rate the charisma', [8, 9, 10])
            looks1 = radio('Rate the looks', [8, 9, 10])
            
            action = "INSERT INTO vote_test(CONTESTANT, TALENT, CHARISMA, LOOKS) values(%s,%s,%s,%s)"
            grade = [(name,talent1,charisma1,looks1),]
            mycursor.executemany(action, grade)
            mydb.commit()

            put_text('Thanks for voting')

        again = radio('Got it! Vote again?', ['Sure', 'Nah'])

            
        if again == 'Sure':
                vote()
        
        else:
                return style(put_text('Thanks, Bye!'), 'color:green')
    
    else:
        style(put_text('Incorrect details'), 'color:red')
    
     
vote()
