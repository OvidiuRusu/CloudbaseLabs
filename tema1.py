from collections import defaultdict

def add_book():
	global inventory
	author = raw_input("Author:")
	title = raw_input("Title:")
	copies = raw_input("Number of copies:")
	inventory[author + '@' + title] += ['available'] * int(copies)
	print inventory


def add_copy():
	global inventory
	author = raw_input("Author:")
	title = raw_input("Title:")
	status = raw_input("Status:")
	inventory[author + '@' + title].append(status)
	print inventory

def delete_book():
	global inventory
	author = raw_input("Author:")
	title = raw_input("Title:")
	if inventory.get(author + '@' + title, 0) == 0:
		print "Book does not exist in inventory"
	else:	
		del inventory[author + '@' + title]
	print inventory

def delete_copy():
	global inventory
	author = raw_input("Author:")
	title = raw_input("Title:")
	if inventory.get(author + '@' + title, 0) == 0:
		print "Book does not exist in inventory"
	else:		
		if len(inventory[author + '@' + title]) == 1:
			del inventory[author + '@' + title]
		else:	
			inventory[author + '@' + title].remove('available')
	print inventory

def books_after_author(inventory, author):
	books = inventory.keys()
	for item in books:
		if item.split('@')[0] == author:
			print item.split('@')[1]

def books_after_word_in_title(inventory, word):
	books = inventory.keys()
	for item in books:
		if word in item.split('@')[1]:
			print item.split('@')[0], ':' , item.split('@')[1]


def update_status_book():
	global inventory
	author = raw_input("Author:")
	title = raw_input("Title:")
	copy = int(raw_input("Number of copy:"))
	status = raw_input("Status:")
	inventory[author + '@' + title][copy] = status
	print inventory


if __name__ == "__main__":
	inventory = defaultdict(list)
	while True:
		print "1. Add a book"
		print "2. Add a copy"
		print "3. Delete_book"
		print "4. Delete_copy"
		print "5. Search books after author"
		print "6. Search books after a word in title"
		print "7. Update status book"
		print "8. Exit"
		option = int(raw_input("Your option:"))
		if option == 1:
			add_book()
		elif option == 2:
			add_copy()
		elif option == 3:
			delete_book()
		elif option == 4:
			delete_copy()
		elif option == 5:
			author = raw_input("Author:")
			books_after_author(inventory, author)	
		elif option == 6:
			word = raw_input("Word:")
			books_after_word_in_title(inventory, word)
		elif option == 7:
			update_status_book()
		elif option == 8:		
			break	




