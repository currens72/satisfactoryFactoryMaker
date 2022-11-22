def itemSelection(item, amount):
    print("-----------------------------------------------------------------------------------")
    print("In order to make " + str(amount) + " " + item + "(s) per minute, you need:")

######################################
####smelter
    if item == "iron ingot":
        baseIngot("iron", amount)
    elif item == "copper ingot":
        baseIngot("copper", amount)
    elif item == "caterium ingot":
        baseIngot("caterium", amount)
######################################
####constructor
    elif item == "iron plate":
        constructor(item, amount)
    elif item == "iron rod":
        constructor(item, amount)
    elif item == "iron rebar":
        constructor(item, amount)
    elif item == "screw":
        constructor(item, amount)
######################################
######################################
    elif item == "steel ingot":               #TODO
        print()
######################################
    elif item == "aluminum ingot":            #TODO
        print()
######################################
    else:
        print("Invalid Selection")
    print("-----------------------------------------------------------------------------------")

def baseIngot(ingot, amount):
    smelters = amount // 30
    if amount % 30 > 0:
        smelters = round(smelters + ((amount % 30) / 30), 2)
    amount = round(amount, 2)
    print(str(amount) + " " + ingot + " ore per minute")
    print(str(smelters) + " smelter(s) making " + ingot + " ingots")

def constructor(product, amount):
    if product == "iron plate":
        constructors = amount // 20
        if amount % 20 > 0:
            constructors = round(constructors + ((amount % 20) / 20), 2)
        baseIngot("iron", amount / 20 * 30)
        print(str(constructors) + " constructor(s) making " + product + "s")
    if product == "iron rod":
        constructors = amount // 15
        if amount % 15 > 0:
            constructors = round(constructors + ((amount % 15) / 15), 2)
        baseIngot("iron", amount / 15 * 15)
        print(str(constructors) + " constructor(s) making " + product + "s")
    if product == "iron rebar":
        constructors = amount // 15
        if amount % 15 > 0:
            constructors = round(constructors + ((amount % 15) / 15), 2)
        constructor("iron rod", amount / 15 * 15)
        print(str(constructors) + " constructor(s) making " + product + "s")
    if product == "screw":
        constructors = amount // 40
        if amount % 40 > 0:
            constructors = round(constructors + ((amount % 40) / 40), 2)
        constructor("iron rod", amount / 40 * 10)
        print(str(constructors) + " constructor(s) making " + product + "s")
    ########################################################
    if product == "aluminum casing":
        constructors = amount // 60
        if amount % 60 > 0:
            constructors = round(constructors + ((amount % 60) / 60), 2)
    ########################################################
    if product == "cable":
        constructors = amount // 30
        if amount % 30 > 0:
            constructors = round(constructors + ((amount % 30) / 30), 2)
    ########################################################
    if product == "concrete":
        constructors = amount // 15
        if amount % 15 > 0:
            constructors = round(constructors + ((amount % 15) / 15), 2)
    ########################################################
    if product == "copper powder":
        constructors = amount // 50
        if amount % 50 > 0:
            constructors = round(constructors + ((amount % 50) / 50), 2)
    ########################################################
    if product == "copper sheet":
        constructors = amount // 10
        if amount % 10 > 0:
            constructors = round(constructors + ((amount % 10) / 10), 2)
    ########################################################
    if product == "empty canister":
        constructors = amount // 60
        if amount % 60 > 0:
            constructors = round(constructors + ((amount % 60) / 60), 2)
    ########################################################
    if product == "empty fluid tank":
        constructors = amount // 60
        if amount % 60 > 0:
            constructors = round(constructors + ((amount % 60) / 60), 2)
    ########################################################
    if product == "quartz crystal":
        constructors = amount // 22.5
        if amount % 22.5 > 0:
            constructors = round(constructors + ((amount % 22.5) / 22.5), 2)
    ########################################################
    if product == "quickwirre":
        constructors = amount // 60
        if amount % 60 > 0:
            constructors = round(constructors + ((amount % 60) / 60), 2)
    ########################################################
    if product == "silica":
        constructors = amount // 37.5
        if amount % 37.5 > 0:
            constructors = round(constructors + ((amount % 37.5) / 37.5), 2)
    ########################################################
    if product == "steel beam":
        constructors = amount // 15
        if amount % 15 > 0:
            constructors = round(constructors + ((amount % 15) / 15), 2)
    ########################################################
    if product == "steel pipe":
        constructors = amount // 20
        if amount % 20 > 0:
            constructors = round(constructors + ((amount % 20) / 20), 2)
    ########################################################