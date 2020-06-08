import utils
import sorts

# bookshelfs
bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

# Sort by title
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

# Sort by Author
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

# Sort by length of the sum of the number of characters in the book and author's name
def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

# Sorting methods
sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort1:
  print(book['title'])

sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort2:
  print(book['author'])

sort3 = sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print("---\nAuthor Quick sort: \n---")
for book in bookshelf_v2:
  print(book['author'])

#sort4 = sorts.bubble_sort(long_bookshelf, by_total_length)
#for book in sort4:
  #print(book['title'])

sort5 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
print("---\nTotal Length Quick sort: \n---")
for book in long_bookshelf:
  print(book['title'])


