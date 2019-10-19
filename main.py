import tkinter


def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg="black", height=250, width=250)
    canvas.pack()
    root.mainloop()
    print("itsa me main")

if __name__ == "__main__":
    main()
