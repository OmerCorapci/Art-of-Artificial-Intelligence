from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from model import modelPrediction

import warnings
warnings.filterwarnings("ignore")

"""
    NOT:İstenilen widget oluşturduktan sonra(button, label, textbox, vb.) bunları 3 şekilde frame/lere yerleştirebiliriz, bunlar;
        Pack, Place ve Grid.
        
        --.Pack() = Bu nesneyi kullanırken frame de nerede oluşmasını istiyorsak side = TOP yazmamız yeterli.
            Yani pack kullanırken istenilen widgetların nerede konumlanacağını side fonksiyonu yardımı ile gerçekleştiriyoruz
            (TOP, RIGHT, LEFT, BOTTOM).
        --.Place() = Bu nesneyi kullanırken frame de nerede oluşmasını istiyorsak konum olarak belirtmemiz gerekiyor.
            Örnek vermek gerekirsek .place(x = 50 , y = 50) ama burada pencereyi küçültüp büyüttüğümüzde konum olarak sabit kalacak ve
            kötü görünüm olacak. Bunun yerine .place(relx = 0.1, rely= 0.1) kullanırsak soldan ve yukarıdan %10 luk boşluk bırak
            diyoruz.
        --.grid() = Ben projemde kullanmadım ama olsun. İstediğimiz widget ı satır ve sütun sayısı vererek konumlandırıyoruz. Mesela,
        .grid(row=0, column=0)
        
"""  
master = Tk() # Bir main frame objesi oluşturuyoruz.
master.title("Art of AI") # Bu frame in başlığını oluşturuyoruz. 
Canvas(master, height=600, width= 1000).pack()

frame_sol = Frame(master, bg="#add8e6") # Ana frame in sol tarafında bulunacak küçük bir tane daha frame oluşturuyoruz.
frame_sol.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.5) # Konumunu, yüksekliğini ve genişlğini ayarlıyoruz. 

frame_orta = Frame(master, bg="#add8e6") #Ana frame in ortasında bir frame oluşturuyoruz
frame_orta.place(relx=0.35, rely=0.1, relwidth=0.30, relheight=0.5) #Konumunu, yüksekliğini ve genişlğini ayarlıyoruz.

frame_sag = Frame(master, bg="#add8e6") #Ana frame in sağ tarafında yer alacak bir küçük frame oluşturuyoruz
frame_sag.place(relx=0.67, rely=0.1, relwidth=0.30, relheight=0.5) #Konumunu, yüksekliğini ve genişlğini ayarlıyoruz.

frame_alt =  Frame(master, bg="#add8e6") #Ana frame in içerisind ve en altında yer alacak alt bir frame oluştuyoruz.
frame_alt.place(relx=0.35, rely=0.62, relwidth=0.30, relheight=0.1) #Konumunu, yüksekliğini ve genişlğini ayarlıyoruz.

scrollbar = Scrollbar(frame_sol) # Scrollbar widget ı oluşturuyoruz ve bu widget ın frame_sol alanında olacağını belirtiyoruz.
scrollbar.pack( side = RIGHT, fill = Y ) # fill diyerek hangi eksen boyunca ve dolu bir şekilde olacağını belirtiyoruz.
#Frame sol kısımda "Desteklenen Ressamlar" adlı bir label oluşturuyoruz.
#"bg" ile arka plan rengini , "text" ile içerisinde yer alacak yazıyı ve "font" ile yazının fontunu ayarlıyoruz.
Label(frame_sol, bg="#add8e6", text="Desteklenen Ressamlar", font="Verdana 12 bold").pack(side=TOP)
#Desteklenecek olan ressamların isimlerini gösterebilmek için bir tane listbox oluşturuyoruz.
#Listbox ın frame_sol kısımda yer alacağını belirtiyoruz.
mylist = Listbox(frame_sol, yscrollcommand= scrollbar.set, bg= "#add8e6", font= "Verdana 10" ) 

liste = ["Albrecht Dürer", "Alfred Sisley", "Edgar Degas", "Francisco Goya", "Marc Chagall", "Pablo Picasso",
         "Paul Gauguin", "Pierre Auguste Renoir", "Rembrandt", "Titian", "Vincent van Gogh"]
for i in liste: # Liste içerisindeki isimleri listbox a aktarıyoruz.
    mylist.insert(END,i)

mylist.pack( side = LEFT, fill = BOTH, expand=True )
scrollbar.config( command = mylist.yview)


pathh = Label(frame_orta)
art = Label(frame_orta)
def open():
    global my_image, filename
    frame_orta.filename = filedialog.askopenfilename(title="Select a File", filetypes=(("All Files","*.*"),))
    filename = frame_orta.filename
    pathh.config(text = filename)
    pathh.pack()
    my_image = ImageTk.PhotoImage(Image.open(filename).resize((200,200)))
    art.config(image=my_image)
    art.pack()

def click():
    artist, prediction, percent = modelPrediction(filename)
    Label(frame_sag, text = "Real artist: "+artist, bg ="#add8e6").place(relx=0.2, rely=0.4)
    Label(frame_sag, text = "Tahmin edilen artist: "+prediction, bg ="#add8e6").place(relx=0.2, rely=0.5)
    Label(frame_sag, text = "% "+str(percent), bg ="#add8e6").place(relx=0.2, rely=0.6)


Label(frame_sag, text = "Sonuç",bg ="#add8e6", font="Verdana 20 bold").pack(side = TOP)
Button(frame_orta, text="Resim Seç", command=open).pack(side = BOTTOM,anchor="s")
Button(frame_alt, text="RUN", width = 35, height= 2, command= click).pack(expand=True)



master.mainloop()

