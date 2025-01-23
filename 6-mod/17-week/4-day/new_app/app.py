class WillPrint:
    """This is wills custom printer"""
    def __init__(self, sep, end):
        self.sep = sep
        self.end = end

    def custom_print(self, *printable):
        print("\n\n")
        print(*printable, sep=self.sep, end=self.end)

wprint = WillPrint("\n\n~~~~~~\n\n", "\n\n").custom_print
import config

from models import avacado

print(avacado.avacado)












# from models.nanner import nanner

# wprint(avacado)

# wprint(__name__)

# if __name__ == "main":
#     app = startapp()
#     app()


# wprint(f" \nconfig module {config}")

# wprint("in module")
