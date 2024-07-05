print("Welcome to ticket counter.")


class ticket:
    def __init__(self, name):
        self.name = name

    def price(self):
        print("Your ticket price is 20 rupee.")

    def train_detail(self):
        print(f"Hii {self.name}!\nYour train will come at 2 number platform.")


train = ticket("Sujal")
train.train_detail()
train.price()
