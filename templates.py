def robolink(link):
    return "[[@robots/%s/logo.svg]][[%s|%s]]" % (link, link, link)


def card(name, img, prev, next, width, lenth, height, mass, model=""):
    o = """<table bgcolor='#8cc' width='100""" + "%" + (""""'>
    <tr><td rowspan='2' width='300px'>%s</td><td><img src='/roshiahito/img/%s/icon.svg'/> %s</td><td rowspan='2'>
    \t<table width='100""" % (("<img src='/roshiahito/img/%s/%s' width='300px'/>" % s(name, img)) if img else "", name, name)) + "%" + """'><tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr></table>
    </tr><tr><td>Ширина : %s см, Длина : %s, см Высота : %s, см Вес : %s кг</td></tr></table>
    <br>
    """ % ("{{robolink|" + "}} {{robolink|".join(prev) + "}}", name, "{{robolink|" + "}} {{robolink|".join(next) + "}}",
           width, lenth, height, mass)
    return o

def model(ldd, sf):
    """<div class="sketchfab-embed-wrapper"><iframe width="640" height="480" src="https://sketchfab.com/models/bd7d5a476c15431fb55bd869a28b0a74/embed" frameborder="0" allowvr allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" onmousewheel=""></iframe>

<p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;">
    <a href="https://sketchfab.com/models/bd7d5a476c15431fb55bd869a28b0a74?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Caravan Peugeot Boxer #03 (draft)</a>
    by <a href="https://sketchfab.com/tankist-scratch?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">tankist-scratch</a>
    on <a href="https://sketchfab.com?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
</p>
</div>"""

def tree(name):
    try:
        pass

                        
    except KeyError:
        pass
all = {"robolink": robolink, "Card" : card, "tree" : tree}

conv = {"robolink": True, "Card": True, "tree" : False}
