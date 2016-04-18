from collections import defaultdict

class Book(object):

	def __init__(self, author, title, copies=1):
		self.author = author
		self.title = title
		self.copies = copies
		self.lent = []

	def add(self):
		self.copies += 1

	def remove(self):
		if self.copies == 1:
			raise Exception("There is only one copy left.")
		self.copies -= 1

	def lend(self, person):
		if len(self.lent) < self.copies:
			self.lent.append(person)
		else:
			raise Exception("There are no books available.")

	def restore(self, person):
		self.lent.remove(person)

	def get_persons(self):
		return self.lent	

	def __repr__(self):
		return "Author: {author}\nTitle: {title}\nNumber of copies: {copies}\nLent: {lent}\n".format(author=self.author, title=self.title, copies=self.copies, lent = self.lent)

	def __str__(self):
		return self.__repr__()	

				
class Inventory(object):
	def __init__(self, database={}):
		self.database = database

	def add_book(self, author, title, copies):
		self.database[author + '@' + title] = Book(author, title, copies)

	def remove_book(self, author, title=None):
		if author and title:
			if self.database.get(author + '@' + title):
				del self.database[author + '@' + title]
			else:
				print "Book does not exist in database."
		else:		
			for key, book in self.find(author):
				del self.database[key]

	def find(self, author=None, title=None):
		if author:
			return filter(lambda x: x.startswith(author + '@'), self.database)
		elif title:
			return filter(lambda x: title in x.split('@')[1], self.database)

	def get_book(self, author, title):
		return self.database.get(author + '@' + title, None)

	def books_lent_to(self, person):
		for book in self.database.values():
			if person in book.get_persons():
				print book.author, ':', book.title

	def book_holders(self, author, title):
		book = self.database.get(author + '@' + title, None)
		if book:
			print book.lent

	def __repr__(self):
		result = ""
		for book in self.database.values():
			result += str(book)
		return result

	def __str__(self):
		return self.__repr__()		


if __name__ == "__main__":
	inventory = Inventory()
	while True:
		print "1. Add a book"
		print "2. Add a copy"
		print "3. Delete_book"
		print "4. Delete_copy"
		print "5. Search books after author"
		print "6. Search books after a word in title"
		print "7. Lend a book"
		print "8. Restore a book"
		print "9. What books has a person"
		print "10. Persons who hold a book"
		print "11. Exit"
		option = int(raw_input("Your option:"))
		if option == 1:
			author = raw_input("Author:")
			title = raw_input("Title:")
			copies = int(raw_input("Number of copies:"))
			inventory.add_book(author, title, copies)
			print inventory
		elif option == 2:
			author = raw_input("Author:")
			title = raw_input("Title:")
			inventory.get_book(author, title).add()
			print inventory
		elif option == 3:
			author = raw_input("Author:")
			title = raw_input("Title:")
			inventory.remove_book(author, title)
			print inventory
		elif option == 4:
			author = raw_input("Author:")
			title = raw_input("Title:")
			inventory.get_book(author, title).remove()
			print inventory
		elif option == 5:
			author = raw_input("Author:")
			bookitems = inventory.find(author)
			for book in bookitems:
				print "Book:", book.split('@')[1]
		elif option == 6:
			word = raw_input("Word:")
			bookitems = inventory.find(title=word)
			for book in bookitems:
				print "Book:", book.split('@')[1], "; Author:", book.split('@')[0]
		elif option == 7:		
			author = raw_input("Author:")
			title = raw_input("Title:")
			person = raw_input("Person:")
			book = inventory.get_book(author, title)
			book.lend(person)
			print book
		elif option == 8:
			author = raw_input("Author:")
			title = raw_input("Title:")
			person = raw_input("Person:")
			book = inventory.get_book(author, title)
			book.restore(person)
			print book
		elif option == 9:
			person = raw_input("Person:")
			inventory.books_lent_to(person)
		elif option == 10:
			author = raw_input("Author:")
			title = raw_input("Title:")
			inventory.book_holders(author, title)
		elif option == 11:
			break	
				
