soru = input("hangi tür kitap okumayı seversiniz ( anı, bilim, eğitim, gezi, hikaye)?")
print(soru)

 


if soru== "anı" :
   konu = input("Konusu nedir? (macera, korku, fantastik, bilim kurgu): ")
   if konu=="macera":
       print(
           "şu kitapları sevebilirsiniz: 1-Dağlar ve Yollar, 2-Çöl Yolculuğu, 3-Anı Hırsızlar, 4-Büyük Yolculuk, 5-Dağın Öte Yanı ")
       print("1-Dağlar ve Yollar Kısa Özet:Dağlar ve Yollar genellikle doğayı ve insanların tabiatta yaşadığı zorlukları anlatan kitaplardır. Bu tür kitaplar, yüksek dağları, vahşi ormanları ve engellerle dolu yolları içerebilir. İnsanların doğayla mücadeleleri, hayatta kalmaya çalışmaları ve doğayla yaşama biçimleri hakkında anlatılar da bu kitaplarda yer alabilir. Ancak, hangi kitapların korku öğeleri içerdiği konusunda net bir bilgimiz yoktur.")
       print("2-Çöl Yolculuğu, Paulo Coelho'nun romanıdır ve gerçek bir olaydan esinlenmiştir. Hikaye, otuz yıl önce Coelho'nun gerçekleşen çöl yolculuğuna dayanır. Yolculuk, Coelho'nun manevi bir öğretmenden aldığı rehberlik ile başlayan bir yolculuktur. Coelho, gizemli bir kadınla tanışana kadar ilerlemekte zorlanır. Kadın, onun kişisel bir anda buluşmasını sağlar ve Coelho'ya birçok hayat dersi verir. Kitap, kişisel gelişim ve kendini keşfetmek hakkında bir hikaye içermektedir.")
       print("3-Anı Hırsızları, Darren Simpson'ın 2022'de yayınlanan gençlik romanıdır. Kitap, Cyan adlı bir genç kızın hikayesini anlatıyor. Cyan, Başkabiryer'de yaşayan ve geçmişinin kötü anıları silinmiş bir gençtir. Cyan, bir gün diğer bir genç olan Lark ile tanışır ve Lark, Cyan'a geçmişinin silinmesine neden olan hafıza silme tedavisinden kurtulmasına yardım eder. Cyan, geçmişini hatırlamaya başladıkça, geçmişiyle yüzleşmek zorunda kalır ve geçmişinin kötü anıları onu rahatsız etmeye başlar. Cyan, geçmişiyle yüzleşmek ve iyi bir insan olmak için mücadele eder.Anı Hırsızları, gençlik romanı türünde yazılmış bir distopik romandır. Roman, geçmişin kötü anıları ile yüzleşmenin önemini ve iyi bir insan olmanın zorluğunu anlatmaktadır.")
       print("4-Dağın Öte Yanı, Ahmet Ümit'in 2006 yılında yayımlanan polisiye romanıdır. Roman, Ankara'da işlenen bir cinayeti araştıran komiser Mehmet Emin Korkmaz'ın hikayesini anlatmaktadır. Korkmaz, cinayeti araştırırken, kendisini 1970'li yılların siyasi atmosferi içinde bulur ve cinayetin siyasi bir bağlantısı olduğunu keşfeder. Korkmaz, cinayeti çözmek için siyasi geçmişini ve 1970'li yılların karanlık dönemini araştırmak zorunda kalır.Dağın Öte Yanı, polisiye türünde yazılmış bir siyasi gerilim romanıdır. Roman, 1970li yılların siyasi atmosferini ve bu dönemin karanlık yüzünü anlatmaktadır. Roman, aynı zamanda geçmişin izlerinin geleceği nasıl etkilediğini de anlatmaktadır.")
       print("5-Büyük Yolculuk, Nuri Bilge Ceylanın 2004 yılında çektiği Türk drama filmidir. Film, iki farklı karakterin bir yolculuğa çıkmalarını ve bu yolculuk sırasında kendilerini ve dünyayı keşfetmelerini anlatmaktadır.Filmin ilk karakteri, İdris (Erdal Beşikçioğlu) adlı bir kamyon şoförüdür. İdris, İstanbuldan Ankaraya giden bir yolculuk yapmaktadır. Yolculuk sırasında İdris, kendi geçmişi ve ailesi hakkında düşünmeye başlar.Filmin ikinci karakteri, Nuri (Cüneyt Arkın) adlı bir emekli öğretmendir. Nuri, İstanbuldan oğlunun yanına gitmek için bir yolculuk yapmaktadır. Yolculuk sırasında Nuri, kendi hayatı ve geçmişi hakkında düşünmeye başlar.yolculuk, İdris ve Nurinin kendilerini ve dünyayı keşfetmelerine yardımcı olur.Büyük Yolculuk, Nuri Bilge Ceylan'ın en önemli filmlerinden biridir. Film, Türkiyenin kültürel ve toplumsal yapısını yansıtmaktadır. Film, aynı zamanda insan ruhunun derinliklerine inmektedir.")
   if konu=="korku":
       print(
       "şu kitapları sevebilirsiniz: 1-Gece Evi, 2-Kan Dökülen Kabuslar, 3-Kabuslar Evi, 4-çatı katı, 5-Bir Cadının İtirafları ")
       print("Gece Evi serisi, Amerikalı yazar P.C. Cast ve kızı Kristin Cast tarafından yazılmış bir vampir-merkezli fantastik romandır. Seri, aylak bir kıza hayatta kalmak ve seçtiği evde savunma dersleri vererek hayatına devam etmeye çalışırken, zamanla olayların gittikçe tehlikeli hale gelmesiyle birlikte yaşananlara odaklanmaktadır.")
       print("Bu kitap, gerçek suç ve korkunç olayların anlatıldığı bir derlemedir. Korku ve gerilim unsurlarının yanı sıra suç, polisiye ve gizem dolu hikayeler içerir.")
       print("Kabuslar Evi Kısa Özet:Kabuslar Evi, gerilim-korku türünde, eski bir çiftlik evi ve bir emlak ofisi arasında geçen, farklı konulardan oluşan bir film serisidir. Harper, psikolojisi sorunlu bir kadındır ve araları bozulan erkek arkadaşından ayrılmıştır. Cadılar Bayramı'ndan önce kendindeki gücü keşfeden Harper, çiftlik evine taşınır ve burada tuhaf olaylar yaşamaya başlar. Filmin diğer konuları arasında uykucular ve korku-kapitalizm gibi unsurlar da yer alır.")
       print("Çatı Katı Kısa Özet:Tüm ülkenin gündemine oturan ve büyük sırlarla dolu Beyaz Ev soruşturmasını yürüten Başkomiser Emris, kendisine ulaşan yeni delillerin ardından araştırmayı derinleştirmeye başlar ve İnterpol’ün desteğiyle yurt dışına taşır. Beyaz Ev’in yeni sahibi Eren ve daha önce Beyaz Ev ile bağlantılı cinayetleri çözen Atlas, Demir, Ala üçlüsünün de dâhil olduğu özel bir ekip kurar.Daha önce ortadan kaybolan Arden’i bulmak, soruşturmanın devamı ve uluslararası suç örgütünün deşifre edilmesi için kilit rol oynamaktadır. Ancak Arden’den hiçbir iz yoktur. Başkomiser Emris, Arden’i bulmak için uğraşırken; Eren için ise eski sevgilisi Arden’e yaklaşmak kendi içinde büyük iç çatışmalara neden olacaktır.Tünelden Önceki Beyaz Ev serisinin başarılı yazarı Işıl Işık’tan her bölümünde ayrı bir heyecan ve merak duyacağınız bir polisiye roman… Beyaz Ev üçlemesinin final kitabı Çatı Katı isimli romanla, hikâye sona yaklaşırken kendinizi bir yandan soluk soluğa bir uluslararası soruşturmanın içinde bulacak, öte yandan Beyaz Ev’deki yeni gizemli olaylarla korku ve gerilimi iliklerinize kadar hissetmeye devam edeceksiniz.")
       print("Bir Cadının İtirafları adlı kitap, Francesca Lia Block tarafından yazılmıştır. Kitap, Los Angeles'ın alternatif kültürüne ve sanat dünyasına duyulan hayranlığı yansıtan bir kısa hikaye koleksiyonudur. Kitapta, ana karakter Weetzie Bat, hayatın zorluklarıyla başa çıkmak için arkadaşları Witch Baby, Dirk ve Duck gibi renkli karakterlere güvenir. Aşk, kayıp, aile ve arkadaşlık gibi konular, zaman zaman fantastik unsurlarla da harmanlanarak anlatılır. Bir Cadının İtirafları, yazarın tanınmış Weetzie Bat serisinde yer alır ve kendi benzersiz tarzı ile okuyuculara hoparlörler, müzik ve alternatif kültür hakkında bir deneyim sunar.")

   if konu=="fantastik":
       print(
           "şu kitapları sevebilirsiniz: 1-Ay'a Yolculuk, 2-Kendi Gökyüzümüz, 3-Yaralı Karanfil, 4-Gecenin Öteki Yüzü, 5-Teknik İntikam ")
       print(
           "1-Ay'a Yolculuk, Neil Armstrong'un Ay'a ilk ayak basan astronot olduğu 1969'daki Apollo 11 görevinin anlatıldığı kitaptır. Kitap, Armstrong'un çocukluğundan NASA'ya katılmaya kadar olan hayatını ve Ay'a yolculuğunu ayrıntılı bir şekilde anlatıyor.Armstrong, Alabamada doğdu ve küçük bir kasabada büyüdü. Çocukluğundan beri bilim ve uzay ile ilgileniyordu. Liseden mezun olduktan sonra Purdue Üniversitesinde havacılık mühendisliği okudu. Üniversiteden mezun olduktan sonra ABD Hava Kuvvetlerinde pilot olarak görev yaptı.1962 yılında NASAya katıldı. NASAda test pilotu ve astronot olarak görev yaptı. 1969 yılında Apollo 11 görevine seçildi. Apollo 11, Aya ilk ayak basan uzay aracıydı.Armstrong ve meslektaşı Buzz Aldrin, 20 Temmuz 1969 tarihinde Aya ayak bastılar. Bu, insanlığın tarihindeki en önemli olaylardan biri olarak kabul edilir. Armstrong, Ayda yaptığı ilk konuşmada, Bu, küçük bir adam için büyük bir adımdır. dedi.Armstrongun Aya yolculuğu, insanlığın tarihindeki önemli bir dönüm noktasıdır. Bu olay, insanlığın teknolojik ve bilimsel gelişiminde önemli bir adımdır. Aynı zamanda insanlığın hayal gücünü ve cesaretini temsil eder.")
       print(
           "2-Kendi Gökyüzümüz, J.D. Salinger'ın 1951 yılında yayımlanan romanıdır. Roman, Holden Caulfield adında 16 yaşındaki bir gencin hikayesini anlatıyor. Holden, Pencey Prep'ten atıldıktan sonra New York City'ye gider ve bir hafta boyunca şehirde dolaşırken yaşadıklarını anlatır.Holde,sosyal açıdan uyumsuz ve asi bir gençtir. Okuldan nefret eder ve ailesi ile de arası iyi değildir. Holden, yalnızdır ve kimseye güvenmez. Kendisini bir yabancı gibi hisseder.Holden, New York Cityde geçirdiği bir hafta boyunca, kendi hayatı ve kendisi hakkında düşünmeye başlar. Kendisini ve yaşadığı dünyayı sorgular. Holden, sonunda kendi gökyüzünü bulmaya çalışır.Kendi Gökyüzümüz, Holden Caulfieldin hikayesi aracılığıyla, gençlik, yalnızlık, yabancılaşma ve büyüme gibi temaları ele alan bir romandır. Roman, yayınlandığı tarihten bu yana birçok ödül kazanmış ve dünya çapında milyonlarca kişi tarafından okunmuştur.")
       print(
           "3-Yaralı Karanfil, 1995 yılında yayımlanan bir romandır. Roman, İran-Irak Savaşı sırasında, İran'ın bir kasabasında yaşayan iki genç kızın hikayesini anlatıyor.Ailesinin maddi durumu iyi olan Maryam, güzel bir genç kızdır. Arkadaşı Leila ise fakir bir ailede büyüyen, güzelliğiyle dikkat çeken bir genç kızdır. Maryam ve Leila, çocukluktan beri arkadaşlardır ve birbirlerine çok yakındırlar.Savaş, Maryam ve Leilanın hayatını alt üst eder. Maryamın babası savaşta öldürülür ve ailesi maddi zorluklar yaşar. Leila ise savaşta yaralanır ve bir bacağını kaybeder.Maryam ve Leila, savaşın zorluklarına rağmen, birbirlerine destek olurlar ve arkadaşlıklarını sürdürürler. Savaş sonunda biter, ancak Maryam ve Leilanın hayatları asla eskisi gibi olmaz.Yaralı Karanfil, savaşın yıkıcı etkilerini ve insan ruhunun gücünü anlatan bir romandır. Roman, yayınlandığı tarihten bu yana birçok ödül kazanmış ve dünya çapında milyonlarca kişi tarafından okunmuştur.")
       print(
           "4-Gecenin Öteki Yüzü, 1973 yılında yayımlanan bir romandır. Roman, Güney Afrika'da apartheid döneminde yaşayan genç bir kadın olan Sarah'ın hikayesini anlatıyor.Sarah, bir gece kulübünde şarkı söyleyen genç bir kadındır. Bir gün, kulüpte tanıştığı bir adamla evlenir ve Johannesburga taşınır. Sarah, Johannesburgda yeni bir hayata başlar, ancak bu yeni hayat ona hayal ettiği mutluluğu getirmez.Apartheid döneminde, Güney Afrikada siyahlar ve beyazlar ayrımı yapılmaktadır. Sarah, beyaz bir adamla evli olduğu için, yaşadığı mahallede dışlanır. Sarah, eşinden şiddet görür ve kocası tarafından terk edilir.Sarah, zorluklara rağmen, hayata tutunmaya çalışır. Sarah, bir barda şarkı söylemeye başlar ve müziği sayesinde, insanların hayatlarına dokunur. Sarah, sonunda, kendi ayakları üzerinde durmayı başarır ve yeni bir hayata başlar.Gecenin Öteki Yüzü, apartheid döneminde Güney Afrikada yaşayan bir kadının hikayesini anlatan bir romandır. Roman, kadın hakları, ayrımcılık ve mücadele gibi temaları ele alır. Roman, yayınlandığı tarihten bu yana birçok ödül kazanmış ve dünya çapında milyonlarca kişi tarafından okunmuştur.")
       print(
           "5-Teknik İntikam, Daniel Suarezin 2019 yılında yayımlanan bir romandır. Roman, bir siber saldırının dünyanın en büyük şirketlerinden birini nasıl çökertebileceğini ve bu saldırının arkasındaki kişilerin nasıl yakalanabileceğini anlatıyor.Romanın ana karakteri Matthew Skowronski, bir siber güvenlik uzmanıdır. Skowronski, bir gün, dünyanın en büyük şirketlerinden biri olan Odin adlı bir şirketin siber saldırıya uğradığını öğrenir. Odin, saldırı sonucunda tüm verilerini kaybeder ve işleyişi aksar.Skowronski, saldırının arkasındakileri bulmak için harekete geçer. Skowronski, soruşturması sırasında, saldırının Odinin eski bir çalışanı olan David Finch tarafından gerçekleştirildiğini öğrenir. Finch, Odinden kovulmuştur ve intikam almak için siber saldırıyı gerçekleştirmiştir.Skowronski, Finchi yakalamak için bir ekip kurar. Ekip, Finchin peşine düşer ve sonunda onu yakalamayı başarır. Finch, mahkemede suçlu bulunur ve hapse gönderilir.Teknik İntikam, siber saldırıların tehlikelerini ve bu saldırıların nasıl önlenebileceğini anlatan bir romandır. Roman, aynı zamanda siber güvenlik uzmanlarının önemini ve bu uzmanların nasıl yetiştirilebileceğini anlatmaktadır.")

   if konu=="bilim kurgu":
       print(
           "şu kitapları sevebilirsiniz: 1-Otomatik Piyano, 2-Sineklerin Tanrısı, 3-Zamanın Kör Noktası, 4-1984, 5-Cesur Yeni Dünya ")
       print(
           "1-Otomatik Piyano, 1996 yılında yayımlanan bir romandır. Roman, otomatik piyanonun icadından günümüze kadar olan tarihini anlatıyor.")
       print(
           "2-Sineklerin Tanrısı, William Golding'in 1984 yılında yayımlanan romanıdır. Roman, bir grup İngiliz okul çocuğunun bir uçak kazasında ıssız bir adaya düşmesini ve burada kendi topluluklarını kurmaya çalışmalarını anlatıyor.Çocuklar, adada ilk başlarda arkadaş canlısı ve yardımseverdirler. Ancak, zamanla, toplum içinde çatışmalar başlar. Çocuklar, kendi aralarında gruplara ayrılırlar ve bu gruplar, birbirine düşman olur.Çocuklar, adada hayatta kalmak için mücadele ederler. Yiyecek ve su bulmak zorundadırlar ve aynı zamanda, adada yaşayan tehlikeli hayvanlardan da korunmalıdırlar. Çocuklar, sonunda, adayı terk etmeyi ve eve dönmeyi başarırlar.Sineklerin Tanrısı, insan doğasının karanlık yönlerini anlatan bir romandır. Roman, aynıcı etkilerini de anlatmaktadır.")
       print(
           "3-Zamanın Kör Noktası, 2009 yılında yayımlanan bir romandır. Roman, zaman yolculuğunun keşfedilmesi ve bu keşfin dünyayı nasıl etkilediğini anlatıyor.")
       print(
           "4-1984, George Orwell tarafından 1949 yılında yazılmış bir distopik romandır. Roman, Büyük Britanya'da geçen bir gelecekte geçmektedir. Büyük Britanya, Büyük Birader tarafından yönetilen totaliter bir devlettir. Büyük Birader, her türlü düşünce ve eylemi kontrol eder. Gerçeklik, Büyük Birader tarafından yeniden yazılır ve herkes bu yeni gerçekliği kabul etmek zorundadır.")
       print(
           "5-Romanın ana karakteri Winston Smith, Büyük Britanyada çalışan bir devlet memurudur. Winston, Büyük Biraderin rejiminden hoşnutsuzdur. Winston, özgür düşünceye ve bağımsızlığa inanır. Winston, Büyük Biraderin rejimi hakkında bir günlüğüne yazmaya başlar. Winstonın günlüğü, Büyük Biraderin dikkatini çeker. Winston, Büyük Biraderin gizli polisleri tarafından tutuklanır ve işkence görerek suçlu bulunur. Winston, sonunda, Büyük Biradere bağlılık yemini eder.1984, totaliter rejimlerin tehlikelerini anlatan bir romandır. Roman, aynı zamanda, özgür düşüncenin ve bağımsızlığın önemini anlatmaktadır.")

       soru = input(
           "hangi tür kitap okumayı seversiniz ( anı, bilim, eğitim, gezi, hikaye, roman, şiir, tarih, yemek kitapları]?")
       print(soru)

 

 


