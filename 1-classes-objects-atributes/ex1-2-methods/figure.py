class Figure:
    type_fig = "ellipse"
    color = "red"


fig1 = Figure()
fig1.start_pt = 10, 5
fig1.__setattr__("end_pt", (20, 10))
#setattr(fig1, "color", (20, 10))
print(getattr(fig1, "color", False))


fig1.center = (1, 5)
print(fig1.__dict__)
print(hasattr(fig1, "color"))