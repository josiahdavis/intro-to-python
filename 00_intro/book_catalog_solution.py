def add_book(catalog, title, author):
    catalog.append({"title": title, "author": author})
    return catalog


def find_books_by_author(catalog, author):
    results = []
    for book in catalog:
        if book["author"].lower() == author.lower():
            results.append(book)
    return results


def print_catalog(catalog):
    for i, book in enumerate(catalog):
        print(f"{i}. Title: {book['title']}, Author: {book['author']}")


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
