def itemSelection(item, amount):
    global finalString, finalPower
    finalString = ""
    finalPower = 0
######################################
####smelter
    if item == "iron ingot":
        smelterFunction("iron", amount)
    elif item == "copper ingot":
        smelterFunction("copper", amount)
######################################
####constructor
    elif item == "iron plate":
        constructorFunction(item, amount)
    elif item == "iron rod":
        constructorFunction(item, amount)
    elif item == "wire":
        constructorFunction(item, amount)
    elif item == "cable":
        constructorFunction(item, amount)
######################################
####assembler
######################################
######################################
######################################
    else:
        return "Invalid Selection"
    finalPower = round(finalPower, 2)
    finalString = str(finalPower) + " MW\n" + finalString
    return finalString

def smelterFunction(ingot, amount):
    global finalString, finalPower
    if ingot == "iron" or ingot == "copper":
        smelters = amount // 30
        if amount % 30 > 0:
            smelters = round(smelters + ((amount % 30) / 30), 2)
        amount = round(amount, 2)
        finalPower = finalPower + (smelters * 4)
        finalString = finalString + str(amount) + " " + ingot + " ore per minute" + "\n"
        finalString = finalString + str(smelters) + " smelter(s) making " + ingot + " ingots" + "\n"

def constructorFunction(product, amount):
    global finalString, finalPower
    constructors = 0
    permin = 0
    inmin = 0
    if product == "iron plate":
        permin = 20
        inmin = 30
        constructors = amount // permin
        if amount % permin > 0:
            constructors = round(constructors + ((amount % permin) / permin), 2)
        smelterFunction("iron", amount / permin * inmin)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "s" + "\n"
    if product == "iron rod":
        permin = 15
        inmin = 15
        constructors = amount // permin
        if amount % permin > 0:
            constructors = round(constructors + ((amount % permin) / permin), 2)
        smelterFunction("iron", amount / permin * permin)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "s" + "\n"
    if product == "wire":
        permin = 30
        inmin = 15
        constructors = amount // permin
        if amount % permin > 0:
            constructors = round(constructors + ((amount % permin) / permin), 2)
        smelterFunction("copper", amount / permin * inmin)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "s" + "\n"
    if product == "cable":
        permin = 30
        inmin = 60
        constructors = amount // permin
        if amount % permin > 0:
            constructors = round(constructors + ((amount % permin) / permin), 2)
        constructorFunction("wire", amount / permin * inmin)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "s" + "\n"
    
    finalPower = finalPower + (constructors * 4)