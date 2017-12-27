header = """<img src='/rht/logo.png' class='menu-logo'><br>
 • <a href='/rht/wiki/'>Главная</a><br>
 • <a href='/rht/tree/'>Все создания</a><br>
<hr>
 • Short link: <a href='https://goo.gl/m1oTU6'>goo.gl/m1oTU6</a>"""

struct = [
    """
<!DOCTYPE html>
<html lang='ru'>
    <head>
        <link href='/rht/styles/common.css' rel='stylesheet'>
        <link href='/rht/styles/menu.css' rel='stylesheet'>
        <link href='/rht/styles/body.css' rel='stylesheet'>
        <link href='/rht/styles/title.css' rel='stylesheet'>
        <link href='/rht/styles/card-rb.css' rel='stylesheet'>
        <link href='/rht/styles/comp.css' rel='stylesheet'>""",
    """
    </head>
    <body bgcolor='#dfe'>
        <table width='100%' bgcolor='#dfe'>
            <tr>
                <td class='menu' rowspan='3'>
                    <div class='menu'>""",
    """
                    </div>
                </td>
                <td rowspan='3'></td>
                <td class='title'>\n""",
    """
                </td>
            </tr>
            <tr>
                <td height='25px'></td>
            </tr>
            <tr>
                <td rowspan='1' class='body'>""",
    """
                </td>
            </tr>
        </table>
    </body>
</html>"""]

main = """
{{comp|Robofinist 2017|Ралли по коридору|Robofinist 2017|{{robolink|RW-U}}|9}}
{{comp|Собери своего робота 2017|Полигон|Собери своего робота 2017|{{robolink|T.Tr Line}}|1}}"""

pages = {
    "RW-U": """{{Card|RW-U||L|RW-U.svg||{{robolink|T.S}} • {{robolink|RW-B}}|40|40|20||f|0.5|87.8}}<br>
    
    {{h2|История создания|History}}
    {{h3|RW-U-a|RW-U-a}}
    {{h3|RW-U-b|RW-U-b}}
    {{h3|RW-U-c|RW-U-c}}
    """"",
    ###
    "RW-B": """{{Card|RW-B||L|RW-B.svg|{{robolink|RW-U}}||40|40|20||f|0.5|87.8}}
    """"",
    ###
    "T.S": """{{Card|T.S||L|T.S.svg|{{robolink|RW-U}}|{{robolink|IKAR-1718-L}} • {{robolink|L-U}}|20|20|10||b||}}

        {{h2|Модели на этой базе|models}}
          • {{robolink|T.S Line}}
        """,
    ###
    "T.S Line": """{{Card|T.S Line||L|T.S Line.svg|{{robolink|T.S}}|{{robolink|L-U}}|||||b||}}""",
    ###
    "IKAR-1718-L": """{{Card|T.S Line||L|T.S Line.svg|{{robolink|T.S}}|{{robolink|L-U}}|||||b||}}""",
    ###
    "L-U": """{{Card|T.S Line||L|T.S Line.svg|{{robolink|T.S Line}} • {{robolink|IKAR-1718-L}}||||||b||}}""",
    ###
    "T.Tr": """{{Card|T.Tr||mB|T.Tr.svg|||20|20|10||b||}}<br>
     
     {{h2|T.Tr bis|T.Tr bis}}
     T.Tr bis - усовершенствованая модель. Блок управления поставлен сзади над моторами, что дало дополнительное место для установки модулей.
     
     {{h2|Модели на этой базе|models}}
     {{h3|{{robolink|T.Tr|#}}|models T.Tr}}
      • {{robolink|T.Tr Line}}
     {{h3|{{robolink|T.Tr bis|#T.Tr bis}}|models T.Tr bis}}
      • {{robolink|T.Tr IKAR-1718-H}}<br/>
      • {{robolink|T.Tr Line}}
     
     {{h2|Соревнования|comp}}
     {{comp|Собери своего робота 2017|Полигон|Собери своего робота 2017|{{robolink|T.Tr Line}}|1}}""",
    ###
    "T.Tr Line": """{{Card|T.Tr Line||mB|T.Tr Line.svg|{{robolink|T.Tr}}||20|20|10||b||}}

     {{h2|Соревнования|comp}}
     {{comp|Собери своего робота 2017|Полигон|Собери своего робота 2017|T.Tr Line|1}}""",
    ###
    "T.Tr IKAR-1718-H": """{{Card|T.Tr IKAR-1718-H||mB|T.Tr IKAR-1718-H.svg|{{robolink|T.Tr|T.Tr#T.Tr bis}}||20|20|10||b||}}""",
    ###
    "Собери своего робота 2017": """{{BCard|Собери своего робота|08/10/2017|http://belsmus.ru/tenders/Konkurs-%22Soberi-svoego-robota-2017%22}}
    {{comp_u|{{robolink|T.Tr Line}}|1}}""",
    ###
    "Robofinist 2017": """{{BCard|Robofinist|28/10/2017 – 29/10/2017|https://robofinist.ru/event/info/competitions/id/132#kind957}}

     {{h2|Соревнования|comp}}
     {{comp|Robofinist 2017|Ралли по коридору|Robofinist 2017|RW-U-c|9}}""",
    ###
    "ИКАР 2018": """{{BCard|ИКАР||http://xn--80apgz.xn--c1awjj.xn--p1ai/ikar-profi}}""",
    ###
    "": ""}

icons = {"RW-U": "RW-U.svg",
         "RW-U-a": "RW-U-a.svg",
         "RW-U-b": "RW-U-b.svg",
         "RW-U-c": "RW-U-c.svg",
         "RW-B": "RW-U-c.svg",
         "T.S": "T.S.svg",
         "T.S Line": "T.S Line.svg",
         "T.Tr": "T.Tr.svg",
         "T.Tr Line": "T.Tr Line.svg",
         "IKAR-1718-L": "IKAR-1718-L.svg",
         "L-U": "L-U.svg",
         "T.Tr bis": "T.Tr bis.svg",
         "T.Tr IKAR-1718-H": "T.Tr IKAR-1718-H.svg"}

styles = {""""""}
