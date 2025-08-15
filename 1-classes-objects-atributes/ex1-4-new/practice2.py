TYPE_OS = 2

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj =  DialogWindows()

        else:
            obj =  DialogLinux()
        obj.name = args[0]
        return obj


dlg = Dialog("Hello")
print(dlg)