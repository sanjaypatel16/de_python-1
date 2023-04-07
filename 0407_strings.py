#Today we are learning about Strings
fruits = ["Apples", "banana", "grapes", "strawberry", "chikoo", "blackberry"]
fruits.append("cherry")
print(fruits)

def replace_email(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        print(index)
    return email

