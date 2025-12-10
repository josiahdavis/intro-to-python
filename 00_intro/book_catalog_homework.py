def add_book(catalog, title, author):
    # FIX ME


def find_books_by_author(catalog, author):
    # FIX ME


def print_catalog(catalog):
    # FIX ME

# ------------------------------
# Test Cases (No user input)
# ------------------------------

catalog = []

# Test Case 1: Adding books
catalog = add_book(catalog, "The Uncontrollability of the World", "Hartmut Rosa")
catalog = add_book(catalog, "The Lord of the Rings", "J. R. R. Tolkien")
catalog = add_book(catalog, "Foundation", "Isaac Asimov")
catalog = add_book(catalog, "Dune", "Frank Herbert")
catalog = add_book(catalog, "Dune Messiah", "Frank Herbert")

print("Catalog After Adding Books:")
print_catalog(catalog)
print("-" * 40)

# Test Case 2: Search by author
print("Books by Frank Herbert:")
matches = find_books_by_author(catalog, "Frank Herbert")
for book in matches:
    print(f"- {book['title']}")
print("-" * 40)

# Test Case 3: Search for author with no matches
print("Books by CS Lewis:")
matches = find_books_by_author(catalog, "CS Lewis")
print("Results:", matches)
print("-" * 40)

# EXPECTED OUTPUT
# 
# Catalog After Adding Books:
# 0. Title: The Uncontrollability of the World, Author: Hartmut Rosa
# 1. Title: The Lord of the Rings, Author: J. R. R. Tolkien
# 2. Title: Foundation, Author: Isaac Asimov
# 3. Title: Dune, Author: Frank Herbert
# 4. Title: Dune Messiah, Author: Frank Herbert
# ----------------------------------------
# Books by Frank Herbert:
# - Dune
# - Dune Messiah
# ----------------------------------------
# Books by CS Lewis:
# Results: []
# ----------------------------------------
