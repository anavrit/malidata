with open("malidata/dashboard/templates/dash_layout.html", "r", encoding="utf-8") as f:
    text = f.read()

def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec

@docstring_parameter(text)
def foo():
    """{0}"""

html_layout = foo.__doc__
