def robolink(link):
    return "[[@robots/%s/logo.svg]][[%s|%s]]" % (link, link, link)


def card(name, img, type, prev, next, width, lenth, height, mass, model=""):
    return """<table bgcolor='#8cc' width='100""" + "%" + (""""'>
    <tr><td rowspan='2' width='300px'>%s</td><td><table width="100%s"><tr><td><img src='/roshiahito/img/%s/icon.svg'/><b>%s</b></td><td style="text-align:right; color:#666;">%s</td></tr></table></td><td rowspan='2'>
    \t<table width='100""" % (
        ("<img src='/roshiahito/img/%s/%s' width='300px'/>" % (name, img)) if img else "", "%", name, name,
        {"L": "Lego Mindstorms", "mB": "MakeBlock"}[type])) + "%" + """'><tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr>
    \t<tr><td>%s</td></tr></table>
    </tr><tr><td>Длина : %s см, Ширина : %s см, Высота : %s см, Вес : %s кг</td></tr></table>
    <br>
    """ % ("{{robolink|" + prev + "}}", name, "{{robolink|" + next + "}}",
           width, lenth, height, mass)


def mod(name, type, img):
    return """<table width="100%s"><tr><td width="100px">[[@mods/types/%s.png]]</td><td width="100px">[[@mods/%s.png]]</td><td><h3>%s</h3></td></tr></table>""" % (
        "%", type, img, name)


def battle(name, type, link, top, robot):
    return """<table width="100%s" bgcolor="#%s"><tr><td><h3>[[%s|%s/%s]]</h3><br><b>%s</b><br><b>%s место</b></td></tr></table>""" % (
        "%", ({"1": "ffa", "2": "ccf", "3": "eca"}[top] if top in {"1", "2", "3"} else "eee"), link, name, type, robot,
        top)


def battleL(name, type, link, top, robot, rl):
    return """<table width="100%s" bgcolor="#%s"><tr><td><h3>[[%s|%s/%s]]</h3><br><b>[[%s|%s]]</b><br><b>%s место</b></td></tr></table>""" % (
        "%", ({"1": "ffa", "2": "ccf", "3": "eca"}[top] if top in {"1", "2", "3"} else "eee"), link, name, type, rl,
        robot, top)


def battleS(robot, rl, top, type=None):
    return """<table width="100%s" bgcolor="#%s"><tr><td><h3>[[%s|%s]]</h3><br>%s<b>%s место</b></td></tr></table>""" % (
        "%", ({"1": "ffa", "2": "ccf", "3": "eca"}[top] if top in {"1", "2", "3"} else "eee"), rl, robot,
        (("<b>%s</b><br>" % type) if type else ""), top)


def BCard(name, data, site):
    return """<table bgcolor='#8cc' width='100%s'><tr><td><b>%s</b></td></tr>
    <tr><td>Дата : %s, <a href='%s'>Ссылка</a></td></tr></table>""" % ("%", name, data, site)


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


all = {"robolink": robolink, "Card": card, "tree": tree, "mod": mod, "battle": battle, "battleL": battleL,
       "battleS": battleS, "BCard": BCard}

conv = {"robolink": True, "Card": True, "tree": False, "mod": True, "battle": True, "battleL": True, "battleS": True,
        "BCard": True}
