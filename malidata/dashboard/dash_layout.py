with open("malidata/templates/layout.html", "r", encoding="utf-8") as f:
    text = f.read()

newhtml = "<div class='container'>{%app_entry%}</div>" + "<footer>{%config%} {%scripts%} {%renderer%}</footer>"
text = text.replace("{% block content %}{% endblock %}", newhtml)
text = text.replace("active", "")
text = text.replace('<a class="nav-link" href="/dashboard/">Dashboard</a>', '<a class="nav-link active" href="/dashboard/">Dashboard</a>')

def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec

@docstring_parameter(text)
def foo():
    """
        {0}
    """

html_layout = foo.__doc__
