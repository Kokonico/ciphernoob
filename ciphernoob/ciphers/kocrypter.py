"""This file contains kocrypter, again, you shouldn't be here."""

from ciphernoob import __utils

# dear whoever reads this
# I am so, very sorry for what you are about to see
# please forgive me.
char_mush = {
  "A1": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890",
  "A2": """:;/|!@#$%^&*()_+-=}{][?><,.'" ☐☑☒✓☺äü·∄∃’‘”“❛❜❝❞—–²¹x⁰ⁱ""",
  "A3": """⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₔ áâäéêëíîïñśó""",
  "A4":  """õöúûüÿ™¢£©®°±µ⧾⧿⨀⨁⨂⨃⨄⨅⨆⨇⨈⨉⨊⨋⨌⨍⨎⨏⨐⨑⨒⨓⨔⨕⨖⨗⨘⨙⨚⨛⨜⨝⨞⨟""",
  "A5": """⨠⨡⨢⨣⨤⨥⨦⨧⨨⨩⨪⨫⨬⨭⨮⨯⨰⨱⨲⨳⨴⨵⨶⨷⨸⨹⨺⨻⨼⨽⨾⨿⩀⩁⩂⩃⩄⩅⩆⩇⩈⩉""",
  "A6": """⩊⩋⩌⩍⩎⩏⩐⩑⩒⩓⩔⩕⩖⩗⩘⩙⩚⩛⩜⩝⩞⩟⩠⩡⩢⩣⩤⩥⩦⩧⩨⩩⩪⩫⩬⩭⩮⩯⩰⩱""",
  "A7": """⩲⩳⩴⩵⩶⩷⩸⩹⩺⩻⩼⩽⩾⩿⪀⪁⪂⪃⪄⪅⪆⪇⪌⪍⪎⪏⪐⪑⪒⪓⪔⪕⪖⪗⪘⪙⪚⪛⪜⪝⪞⪟""",
  "A8": """⪠⪡⪢⪣⪤⪥⪦⪧⪨⪩⪪⪫⪬⪭⪮⪯⪰⪱⪲⪳⪴⪵⪶⪷⪸⪹⪺⪻⪼⪽⪾⪿⫀⫁⫂⫃⫄⫅⫆⫇⫈⫉⫊⫋""",
  "A9": """⫌⫍⫎⫏⫐⫑⫒⫓⫔⫕⫖⫗⫘⫙⫚⫛⫝̸⫝⫞⫟⫠⫡⫢⫣⫤⫥⫦⫧⫨⫩⫪⫫⫬⫭⫮⫯⫰⫱⫲⫳⫴⫵⫶⫷⫸""",
  "A10": """⫹⫺⫻⫼⫽⫾⫿⬀⬁⬂⬃⬄⬅⬆⬇⬈⬉⬊⬋⬌⬍⬎⬏⬐⬑⬒⬓⬔⬕⬖⬗⬘⬙⬚⬛⬜⬝⬞⬟⬠⬡⬢⬣⬤""",
  "A11": """⬥⬦⬧⬨⬩⬪⬫⬬⬭⬮⬯⬰⬱⬲⬳⬴⬵⬶⬷⬸⬹⬺⬻⬼⬽⬾⬿⭀⭁⭂⭃⭄⭅⭆⭇⭈⭉⭊⭋⭌⭍⭎⭏⭐⭑""",
  "A12": """⭒⭓⭔⭕⭖⭗⭘⭙⭚⭛⭜⭝⭞⭟⭠⭡⭢⭣⭤⭥⭦⭧⭨⭩⭪⭫⭬⭭⭮⭯⭰⭱⭲⭳⭴⭵⭶⭷⭸⭹⭺⭻⭼⭽⭾""",
  "A13": """⭿⮀⮁⮂⮃⮄⮅⮆⮇⮈⮉⮊⮋⮌⮍⮎⮏⮐⮑⮒⮓⮔⮕⮖⮗⮘⮙⮚⮛⮜⮝⮞⮟⮠⮡⮢⮣⮤⮥⮦⮧⮨⮩⮪⮫""",
  "A14": """⮬⮭⮮⮯⮰⮱⮲⮳⮴⮵⮶⮷⮸⮹⮺⮻⮼⮽⮾⮿⯀⯁⯂⯃⯄⯅⯆⯇⯈⯉⯊⯋⯌⯍⯎⯏⯐⯑⯒⯓⯔⯕⯖⯗⯘""",
  "A15": """⯙⯚⯛⯜⯝⯞⯟⯠⯡⯢⯣⯤⯥⯦⯧⯨⯩⯪⯫⯬⯭⯮⯯⯰⯱⯲⯳⯴⯵⯶⯷⯸⯹⯺⯻⯼⯽⯾⯿""",
  "A16": """ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢⰣⰤⰥⰦⰧⰨⰩⰪⰫ""",
  "A17": """ⰬⰭⰮⰯⰰⰱⰲⰳⰴⰵⰶⰷⰸⰹⰺⰻⰼⰽⰾⰿⱀⱁⱂⱃⱄⱅⱆⱇⱈⱉⱊⱋⱌⱍⱎⱏⱐⱑⱒⱓⱔⱕⱖⱗⱘ""",
  "A18": """ⱙⱚⱛⱜⱝⱞⱟⱠⱡⱢⱣⱤⱥⱦⱧⱨⱩⱪⱫⱬⱭⱮⱯⱰⱱⱲⱳⱴⱵⱶⱷⱸⱹⱺⱻⱼⱽⱾⱿⲀⲁⲂⲃⲄⲅⲆⲇ""",
  "A19": """ⲈⲉⲊⲋⲌⲍⲎⲏⲐⲑⲒⲓⲔⲕⲖⲗⲘⲙⲚⲛⲜⲝⲞⲟⲠⲡⲢⲣⲤⲥⲦⲧⲨⲩⲪⲫⲬⲭⲮⲯⲰⲱⲲⲳ""",
  "A20": """ⲴⲵⲶⲷⲸⲹⲺⲻⲼⲽⲾⲿⳀⳁⳂⳃⳄⳅⳆⳇⳈⳉⳊⳋⳌⳍⳎⳏⳐⳑⳒⳓⳔⳕⳖⳗⳘⳙⳚⳛⳜⳝⳞⳟ""",
  "A21": """ⳠⳡⳢⳣⳤ⳥⳦⳧⳨⳩⳪ⳫⳬⳭⳮ⳯⳰⳱Ⳳⳳ⳴⳵⳶⳷⳸⳹⳺⳻⳼⳽⳾⳿ⴀⴁⴂⴃⴄⴅⴆⴇⴈⴉⴊⴋ""",
  "A22": """ⴌⴍⴎⴏⴐⴑⴒⴓⴔⴕⴖⴗⴘⴙⴚⴛⴜⴝⴞⴟⴠⴡⴢⴣⴤⴥ⴦ⴧ⴨⴩⴪⴫⴬ⴭ⴮⴯ⴰⴱⴲⴳⴴⴵⴶⴷⴸ""",
  "A23": """ⴹⴺⴻⴼⴽⴾⴿⵀⵁⵂⵃⵄⵅⵆⵇⵈⵉⵊⵋⵌⵍⵎⵏⵐⵑⵒⵓⵔⵕⵖⵗⵘⵙⵚⵛⵜⵝⵞⵟⵠⵡⵢⵣⵤ""",
  "A24": """ⵥⵦⵧ⵨⵩⵪⵫⵬⵭⵮ⵯ⵰⵱⵲⵳⵴⵵⵶⵷⵸⵹⵺⵻⵼⵽⵾⵿ⶀⶁⶂⶃⶄⶅⶆⶇⶈⶉⶊⶋⶌⶍⶎⶏⶐ""",
  "A25": """ⶑⶒⶓⶔⶕⶖ⶗⶘⶙⶚⶛⶜⶝⶞⶟ⶠⶡⶢⶣⶤⶥⶦ⶧ⶨⶩⶪⶫⶬⶭⶮ⶯ⶰⶱⶲⶳⶴⶵⶶ⶷ⶸⶹⶺⶻⶼⶽⶾ""",
  "A26": """⶿ⷀⷁⷂⷃⷄⷅⷆ⷇ⷈⷉⷊⷋⷌⷍⷎ⷏ⷐⷑⷒⷓⷔⷕⷖ⷗ⷘⷙⷚⷛⷜⷝⷞ⷟ⷠⷡⷢⷣⷤⷥⷦⷧⷨⷩⷪⷫⷬ""",
  "A27": """ⷭⷮⷯⷰⷱⷲⷳⷴⷵⷶⷷⷸⷹⷺⷻⷼⷽⷾⷿ⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘""",
  "A28": """⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿""",
  "A29": """⠀⠁⠂⠃⠄⠅⠆⠇⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠""",
  "A30": """⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉""",
  "A31": """⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴""",
  "A32": """⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟""",
  "A33": """⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿""",
}

