# Base class Person to store basic personal information
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Introduce method to display basic details
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}."

# Member class inheriting from Person with additional library-specific info
class Member(Person):
    def __init__(self, name, age, gender, membership_id):
        super().__init__(name, age, gender)
        self.membership_id = membership_id

    # Override introduce to include membership ID
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}, with membership ID: {self.membership_id}."

# Author class inheriting from Person, with a list of books written
class Author(Person):
    def __init__(self, name, age, gender, books_written=None):
        super().__init__(name, age, gender)
        self.books_written = books_written if books_written else []

    # Override introduce to list books written
    def introduce(self):
        books = ', '.join(self.books_written)
        return f"I am {self.name}, {self.age} years old, {self.gender}. Books written: {books if books else 'None'}."

# Combined class AuthorMember inheriting from both Member and Author
class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written=None):
        Member.__init__(self, name, age, gender, membership_id)
        Author.__init__(self, name, age, gender, books_written)

    # Override introduce to show membership and books together
    def introduce(self):
        books = ', '.join(self.books_written)
        return (f"I am {self.name}, {self.age} years old, {self.gender}, with membership ID: {self.membership_id}. "
                f"Books written: {books if books else 'None'}.")

# Example usage of the classes to check output
if __name__ == "__main__":
    # Create instances with realistic data
    person = Person("Asir", 20, "male")
    member = Member("Sarah", 28, "female", "M789")
    author = Author("John", 45, "male", ["AI Revolution", "Code Mastery"])
    author_member = AuthorMember("Emily", 32, "female", "M101", ["The Future of Tech", "Data Science Guide"])

    # Print introductions for each instance
    print(person.introduce())
    print(member.introduce())
    print(author.introduce())
    print(author_member.introduce())



