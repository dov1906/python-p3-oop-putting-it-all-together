#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  
        
    
    @property
    def page_count(self):
        return self.page

    @page_count.setter
    def page_count(self, value):
        if type(value) == int:
            self.page = value
        else:
            print("page_count must be an integer")
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    
book1 = Book("hello", 100)




    

        