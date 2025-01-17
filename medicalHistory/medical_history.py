import tkinter as tk
from patient.gui import Frame 

def main():
    root = tk.Tk()
    root.title('Dra. Pili Historia Medica')
    #icon = tk.PhotoImage(file='media/dra_pili.png')
    #root.iconphoto(True,icon)
    #root.iconbitmap('media/dra_pili.ico')
    app = Frame(root)
    app.inputs_patient()

    app.mainloop()


if __name__ == "__main__":
    main()
