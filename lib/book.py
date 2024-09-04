#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.set_title(title)
        self.set_page_count(page_count)
    
    def set_title(self, title):
        self.title = title
    
    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count  # Directly set the internal variable
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        self.set_page_count(value)  # Calls the set_page_count method
