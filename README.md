# libraryManagement
Python &amp; Tkinter kütüphane otomasyonu

1	Modül Kurulumları

![image](https://user-images.githubusercontent.com/26578414/168471680-d68e4399-9943-471a-950e-0160819a746a.png)

Projemizde IDE olarak Pycharm’ı seçtik. SQL kodlarımızı çalıştıracağımız ve tablolarımızı görüntüleyebileceğimiz noktada da DB Browser yazılımını kurduk. Bu yazılımların kurumlarını es geçtim, linklerini kaynaklar kısmında bulabilirsiniz.
Modüllerimizi kurmadan önce python modül yükleyici paketeimizi resimdeki yazım diziniyle güncelliyoruz. Aynı işlemi Pycharm’ın bize sunduğu terminal kısmından da gerçekleştirebiliriz.

![image](https://user-images.githubusercontent.com/26578414/168471691-e66b7518-a489-4b8a-bec5-9dd7f723ad27.png)
 
Bu modül bize uygulamamızda gerekli olacak takvim nesnelerini sunar. 

 ![image](https://user-images.githubusercontent.com/26578414/168471701-6455465b-a1fa-46fc-b4fb-82dcb47a2234.png)

Excel çıktıları ve nesnelerini kullanabilmek için Openpyxl modülünü kurduk. Uygulamamızdan Excel sayfaları, çıktıları oluşturmamıza olanak sunar.


 
Bu modül ise pdf çıktıları için gerekli olan modüldür. Uygulamamızdan PDF sayfaları,çıktıları oluşturmamıza olanak sunar.

2	Modüllerin Projeye dâhil edilmesi

 ![image](https://user-images.githubusercontent.com/26578414/168471709-f208e922-0c96-4e8b-8dd7-7a952035b8cd.png)

Tkinter modülünü install komutuna gerek duymadan resimdeki gibi dahil ettik. Kurulumunu yaptığımız diğer modülleri, işletim sisteminde dosya işlemleri yapabilmemizi sağlayan os modülünü ve sql sorgularımızı çalıştırması için Sqlite modüllerini aktardık.

3	Ana sayfa Tasarımı

 ![image](https://user-images.githubusercontent.com/26578414/168471719-43f19a1b-4be1-44a6-9cba-c31d97da9476.png)

İlk etapta sayfa içerisindeki nesnelerimizi tutmamızı ve arka plan oluşturmak için çerçeve oluşturduk. 
Anasayfa penceremizin boyutlarını belirleyip Tkinter’ın pencere oluşturmamıza yarayan nesnesiyle çizdik. Bu tasarım nesnelerini kütüphane isimli bir sınıf tanımlayıp, öznitelik olarak bu sınıfta tanımladık. 
Uygulamamızda temel düzeyde 3 sayfa olacak şekilde olacak tasarladık. Tkinter’ın TopLevel komutundan faydalanarak üyeler kitaplar ve kitaplık sayfalarını alt pencereler olarak belirledik. Bu sayede butonlara tıkladığımızda ilgili butonların sayfalarını bağlantılı olarak açabileceğiz. İkonumuzu png dosyası olarak iconArchive sitesinden aldık ve konumunu ayarlayarak çerçevemize yerleştirdik. Ayrıca butonlarımız da birer tkinter nesnesi boyutları, yükseklikleri, konumları, fontu ayarlanarak çerçevemizin içine konumlandırdık.

4	Üye Sayfası Tasarımı

 ![image](https://user-images.githubusercontent.com/26578414/168471726-05008992-4394-4e71-b2c7-845d70df247b.png)

Üye sayfamızda bir kütüphaneye kayıt gerçekleştirmek isteyen kişinin temel bilgilerini ve daha sonrasında borç ve üye durumunu güncelleyebileceğimiz bir sayfa tasarladık. Üyelik türüne tek seçim yapabilmemiz için bir combobox nesnesi yerleştirdik. Bunun içerisinde öğrenci, normal ve kütüphane görevlisi ismiyle 3 etiket var. Kaydı yapılacak üyenin bilgileri burada girilerek kaydetme işlemi kaydet butonuna tıkladığımızda veri tabanında oluşturacağımız Üyeler tablosuna eklenerek kaydı gerçekleşecek. Daha sonrasında kitap gecikmesinden oluşan borcu da kişinin hanesine bu sayfada gerçekleştireceğiz.


5	Kitap Bilgileri Tasarımı

![image](https://user-images.githubusercontent.com/26578414/168471740-14c32cd2-02d1-4238-b989-ec640c8e3745.png)

Kitaplar sayfasında, kitap bilgileri, barkodu ödünç, teslim tarihi gibi bilgileri almak için form nesneleri  oluşturduk tarih ve zaman bilgisi için tkcalendar kütaphenesini import ettik. Kaydet, güncelle, sil gibi fonksiyonel butonları yerleştirdik. Bu butonlara fonksiyonlar oluşturup SQL komutları ile DB Browser ile  görüntüleyebileceğimiz veritabanı işlemleri gerçekleştireceğiz. Barkod kitabımızın tekil kodu olarak düşünüldü, kaydetme  ve sorgulama işlemlerini bu numarayı belirleyerek gerçekleştireceğiz. 


6	Kitaplık Sayfası Tasarımı

![image](https://user-images.githubusercontent.com/26578414/168471753-fb7aa54a-2785-4efc-a92a-1174ddb3ec46.png)

Kitaplık sayfamıza bir Treeview nesnesi yerleştirdik. Bu nesne bize sütun bazlı ağaç görünümünde detaylı bir okunabilirlik sağlıyor, bu sayfanın tek amacı elimizde bulunan kitapları görebilmek ve bunları excel veya pdf formatlarına çevirebilmek. Butonlarımızı tasarladıktan sonra boş fonksiyonlarını tanımladık ve konumlandırmasını ayarladık.

7 Üye Bilgilerini Görüntüleme, Kaydetme Güncelleme, Silme 

![image](https://user-images.githubusercontent.com/26578414/168471760-569a0c88-c17a-40ff-8143-5036f30c151f.png)
![image](https://user-images.githubusercontent.com/26578414/168471761-92bab768-bb74-4371-b8f8-030ef4b7de6d.png)
![image](https://user-images.githubusercontent.com/26578414/168471780-451de66f-a419-4e63-9299-bfee0dd1223b.png)

SQ lite DB Browser’a 2 üyeler ve kitaplar isimli 2 tane küçük veritabanı oluşturduk bunları sorgu olarak editörümüzün içinde yazdık. Üye sayfasındaki Getir butonunu kayıtları görüntülemek için kullandık. Üyenin referans numarasını metin kutusuna girdiğimizde ve getir butonuna tıkladığımızda referans numarasını girdiğimiz üyenin diğer bilgilerinin tümünü kalan metin kutularına yazdığımız SQL kodları ile çağırabiliyoruz.. Güncelleme butonumuzun fonksiyonunda ise bilgilerini çağırmış olduğumuz üyeye ilgili değişiklikler yapıldıktan sonra üyenin referans numarasına göre güncelleme sorgusunu yazdık. Butonların işlemi gerçekleştikten sonra form nesnelerinin içlerinin temizlenmesi için temizleme fonksiyonu tanımladık. Güncelleme, kaydetme ve silme işleminden sonra form nesnelerinin değerlerini sıfırlayıp ekrana bir uyarı ile işlemin başarılı olduğunun bilgisini veriyor. 

8	Kitap Bilgilerini Getirme, Takvim işlemleri, Borç Durumu Hesaplatma

![image](https://user-images.githubusercontent.com/26578414/168471783-d6fc5442-e614-45fd-b2c3-8531e5f39753.png)
![image](https://user-images.githubusercontent.com/26578414/168471786-b2c70fce-c47c-49fd-bf35-c0419e65a7cb.png)

Kitap Bilgilerini barkod numarasına göre üye bilgilerindeki gibi değerlerini görüntüleme işlemini gerçekleştirdik. Kaydetme ve silme işlemi üyeler sayfasındaki gibi aynı sql sorgu işlemlerini içeriyor. Güncelleme işleminde ise üyemize kitap veriliş ve teslim alma işlemini bu kısımda gerçekleştirdik. Kısaca, verilmek istenilen kitap, kitap bilgileri çağırıldıktan sonra “kime” combobox’ına verileceği üyenin referans numarası giriliyor. Ödünç işlemi gerçekleştikten sonra Kitaplar veri tabanında kitabın hangi üyede olduğunu gösterecek referans numarası güncelleniyor. 
Rafta ve ödünç verilmiş radio buton değerlerini de veritabanında ‘odunc’ 0-1 değerlerini saklayan sütunda veri tabanında güncelledik .Bu combobox nesnesini hem üyenin referans numarasını girmesi için bir metin kutusu gibi değer girilmesi üstüne hem de eğer bu kutuya bir değer girilmemişse teslim alma işlemi gerçekleştirildiğini varsayarak ‘Teslim Al’ seçeneği seçilebilmesi üzerine tasarladık. Tarih  işlemlerine gelecek olursak Datetime kütüphanesini işlevini bu kısımda  kullandık. Sistem tarihini üyenin referans numarası girildikten sonra otomatik olarak ödünç alacağı tarih yani bugün aldığımızı düşünürsek bugünün tarihini Ödünç Tarihi Combox’ına hesaplattıran bir fonksiyon tanımladık. Teslim tarihimizi de ödünç tarihinin üzerine 14 gün sayan ve bunu tarih formatında tekrar teslim combobox’ımıza yazdıran bir fonksiyonz yazdık. Bu işlemleri kitaplar sınıfının altında işlemler fonksiyonu altında toparladık. Datetime kütüphanesi tarih bilgisini b ize Yıl-Ay-Gün biçiminde sunuyordu, bu formatıda Gün-Ay-Yıl şeklinde formatlayıp combobox nesnelerimizde düzelttik. Teslim tarihinde tanımladığımız 14 gün zaman aşımına geçtiği her gün için borç kısmını 1 Tl artıracak  bir fonksiyon tanımladık. 

 ![image](https://user-images.githubusercontent.com/26578414/168471795-76fc4702-fee5-49c5-9d42-b3f4bf2fb17f.png)

Sayfanın ilk görünümde gizli konumda olan borç label’ımız kitabı teslim al seçeneği seçildiğinde hesaplanarak ekranda görünür duruma getiriliyor.

![image](https://user-images.githubusercontent.com/26578414/168471831-ac94233f-8d72-4469-ac9e-342e6d6ae9b4.png)

Kitap verilme işlemi gerçekleştikten sonra veri tabanımızdaki tabloların durumları resimlerdeki gibi güncellenir. 
 
![image](https://user-images.githubusercontent.com/26578414/168471836-b22b26c4-19dd-4cfe-bd0b-ffe651e90d91.png)

9	Kitaplık Sayfasının Fonksiyonları
 
![image](https://user-images.githubusercontent.com/26578414/168471843-fa4e2c9e-3427-4dcb-ba74-4ab8f4e59c51.png)

Kitaplar sayfasında Treeview nesnesinde elimizde olan kitapları  göstermek için veri tabanından çektiğimiz kitapları Ağaç yapısının sütunu kadar parçalayarak liste halinde yerleştirdik. OPENPYXL ve FPDF kütüphanelerini projeye aktardık. EXCEL ve PDF butonlarının fonksiyonlarını yazdık. Treeview’de liste halinde gözüken kitap bilgilerini bu dosyalar halinde çıktısını projenin bulunduğu klasöre oluşturmasını sağladım. Türkçe karakterler bulunduğu için PDF formatına çevirirken hata veriyordu. Bunun için internetten Türkçe desteği olan bir font indirdik ve projeye dahil ettik. Üyeler kısmındaki MAİL butonu için email ve smtp kütüphanelerini import ettik. Mail ile üyenin teslim tarihini geçtikten sonra oluşan borcunu tanımladığım alıcı ve gönderici arasında aktarımını sağlıyor. 

 ![image](https://user-images.githubusercontent.com/26578414/168471852-ae852bcb-2e64-414f-9815-2b6e8c25f8c6.png)


10	PDF dosyası oluşturmada Türkçe karakter sorunu

 ![image](https://user-images.githubusercontent.com/26578414/168471863-543dcfdf-9b67-4081-adf3-94e38fdf0c6c.png)

Kitaplık sayfasında ağaç nesnesinde görüntülediğimiz kitap listesini pdf dosyasına çevirmek istediğimizde bu pdf dosyasını oluştururken font tanımlamamız gerekir. Eğer Türkçe karakter destekli bir font edinmezsek dosyayı oluşturma işlemi gerçekleşmeyecektir. 
Uygulamamızın bulunduğu klasöre font dosyamızı ekleyip kodlarımızın içinde yeni bir font nesnesi tanımlayıp indirdiğimiz fontu tanıtarak sorunumuzu çözdük.