if soru == "bilim":
   konu = input("Konusu nedir? (macera, korku, fantastik, bilim kurgu): ")

   if konu == "macera":
               print(
                   "şu kitapları sevebilirsiniz: 1-Jurassic Park, 2-Uzayda Rendezvous, 3-Kara Delikler ve Bebek Evrenler, 4-Artemis, 5-Yenilmez ")
               print(
                   "1-Michael Crichton: Genetik mühendislikle yaratılan dinozorların yer aldığı bu romanda, bilim insanları ve ziyaretçilerin tehlikeli ve sürpriz dolu bir adada geçen macerasını takip ediyoruz.")
               print(
                   "2-Arthur C. Clarke: Uzayda gerçekleşen heyecan dolu bir buluşma hikayesini anlatan bu bilim kurgu romanında, astronotlar ve bir gizemli uzay gemisi arasındaki etkileşimler büyüleyici bir şekilde işleniyor.")
               print(
                   "3-Stephen Hawking: Dünyaca ünlü fizikçi Stephen Hawking, karmaşık bilimsel konuları anlaşılır bir şekilde anlatarak okuyucuları evrenin sırlarıyla dolu bir maceraya çıkarıyor.")
               print(
                   "4-Andy Weir: Yine Andy Weir'in kaleme aldığı bu kitap, Ay'da geçen bir hikayeyi anlatıyor. Suç, macera ve bilim, Ay kolonisinde yaşayan genç bir kadının etrafında dönüyor.")
               print(
                   "5-Stanislaw Lem: Gelişmiş teknolojilerle donatılmış bir uzay gemisinin gönderildiği, uzayda yaşanan garip olayları ve karşılaşılan gizemli varlıkları anlatan bir bilim kurgu klasiği.")
   if konu == "korku":
               print(
                   "şu kitapları sevebilirsiniz: 1-Frankenstein, 2-Labirent, 3-Parazit, 4-Sis, 5-Dünya Dışı ")
               print(
                   "Mary Shelley: Klasik bir eser olan Frankenstein, modern bilimle insana hayat vermenin sonuçlarına odaklanan bir korku hikayesidir..")
               print(
                   "Kate Mosse: Bu kitap, tarihi ve bilimsel bir araştırma ile karanlık bir efsanenin iç içe geçtiği gizemli bir korku hikayesini anlatır.")
               print(
                   "Mira Grant: Genetik mühendislik ve salgın hastalıkların merkezinde geçen bu kitap, bilim kurgu ve korkuyu başarıyla bir araya getirir.")
               print(
                   "Stephen King: Stephen King'in korku ve bilim kurgu türlerini harmanlayarak kaleme aldığı bu kitap, korkunun kalbinde geçen bir hikayeyi sunar.")
               print(
                   "Jeff VanderMeer: Gizemli bir bölge olan X Bölgesinde geçen bu kitap, doğaüstü olayların ve bilimsel keşiflerin izini sürerken okuyucuya gerilim dolu bir atmosfer sunar.")

   if konu == "fantastik":
               print(
                   "şu kitapları sevebilirsiniz: 1-Harry Potter serisi, 2-Yüzüklerin Efendisi, 3-Hobbit, 4-Kızıl Yükseliş, 5-Eragon ")
               print(
                   "1-J.K. Rowling: Büyücülük dünyasına giren genç bir çocuğun maceralarını anlatan bu seride, Harry Potter ve arkadaşlarının Voldemort ile olan mücadelesine tanık olursunuz")
               print(
                   "2-J.R.R. Tolkien: Bu ünlü epik fantastik kitap serisi, Orta Dünyada geçen bir yolculuğu ve iyi ile kötü arasındaki savaşı anlatır.")
               print(
                   "3-J.R.R. Tolkien: Yüzüklerin Efendisi öncesi geçen bu kitap, hobbit Bilbo Baggins'in ejderha Smaug'un hazinesini ele geçirmek için yaptığı yolculuğu anlatır.")
               print(
                   "4-Pierce Brown: Bu kitap, uzayda geçen ve farklı sınıflar arasındaki mücadeleyi konu alan heyecan dolu bir bilim kurgu-fantastik eserdir.")
               print(
                   "5-Christopher Paolini: Bu kitap, ejderhalar, büyücüler ve kahramanların yer aldığı epik bir fantastik dünyada geçen bir hikaye sunar.")

   if konu == "bilim kurgu":
               print(
                   "şu kitapları sevebilirsiniz: 1-Marslı, 2-Fareler ve İnsanlar, 3-Sarı Odanın Esrarı, 4-Uzay Gemisi Yolcuları, 5-Ay'ın Öteki Yüzü ")
               print(
                   "1-Andy Weir (Türkçe çevirisi): Mars'ta mahsur kalan bir astronotun hayatta kalma mücadelesini anlatan bu kitap, bilimsel gerçekçiliği ve mizahi üslubuyla ünlüdür.")
               print(
                   "2-Tayfun Pirselimoğlu: İnsanların farelere dönüştüğü distopik bir gelecekte geçen bu kitap, bilim kurgu ve toplumsal eleştiri unsurlarını bir araya getirir.")
               print(
                   "3-Emrah Serbes: Uzayda geçen ve bilim kurgu türünün ögelerini taşıyan bu kitap, bir grup astronotun gizemli olaylarla dolu yolculuğunu anlatır.")
               print(
                   "4-Cem Güventürk: Yazar, bilimsel gerçekçilikle harmanlanmış bir hikaye ile uzay yolculuğunun insan psikolojisi üzerindeki etkilerini ele alır.")
               print(
                   "5-Faruk Duman: Ay'da geçen ve alternatif bir tarih temasını ele alan bu kitap, bilim kurgu ve tarih öğelerini birleştirir.")

 

 

