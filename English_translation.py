
'''
Author: rosa wang 
Date: 2020-11-04 18:05:16
LastEditTime: 2021-02-16 19:09:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Desktop/ten_apps/app1/DBversion2.py
'''
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
cursor = con.cursor()
word = input('Enter a word: ')
query = cursor.execute("SELECT * FROM Dictionary")#fetch all date on sql database
results = cursor.fetchall()
#print(type(results))

#convert list into a dict
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
dictionary = {}      
results = Convert(results, dictionary)

def my_dictionary(results):
    if word in results:
        print(results[word])
    elif word.title() in results:
        print(results[word.title()])
    elif word.upper() in results: 
        print(results[word.upper()])
    elif len(get_close_matches(word, results.keys()))>0:
        yn=input('Did you mean %s instead? Enter Y if yes or N' %get_close_matches(word, results.keys())[0])
        if yn in ['Y','y','yes','YES']:
            print (results[get_close_matches(word, results.keys())[0]])
        elif yn in ['n','N','no']:
            uInput=input('Did you mean %s instead? Enter Y if yes or N' %get_close_matches(word, results.keys())[1])
            if uInput in ['Y','y','yes','YES']:
                print(results[get_close_matches(word, results.keys())[1]])
                
                
        else:
            print ('We don\'t understand your input!')
            my_dictionary(results)
            
        
    else:
        print ('The word does not exist, Please input a valid one')
my_dictionary(results) 