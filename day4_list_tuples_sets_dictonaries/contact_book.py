contacts = [
    {"name": "Alice", "phone": "123", "city": "NYC"},
    {"name": "Bob", "phone": "456", "city": "LA"}
]

la_contacts = [c for c in contacts if c["city"] == "LA"]
print(la_contacts)
