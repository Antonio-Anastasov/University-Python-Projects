def classify_books(*args, **kwargs):
    # Initialize dictionaries to store books by genre
    fiction_books = {}
    non_fiction_books = {}

    # Process the tuples (genre, title)
    for genre, title in args:
        if genre == "fiction":
            fiction_books[title] = None  # Placeholder for ISBN
        elif genre == "non_fiction":
            non_fiction_books[title] = None  # Placeholder for ISBN

    # Process the keyword arguments (ISBN: title)
    for isbn, title in kwargs.items():
        if title in fiction_books:
            fiction_books[title] = isbn
        elif title in non_fiction_books:
            non_fiction_books[title] = isbn

    # Sort fiction books by ISBN (ascending)
    sorted_fiction = sorted(
        [(isbn, title) for title, isbn in fiction_books.items() if isbn is not None],
        key=lambda x: x[0]
    )

    # Sort non-fiction books by ISBN (descending)
    sorted_non_fiction = sorted(
        [(isbn, title) for title, isbn in non_fiction_books.items() if isbn is not None],
        key=lambda x: x[0],
        reverse=True
    )

    # Build the output
    output = []

    # Fiction books
    if sorted_fiction:
        output.append("Fiction Books:")
        for isbn, title in sorted_fiction:
            output.append(f"~~~{isbn}#{title}")

    # Non-fiction books
    if sorted_non_fiction:
        output.append("Non-Fiction Books:")
        for isbn, title in sorted_non_fiction:
            output.append(f"***{isbn}#{title}")

    # Join the output with newlines and return
    return "\n".join(output)