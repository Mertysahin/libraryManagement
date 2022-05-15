from tkinter import *
from tkinter import ttk #combobox icin
from tkcalendar import * #takvim nesnesi icin gerekli
from tkinter import messagebox
from datetime import*
import sqlite3
from openpyxl import Workbook #excele aktarmak icin
import os
from fpdf import FPDF
#mail gönderimi icin gerekli kütüphaneler
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#sqlite bağlantısı,tablo

con = sqlite3.connect(r"C:\Users\user\Desktop\Proje\kutuphane.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (id INT, tur TEXT,"
                 "referans TEXT, isim TEXT, soyisim TEXT, telefon TEXT,"
                 "email TEXT, adres TEXT, durum TEXT, borc TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (barkod TEXT, baslik TEXT,"
                 "yazar TEXT, sayi TEXT, raf TEXT, odunc TEXT,"
                 "teslim TEXT, kime TEXT)")
con.commit()

class Kutuphane(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kütüphane Yönetim Sistemi")
        self.wm_resizable(False, False)

        #combobox icin tkinter teması
        combostyle = ttk.Style()
        combostyle.theme_create("combostyle", parent="alt", settings={"TCombobox":
                                                                          {"configure":
                                                                              {
                                                                            "fieldbackground": "#fed39f",
                                                                                "background": "#f6eec9"
                                                                                    }}})
        combostyle.theme_use("combostyle")

        self.frame1 = Frame(self, height=150, bg="#F0A500") #colorpaletteden aldım
        self.frame1.pack(fill=X)
        self.frame2 = Frame(self, height=450, bg="#334756")
        self.frame2.pack(fill=X)

        self.resim = PhotoImage(file=r"C:\Users\user\Desktop\Proje\books2.png") #iconArchive sitesinden aldım
        self.baslik_görseli = Label(self.frame1, image=self.resim, bg="#F0A500")
        self.baslik_görseli.place(x=65, y=5)
        self.baslik = Label(self.frame1, text="KÜTÜPHANE", font=("Garamond", 35, "bold"), bg="#F0A500")
        self.baslik.place(x=210, y=43)
        self.baslik = Label(self.frame1, text="YÖNETİM SİSTEMİ", font=("Garamond", 25, "bold"), bg="#F0A500")
        self.baslik.place(x=210, y=88)

 #Butonlar
        self.dugme1 = Button(self.frame2, text="Üyeler", font=("Garamond", 15 ,"bold"),bg="#f6eec9",
        activebackground="#DADDFC", command=Uyeler)

        self.dugme1.place(x=200, y=60, width=200)

        self.dugme1 = Button(self.frame2, text="Kitaplar", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#DADDFC", command=Kitaplar)

        self.dugme1.place(x=200, y=100, width=200)

        self.dugme1 = Button(self.frame2, text="Kitaplık", font=("Garamond", 15, "bold"), bg="#f6eec9",
                             activebackground="#DADDFC", command=Kitaplik)

        self.dugme1.place(x=200, y=140, width=200)

class Uyeler(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Üyeler")
        self.wm_title("Kütüphane Yönetim Sistemi")
        self.wm_resizable(False, False)

        self.frame1 = Frame(self, bg="#F0A500", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="ÜYE BİLGİLERİ", bg="#F0A500", font=("Arial", 25, "bold")).place(x=175)
        Label(self.frame1, text="Üyelik Türü ", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=50)
        Label(self.frame1, text="Referans No", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=80)
        Label(self.frame1, text="İsim", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=110)
        Label(self.frame1, text="Soyad", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=140)
        Label(self.frame1, text="Telefon", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=170)
        Label(self.frame1, text="Email", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=200)
        Label(self.frame1, text="Adres", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=230)
        Label(self.frame1, text="Üyelik Durumu", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=280)
        Label(self.frame1, text="Borç", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=310)

        self.tur = ttk.Combobox(self.frame1, font=("Arial", 15,  "bold"), state="readonly",
                               values=["Öğrenci", "Normal", "Kütüphane Görevlisi"])
        self.tur.place(x=350,y=50, width=200)

        self.referans = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.referans.place(x=350, y=80, width=200)

        self.isim = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.isim.place(x=350, y=110, width=200)

        self.soyisim = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.soyisim.place(x=350, y=140, width=200)

        self.telefon = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.telefon.place(x=350, y=170, width=200)

        self.email = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.email.place(x=350, y=200, width=200)

        self.adres = Text(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f",height=2)
        self.adres.place(x=350, y=230, width=200)

        self.sayi = IntVar(self.frame1)
        self.durum0 = Radiobutton(self.frame1,text="Aktif", variable=self.sayi, value=1, bg="#F0A500")
        self.durum0.place(x=350, y=280)
        self.durum1 = Radiobutton(self.frame1, text="Beklemede", variable=self.sayi, value=2, bg="#F0A500")
        self.durum1.place(x=400, y=280)
        self.durum2 = Radiobutton(self.frame1, text="İptal", variable=self.sayi, value=3, bg="#F0A500")
        self.durum2.place(x=500, y=280)

        self.borc = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.borc.place(x=350,  y=310, width=200)

        Button(self.frame1, text="KAYDET", command=self.kaydet, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=45, y=350, width=125)

        Button(self.frame1, text="GÜNCELLE", command=self.guncelle, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=171, y=350, width=125)

        Button(self.frame1, text="GETİR", command=self.getir, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=298, y=350, width=125)

        Button(self.frame1, text="MAİL", command=self.mail_gonder, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=425, y=350, width=125)
##################BUTONLAR####################
    def mail_gonder(self):

        gonderen = "@gmail.com"
        alici = "@gmail.com"
        parola = ""

        mesaj = MIMEMultipart("alternative")
        mesaj["Subject"] = "Kütüphane Borcu"
        mesaj["From"] = gonderen
        mesaj["To"] = alici

        icerik = f"Merhaba, borcunuz {self.borc.get()} TL olup, bu ay içinde ödenmezse evinize haciz gelecektir."
        part1 = MIMEText(icerik, "html")
        mesaj.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gonderen, parola)
            server.sendmail(gonderen, alici, mesaj.as_string())

    def kaydet(self):

        try:
            sql = "INSERT INTO IF NOT EXISTS uyeler (tur, referans, isim, soyisim, telefon, email, adres, durum) " \
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            val = (self.tur.get(), self.referans.get(), self.isim.get(), self.soyisim.get(), self.telefon.get(),
                   self.email.get(), self.adres.get('1.0', END), self.sayi.get())
            cursor.execute(sql, val)
            con.commit()
            messagebox.showinfo("Başarılı", "İşlem Başarılı")
            self.temizle()
        except:
            messagebox.showinfo("Başarısız", "Üye Zaten Var")

    def getir(self):

        sql = "SELECT * FROM uyeler WHERE referans=?"
        val = (self.referans.get(),)
        cursor.execute(sql, val)
        sonuc = cursor.fetchall()

        for i in sonuc:
            self.tur.set("")
            self.isim.delete(0, END)
            self.soyisim.delete(0, END)
            self.telefon.delete(0, END)
            self.email.delete(0, END)
            self.adres.delete("1.0", END)
            self.sayi.set(0)

            self.tur.set(i[1])
            self.isim.insert(0, i[3])
            self.soyisim.insert(0, i[4])
            self.telefon.insert(0, i[5])
            self.email.insert(0, i[6])
            self.adres.insert("end", i[7])
            self.sayi.set(i[8])

        self.focus()

    def guncelle(self):

        sql = "UPDATE uyeler SET tur=?, isim=?, soyisim=?, telefon=?, email=?, adres=?, durum=? " \
              "WHERE referans=?"
        val = (self.tur.get(), self.isim.get(), self.soyisim.get(), self.telefon.get(), self.email.get(),
               self.adres.get('1.0', END), self.sayi.get(), self.referans.get())
        cursor.execute(sql, val)
        con.commit()
        self.temizle()


    #kayıt işleminden sonra sayfayı temizlemek icim
    def temizle(self):
        messagebox.showinfo("Başarılı","İşlem Başarılı")
        self.tur.set("")
        self.referans.delete(0, END)
        self.isim.delete(0, END)
        self.soyisim.delete(0, END)
        self.telefon.delete(0, END)
        self.email.delete(0, END)
        self.adres.delete("1.0", END)
        self.sayi.set(0) #radio buton secili gelmemesi icin.
        self.focus() #kayıt tamamlanınca sayfada kalmak için.

##################BUTONLAR####################

class Kitaplar(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitap Bilgileri")
        self.wm_resizable(False, False)

        style = ttk.Style()
        style.theme_use("combostyle")

        self.frame1 = Frame(self, bg="#F0A500", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="KİTAP BİLGİLERİ", bg="#F0A500", font=("Arial", 25, "bold")).place(x=150)

        Label(self.frame1, text="Barkod ", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=50)
        Label(self.frame1, text="Başlık", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=80)
        Label(self.frame1, text="Yazar", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=110)
        Label(self.frame1, text="Durum", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=140)
        Label(self.frame1, text="Raf", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=170)
        Label(self.frame1, text="Kime", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=200)
        Label(self.frame1, text="Ödünç Tarihi", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=230)
        Label(self.frame1, text="Teslim Tarihi", bg="#F0A500", font=("Arial", 15, "bold")).place(x=45, y=260)

        self.barkod = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.barkod.place(x=350, y=50, width=200)

        self.baslik = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.baslik.place(x=350, y=80, width=200)

        self.yazar = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.yazar.place(x=350, y=110, width=200)

        self.sayi = IntVar(self.frame1)
        self.durum0 = Radiobutton(self.frame1, text="Rafta", variable=self.sayi, value=1, bg="#F0A500")
        self.durum0.place(x=350, y=140)
        self.durum1 = Radiobutton(self.frame1, text="Ödünç Verilmiş", variable=self.sayi, value=2, bg="#F0A500")
        self.durum1.place(x=440, y=140)

        self.raf = Entry(self.frame1, font=("Arial", 15, "bold"), bg="#fed39f")
        self.raf.place(x=350, y=170, width=200)

        self.kime = ttk.Combobox(self.frame1, font=("Arial", 15, "bold"), values=["Teslim Al"])
        self.kime.place(x=350, y=200, width=200)
        self.kime.bind("<KeyRelease>", self.islemler)   # herhangibir tusa basılınca
        self.kime.bind("<Button-1>", self.islemler)   # mouse ile tıklandıgında
        self.kime.bind("<Return>", self.islemler)     # enter tusuna basıldıgında
        self.kime.bind("<<ComboboxSelected>>", self.islemler) #combobox ile secim yapıldıgında

        self.odunc = DateEntry(self.frame1, font=("Arial", 15, "bold"), bg="#F0A500", locale="tr_TR",
                               selectbackground="#fed39f", weekendbackground="#f6eec9", state="disabled")
        self.odunc.place(x=350, y=230, width=200)

        self.teslim = DateEntry(self.frame1, font=("Arial", 15, "bold"), bg="#F0A500", locale="tr_TR",
                               selectbackground="#fed39f", weekendbackground="#f6eec9", state="disabled")
        self.teslim.place(x=350, y=260, width=200)

        self.borc = Label(self.frame1, bg="#F0A500", font=("Arial", 15, "bold"))
        self.borc.place(x=350, y=290)

        Button(self.frame1, text="KAYDET", command=self.kaydet, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=45, y=350, width=125)

        Button(self.frame1, text="GÜNCELLE", command=self.guncelle, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=171, y=350, width=125)

        Button(self.frame1, text="GETİR", command=self.getir, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=298, y=350, width=125)

        Button(self.frame1, text="SİL", command=self.sil, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 12, "bold")).place(x=425, y=350, width=125)

        self.onceki_borc = 0

    def islemler(self, event):
        if len(self.kime.get()) != 0:               #kime kısmı boş bırakılmamışsa
            if self.kime.get() != "Teslim Al":      #comboboxtan teslim al seçilmemimş, kime kısmı el ile doldurulmuşsa
                self.sayi.set(2)                    #durum ödünc verilmiş olarak güncellensin
                self.odunc.config(state='normal')   #otomatik olarak bugünün tarihi gelecek
                self.teslim.config(state='normal')  #14 gün sonraya ayarlanacak
                self.teslim_tarihi(event=None)      #ödünc tarihinden 14 gün sonraya ayarlama fonksiyonu
            else:
                if len(self.odunc.get()) != 0:      #kitap ödünc tarihi varsa yeni ödünc verilmişse
                    self.teslim.config(state='normal')
                    t1 = self.teslim.get_date()     #teslim tarihini elle girmeden t1 isimli değişkene kaydettik
                    t2 = date.today()               #bugünün tarihi
                    self.teslim.delete(0, END)
                    t3 = str(t2).split("-")
                    t4 = str(t3[2] + "." + str(t3[1]) + "." + str(t3[0]))
                    self.teslim.insert(0, t4)
                    gun = (t2-t1).days              #gecikme
                    if gun > 0:
                        self.borc["text"] = gun * 1  # gün başına 1 tl gecikme
                    else:
                        self.borc['text'] = 0

                else:
                    messagebox.showerror("Hata", "Kitap ödünç verilmemiş") #teslim al seçiliyse  hata vermeli
                    self.kime.delete(0, END)
                    self.focus()
        else:
            self.sayi.set(1)    #durum rafta olarak kalmalı
            self.odunc.delete(0, END)
            self.teslim.delete(0, END)
            self.odunc.config(state='disabled')
            self.teslim.config(state='disabled')

    def teslim_tarihi(self, event):
        a = self.odunc.get_date()  #tarihi get_date() metoduyla date formatında alıyoruz DateEntry den
        print(a)
        y = a + timedelta(days=14) #14 gün ekliyoruz
        print(y)
        b = str(y).split("-")
        print(b)
        c = b[2] + "." + b[1] + "." + b[0]
        self.teslim.delete(0, END)
        self.teslim.insert(0, c)
        self.odunc.config(state='disabled')
        self.teslim.config(state='disabled')

    def kaydet(self):

        sql = "INSERT INTO kitaplar (barkod, baslik, yazar, sayi, raf, odunc, teslim) VALUES(?,?,?,?,?,?,?)"
        val = (self.barkod.get(), self.baslik.get(), self.yazar.get(), self.sayi.get(), self.raf.get(),
               self.odunc.get(), self.teslim.get())
        cursor.execute(sql, val)
        con.commit()
        self.temizle()

    def getir(self):

        sql = "SELECT * FROM kitaplar WHERE barkod=?"
        val = (self.barkod.get(), )
        cursor.execute(sql, val)
        sonuc = cursor.fetchall()

        for i in sonuc:
            self.baslik.delete(0, END)
            self.baslik.insert(0, i[1])
            self.yazar.delete(0, END)
            self.yazar.insert(0, i[2])
            self.sayi.set(i[3])
            self.raf.delete(0, END)
            self.raf.insert(0, i[4])
            self.odunc.config(state='normal')
            self.odunc.delete(0, END)
            self.odunc.insert(0, i[5])
            self.odunc.config(state='disabled')
            self.teslim.config(state='normal')
            self.teslim.delete(0, END)
            self.teslim.insert(0, i[6])
            self.teslim.config(state='disabled')
            try:
                self.kime.delete(0, END)
                self.kime.insert(0, i[7])
            except TclError:
                pass

            self.referans = self.kime.get()  #silmeden referans isimli değişkene kaydettik

    def guncelle(self):
        # iki koşulumuz olacak, teslim al seçip kitabı teslim almak ya da referans girip kitap ödünç vermek
        if self.kime.get() == "Teslim Al":
            self.sayi.set(1)    #Rafta
            self.odunc.config(state='normal')
            self.teslim.config(state='normal')
            self.odunc.delete(0, END)
            self.teslim.delete(0, END)
            self.kime.delete(0, END)

            sql = "UPDATE kitaplar SET baslik=?, yazar=?, sayi=?, raf=?, odunc=?, teslim=?, kime=? WHERE barkod=?"
            val = (self.baslik.get(), self.yazar.get(), self.sayi.get(), self.raf.get(), self.odunc.get(),
                   self.teslim.get(), self.kime.get(), self.barkod.get())
            cursor.execute(sql, val)
            con.commit()

            # üye tablosunda borcu güncellemek icin
            sql = "SELECT * FROM uyeler WHERE referans=?"
            val = (self.referans,)
            cursor.execute(sql, val)
            sonuc = cursor.fetchall()
            for i in sonuc:
                self.onceki_borc = i[9]  # üyeler tablosunda 9.indexde
            try:

                sql = "UPDATE uyeler SET borc=? WHERE referans=?"
                val = (int(self.onceki_borc) + int(self.borc['text']), self.referans)  #borc başta 0 oldugu icin 0'ı inte cevirip toplayamıyor try exceptle gectim
                cursor.execute(sql, val)
                con.commit()
            except TypeError:
                sql = "UPDATE uyeler SET borc=? WHERE referans=?"
                val = (0 + int(self.borc['text']), self.referans)
                cursor.execute(sql, val)
                con.commit()

        else:
            sql = "UPDATE kitaplar SET baslik=?, yazar=?, sayi=?, raf=?, odunc=?, teslim=?, kime=? WHERE barkod=?"
            val = (self.baslik.get(), self.yazar.get(), self.sayi.get(), self.raf.get(), self.odunc.get(),
                   self.teslim.get(), self.kime.get(), self.barkod.get())
            cursor.execute(sql, val)
            con.commit()
        self.temizle()

    def sil(self):
        sql = "DELETE FROM kitaplar WHERE barkod=?"
        val = (self.barkod.get(),)
        cursor.execute(sql, val)
        con.commit()
        self.temizle()

    def temizle(self):
        messagebox.showinfo("Başarılı", "İşlem Başarılı")
        self.barkod.delete(0, END)
        self.baslik.delete(0, END)
        self.yazar.delete(0, END)
        self.sayi.set(0)
        self.kime.delete(0, END)
        self.raf.delete(0, END)
        self.odunc.config(state="normal")
        self.teslim.config(state="normal")
        self.odunc.delete(0,END)
        self.teslim.delete(0, END)
        self.odunc.config(state="disabled")
        self.teslim.config(state="disabled")
        self.borc['text'] = ""
        self.focus()

class Kitaplik(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.wm_geometry("600x400+400+100")
        self.wm_title("Kitaplık")
        self.wm_resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        self.frame1 = Frame(self, bg="#F0A500", width=600, height=400)
        self.frame1.pack()

        Label(self.frame1, text="KİTAPLIK", bg="#F0A500", font=("Arial", 25, "bold")).place(x=220)

        self.kaydirma = Scrollbar(self.frame1)
        self.kaydirma.place(x=529, y=50, height=300)

        self.agac = ttk.Treeview(self.frame1, yscrollcommand=self.kaydirma.set,
                                 columns=("sütun1", "sütun2", "sütun3", "sütun4"), show="headings")
        self.agac.heading("sütun1", text="Barkod")
        self.agac.heading("sütun2", text="Kitap")
        self.agac.heading("sütun3", text="Yazar")
        self.agac.heading("sütun4", text="Raf")

        self.agac.column("sütun1", width=120)
        self.agac.column("sütun2", width=120)
        self.agac.column("sütun3", width=120)
        self.agac.column("sütun4", width=120)

        self.agac.place(x=45, y=50, height=300)
        self.kaydirma.config(command=self.agac.yview)

        self.barkod_listesi = []
        self.kitap_listesi = []
        self.yazar_listesi = []
        self.raf_listesi = []

        cursor.execute("SELECT * FROM kitaplar")
        sonuc = cursor.fetchall()
        for i in sonuc:
            self.barkod_listesi.append(i[0])
            self.kitap_listesi.append(i[1])
            self.yazar_listesi.append(i[2])
            self.raf_listesi.append(i[4])

        self.kitaplık_listesi = list(zip(self.barkod_listesi, self.kitap_listesi, self.yazar_listesi, self.raf_listesi))
        print(self.kitaplık_listesi)

        for i in self.kitaplık_listesi:
            self.agac.insert("", END, values=(i[0], i[1], i[2], i[3]))

        Button(self.frame1, text="EXCEL", command=self.excel, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 15, "bold")).place(x=45, y=355, width=125)

        Button(self.frame1, text="PDF", command=self.pdf, bg="#F3F0D7",
               activebackground="#DADDFC", font=("Arial", 15, "bold")).place(x=420, y=355, width=125)

    def excel(self):
            calismakitabı = Workbook()
            sayfa = calismakitabı.active

            # başlıklar
            sayfa.append(["Barkod", "Kitap", "Yazar", "Raf"])

            # kitaplar
            for i in self.kitaplık_listesi:
                sayfa.append(i)
            # kaydet
            calismakitabı.save("kitaplık.xlsx")
            # exceli aç
            os.startfile("kitaplık.xlsx")

    def pdf(self):

            data = [["Barkod", "Kitap", "Yazar", "Raf"]]
            for i in self.kitaplık_listesi:
                data.append(list(i))

            pdf = FPDF()
            pdf = FPDF()
            #türkçe karakter destekleyen font indirdim aksi takdirde pdf dosyası hata veriyor
            pdf.add_font("YeniFont", style="", fname="BebasNeue-Regular.ttf", uni=True)
            pdf.set_font("YeniFont", size=12)
            pdf.add_page()

            sutun_genislik = pdf.w / 4
            satir_genislik = pdf.font_size

            for i in data:
                for j in i:
                    pdf.cell(sutun_genislik, satir_genislik*2, txt=j, border=1)
                pdf.ln(satir_genislik*2)


            pdf.output("kitaplik.pdf")
            os.startfile("kitaplik.pdf")

if __name__ == "__main__":
    app = Kutuphane()
    app.mainloop()