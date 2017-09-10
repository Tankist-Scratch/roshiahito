def robolink(link):
    return "[[@robots/%s/logo.svg]][[%s|%s]]" % (link, link, link)


def card(name, img, prev, next, width, lenth, height, mass, model=""):
    o = """<table bgcolor='#ccc' width='100""" + "%" + (""""'>
    <tr><td rowspan='2' width='300px'>%s</td><td><img src='/roshiahito/img/%s/icon.svg'/> %s</td><td rowspan='2'>
    \t<table width='100""" % (("<img src='/roshiahito/img/%s/%s' width='300px'/>" % s(name, img)) if img else "", name, name)) + "%" + """'><tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr></table>
    </tr><tr><td>Ширина : %s см, Длина : %s, см Высота : %s, см Вес : %s кг</td></tr></table>
    <br>
    """ % ("{{robolink|" + "}} {{robolink|".join(prev) + "}}", name, "{{robolink|" + "}} {{robolink|".join(next) + "}}",
           width, lenth, height, mass)
    return o


all = {"robolink": robolink, "Card" : card}

conv = {"robolink": True, "Card": True}
