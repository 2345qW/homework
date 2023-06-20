# class Auto :

#     def __init__(self,model,year_of_manufacture,maker,manufacturer,color_auto,price) -> None:
#         self.model=model
#         self.year_of_manufacture=year_of_manufacture
#         self.maker=maker
#         self.manufacturer=manufacturer
#         self.color_auto=color_auto
#         self.price=price

#     def input_data(self) :
#         self.model=(input('введіть модель авто :'))
#         self.year_of_manufacture=int(input('введіть дату випуску :'))
#         self.maker = input('введіть виробника :')
#         self.manufacturer=input("ввудіть об'єм двигуна:")
#         self.color_auto=input('введіть колір авто :')
#         self.price=input('введіь ціну авто :')
#         return self.model ,self.year_of_manufacture,self.manufacturer,self.color_auto,self.price

#     def print_data(self):
#         print(f'модель авто - {self.model}')
#         print(f'дата випуку - {self.year_of_manufacture}')
#         print(f'виробник - {self.maker}')
#         print(f'обєм двигуна - {self.manufacturer}')
#         print(f'колір авто - {self.color_auto}')
#         print(f'цінна авто - {self.price}')



# auto1 = Auto(2106,1991,'vaz',1.2,'red',850)
# auto1.input_data()        
# auto1.print_data()
#-----------------------------------------------
'''назва-book_title
    рік -year_of_issue
    видавець-publisher
    жанр -genre
    автора-author
    ціну.-price
'''
class book :
    def __init__(self,book_title,year_of_issue,publisher,genre,author,price) -> None:
        self.book_title=book_title
        self.year_of_issue=year_of_issue
        self.publisher=publisher
        self.genre=genre
        self.author=author
        self.price=price

    def input_data(self):
        self.book_title=input('введіть назву книги :')
        self.year_of_issue=int(input('введіть рік видавництва:'))
        self.publisher=input('введіть видавця:')
        self.genre=input('введіть жанр книги:')
        self.author=input('введіть автора:')
        self.price=int(input('введіть ціну в ₴:'))
        return self.book_title,self.year_of_issue,self.publisher,self.genre,self.author,self.price
    
    def prit_data (self):
        print(f'назва книги -{self.book_title}')
        print(f'рік видання{self.year_of_issue}')
        print(f'видавець{self.publisher}')
        print(f'жанр{self.genre}')
        print(f'автор{self.author}')
        print(f'ціна {self.price}₴')
        