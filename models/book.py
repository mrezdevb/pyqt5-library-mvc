class Book:
	def __init__(self, title, author, isbn):
		self.title = title
		self.author = author
		self.isbn = isbn
		self.is_barrowed = False
	def __str__(self):
		return f'{self.title} writted by {self.author}  | isbn : {self.isbn}'

