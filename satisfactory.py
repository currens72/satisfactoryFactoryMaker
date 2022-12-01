import itemList
import tkinter as tk
from tkinter import END
from tkinter import *
import re

def itemCreation():
    item = itemEntry.get()
    amount = outputEntry.get()
    amount = int(amount)
    item = item.lower()
    finalOutput = itemList.itemSelection(item, amount)

    test = finalOutput.splitlines()
    finalOutput = ""
    for i in range(len(test)):
        if i < len(test) - 1:
            finalOutput = finalOutput + test[i] + "\n"
        else:
            finalOutput = finalOutput + "\n" + test[i]

    finalStringTextBox.delete("1.0", "end")
    finalStringTextBox.insert("1.0", "In order to make " + str(amount) + " " + item + "(s) per minute, you need:\n\n" + finalOutput)

def main():
    global itemEntry, outputEntry, finalStringTextBox
    #menu()
    window = tk.Tk()
    window.title("Satisfactory Factory Maker")
    window.geometry("1650x1000")
    window.resizable(width=True, height=True)
    window.config(bg="gray15")
    #Grid.rowconfigure(window,0,weight=1)
    #Grid.columnconfigure(window,0,weight=1)
    #Grid.rowconfigure(window,1,weight=1)

    #spacer labels
    spacer1 = tk.Label(master=window, text="\n", font=("Arial", 5), bg="gray15")
    spacer2 = tk.Label(master=window, text="\n", font=("Arial", 5), bg="gray15")
    spacer3 = tk.Label(master=window, text="\n", font=("Arial", 5), bg="gray15")
    spacer4 = tk.Label(master=window, text="                 \n", font=("Arial", 5), bg="gray15")
    spacer5 = tk.Label(master=window, text="\n", font=("Arial", 5), bg="gray15")

    #button to calculate based off desired item
    calculateFrame = tk.Frame(master=window)
    calculateButton = tk.Button(master=calculateFrame,
                                text="Calculate Factory",
                                font=("Arial", 20),
                                command=itemCreation,
                                bg="gray60"
                                )
    calculateButton.pack(side=LEFT and TOP, anchor=W)

    #frame for desired item entry
    itemFrame = tk.Frame(master=window, bg="gray15")
    stringVar = tk.StringVar()
    itemEntry = tk.Entry(master=itemFrame, textvariable=stringVar, width=40, font=("Arial", 20), bg="gray60")
    itemLabel = tk.Label(master=itemFrame, text="Enter Desired Item Here:", font=("Arial", 20), bg="gray60")
    itemLabel.pack(side=LEFT and TOP, anchor=W)
    itemEntry.pack(side=LEFT and TOP, anchor=W)

    #frame for desired output per min of item
    outputFrame = tk.Frame(master=window, bg="gray15")
    outputEntry = tk.Entry(master=outputFrame, width=5, font=("Arial", 20), bg="gray60")
    outputLabel = tk.Label(master=outputFrame, text="Enter Desired Output /min Here:", font=("Arial", 20), bg="gray60")
    outputLabel.pack(side=LEFT and TOP, anchor=W)
    outputEntry.pack(side=LEFT and TOP, anchor=W)

    #frame for final string
    finalStringTextBox = tk.Text(master=window, font=("Arial", 20), bg="gray60")

    l1 = tk.Listbox(window,
                    height=3,
                    width=40,
                    bg="gray30",
                    font=("Arial", 20),
                    relief='flat',
                    highlightcolor= 'SystemButtonFace')

    #grid layout
    #spacer1.grid(row=0, column=0, padx=10, sticky="nsew")
    #calculateFrame.grid(row=6, column=0, padx=10, sticky="nsew")
    #spacer2.grid(row=3, column=0, padx=10, sticky="nsew")
    #itemFrame.grid(row=1, column=0, padx=10, sticky="nsew")
    #spacer3.grid(row=5, column=0, padx=10, sticky="nsew")
    #outputFrame.grid(row=4, column=0, padx=10, sticky="nsew")
    #spacer5.grid(row=7, column=0, padx=10, sticky="nsew")
    #spacer4.grid(row=0, column=1, padx=10, sticky="nsew")
    #finalStringFrame.grid(column=2, padx=10, sticky="nsew")
    #spacer1.pack(side=LEFT and TOP)
    itemFrame.pack(side=LEFT and TOP, anchor=W)
    l1.pack(side=LEFT and TOP, anchor=W)
    spacer2.pack(side=LEFT and TOP, anchor=W)
    outputFrame.pack(side=LEFT and TOP, anchor=W)
    spacer3.pack(side=LEFT and TOP, anchor=W)
    calculateFrame.pack(side=LEFT and TOP, anchor=W)
    finalStringTextBox.pack(side=RIGHT, anchor=E)


    #autocomplete stuff
    def my_upd(my_widget):
        my_w = my_widget.widget
        index = int(my_w.curselection()[0])
        value = my_w.get(index)
        stringVar.set(value)
        l1.delete(0,END)
    def my_down(my_widget):
        l1.focus()
        l1.selection_set(0)

    #l1.grid(row=2,column=0, padx=10, sticky="nsew")

    def get_data(*args):
        search_str = itemEntry.get()
        l1.delete(0,END)
        for element in completedItemList:
            if(re.match(search_str,element,re.IGNORECASE)):
                l1.insert(tk.END,element)
    
    itemEntry.bind('<Down>', my_down)
    l1.bind('<Right>', my_upd)
    l1.bind('<Return>', my_upd)
    stringVar.trace('w',get_data)
    #autocomplete stuff

    window.mainloop()

#intiator line

completedItemList = [
#TIER 0
'iron ingot',
'iron plate',
'iron rod',
'copper ingot',
'wire',
'cable',
'concrete',
'screw',
'reinforced iron plate',

#TIER 1

#TIER 2
'copper sheet',
'rotor',
'modular frame',
'smart plating',

#TIER 3
'steel ingot',
'steel beam',
'steel pipe',
'versatile framework'

#TIER 4

#TIER 5

#TIER 6

#TIER 7

#TIER 8

#Alternate Recipes
]

#switch list to alphabetical
completedItemList = sorted(completedItemList)

main()