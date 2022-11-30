import itemList
import tkinter as tk

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
    calculateButton.grid(row=1, column=0, sticky="w")

    #frame for desired item entry
    itemFrame = tk.Frame(master=window, bg="gray15")
    itemEntry = tk.Entry(master=itemFrame, width=40, font=("Arial", 20), bg="gray60")
    itemLabel = tk.Label(master=itemFrame, text="Enter Desired Item Here:", font=("Arial", 20), bg="gray60")
    itemEntry.grid(row=1, column=0, sticky="w")
    itemLabel.grid(row=0, column=0, sticky="w")

    #frame for desired output per min of item
    outputFrame = tk.Frame(master=window, bg="gray15")
    outputEntry = tk.Entry(master=outputFrame, width=5, font=("Arial", 20), bg="gray60")
    outputLabel = tk.Label(master=outputFrame, text="Enter Desired Output /min Here:", font=("Arial", 20), bg="gray60")
    outputEntry.grid(row=1, column=0, sticky="w")
    outputLabel.grid(row=0, column=0, sticky="w")

    #frame for final string
    finalStringFrame = tk.Frame(master=window, bg="gray15")
    finalStringTextBox = tk.Text(master=finalStringFrame, height=30, width=60, font=("Arial", 20), bg="gray60")
    finalStringTextBox.grid(row=0, column=0, sticky="w")

    #grid layout
    spacer1.grid(row=0, column=0, padx=10, sticky="w")
    calculateFrame.grid(row=5, column=0, padx=10, sticky="w")
    spacer2.grid(row=2, column=0, padx=10, sticky="w")
    itemFrame.grid(row=1, column=0, padx=10, sticky="w")
    spacer3.grid(row=4, column=0, padx=10, sticky="w")
    outputFrame.grid(row=3, column=0, padx=10, sticky="w")
    spacer5.grid(row=6, column=0, padx=10, sticky="w")
    spacer4.grid(row=0, column=1, padx=10)
    finalStringFrame.place(x=700, y=10)

    window.mainloop()

#intiator line
main()

#completed item list

#TIER 0
#iron ingot
#iron plate
#iron rod
#copper ingot
#wire
#cable
#concrete
#screw
#reinforced iron plate

#TIER 1

#TIER 2
#copper sheet
#rotor

#TIER 3

#TIER 4

#TIER 5

#TIER 6

#TIER 7

#TIER 8