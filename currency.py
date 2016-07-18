class Currency:
    def __init__(self, code, value=None):
        self.code = code
        if value:
            self.value = float(value)
        else:
            clean_string = self.code.replace(' ', '')
            symbol = clean_string[0]
            self.code = CURRENCY_SYMBOLS[symbol]
            self.value = float(clean_string[1:])

    def __str__(self):
        return "Currency({}, {})".format(self.code, self.value)

    def __add__(self, other):
        if self.code != other.code:
            raise DifferentCurrencyCodeError
        else:
            return Currency(self.code, self.value + other.value)

    def __sub__(self, other):
        if self.code != other.code:
            raise DifferentCurrencyCodeError
        else:
            return Currency(self.code, self.value - other.value)

    def __mul__(self, mul_by):
        return Currency(self.code, self.value * mul_by)

    def __eq__(self, other):
        return self.code == other.code and self.value == other.value

class DifferentCurrencyCodeError(Exception):
    pass

#later in code we will use raise(DifferentCurrencyCodeError)

#currencies = [('USD', 1), ('EUR', 1)]
#[Currency(type, value) for type, value in currencies]

CURRENCY_SYMBOLS = {'$':'USD', '€':'EUR', '¥':'JPY'}

CURRENCY_CONVERSIONS = {"ADF":5.941770647653001, "ADP":150.71590052750565,
                        "AED":3.6724201248622843, "AFN":68.7757909215956,
                        "ALL":121.71372930866603, "AMD":476.64442326024783,
                        "ANG":1.7699115044247788, "AOA":165.0709805216243,
                        "AON":165.0709805216243, "ARS":14.923145799134458,
                        "ATS":12.464165524118162, "AUD":1.3190871916633689,
                        "AWG":1.7898693395382137, "AZM":7788.16199376947,
                        "AZN":1.558117793705204, "BAM":1.771793054571226,
                        "BBD":2, "BDT":77.51937984496124,
                        "BEF":36.53635367190355, "BGN":1.763357432551578,
                        "BHD":0.3744757339724386, "BIF":1645.5487905216391,
                        "BMD":1, "BND":1.3338668800853675,
                        "BOB":6.7704807041299935, "BRL":3.2743942370661427,
                        "BSD":0.984251968503937, "BTN":67.02412868632707,
                        "BWP":10.711225364181663, "BYR":20020.02002002002,
                        "BZD":1.9688915140775742, "CAD":1.2966804979253113,
                        "CDF":939.8496240601503, "CHF":0.9821253191907288,
                        "CLP":645.1612903225806,"CNY":6.688963210702341,
                        "COP":2898.5507246376815, "CRC":539.0835579514825,
                        "CUC":1, "CUP":22.22222222222222,
                        "CVE":99.9000999000999, "CYP":0.5301383661135556,
                        "CZK":24.49179524859172, "DEM":1.7714791851195748,
                        "DJF":176.5848490199541, "DKK":6.734006734006734,
                        "DOP":45.662100456621005, "DZD":110.13215859030838,
                        "ECS":24096.385542168675, "EEK":14.17233560090703,
                        "EGP":8.857395925597874, "ESP":150.71590052750565,
                        "ETB":21.734405564007822, "EUR":0.9057971014492753,
                        "FIM":5.385029617662897, "FJD":2.0521239482864764,
                        "FKP":0.757920266787934, "FRF":5.941770647653001,
                        "GBP":0.7581501137225171, "GEL":2.340823970037453,
                        "GHC":39698.292973402145, "GHS":3.969829297340214,
                        "GIP":0.757920266787934, "GMD":42.158516020236085,
                        "GNF":8992.805755395682, "GRD":308.641975308642,
                        "GTQ":7.501875468867217, "GYD":200.92425155716296,
                        "HKD":7.751937984496124, "HNL":22.578460149017836,
                        "HRK":6.784260515603799, "HTG":63.171193935565384,
                        "HUF":285.06271379703537, "IDR":13054.830287206265,
                        "IEP":0.713368526180625, "ILS":3.865481252415926,
                        "INR":66.93440428380187, "IQD":1154.4677903486493,
                        "IRR":30075.18796992481, "ISK":121.00677637947724,
                        "ITL":1753.77060680463, "JMD":126.13521695257317,
                        "JOD":0.7069136151562279, "JPY":104.81081647626036,
                        "KES":99.50248756218906, "KGS":67.24949562878278,
                        "KHR":4032.258064516129, "KMF":425.1700680272109,
                        "KPW":135.00742540839747, "KRW":1136.8804001819008,
                        "KWD":0.3015226895823911, "KYD":0.8229098090849243,
                        "KZT":339.67391304347825, "LAK":7949.12559618442,
                        "LBP":1488.7598630340926, "LKR":144.07145944388415,
                        "LRD":90.00900090009002, "LSL":14.535517537101908,
                        "LTL":3.127932436659368, "LUF":36.53635367190355,
                        "LVL":0.6365777579731364, "LYD":1.373437714599643,
                        "MAD":9.551098376313275, "MDL":19.71608832807571,
                        "MGA":2976.190476190476, "MGF":9149.130832570905,
                        "MKD":55.40166204986149, "MMK":1170.9601873536299,
                        "MNT":2002.0020020020017, "MOP":7.880220646178092,
                        "MRO":353.1073446327684, "MTL":0.3888478438387059,
                        "MUR":34.059945504087196, "MVR":14.961101137043688,
                        "MWK":712.2507122507122, "MXN":18.58045336306206,
                        "MYR":3.9154267815191854, "MZM":65316.78641410842,
                        "MZN":65.31678641410842, "NAD":14.535517537101908,
                        "NGN":284.25241614553727, "NIO":28.264556246466928,
                        "NLG":1.996007984031936, "NOK":8.460236886632826,
                        "NPR":106.78056593699947, "NZD":1.4033118158854898,
                        "OMR":0.3836415253587049, "PAB":1,
                        "PEN":3.238341968911917, "PGK":3.1240237425804436,
                        "PHP":46.70714619336759, "PKR":104.36234606553955,
                        "PLN":4.00320256204964, "PTE":181.58707100054477,
                        "PYG":5530.973451327433, "QAR":3.6403349108117946,
                        "ROL":40567.95131845842, "RON":4.056795131845842,
                        "RSD":111.25945705384959, "RUB":63.331222292590255,
                        "RWF":777.6049766718506, "SAR":3.746721618583739,
                        "SBD":7.8431372549019605, "SCR":11.940298507462686,
                        "SDD":610.1281269066503, "SDG":6.101281269066504,
                        "SDP":2260.9088853719195, "SEK":8.56898029134533,
                        "SGD":1.3468013468013467, "SHP":0.5743165632896853,
                        "SIT":217.06099413935317, "SKK":27.28512960436562,
                        "SLL":5485.463521667581, "SOS":554.9389567147614,
                        "SRD":7.032348804500703, "SRG":7032.348804500704,
                        "STD":22202.48667850799, "SVC":8.613264427217915,
                        "SYP":215.88946459412782, "SZL":14.535517537101908,
                        "THB":34.81894150417828, "TJS":7.867820613690008,
                        "TMM":17543.859649122805, "TMT":3.4916201117318435,
                        "TND":2.2143489813994686, "TOP":2.2507314877335136,
                        "TRL":3008423.5860409145, "TRY":3.008423586040915,
                        "TTD":6.622516556291391, "TWD":31.746031746031747,
                        "TZS":2166.8472372697724, "UAH":24.8015873015873,
                        "UGX":3354.579000335458, "USD":1,
                        "UYU":30.093289196509176, "UZS":2944.6407538280328,
                        "VEB":9980.039920159681, "VEF":9.980039920159681,
                        "VND":22153.300841825432, "VUV":105.21885521885521,
                        "WST":2.5432349949135302, "XAF":594.5303210463734,
                        "XAG":0.04932888057971301, "XAU":0.0007473618128008132,
                        "XCD":2.6881720430107525, "XEU":0.9057971014492753,
                        "XOF":594.5303210463734, "XPD":0.0015435552708553612,
                        "XPF":108.08473843493299, "XPT":0.0009150386603834012,
                        "YER":249.8750624687656, "YUN":111.25945705384959,
                        "ZAR":14.534883720930232, "ZMK":5175.983436853002,
                        "ZMW":10.17708121310808, "ZWD":373.2736095558044}

