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
    o = ""
    try:
        all = {"VD" : [[["r", "VD I (b)", "VD I"]]], "VD I" : [[["c", "VD I (a)", "VD I#VD I (a)"]], [["a", "v"]], [["c", "VD I (b)", "VD I#VD I (b)"]]]}
        all = all[name]
        o += "<table>"
        for x in range(len(all)):
            o += "<tr>"
            for y in range(len(all[x])):
                if len(all[x][y]) > 0:
                    o += "<td %s style='border:%s solid #000'>" % ("bgcolor='#aaf'" if all[x][y][0] == "r" else "", "2px" if all[x][y][0] == "r" else ("1px" if all[x][y][0] == "c" else "0px"))
                    o += ("<a href='wiki/%s'>%s<img src='img/tree/%s.png wigth='50' height='50'></a>" % (all[x][y][2], all[x][y][1], all[x][y][1])) if all[x][y][0] in {"r", "c"} else {"v" : "<img src='img/tree/arrows/v' heidth='100%' style='min-height:50px'>"}[all[x][y][1]]
                    o += "</td>"
                else:
                    o += "<td></td>"
            o += "</tr>"
        o += "</table>"

                        
    except KeyError:
        pass
    return o
all = {"robolink": robolink, "Card" : card, "tree" : tree}

conv = {"robolink": True, "Card": True, "tree" : False}
