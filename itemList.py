def itemSelection(item, amount):
    global finalString, finalPower, topLevel
    topLevel = True
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
    elif item == "concrete":
        constructorFunction(item, amount)
    elif item == "screw":
        constructorFunction(item, amount)
    elif item == "copper sheet":
        constructorFunction(item, amount)
    elif item == "steel beam":
        constructorFunction(item, amount)
    elif item == "steel pipe":
        constructorFunction(item, amount)
######################################
####assembler
    elif item == "reinforced iron plate":
        assemblerFunction(item, amount)
    elif item == "rotor":
        assemblerFunction(item, amount)
    elif item == "modular frame":
        assemblerFunction(item, amount)
    elif item == "smart plating":
        assemblerFunction(item, amount)
    elif item == "versatile framework":
        assemblerFunction(item, amount)
######################################
####assembler
    elif item == "steel ingot":
        foundryFunction(item, amount)
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
        finalString = finalString + "\n" + str(amount) + " " + ingot + " ore per minute\n"
        finalString = finalString + str(smelters) + " smelter(s) making " + ingot + " ingot(s)\n"

def constructorFunction(product, amount):
    global finalString, finalPower
    constructors = 0
    output = 0
    input1 = 0
    if product == "iron plate":
        output = 20
        input1 = 30
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        smelterFunction("iron", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "iron rod":
        output = 15
        input1 = 15
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        smelterFunction("iron", amount / output * output)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "wire":
        output = 30
        input1 = 15
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        smelterFunction("copper", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "cable":
        output = 30
        input1 = 60
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        constructorFunction("wire", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "concrete":
        output = 15
        input1 = 45
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        finalString = finalString + str(round(constructors * 45)) + " limestone per minute\n"
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "\n"
    if product == "screw":
        output = 40
        input1 = 10
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        constructorFunction("iron rod", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "copper sheet":
        output = 10
        input1 = 20
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        smelterFunction("copper", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "steel beam":
        output = 15
        input1 = 60
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        foundryFunction("steel ingot", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"
    if product == "steel pipe":
        output = 20
        input1 = 30
        constructors = amount // output
        if amount % output > 0:
            constructors = round(constructors + ((amount % output) / output), 2)
        foundryFunction("steel ingot", amount / output * input1)
        finalString = finalString + str(constructors) + " constructor(s) making " + product + "(s)\n"

    finalPower = finalPower + (constructors * 4)

def assemblerFunction(product, amount):
    global finalString, finalPower, topLevel
    assemblers = 0
    input1 = 0
    input2 = 0
    output = 0
    if product == "reinforced iron plate":
        input1 = 30
        input2 = 60
        output = 5
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        if topLevel:
            topLevel = False
            finalString = finalString + "\n-----------First Input Object Line-----------"
            topLevel = topLevel - 1
            constructorFunction("iron plate", amount / output * input1)
            finalString = finalString + "\n-----------Second Input Object Line-----------"
            constructorFunction("screw", amount / output * input2)
            finalString = finalString + "\n-----------Final Assembler(s)-----------\n"
        else:
            constructorFunction("iron plate", amount / output * input1)
            constructorFunction("screw", amount / output * input2)
            finalString = finalString + "\n"
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"
    if product == "rotor":
        input1 = 20
        input2 = 100
        output = 4
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        if topLevel:
            topLevel = False
            finalString = finalString + "\n-----------First Input Object Line-----------"
            constructorFunction("iron rod", amount / output * input1)
            finalString = finalString + "\n-----------Second Input Object Line-----------"
            constructorFunction("screw", amount / output * input2)
            finalString = finalString + "\n-----------Final Assembler(s)-----------\n"
        else:
            constructorFunction("iron rod", amount / output * input1)
            constructorFunction("screw", amount / output * input2)
            finalString = finalString + "\n"
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"
    if product == "modular frame":
        input1 = 3
        input2 = 12
        output = 2
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        if topLevel:
            topLevel = False
            finalString = finalString + "\n-----------First Input Object Line-----------"
            assemblerFunction("reinforced iron plate", amount / output * input1)
            finalString = finalString + "\n-----------Second Input Object Line-----------"
            constructorFunction("iron rod", amount / output * input2)
            finalString = finalString + "\n-----------Final Assembler(s)-----------\n"
        else:
            assemblerFunction("reinforced iron plate", amount / output * input1)
            constructorFunction("iron rod", amount / output * input2)
            finalString = finalString + "\n"
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"
    if product == "smart plating":
        input1 = 2
        input2 = 2
        output = 2
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        if topLevel:
            topLevel = False
            finalString = finalString + "\n-----------First Input Object Line-----------"
            assemblerFunction("reinforced iron plate", amount / output * input1)
            finalString = finalString + "\n-----------Second Input Object Line-----------"
            assemblerFunction("rotor", amount / output * input2)
            finalString = finalString + "\n-----------Final Assembler(s)-----------\n"
        else:
            assemblerFunction("reinforced iron plate", amount / output * input1)
            assemblerFunction("rotor", amount / output * input2)
            finalString = finalString + "\n"
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"
    if product == "versatile framework":
        input1 = 2.5
        input2 = 30
        output = 5
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        if topLevel:
            topLevel = False    
            finalString = finalString + "\n-----------First Input Object Line-----------"
            assemblerFunction("modular frame", amount / output * input1)
            finalString = finalString + "\n-----------Second Input Object Line-----------"
            constructorFunction("steel beam", amount / output * input2)
            finalString = finalString + "\n-----------Final Assembler(s)-----------\n"
        else:
            assemblerFunction("modular frame", amount / output * input1)
            constructorFunction("steel beam", amount / output * input2)
            finalString = finalString + "\n"
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"

    finalPower = finalPower + (assemblers * 15)

def foundryFunction(product, amount):
    global finalString, finalPower
    foundries = 0
    input1 = 0
    input2 = 0
    output = 0
    if product == "steel ingot":
        input1 = 45
        input2 = 45
        output = 45
        foundries = amount // output
        if amount % output > 0:
            foundries = round(foundries + ((amount % output) / output), 2)
        finalString = finalString + "\n" + str(amount / output * input1) + " iron ore per minute\n"
        finalString = finalString + str(amount / output * input2) + " coal per minute\n"
        finalString = finalString + str(foundries) + " foundries making " + product + "(s)\n"
    
    finalPower = finalPower + (foundries * 16)

#TODO item list

#TIER 0

#TIER 1

#TIER 2

#TIER 3

#TIER 4
#encased industrial beam
#stator
#motor
#automated wiring
#heavy modular frame

#TIER 5
#plastic
#rubber
#fuel
#petroleum coke
#circuit board
#computer
#modular engine
#adaptive control unit
#empty canister

#TIER 6

#TIER 7
#alumina solution
#aluminum scrap
#aluminum ingot
#alclad aluminum sheet
#aluminum casing
#radio control unit
#sulfuric acid
#battery
#supercomputer
#assembly director system
#iodine infused filter

#TIER 8
#encased uranium cell
#electromagnetic control rod
#uranium fuel rod
#magnetic field generator
#empty fluid tank
#heat sink
#cooling system
#fused modular frame
#turbo motor
#nitric acid
#non-fissile uranium
#plutonium pellet
#encased plutonium cell
#plutonium fuel rod
#copper powder
#pressure conversion cube
#nuclear pasta

#Alternate Recipes