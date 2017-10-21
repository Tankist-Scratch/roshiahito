header = """<img src='/roshiahito/logo.png' class='menu-logo'><br>
 • <a href='/roshiahito/wiki/'>Главная</a><br>
 • <a href='/roshiahito/tree/'>Все создания</a><br>
<hr>
 • Short link <a href='https://goo.gl/g5SiYW'>goo.gl/g5SiYW</a>"""

struct = ["<!DOCTYPE html><html lang='ru'><head><link href='/roshiahito/styles/common.css' rel='stylesheet'><link href='/roshiahito/styles/menu.css' rel='stylesheet'><link href='/roshiahito/styles/body.css' rel='stylesheet'><link href='/roshiahito/styles/title.css' rel='stylesheet'><link href='/roshiahito/styles/card-rb.css' rel='stylesheet'><link href='/roshiahito/styles/comp.css' rel='stylesheet'>",
          "\n</head><body bgcolor='#dfe'>\n<table width='100%' bgcolor='#dfe'><tr><td class='menu' rowspan='3'>\n",
          "\n<td rowspan='3'></td><td class='title'>\n", "\n</h1></td></tr>\n<tr><td height='25px'></td></tr><tr><td rowspan='2' class='body'>",
          "</td></tr><tr><td></td></tr></table>\n</body></html>"]

main = """"""

pages = {
    "RW-U": """{{Card|RW-U||L|RW-U.svg||{{robolink|T.S|T.s|T.S.svg}}|40|40|20||f|0.5|87.8}} RW-U - первый робот ветки внедорожников. Первый раз принял участие в [[Robofinist 2017|'Ралли по коридору']] в 2017 году.<br>
    
    {{h2|История|History}}
    {{id|RW-U-a}}
    {{Card|RW-U-a||L|RW-U-a.svg||{{robolink|RW-U-b|#RW-U-b|RW-U-b.svg}}|40|40|20||b||}}
    Самый первый робот из настоящих машин. Имел много недостатков, из-за чего был разобран.<br>
    {{id|RW-U-b}}
    {{Card|RW-U-b||L|RW-U-b.svg|{{robolink|RW-U-a|#RW-U-a|RW-U-a.svg}}|{{robolink|RW-U-c|#RW-U-c|RW-U-c.svg}} {{robolink|T.S|T.s|T.S.svg}}|40|40|20||b||}}
    Уменьшенная модель RW-U-a. 
    {{id|RW-U-c}}
    {{Card|RW-U-c||L|RW-U-c.svg|{{robolink|RW-U-b|#RW-U-b|RW-U-b.svg}}|{{robolink|RW-B|RW-B|RW-U.svg}}|40|40|20||f|0.5|87.8}}
    """"",
    "Robofinist 2017": """{{BCard|Robofinist|28/10/2017 – 29/10/2017|https://robofinist.ru/event/info/competitions/id/132#kind957}}""",
    "T.Tr": """{{Card|T.Tr||mB|T.Tr.svg|||20|20|10||b||}}T.Tr - самый первый робот собраный на MakeBlock. Хорошо подходит для езды по линии.<br>
         
         <h2>Модули</h2>
         {{mod|mB-Line-U|mB-Line|mB-Line-U}}
         
         <h2>Соревнования</h2>
         {{comp|Собери своего робота 2017|Полигон|Собери своего робота 2017|T.Tr|1}}""",
    "T.S": """{{Card|T.S||L|T.S.svg|{{robolink|RW-U|RW-U|RW-U.svg}}||20|20|10||b||}}T.S - тележка построеная на базе {{robolink|RW-U|RW-U|}}. Унаследовала помещение электроники в трубу, что увеличивает количество мест для крепления.""",
    "Собери своего робота 2017": """{{BCard|Собери своего робота|08/10/2017|http://belsmus.ru/tenders/Konkurs-%22Soberi-svoego-robota-2017%22}}
    
    <h2>Участники</h2>
    {{battleS|T.Tr Line-U|T.Tr|1|Полигон}}"""}
icons = {"RW-U" : "RW-U.svg",
    "RW-U-a" : "RW-U-a.svg",
    "RW-U-b" : "RW-U-b.svg",
    "RW-U-c" : "RW-U-c.svg",
    "RW-B" : "RW-U-c.svg",
    "T.S" : "T.S.svg",
    "T.Tr" : "T.Tr.svg"}

styles = {""""""}
