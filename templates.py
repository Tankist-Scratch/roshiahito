def robolink(name, link=False, icon=False):
    import data
    return "[[@icons/%s]][[%s|%s]]" % (icon if icon else data.icons[name], link if link else name, name)


def card(name, img, type, icon, prev, next, lenth="", width="", height="", mass="", motor="", speed="", rotate=""):
    return """
    <table class='card-rb'>
        <tr>
            <td rowspan='2' class='card-rb-img'>
                <img src='/roshiahito/img/%s' class='card-rb-img'/>
            </td>
            <td class='card-rb-title'>
                <table  class='card-rb-title'>
                    <tr>
                        <td><img src='/roshiahito/img/icons/%s'/><b>%s</b></td>
                        <td class='card-rb-type'>%s</td>
                    </tr>
                </table>
            </td>
            <td rowspan='2' class='card-rb-tree'>
                <table class='card-rb-tree'>
                    <tr>
                        <td>%s</td>
                    </tr>
                    <tr>
                        <td  class='card-rb-tree-cur'><img src='/roshiahito/img/icons/%s'/><b>%s</b></td>
                    </tr>
                    <tr>
                        <td>%s</td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table class='card-rb-data'>
                    <tr>
                        <td class='card-rb-data-metric'>Длина : %s см, Ширина : %s см, Высота : %s см, Вес : %s кг.</td>
                    </tr>
                    <tr>
                        <td>Привод : %s, Скорость : %s м/с, Поворот : %s °/с.</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
    """ % (img, icon, name, {"L": "Lego Mindstorms", "mB": "MakeBlock"}[type], prev, icon, name, next, lenth, width, height, mass, {"f": "Передний", "b": "Задний", "d": "Полный", "": ""}[motor], speed, rotate)

def mod(name, type, img):
    return """
    <table width="100%s">
        <tr>
            <td width="100px">
                [[@mods/types/%s.png]]
            </td>
            <td width="100px">
                [[@mods/%s.png]]
            </td>
            <td>
                <h3>%s</h3>
            </td>
        </tr>
    </table>""" % (
        "%", type, img, name)


def comp(name, type, link, robot, top, desc=""):
    m = top if top in {"1", "2", "3"} else "d"
    return """
    <table class='comp c-m%s'>
        <tr>
            <td colspan='2' class='comp-title comp-m%s-title'>
                <b>[[%s|%s/%s]]</b>
            </td>
        </tr>
        <tr>
            <td class='comp-data'>
                %s
            </td>
            <td class='comp-data'>
                %s место
            </td>
        </tr>
        <tr>
            <td class='comp-m%s-desc' colspan='2'>
                %s
            </td>
        </tr>
    </table>""" % (m, m, link, name, type, robot, top, m, desc)


def comp_u(robot, top, desc=""):
    m = top if top in {"1", "2", "3"} else "d"
    return """
    <table class='comp c-m%s'>
        <tr>
            <td class='comp-data'>
                %s
            </td>
            <td class='comp-data'>
                %s место
            </td>
        </tr>
        <tr>
            <td class='comp-m%s-desc' colspan="2">
                %s
            </td>
        </tr>
    </table>""" % (m, robot, top, m, desc)


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


def id(id):
    return "<span id='%s'></span>" % id


def tree(name):
    try:
        pass


    except KeyError:
        pass


def h2(name, id=False):
    return "<h2 class='title-h2' id='%s'>%s</h2>" % (id if id else name, name)

def h3(name, id=False):
    return "<h3 class='title-h3' id='%s'>%s</h3>" % (id if id else name, name)

all = {"robolink": robolink, "Card": card, "tree": tree, "mod": mod, "comp": comp, "BCard": BCard, "id": id, "h2": h2, "h3": h3, "comp_u" : comp_u}

conv = {"robolink": True, "Card": True, "tree": False, "mod": True, "comp": True,
        "BCard": True, "id": False, "h2": False, "h3": False, "comp_u":True}

css = {}