ALPHABET = __utils.d_mush(char_mush)

def kocrypt(
    cmdinput,
    cmdkey,
    mode: bool,
):
    """Encrypts plain text by shifting and converting into numbers. use "mode" to select
    encryption or decryption"""
    if mode:
        offset_number = int(cmdkey)
        pos = offset_number
        output = ""
        outlist = []

        # Calculate the true shift value
        numre = 0
        trueshift = 0
        alpha_l = len(ALPHABET)

        while numre != offset_number:
            numre += 1
            trueshift += 1
            if trueshift >= alpha_l:
                trueshift = 0

        for x in cmdinput:
            if x in ALPHABET:
                n = (ALPHABET.index(x) + trueshift) % alpha_l
                n = str(n)
                outlist.append(n)

        pos %= len(outlist)
        output = "/".join(map(str, outlist[-pos:] + outlist[:-pos]))
        return output
    else:
        if not mode:
            offset_code = cmdinput
            offset_key = int(cmdkey)
            reverse_offset = offset_key * -1
            inlist = offset_code.split("/")
            offpos = reverse_offset
            offpos %= len(inlist)
            inlist = inlist[-offpos:] + inlist[:-offpos]
            inlist2 = []
            result = []

            # Calculate the true shift value for decryption
            numre = 0
            trueshift = 0
            alpha_l = len(ALPHABET)

            while numre != offset_key:
                numre += 1
                trueshift += 1
                if trueshift >= alpha_l:
                    trueshift = 0

            # Remove offset using the key
            for a in inlist:
                n = (int(a) - trueshift) % alpha_l
                n = str(n)
                inlist2.append(n)

                # Convert back to regular characters
            for y in inlist2:
                if y.isdigit():
                    result.append(ALPHABET[int(y)])

            return "".join(result)
        else:
            # tell the user they don't know what they are doing
            ValueError("invalid mode")
