class Learning:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create instances of Learning with different ages
s = Learning("helloworld", 1)
s1 = Learning("helloworld", 2)
s2 = Learning("helloworld", 3)
s3 = Learning("helloworld", 4)
s4 = Learning("helloworld", 5)

# Store instances in a list
instances = [s, s1, s2, s3, s4]

# Iterate through the list and print name and age of each instance
for instance in instances:
    print(instance.name, instance.age)