"""
Currency objects

Must be created with an amount and a currency code.
Must equal another Currency object with the same amount and currency code.
Must NOT equal another Currency object with different amount or currency code.
Must be able to be added to another Currency object with the same currency code.
Must be able to be subtracted by another Currency object with the same currency code.
Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
Must be able to be multiplied by an int or float and return a Currency object.
Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or "€ 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
CurrencyConverter objects

Must be initialized with a dictionary of currency codes to conversion rates (see link to rates below).
At first, just make this work with two currency codes and conversation rates, with one rate being 1.0 and the other being the conversation rate. An example would be this: {'USD': 1.0, 'EUR': 0.74}, which implies that a dollar is worth 0.74 euros.
Must be able to take a Currency object and a requested currency code that is the same currency code as the Currency object's and return a Currency object equal to the one passed in. That is, currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD').
Must be able to take a Currency object that has one currency code it knows and a requested currency code and return a new Currency object with the right amount in the new currency code.
Must be able to be created with a dictionary of three or more currency codes and conversion rates. An example would be this: {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}, which implies that a dollar is worth 0.74 euros and that a dollar is worth 120 yen, but also that a euro is worth 120/0.74 = 162.2 yen.
Must be able to convert Currency in any currency code it knows about to Currency in any other currency code it knows about.
Must raise an UnknownCurrencyCodeError when you try to convert from or to a currency code it doesn't know about.
"""