if soru == "eğitim":
   konu = input("Konusu nedir? (macera, korku, fantastik, bilim kurgu): ")
   if konu == "macera":
               print(
                   "şu kitapları sevebilirsiniz: 1-Robinson Crusoe, 2-Yüzbaşının Kızı, 3-Kaptan Grant'ın Çocukları, 4-Kızıl Yelkenli, 5-Huckleberry Finn'in Maceraları ")
               print(
                   "1-Daniel Defoe:Bu klasik eser, gemi kazası sonucu ıssız bir adaya düşen Robinson Crusoenun hayatta kalma mücadelesini anlatır. Kitap, cesaret, dayanıklılık ve yaratıcılık gibi önemli değerleri vurgularken aynı zamanda keşiflerle dolu bir maceraya sahiptir.")
               print(
                   "2-Alexander Pushkin:Bu Rus klasik eseri, bir genç subayın gizli aşkı ve tehlikeli maceralarla dolu hikayesini anlatır. Kitap, aşkın gücü ve insan doğasının karmaşıklığı üzerine derin düşüncelere sahiptir.")
               print(
                   "3-Jules Verne:Bu klasik macera romanı, dünyanın farklı yerlerine yapılan heyecan dolu bir yolculuğu konu alır. Maceraperest çocuklar, kayıp denizci Kaptan Grantı bulmak için zorlu bir serüvene atılırlar.")
               print(
                   "4-Jack London:Bu kitap, yalnız bir kurt olan Buckın Alaskada altın arayıcılığı için çalıştığı zorlu koşulları ve hayatta kalma mücadelesini anlatır. Kitap, doğanın gücü ve sadakatin önemini vurgular.")
               print(
                   "5-Mark Twain:Bu klasik roman, Huck Finn ve kaçak köle Jimin Mississippi Nehri boyunca geçen maceralarını anlatır. İkili, köleliğin adaletine ve insanlık değerlerine meydan okuyan zorlu durumlarla karşı karşıya kalır.")
   if konu == "korku":
               print(
                   "şu kitapları sevebilirsiniz: 1-Goosebumps Serisi, 2-Nightmare Academy, 3-Coraline, 4-Doll Bones, 5-Carnegie Hayaletleri")
               print(
                   "MR.L. Stine: Bu popüler seride, çocuklar ve genç yetişkinler için korku dolu hikayeler ve ürkütücü olaylar yer alır. Seride birçok farklı kitap bulunmaktadır ve her biri bağımsız hikayelere sahiptir.")
               print(
                   "Dean Lorey: Bu seri, bir korku okulunda geçen fantastik bir macerayı anlatır. Öğrencilerin kabuslara ve korkunç yaratıklara karşı mücadele ettiği bir dünyayı keşfeder.")
               print(
                   "Neil Gaiman: Bu kitap, küçük bir kızın gizemli ve korkutucu bir dünyada yaşadığı maceraları anlatır. Neil Gaiman'ın ödüllü eserlerinden biridir.")
               print(
                   "Holly Black: Bu kitap, ürkütücü bir bebek bezi dolabı oyuncağı hakkında bir korku hikayesini anlatır ve macera dolu bir yolculuğa çıkarır.")
               print(
                   "Erol Toy: Bu kitap, genç okuyuculara yönelik Türk edebiyatından bir korku öyküsüdür. Carnegie Kütüphanesi'nde geçen bu hikaye, bir grup çocuğun gizemli olayları çözmeye çalışırken yaşadıkları korku dolu maceraları anlatır. Erol Toy, korku ve gerilim unsurlarını kullanarak çocuklara ve genç yetişkinlere eğitici ve heyecan verici bir kitap sunar.")

   if konu == "fantastik":
               print(
                   "şu kitapları sevebilirsiniz: 1-Alice Harikalar Diyarında, 2-Narnia Günlükleri, 3-Percy Jackson, 4-His Dark Materials, 5-His Majesty's Dragon ")
               print(
                   "1-Lewis Carroll:Bu klasik eser, Alice'in tavşan deliğinden geçerek Harikalar Diyarına düşmesi ve burada fantastik maceralar yaşamasını anlatır. Kitap, mantık ve gerçeklik kavramları üzerine düşündürücüdür.")
               print(
                   "2- C.S. Lewis:Bu seride, çocuklar, bir gardırop aracılığıyla gizemli bir dünya olan Narniaya ulaşır ve burada aslan kral Aslan ile birlikte maceralara atılır. Kitap, cesaret, sadakat ve iyilik gibi değerleri işler.")
               print(
                   "3-Rick Riordan:Bu seride, modern zamanlarda tanrıların soyundan gelen kahraman Percy Jacksonın Yunan mitolojisiyle dolu maceraları konu alınır. Kitap, özgüven, sorumluluk ve kabul gibi değerleri vurgular.")
               print(
                   "4-Philip Pullman:Bu seride, Lyra adlı bir kızın sihirli bir pusulanın yardımıyla çok boyutlu bir maceraya çıkması ve evreni değiştirebilecek bir gizemi çözmeye çalışması anlatılır. Kitap, cüret, gerçeklik ve özgürlük konularına değinir.")
               print(
                   "5-Naomi Novik:Bu kitap, alternatif bir tarihsel dünyada geçen fantastik bir hikayedir. Napolyon Savaşları döneminde, deniz kaptanı olan Laurence, bir Fransız gemisinden ele geçirdiği ejderhacık yumurtasını kurtarmak zorunda kalır. Yumurta açıldığında ortaya çıkan ejderha, Laurence'ın beklemediği şekilde onunla bağ kurar. Laurence ve yeni ejderhası, güçlerini ve bağlılıklarını keşfederek savaşlara katılırlar. Kitap, dostluğun, sadakatin ve sıradışı bağların gücünü anlatırken, tarihi olayları fantastik bir")

   if konu == "bilim kurgu":

               print("şu kitapları sevebilirsiniz: 1-Dune, 2-Brave New World, 3-The Left Hand of Darkness, 4-Snow Crash, 5- Ready Player One")
               print("1-Frank Herbert: Uzak gelecekteki gezegen Dune'da geçen bu kitap, politika, din, ekoloji ve güç ilişkilerini ele alarak derin düşünceye sevk eder.")
               print("2-Aldous Huxley: Toplumu kontrol altında tutmak için bilimsel ve teknolojik yöntemlerin kullanıldığı distopik bir geleceği konu alır. Özgürlük, bireysellik ve toplumsal kontrol gibi konulara odaklanır.")
               print("3-Ursula K. Le Guin: Ekoloji ve cinsiyet konusunu işleyen bu kitap, uzaylı bir gezegenin toplum yapısını ve insanlar arasındaki ilişkileri inceler.")
               print("4-Neal Stephenson: Sanal gerçeklik, bilgisayar programlaması ve dilbilim gibi temaları içeren bu kitap, gelecekteki bir distopik dünyayı anlatır.")
               print("5-Ernest Cline: Sanal gerçeklik ve pop kültürüne büyük bir vurgu yapan bu kitap, genç bir karakterin sürükleyici ve tehlikeli bir sanal dünya yarışmasına katılmasını konu alır.")

 

 

 

