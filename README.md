__Rama__ __Aditya__ __Rifki__ __Harmono__ __(2306165502)__
# TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

- Untuk membuat proyek Django baru, saya membuat sebuah directory baru bernama jersey di local. Setelah itu, saya membuka terminal pada directory tersebut dan membuat virtual environment baru serta mengaktifkannya. Sebelum membuat Django, saya membuat dependencies melalui sebuah file bernama requirements.txt (berbeda dengan tutorial, saya menambahkan package Pillow) lalu baru di instalasi. Setelah selesai instalasi, saya baru membuat proyek Django yang saya namakan jersey. Setelah terbentuk proyek baru saya merubah pengaturan Allowed Host untuk keperluan deployment baru setelahnya saya test run. 
- Kemudian saya upload semua progress perubahan melalui platform GitHub. Saya membuat repository kemudian menginisiasi git init di directory jersey. Setelah itu, sebelum melakukan command berikutnya, perlu membuat berkas .gitignore untuk tidak membaca beberapa file yang akan diunggah ke GitHub. Kemudian, saya membuat sebuah berkas README.md yang berisi tulisan yang akan diupload. Setelahnya, saya melakukan command git add, commit, dan push untuk mengunggahnya ke GitHub. 
- Untuk tahap selanjutnya, yaitu membuat aplikasi baru bernama main, saya melakukan command startapp dan menambahkan aplikasi ke dalam pengaturan proyek jersey, tepatnya di bagian installed apps. Kemudian akan terbentuk sebuah subdirektori yang di dalamnya terdapat berkas-berkas seperti admin.py, apps.py, models.py, test.py, urls.py, views.py, __pycache__, dan subdirektori migrations. Kemudian saya juga menambahkan subdirektori templates untuk menerapkan MVT isinya berupa berkas html (saya membuat dua yaitu base.html dan main.html).
- Kemudian saya membuat sebuah class dengan nama Jersey di berkas models.py tetap pada aplikasi main. Saya juga mengimport module models sebagai kelas dasar. Pada class ini, saya mendeklarasikan beberapa atribut sebagai item yang saya inginkan berada dalam web nantinya. Atribut tersebut berupa name sebagai nama produk (dengan data fields CharField sepanjang 255), price sebagai harga produk (dengan data fields IntegerField), description (dengan data fields TextField), image sebagai foto produk berformat .jpg (dengan data fields CharFields sepanjang 2083), dan quantity sebagai jumlah stok (dengan data fields IntegerField). Untuk menyimpan model saya menjalankan command makemigrations untuk membuat berkas migration yang belum diaplikasikan. Kemudian saya aplikasikan perubahan model ke database dengan menjalankan command migrate.
- Karena saya ingin menginput banyak produk pada web dan menghindari redundan, saya menghindari input atribut secara manual. Saya menambahkan class pada admin.py yang mengimport admin, disini saya menambahkan sebuah tuple yang berisi atribut yang dapat diisi di web admin nantinya. Kemudian, saya mendaftarkan diri sebagai admin dengan command createsuperuser. Lalu, menuju ke urls.py dari proyek (jersey) dan melakukan import path. Berikutnya, perlu menambahkan kode di urlpattern dengan memanggil fungsi path yang didalamnya memuat admin/.Setelah perintah itu, saya dapat mengakses web admin dan input item di admin. Pada views.py, saya membuat sebuah function show_main yang mereturn render ke berkas main.html menggunakan data yang telah ditambahkan melalui web admin. Fungsi render memiliki 3 argumen yaitu request (objek request dari user), berkas main.html, dan dictionary berisi data yang telah diinput admin. Kemudian, saya akan mengisi subdirektori template dengan tulisan yang saya inginkan untuk dikeluarkan dengan hanya memberi tanda {{ nama atribut }} yang di loop. Di template juga saya membuat 2 berkas, agar satu berkas difokuskan untuk design (button dan layout) dan judul website yaitu base.html. Sedangkan untuk main.html, saya fokuskan untuk penempatan atribut. Saya dibantu oleh template dari website BootStrap dalam pengerjaan berkas html ini. 
- Setelah mengisi bagan views.py, sekarang saatnya membuat routing pada urls.py di aplikasi main untuk mengatur rute URL yang terkait dengan aplikasi. Disini saya mengimpor fungsi path dan juga show_main dari views.py sebelumnya. Kemudian saya mendeklarasikan nama unik pada pola URL dan juga sebuah urlpattern dengan memanggil fungsi path yang telah diimpor dan berargumen string kosong dengan fungsi show_main. Setelah selesai, perlu menghubungkan URL proyek (jersey) dan aplikasi (main) dengan import include menambahkan kode di urlpattern, panggil fungsi path dengan memanggil fungsi include didalamnya yang memuat main.urls (urls.py dari main). 
- Sampai titik ini web sudah siap untuk di deploy, berikutnya perlu melakukan deployment ke PWS. Saya kemudian membuat proyek baru dengan Create New Project di site PWS. Setelahnya, saya perlu ke settings.py pada proyek (jersey) dan menambahkan kode URL deployment di Allowed Host. Kemudian, saya melakukan command git add, commit, dan push ke repository GitHub. Setelahnya kredensial unik akan di request dan langkah selanjutnya yaitu melakukan branching ke master dan command push ke PWS master. Terakhir, perlu melakukan branching kembali ke main dan menunggu build running di PWS. Web telah ready di deploy melalui button View Project di PWS.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 
urls.py, views.py, models.py, dan berkas html.

