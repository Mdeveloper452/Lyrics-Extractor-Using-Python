from tkinter import *
from lyrics_extractor import SongLyrics

# User-defined function
def get_lyrics():
    extract_lyrics = SongLyrics(
        "AIzaSyD27R4Wo_o2MJ9gZAoEiMrQ-RN4jL5GeRA", "7593fadfe3d633e73")
    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result.set(res)

# GUI setup
master = Tk()
master.configure(bg='#e6e6e6')
master.title('Lyrics Extractor by G19')

result = StringVar()

Label(master, text="Enter Song Name : ", font='arial 10 bold', bg="light grey").grid(row=0, sticky=W)
Label(master, text="Lyrics : ", font='arial 10 bold', bg="light grey").grid(row=3, sticky=W)
Label(master, text="", textvariable=result, bg="light grey").grid(row=3, column=1, sticky=W)

v = Scrollbar(master, orient='vertical')
e = Entry(master, width=50)
e.grid(row=0, column=1)

b = Button(master, text="Show", command=get_lyrics, bg="Blue")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
