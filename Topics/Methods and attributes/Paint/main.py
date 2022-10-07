class Friend:
    def __init__(self, name):
        self.name = name
        self.best_friend = None

    def set_best_friend(self, bff_name):
        self.best_friend = bff_name


kate = Friend("Kate")
alex = Friend("Alex")
jess = Friend("Jess")

kate.set_best_friend("Melani")
jess.set_best_friend("Kate")
kate.set_best_friend("Jess")

print(kate.best_friend)
