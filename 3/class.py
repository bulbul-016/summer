class Adam():
    def __init__(self, name, age):
        self.nam=name
        self.agee=age
    def __str__(self):
        return f"{self.nam} - {self.agee}"
    def deee(self):
        print(f'hi {self.nam}')

p=Adam("Baby", 16)
p.deee()

print(p)