![Alt text](<Screenshot 2024-09-11 at 03.48.28.png>)

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git merupakan tools yang sangat bermanfaat bagi programmer dalam melakukan pelacakan perubahan kode. Dengan adanya git, programmer dapat mengembangkan software secara kolaboratif atau bersamaan. Selain itu, git juga berguna untuk melihat progress yang telah dilakukan selama pengerjaan pemrograman. Git juga menyediakan riwayat perubahan, ini berarti programmer dapat melakukan recovery proyek ke versi sebelumnya.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan permulaan pembelajaran software development karena framework ini mudah untuk digunakan bagi pemula. Selain itu, Django juga menyediakan banyak fitur bawaan sehingga mempermudah bagi pengembangan dan memfasiltasi proses update data secara berkala bagi user. Terakhir, Django memiliki dokumentasi yang lengkap yang berarti mempermudah para programmer pemula untuk memahami lebih cepat.

5. Mengapa model pada Django disebut sebagai ORM?

Karena model Django menghubungkan objek Python ke tabel dalam database relasional. Pengembang dapat berinteraksi dengan database menggunakan kode Python. Ini menghindari penulisan SQL dan memungkinkan pengelolaan data yang efektif melalui pemetaan objek ke format tabel.

__Link__ __Deployment:__
Tautan PWS: http://rama-aditya31-jerseyku.pbp.cs.ui.ac.id // Tautan Vercel: https://jersey-lxa7.vercel.app

# TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery sangat penting dalam pengimplementasian sebuah platform, hal ini dikarenakan data delivery berguna untuk meningkatkan efisiensi dengan memastikan bahwa data yang diperlukan oleh user atau aplikasi tersedia secara tepat waktu dan dalam format yang sesuai. Data delivery memungkinkan sinkronisasi data secara real-time, pemrosesan data, dan komunikasi yang efisien antara sistem yang berbeda, mendukung fungsionalitas aplikasi.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut pendapat saya, keduanya memiliki kegunaan yang sama-sama bermanfaat, namun jika dilihat dari kacamata pribadi, JSON lebih baik. Hal ini karena syntax atau format yang dimiliki oleh JSON dapat lebih mudah untuk dibaca. JSON lebih populer karena strukturnya yang lebih sederhana dan efisien dalam hal penggunaan bandwidth dan kecepatan parsing dibanding XML yang lebih kompleks.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada platform Django digunakan untuk memvalidasi data yang diberikan pada form valid atau tidak. Apabila data valid, method is_valid() akan mengembalikan nilai `True` sehingga bisa mengakses data yang sudah bersih. Sebaliknya, apabila data tidak valid, method is_valid() akan mengembalikan nilai `False` dan bisa mendapatkan pesan kesalahan yang spesifik. Method ini diperlukan untuk memastikan data yang masuk sesuai dengan ketentuan yang diterapkan dan menjaga keamanan serta mencegah kesalahan yang lebih banyak.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` digunakan untuk kegunaan sekuritas dari segala bentuk serangan yang dapat terjadi seperti serangan CSRF (Cross-Site Request Forgery). Ini dapat dieksploitasi oleh penyerang untuk melakukan aksi tanpa sepengetahuan pengguna. Tanpa adanya `csrf_token`, penyerang bisa memalsukan permintaan ke server dan mengambil alih sesi pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

a. Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Pertama, saya membuat sebuah berkas baru bernama forms.py di direktori aplikasi (main), kemudian membuat fungsi bernama JerseyForm. Di dalam fungsi tersebut, terdapat dua variabel, yaitu model dan fields. Model akan digunakan untuk menunjukkan model yang akan digunakan untuk form. Fields akan menunjukkan field dari model items yang dimiliki.
- Mengimport yang akan digunakan pada views.py yang berada pada direktori main. 
![Alt text](<Screenshot 2024-09-18 at 02.15.42.png>)
- Membuat fungsi baru yang bernama add_jersey pada views.py yang akan digunakan untuk mengelola input form. Dalam function ini, form JerseyForm diisi dengan data dari request.POST dan akan dilakukan pengecekan. Jika valid, data akan disimpan dan pengguna akan diarahkan kembali ke halaman utama.
- Import NewJersey dari models.py ke berkas views.py dan tambahkan NewJersey pada fungsi show_main di berkas views.py.
- Dalam berkas views.py saya menambahkan variabel items yang akan digunakan untuk mengambil semua item yang ada pada database.
- Buka urls.py dan import fungsi add_jersey yang berasal dari views.py
- Kemudian, saya menambahkan path('add-jersey', add_jersey, name='add_jersey'), pada urlpatterns yang ada di urls.py untuk mengakses fungsi yang sudah diimport sebelumnya.
- Selanjutnya saya membuat file html add_jersey.html pada subdirektori templates yang ada pada direktori main dengan isi:
![Alt text](<Screenshot 2024-09-18 at 02.10.16.png>)

b. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Pertama, buat fungsi show_xml dalam views.py dan menambahkan path URL. Fungsi ini akan mengambil data Item dan mengembalikannya dalam format XML.
- Kemudian, buat fungsi show_json dalam views.py dan menambahkan path URL. Fungsi ini mengambil data Item dan mengembalikannya dalam format JSON.
- Lalu, buat fungsi show_xml_by_id dalam views.py dan menambahkan path URL. Fungsi ini mengambil data Item berdasarkan ID yang disediakan dan mengembalikannya dalam format XML.
- Terakhir, buat fungsi show_json_by_id dalam views.py dan menambahkan path URL. Fungsi ini mengambil data Item berdasarkan ID yang disediakan dan mengembalikannya dalam format JSON

c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Import beberapa function ke urls.py yang ada di folder main yaitu show_xml, show_json, show_xml_by_id, show_json_by_id.
- Saya menambahkan path url ke dalam urlpatterns
![Alt text](<Screenshot 2024-09-18 at 01.55.14-1.png>)

d. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- Mengakses XML
![Alt text](<Screenshot 2024-09-17 at 00.58.57.png>)
- Mengakses JSON
![Alt text](<Screenshot 2024-09-17 at 00.59.18.png>)
- Mengakses XML by ID
![Alt text](<Screenshot 2024-09-17 at 01.01.07.png>)
- Mengakses JSON by ID
![Alt text](<Screenshot 2024-09-17 at 01.00.56.png>)

e. Melakukan add-commit-push ke GitHub.
![Alt text](<Screenshot 2024-09-18 at 02.14.08.png>)
