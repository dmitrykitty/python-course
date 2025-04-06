class Car:
    pass  # aby zrobic pustą klase


setattr(Car, "model", "toyota")
setattr(Car, "color", "black")

print(Car.__dict__["color"])  # uzyskanie coloru


class Notes:
    uid = 1000453
    author = "Stephen King"
    pages = 2


print(getattr(Notes, "author", False))


class TravelBlog:
    total_blogs = 10


tb1 = TravelBlog()
tb1.name = "France"

tb2 = TravelBlog()
tb2.name = "Germany"


class Figure:
    type_fig = "ellipse"
    color = "blue"


fig1 = Figure()
print(fig1.type_fig) #ellipse
fig1.color = "red"
fig1.center = (1, 5)
fig1.radius = 1


def print_ats(fig):
    for item in fig.__dict__.items():
        print(item, end=" ")
    print()


print_ats(fig1)

del fig1.color

print_ats(fig1)

print("Yes" if hasattr(Notes, "color") else "No")