if soru == "gezi":
   konu = input("Konusu nedir? (macera, korku, fantastik, bilim kurgu): ")
   if konu == "macera":
               print(
                   "şu kitapları sevebilirsiniz: 1-Bir Gün Tek Başına, 2-Kırk Gün Kırk Gece, 3-Yolun İki Yüzü, 4-Atlas - Benim Yolum, 5-Keşfetmek: Dünyanın En İlginç 100 Yerini Geziyorum ")
               print(
                   "1-İlber Ortaylı: Tarihçi İlber Ortaylı'nın kişisel gezi deneyimlerini anlattığı bu kitap, yazarın dünya çapında yaptığı gezileri ve gözlemlerini içerir.")
               print(
                   "2-Yaşar Nuri Öztürk: Yaşar Nuri Öztürk'ün yedi kıtada 47 ülkeyi dolaşarak gerçekleştirdiği eşsiz gezi serüvenini anlattığı kitaptır.")
               print(
                   "3-Cem Mumcu: Gazeteci ve yazar Cem Mumcu'nun dünya turu esnasında yaşadığı maceraları ve deneyimlerini içeren kitaptır")
               print(
                   "4-İlber Ortaylı: Tarihçi İlber Ortaylı'nın gezgin kimliğiyle dünyayı dolaşırken edindiği gözlemler ve izlenimlerini aktardığı kitaptır.")
               print(
                   "5-Serdar Çelik: Yazar Serdar Çelik'in, dünyanın en ilginç 100 yerini ziyaret ettiği, macera dolu ve ilgi çekici bir gezi kitabıdır.")
   if konu == "korku":
               print(
                   "şu kitapları sevebilirsiniz: 1-Gece Yarısı Gezintisi, 2-Ghostland: An American History in Haunted Places, 3-Dark Star Safari: Overland from Cairo to Cape Town, 4-The Devil in the White City: Murder, Magic, and Madness at the Fair That Changed America, 5-House of Leaves ")
               print(
                   "1-Derviş İsmail Zülfikar: Türk edebiyatının ilk korku türündeki kitaplarından biri olarak kabul edilen bu eser, Osmanlı İstanbul'unda korkunç olayları anlatır.")
               print(
                   "2-Colin Dickey: Amerika Birleşik Devletleri'ndeki hayaletli ve ürkütücü mekanları keşfeden bir yazarın gezi notları ve incelemelerini içeren kitaptı")
               print(
                   "3-Paul Theroux: Ünlü gezgin yazar Paul Theroux'un Kuzey Afrika'dan Güney Afrika'ya uzanan, zorlu ve korku dolu bir seyahati anlattığı kitaptır.")
               print(
                   "4-Erik Larson: 1893 Chicago Dünya Fuarı sırasında işlenen seri cinayetleri ve hikayelerini anlatan gerilim dolu bir kitaptır.")
               print(
                   "5-Mark Z. Danielewski: Bu roman, korku ve gerilim unsurlarını içeren karmaşık bir yapıya sahiptir ve korku dolu bir evin sırlarını keşfetmeye çalışan karakterlerin hikayesini ele alır.")

   if konu == "fantastik":
               print(
                   "şu kitapları sevebilirsiniz: 1-Gulliver's Travels, 2-The Hobbit, 3-The Chronicles of Narnia, 4-The City of Dreaming Books, 5-Neverwhere ")
               print(
                   "1-Jonathan Swift: Lemuel Gulliver'ın fantastik yolculukları, cüce ülkesi Lilliput'tan devlerin ülkesi Brobdingnag'a, uçan adalardan Görünmez Adam'ın ülkesine kadar pek çok hayali dünyayı içerir.")
               print(
                   "2-J.R.R. Tolkien: Hobbit Bilbo Baggins'in, ejderha Smaug'un hazine dolu dağındaki mağarasından başlayarak Orta Dünya'nın fantastik coğrafyalarını dolaşan maceralarını anlatır.")
               print(
                   "3-C.S. Lewis: Yedi kitaptan oluşan bu seri, çocuklar ile birlikte fantastik bir dünya olan Narnia'yı keşfeder ve orada yaşanan maceralara tanık olurlar.")
               print(
                   "4-Walter Moers: Yazarın Zamonia serisinin bir parçası olan bu kitap, hayali kitapçılar ve kitaplardan oluşan bir şehirde geçen büyülü bir macerayı anlatır.")
               print(
                   "5-Neil Gaiman: Gizemli ve sihir dolu Londra Altı Şehri'nde geçen bu kitap, normal dünyadan çekilmiş fantastik bir macerayı işler.")

   if konu == "bilim kurgu":
               print(
                   "şu kitapları sevebilirsiniz: 1-The Long Way to a Small, Angry Planet, 2-Red Mars, 3-Ringworld, 4-Hyperion, 5-The Left Hand of Darkness ")
               print(
                   "1-Becky Chambers: Uzay gemisi Wayfarer'ın mürettebatının, uzak galaksilere gerçekleştirdikleri maceraları ve farklı gezegenlerle olan etkileşimlerini anlatan kitaptır.")
               print(
                   "2-Kim Stanley Robinson: Bilim kurgu klasiklerinden biri olan bu kitap, insanların Mars'a yerleşmeye çalıştığı ve gezegeni terraform etmeye çalıştığı gelecekteki bir dünyayı anlatır.")
               print(
                   "3-Larry Niven: Büyük bir halka şeklinde olan ve güneş sisteminin etrafında dönen bir yapay dünya olan Ringworld gezegenine yapılan macerayı konu alır.")
               print(
                   "4-Dan Simmons: Gelecekteki bir zamanda, yedi gezginin, gezegen Hyperion'u ziyaret ederek orada yaşanan gizemli olayları ve korkunç varlıkları keşfetmelerini anlatır.")
               print(
                   "5-Ursula K. Le Guin: Uzaydaki farklı gezegenler arasında yapılan bir görev sırasında yaşanan siyasi entrikaları ve farklı bir cinsiyet sistemiyle yaşayan gezegeni anlatır.")

 

 

