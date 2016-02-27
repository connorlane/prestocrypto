import Tkinter

root = Tkinter.Tk()

padding = 10

textWidth = 50
textHeight = 8

## ID Frame ##
idFrame = Tkinter.Frame(root)
idFrame.pack(fill = Tkinter.X, padx = padding)

yourIdFrame = Tkinter.Frame(idFrame, bg="red")
yourIdFrame.pack(side = Tkinter.LEFT, fill = Tkinter.X, padx = padding, pady = padding)

yourIdLabelFrame = Tkinter.Frame(yourIdFrame)
yourIdLabelFrame.pack(fill = Tkinter.X)

yourIdLabel = Tkinter.Label(yourIdLabelFrame, text = "Your ID: ")
yourIdLabel.pack(side = Tkinter.LEFT)

yourIdPasteButton = Tkinter.Button(yourIdLabelFrame, text="PASTE")
yourIdPasteButton.pack(side = Tkinter.RIGHT)

yourIdCopyButton = Tkinter.Button(yourIdLabelFrame, text="COPY")
yourIdCopyButton.pack(side = Tkinter.RIGHT)

yourIdText = Tkinter.Text(yourIdFrame, height = textHeight, width = textWidth, state = "disabled")
yourIdText.pack(fill = Tkinter.X)

theirIdFrame = Tkinter.Frame(idFrame)
theirIdFrame.pack(side = Tkinter.LEFT, fill = Tkinter.X, padx = padding)

theirIdLabelFrame = Tkinter.Frame(theirIdFrame)
theirIdLabelFrame.pack(fill = Tkinter.X)

theirIdLabel = Tkinter.Label(theirIdLabelFrame, text = "Their ID: ")
theirIdLabel.pack(side = Tkinter.LEFT)

theirIdPasteButton = Tkinter.Button(theirIdLabelFrame, text="PASTE")
theirIdPasteButton.pack(side = Tkinter.RIGHT)

theirIdCopyButton = Tkinter.Button(theirIdLabelFrame, text="COPY")
theirIdCopyButton.pack(side = Tkinter.RIGHT)

theirIdText = Tkinter.Text(theirIdFrame, height = textHeight, width = textWidth)
theirIdText.pack(fill = Tkinter.X)

## Message Frame ##

messageFrame = Tkinter.Frame(root)
messageFrame.pack(fill = Tkinter.X, padx = padding)

plaintextFrame = Tkinter.Frame(messageFrame)
plaintextFrame.pack(side = Tkinter.LEFT, fill = Tkinter.X, padx = padding, pady = padding)

plaintextLabelFrame = Tkinter.Frame(plaintextFrame)
plaintextLabelFrame.pack(fill = Tkinter.X)

plaintextLabel = Tkinter.Label(plaintextLabelFrame, text = "Message: ")
plaintextLabel.pack(side = Tkinter.LEFT)

plaintextPasteButton = Tkinter.Button(plaintextLabelFrame, text="PASTE")
plaintextPasteButton.pack(side = Tkinter.RIGHT)

plaintextCopyButton = Tkinter.Button(plaintextLabelFrame, text="COPY")
plaintextCopyButton.pack(side = Tkinter.RIGHT)

plaintextText = Tkinter.Text(plaintextFrame, height = textHeight, width = textWidth)
plaintextText.pack(fill = Tkinter.X)

ciphertextFrame = Tkinter.Frame(messageFrame)
ciphertextFrame.pack(side = Tkinter.LEFT, fill = Tkinter.X, padx = padding, pady = padding)

ciphertextLabelFrame = Tkinter.Frame(ciphertextFrame)
ciphertextLabelFrame.pack(fill = Tkinter.X)

ciphertextLabel = Tkinter.Label(ciphertextLabelFrame, text = "Encrypted Text: ")
ciphertextLabel.pack(side = Tkinter.LEFT)

ciphertextPasteButton = Tkinter.Button(ciphertextLabelFrame, text="PASTE")
ciphertextPasteButton.pack(side = Tkinter.RIGHT)

ciphertextCopyButton = Tkinter.Button(ciphertextLabelFrame, text="COPY")
ciphertextCopyButton.pack(side = Tkinter.RIGHT)

ciphertextText = Tkinter.Text(ciphertextFrame, height = textHeight, width = textWidth)
ciphertextText.pack(fill = Tkinter.X)

## States ##

def setState(state):
	if state == "reset":
		plaintextText.config(state = "disabled", bg = "light grey")
		plaintextText.delete("1.0", Tkinter.END)
		plaintextText.insert("1.0", "Hello")

## Mainloop ##

setState("reset")

root.mainloop()

