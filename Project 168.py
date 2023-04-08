# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:42:46 2023

@author: Akshara Sagar Dhoble
"""

class Book:
    
    def __init__(self , name , aunthor , price , publishing_year):
        self.book_name = name
        self.book_aunthor = aunthor
        self.book_price = price
        self.book_publishing_year = publishing_year
    def add_book (self):
        print("Book Name : " + self.book_name)
        print("Book aunthor : " + self.book_aunthor)
        print("Book price : " + (self.book_price) + "/-")
        print("Book publishing year : " + str(self.book_publishing_year))
        print("Book Added")
        
    def year_since_pub(self):
        year_ago_pub = 2020 - self.book_publishing_year
        print("The Book Was Published" + str(year_ago_pub)+"Years Ago")
       
book_1 = Book("Harry potter and the philosopher's Stone " , "J.K. Rowling", 1928 , 1997)  
book_1.add_book()
book_1.year_since_pub()

book_2 = Book("Diary of a wimpy kid " , "Jeff Kinney", 700 , 2017)  
book_2.add_book()
book_2.year_since_pub()
    
    