if soru == "hikaye":
   konu = input("Konusu nedir? (macera, korku, fantastik, bilim kurgu): ")
   if konu == "macera":
           print(
               "şu kitapları sevebilirsiniz: 1-Macera Dolu Yıllar, 2-Hobbit, 3-Robinson Crusoe, 4-Indiana Jones Serisi, 5-Hazine Adası ")
           print(
               "1-Mark Twain: Tom Sawyer ve Huckleberry Finn'in maceralarını anlatan klasik bir kitap.")
           print(
               "2- J.R.R. Tolkien: Orta Dünya'da geçen bu epik fantastik kitap, Bilbo Baggins'in macerasını konu alıyor.")
           print(
               "3-Daniel Defoe: İngiliz tüccar Robinson Crusoe'nun ıssız bir adaya düşmesi ve hayatta kalma mücadelesi hikayesini anlatır.")
           print(
               "4-Campbell Black ve James Rollins: Indiana Jones karakteri etrafında dönen serüven dolu macera kitapları.")
           print(
               "5-Robert Louis Stevenson: Gemi adamı Jim Hawkins'in korsanlar ve hazine arayışıyla dolu macerasını anlatan klasik bir roman.")
   if konu == "korku":
       print(
           "şu kitapları sevebilirsiniz: 1-The Shining, 2-It, 3-American Psycho, 4-Hayalet Hikayeleri, 5-Gone Girl ")
       print(
           "1-Stephen King: Bir otelde yaşanan doğaüstü olayları konu alan ünlü yazar Stephen King'in korku dolu bir başyapıtı.")
       print(
           "2-Stephen King: Maine kasabasında bir grup çocuğun, Pennywise adlı korkunç bir palyaço tarafından rahatsız edilmesini anlatan korku dolu bir kitap")
       print(
           "3- Bret Easton Ellis: Bir seri katilin zihniyle giderek deliren bir yatırım bankacısının hikayesini anlatan karanlık bir roman.")
       print(
           "4- M.R. James: Eski İngiliz hayalet hikayelerinin usta yazarı M.R. James'in korku dolu öykülerinden oluşan bir derleme.")
       print(
           "5-Gillian Flynn: Kaybolan bir kadının hikayesini anlatan bu psikolojik gerilim romanı, okuyucuları şaşırtacak birçok sürpriz barındırır.")

   if konu == "fantastik":
       print(
           "şu kitapları sevebilirsiniz: 1-Narnia Günlükleri, 2-Buz ve Ateşin Şarkısı, 3-Artemis Fowl Serisi, 4-Percy Jackson ve Olimposlular Serisi, 5-His Dark Materials ")
       print(
           "1-C.S. Lewis: Dolap aracılığıyla gizemli bir dünyaya giren çocukların fantastik maceralarını konu alan sevilen bir seri.")
       print(
           "2-George R.R. Martin: Westeros adlı kurgusal bir dünyada geçen politik entrikalar ve fantastik yaratıklarla dolu epik bir seri.")
       print(
           "3-Eoin Colfer: Dahilikle tanınan genç Artemis Fowl'un sihir ve teknolojiyi kullanarak elf ve cüce gibi fantastik varlıklarla mücadelesini anlatan kitaplar.")
       print(
           "4-Philip Pullman: Lyra Belacqua'nın, farklı boyutları keşfettiği ve büyülü hayvanlarla dolu bir evrende geçen fantastik bir seri.")
       print(
           "5-Margaret Weis ve Tracy Hickman: Ejderhalar, büyücüler ve kahramanlar arasındaki savaşı anlatan popüler bir fantastik serüven.")

   if konu == "bilim kurgu":
       print(
           "şu kitapları sevebilirsiniz: 1-Blade Runner, 2-Sissoylu Serisi, 3-Yıldız Gemisi Askerleri, 4-Babalar ve Oğullar, 5-Hiperion Cantos Serisi ")
       print(
           "1-Philip K. Dick: İnsan benzeri androidlerin var olduğu gelecekte geçen bu roman, insan doğasını ve kimliğini sorgulayan derin bir bilim kurgu eseri")
       print(
           "2-Brandon Sanderson: Fantastik ve bilim kurgu öğelerini başarıyla bir araya getiren epik bir seri.")
       print(
           "3-Robert A. Heinlein: Askerlerin uzayda savaştığı ve askeri eğitimle ilgili bir hikaye sunan klasik bir bilim kurgu romanı.")
       print(
           "4-Ivan Sergeyeviç Turgenyev: 19. yüzyıl Rus edebiyatında yer alan bu roman, bilim kurgunun erken dönem örneklerinden biri olarak kabul edilir.")
       print(
           "5-Dan Simmons: Karmaşık karakterler ve olay örgüsüyle dolu, büyüleyici bir bilim kurgu epik serisi.")

if soru != "hikaye":
   print("lütfen doğru bir şey giriniz.")
else:
   print("lütfen doğru bir şey giriniz.")
