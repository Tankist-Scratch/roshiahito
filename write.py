import data, templates as templ, os

def head():
    return ""


def write(s, page=False, name=""):
    i = 0
    t = ""
    _s = []
    o = (data.struct[0] + "<meta charset='UTF-8'><title>" + name + " | Roshiahito Ink</title>" + head() + data.struct[1] + data.header + data.struct[2] + name + data.struct[3]) if page else ""
    while i < len(s):
        # links (<a>), images (<img>)
        if t == "[":
            if s[i] == "[":
                t = "[["
                i += 1
                _s.append("")
            else:
                o += "[" + s[i]
                i += 1
                t = ""
            continue
        elif t == "[[":
            if s[i] == "@":
                t = "[i"
                _s.append("")
                i += 1
            else:
                t = "[a"
                _s[-1] += s[i]
                i += 1
            continue
        elif t == "[i":
            if s[i] == "]":
                t = "[i]"
                i += 1
            else:
                _s[-1] += s[i]
                i += 1
            continue
        elif t == "[i]":
            if s[i] == "]":
                o += "<img src='img/%s'/>" % ( _s[-1])
                t = ""
                i += 1
                _s.pop()
            else:
                _s[-1] += "]" + s[i]
                t = "[i"
                i += 1
            continue
        elif t == "[a":
            if s[i] == "|":
                i += 1
                t = "[|"
            else:
                _s[-1] += s[i]
                i += 1
            continue
        elif t == "[|":
            _s.append("")
            if s[i] == "]":
                t = "[t]"
                i += 1
            else:
                _s[-1] += s[i]
                t = "[t"
                i += 1
            continue
        elif t == "[t":
            if s[i] == "]":
                t = "[t]"
                i += 1
            else:
                _s[-1] += s[i]
                i += 1
            continue
        elif t == "[t]":
            if s[i] == "]":
                o += "<a href='wiki/%s' title='%s'>%s</a>" % (_s[-2], _s[-2], _s[-1])
                t = ""
                i += 1
                _s.pop()
                _s.pop()
            else:
                _s[-1] += "]" + s[i]
                t = "[t"
                i += 1
            continue
        # templates
        if t == "{":
            if s[i] == "{":
                t = "{t"
                i += 1
                _s.append([""])
            else:
                o += "{" + s[i]
                t = ""
                i += 1
            continue
        elif t == "{t":
            if s[i] == "}":
                t = "{t}"
                i += 1
            elif s[i] == "|":
                t = "{|"
                i += 1
            else:
                _s[-1][-1] += s[i]
                i += 1
            continue
        elif t == "{|":
            if s[i] == "}":
                t = "{t}"
                i += 1
                _s[-1].append("")
            else:
                if s[i] == "|":
                    t = "{|"
                    i += 1
                    _s[-1].append("")
                else:
                    _s[-1].append(s[i])
                    t = "{t"
                    i += 1
            continue
        elif t == "{t}":
            if s[i] == "}":
                t = ""
                i += 1
                o += write(templ.all[_s[-1][0]](*_s[-1][1:])) if templ.conv else templ.all[_s[-1][0]](*_s[-1][1:])
                _s.pop()
            else:
                if s[i] == "|":
                    t = "{|"
                    i += 1
                    _s[-1][-1] += "}"
                else:
                    t = "{t"
                    _s[-1][-1] += "}" + s[i]
                    i += 1
        else:
            if s[i] == "[":
                t = "["
                i += 1
            elif s[i] == "{":
                t = "{"
                i += 1
            else:
                o += s[i]
                i += 1
    return o + (data.struct[4] if page else "")
# print(write(data.pages["VD I"], True))

page = open("wiki/index.html", "w", encoding="utf-8")
page.write(write(data.main, True, "Главная"))
page.close()

page = open("wiki/all/index.html", "w", encoding="utf-8")
page.write(write("<table width='100%'>" + "".join(["""<tr bgcolor="#aaa">
      <td>{{tree|%s}}</td>
      </tr>""" % i for i in data.all]) + "</table>", True, "Все создания"))
page.close()

for nmpg in data.pages.keys():
    try:
        os.mkdir("wiki/" + nmpg)
    except:
        pass
    page = open("wiki/%s/index.html" % nmpg, "w", encoding="utf-8")
    page.write(write(data.pages[nmpg], True, nmpg))
    page.close()
