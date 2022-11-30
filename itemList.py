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
    elif item == "concrete":
        constructorFunction(item, amount)
    elif item == "screw":
        constructorFunction(item, amount)
    elif item == "copper sheet":
        constructorFunction(item, amount)
######################################
####assembler
    elif item == "reinforced iron plate":
        assemblerFunction(item, amount)
    elif item == "rotor":
        assemblerFunction(item, amount)
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

    finalPower = finalPower + (constructors * 4)

def assemblerFunction(product, amount):
    global finalString, finalPower
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
        constructorFunction("iron plate", amount / output * input1)
        constructorFunction("screw", amount / output * input2)
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"
    if product == "rotor":
        input1 = 20
        input2 = 100
        output = 4
        assemblers = amount // output
        if amount % output > 0:
            assemblers = round(assemblers + ((amount % output) / output), 2)
        constructorFunction("iron rod", amount / output * input1)
        constructorFunction("screw", amount / output * input2)
        finalString = finalString + str(assemblers) + " assembler(s) making " + product + "(s)\n"

    finalPower = finalPower + (assemblers * 15)

#TODO item list

#TIER 0

#TIER 1

#TIER 2

#TIER 3
#steel ingot
#steel beam
#steel pipe
#versatile framework

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