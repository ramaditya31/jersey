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


# TUGAS 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
- **HttpResponseRedirect()** adalah subclass dari HttpResponse yang digunakan untuk mengirimkan respons pengalihan (redirect) ke pengguna. Fungsi ini secara khusus mengarahkan pengguna ke URL tertentu dengan menghasilkan HttpResponse. Sedangkan **redirect()** adalah fungsi pendek yang lebih mudah digunakan dan fleksibel untuk mengatur pengalihan. Fungsi ini memungkinkan pengalihan dilakukan tanpa perlu menentukan URL secara langsung, terutama saat menggunakan nama view atau objek sebagai parameternya.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model NewJersey dengan model User dilakukan menggunakan field ForeignKey. Variabel user menyambungkan ke model User dari Django yang memungkinkan setiap penambahan barang disambungkan dengan user yang terdaftar. on_delete_models.CASCADE berfungsi apabila pengguna dihapus, maka semua input barang yang tersambung dengan user tersebut juga akan terhapus secara otomatis. 

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication dan authorization adalah dua konsep kunci dalam keamanan aplikasi web. Authentication memverifikasi identitas pengguna, biasanya saat login dengan username dan password. Authorization menentukan hak akses pengguna setelah terverifikasi, seperti apa yang bisa mereka lihat atau lakukan dalam sistem. Di Django, authentication diatur melalui form login dan backend otentikasi, sedangkan authorization dikelola melalui izin yang dapat diatur pada pengguna atau grup.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan sesi (session) untuk mengingat pengguna yang sudah login. Setelah berhasil login, Django menyimpan informasi sesi di server, sementara browser menyimpan session ID dalam cookie. Pada permintaan berikutnya, browser mengirim cookie tersebut agar Django bisa mengenali pengguna tanpa perlu login ulang. Selain untuk session ID, cookies juga digunakan untuk menyimpan preferensi pengguna, melacak keranjang belanja, atau analitik. Namun, cookies bisa rentan, sehingga Django menyediakan pengaturan seperti HttpOnly untuk mencegah akses melalui JavaScript dan Secure untuk memastikan cookie hanya dikirim lewat HTTPS.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Mengimplenentasikan fungsi registrasi, login, dan logout.

Fungsi Register

a. Mengimport redirect, UserCreationForm, dan messages pada file views.py yang ada pada direktori main.
b. Membuat fungsi register pada views.py untuk form registrasi dan menghasilkan akun baru ketika data disubmit dari form.
c. Membuat file register.html pada main/templates untuk membuat interface saat ingin membuat akun.
d. Mengimport fungsi register ke urls.py yang ada di direktori main.
e. Menambahkan path URL untuk register pada urls.py

Fungsi Login

a. Mengimport authenticate dan login pada file views.py yang ada pada direktori main.
b. Membuat fungsi login_user pada views.py untuk mengautentikasi user yang akan login.
c. Membuat file login.html pada main/templates untuk membuat interface saat pengguna ingin login.
d. Mengimport fungsi login_user ke urls.py yang ada di direktori main.
e. Menambahkan path URL untuk login_user pada urls.py

Fungsi Logout

a. Import logout pada file views.py yang ada pada di direktori main.
b. Membuat fungsi logout_user pada views.py untuk mengautentikas user yang ingin melakukan logout.
c. Menambahkan button logout pada templates/main.html.
d. Mengimport fungsi logout_user ke urls.py yang ada di direktori main.
e. Menambahkan path URL untuk logout_user pada urls.py.

- Menghubungkan model Product dengan User.

a. Import User pada file models.py.
b. Menambahkan ForeignKey pada model di file models.py untuk menghubungkan barang dengan user.
c. Ubah fungsi add_jersey yang ada pada views.py.
d. Menambahkan parameter commit = False pada variable add_form yang berfungsi agar Django tidak langsung menyimpan objek ke database.
e. Isi field user dengan objek User dari return value request.user untuk menandakan bahwa objek tersebut dimiliki pengguna yang sedang login.

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
![Alt text](<Screenshot 2024-09-25 at 03.14.30.png>)
![Alt text](<Screenshot 2024-09-25 at 03.14.33.png>)
![Alt text](<Screenshot 2024-09-25 at 03.22.39.png>)
![Alt text](<Screenshot 2024-09-25 at 03.22.42.png>)


- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
a. Mengimport HttpResponseRedirect, reverse, dan datetime pada file models.py.
b. Menambahkan kode pada fungsi login_user untuk melihat status last_login.
1. Edit blok if user is not None dengan menambahkan kode berikut:
login(request, user)
response = HttpResponseRedirect(reverse("main:show_main))
response.set_cookie('last_login', str(datetime.datetime.now()))
return response
2. Pada fungsi show_main tambahkan 'last_login': request.COOKIES['last_login'] pada variabel context.
3. Ubah fungsi logout_user dengan menambahkan kode:
response = HttpResponseRedirect(reverse('main:login'))
response.delete_cookie('last_login')
return response
4. Pada file main.html tambahkan kode <h5>Sesi terakhir login: {{ last_login }}</h5> untuk menampilkan kapan user terakhir login.

- Melakukan add-commit-push ke GitHub.
![Alt text](<Screenshot 2024-09-25 at 03.34.45.png>)

# TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas pengambilan CSS selector adalah sebagai berikut:
a. Inline Styles: Gaya yang ditulis langsung pada elemen HTML menggunakan atribut `style` memiliki prioritas tertinggi. Misalnya: `<div style="color: red;">`.
b. ID Selector:Selector yang menggunakan ID HTML, ditandai dengan `#`, memiliki prioritas lebih tinggi daripada class, attribute, atau element selector. Misalnya: `#header`.
c. Class, Pseudo-class, dan Attribute Selector: Selector yang menggunakan class (misalnya `.class-name`), pseudo-class (misalnya `:hover`), atau attribute selector (misalnya `[type="text"]`) berada di urutan berikutnya dalam hal prioritas.
d. Element dan Pseudo-element Selector: Selector berdasarkan nama elemen HTML (misalnya `div`, `p`) atau pseudo-element (misalnya `::before`, `::after`) memiliki prioritas yang paling rendah.
e. Universal Selector (`*`) dan Inheritance: Selector universal (`*`) dan aturan CSS yang diwariskan dari elemen induk tidak memiliki prioritas tinggi, tetapi tetap berlaku jika tidak ada gaya lain yang lebih spesifik.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsi situs atau aplikasi beradaptasi dengan berbagai ukuran layar dan perangkat (desktop, tablet, smartphone). Dengan semakin banyaknya pengguna yang mengakses web melalui perangkat mobile, responsive design memastikan pengalaman pengguna yang optimal di semua perangkat, meningkatkan aksesibilitas, keterbacaan, dan navigasi. Contoh aplikasi yang sudah menerapkan responsive design adalah Twitter, tampilannya menyesuaikan di berbagai perangkat, memberikan pengalaman konsisten di desktop dan mobile. Contoh aplikasi yang belum menerapkan responsive design adalah Old CraigList.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin adalah ruang di luar elemen, yang mempengaruhi seberapa jauh elemen tersebut dari elemen lain. Margin diatur menggunakan properti `margin`, dengan nilai bisa diterapkan secara individual (atas, kanan, bawah, kiri) atau sekaligus.
- Border adalah ruang yang disekitar elemen atau garis yang membungkus padding. Border diatur menggunakan properti `border`, dengan nilai seperti `border-width`, `border-style`, dan `border-color`.
- Padding adalah ruang di dalam elemen, yang mempengaruhi seberapa jauh konten dari tepi elemen. Padding diatur menggunakan properti `padding`, serupa dengan margin, bisa diterapkan untuk tiap sisi atau sekaligus.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

a. Flexbox
Flexbox adalah metode layout CSS yang dirancang untuk menyusun elemen dalam satu dimensi, baik secara horizontal (baris) atau vertikal (kolom). Flexbox memudahkan pengaturan posisi, ukuran, dan distribusi ruang antar elemen dalam sebuah kontainer, tanpa bergantung pada ukuran tetap atau posisi manual. Flexbox, untuk satu dimensi (baris atau kolom), cocok untuk elemen dalam satu garis.

b. Grid Layout
Grid layout adalah metode layout dua dimensi yang memungkinkan kita membuat tata letak yang lebih kompleks, baik secara horizontal maupun vertikal. Grid memungkinkan untuk membuat layout berbasis baris dan kolom secara bersamaan, dengan kontrol penuh terhadap elemen-elemen yang ada di dalam grid. Grid layout, untuk dua dimensi (baris dan kolom), cocok untuk tata letak halaman yang lebih kompleks.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Implementasikan fungsi untuk menghapus dan mengedit product.
a. Membuat fungsi baru bernama edit_jersey dan delete_jersey yang menerima parameter request dan id:

def edit_jersey(request, id):
    # Get new jersey berdasarkan id
    jersey = NewJersey.objects.get(pk = id)

    # Set new jersey sebagai instance dari form
    form = JerseyForm(request.POST or None, instance=jersey)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_jersey.html", context)

def delete_jersey(request, id):
    # Get mood berdasarkan id
    jersey = NewJersey.objects.get(pk = id)
    # Hapus mood
    jersey.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

b. Menambahkan import reverse pada views.py:

from django.shortcuts import .., reverse

c. Membuat berkas HTML baru dengan nama edit_jersey.html pada subdirektori main/templates.

{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Jersey</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Jersey"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}

d. Mengimport fungsi edit_jersey dan delete_jersey ke urls.py

from main.views import edit_jersey, delete_jersey

e. Menambahkan path url ke urlpatterns:

path('edit-jersey/<uuid:id>/', edit_jersey, name='edit_jersey'),
path('delete-jersey/<uuid:id>/', delete_jersey, name='delete_jersey')

f. Menambahkan kode ke main.html di card

<div class="card-body text-center">
    <a href="{% url 'main:edit_jersey' jersey.pk %}" class="btn btn-sm btn-warning">Edit</a>
    <a href="{% url 'main:delete_jersey' jersey.pk %}" class="btn btn-sm btn-danger">Delete</a>
</div>


- Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework Bootstrap dengan ketentuan sebagai berikut:

a. Halaman Login:
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="container-fluid">
  <div class="row vh-100">
    <div class="col-md-6 p-0">
      <img src="{% static 'image/legend.jpeg' %}" alt="background" class="img-fluid h-100 w-100" style="object-fit: cover;">
    </div>

    <div class="col-md-6 d-flex flex-column align-items-center justify-content-center">
      <div class="text-center mb-4">
        <h1 class="site-title">JERSEYKU .</h1>
      </div>

      <div class="login shadow-lg p-4">
        <h3 class="mb-4">Login</h3>

        <form method="POST" action="">
          {% csrf_token %}
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" id="username" name="username" class="form-control rounded-pill" placeholder="Enter your username" required>
          </div>
          
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" name="password" class="form-control rounded-pill" placeholder="Enter your password" required>
          </div>
          
          <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary btn-block rounded-pill login_btn">Enter</button>
          </div>
        </form>

        {% if messages %}
        <ul class="mt-3">
          {% for message in messages %}
          <li class="alert alert-info">{{ message }}</li>
          {% endfor %}
        </ul>
        {% endif %}
        
        <div class="mt-3 text-center">
          <p class="text-muted">Don't have an account yet? 
            <a href="{% url 'main:register' %}" class="text-primary text-decoration">Register Now</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
    body {
        background-color: #eae5e0;
    }

    .login {
        background-color: white;
        border-radius: 15px;
        max-width: 400px;
        width: 100%;
        padding: 30px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1); 
    }
    
    .site-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #333;
        text-align: center;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        margin-bottom: 20px;
    }

    .login h3 {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        text-align: center;
        font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    .form-control {
        padding: 12px 20px;
        border: 1px solid #ced4da;
        border-radius: 50px;
        background-color: #f9f9f9;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .form-control:focus {
        border-color: #717c31;
        box-shadow: 0 0 10px rgba(0, 123, 255, 0.2);
        background-color: white;
    }

    .form-label {
        margin-top: 10px;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    .login_btn {
        font-size: 1.2rem;
        padding: 10px 0;
        background-color: #8b1a1a;
        border: none;
        color: white;
        border-radius: 50px;
        transition: background-color 0.3s ease;
        font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    .login_btn:hover {
        background-color: rgb(82, 12, 12);
    }

    .text-muted {
        font-size: 0.9rem;
        font-variant: small-caps;
    }
</style>

{% endblock content %}

b. Halaman Register
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="container d-flex align-items-center justify-content-center min-vh-100">
  <div class="col-lg-6 col-md-8 col-sm-10">
    <div class="card shadow-lg p-4">
      <div class="card-body">
        <h2 class="text-center title text-dark">
          Create your account
        </h2>
        <form method="POST" class="d-flex flex-column align-items-center">
          {% csrf_token %}
          <div class="mb-3 w-75">
            {% for field in form %}
              <div class="form-group w-100 text-center">
                <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
                <div class="input-group justify-content-center">
                  {{ field }}
                  {% if field.errors %}
                    <div class="input-group-append">
                      <span class="input-group-text bg-danger text-white">
                        <i class="fas fa-exclamation-triangle"></i>
                      </span>
                    </div>
                  {% endif %}
                </div>
                {% if field.errors %}
                  {% for error in field.errors %}
                    <div class="text-danger small mt-1">{{ error }}</div>
                  {% endfor %}
                {% endif %}
              </div>
            {% endfor %}
          </div>

          <div class="d-grid w-50">
            <button type="submit" class="btn btn-primary btn-block large-btn">
              Register
            </button>
          </div>
        </form>

        {% if messages %}
        <div class="mt-4">
          {% for message in messages %}
          <div class="alert alert-danger" role="alert">
            {{ message }}
          </div>
          {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
          <p class="text-dark">
            Already have an account?
            <a href="{% url 'main:login' %}" class="text-primary">
              Login here
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
    body {
    background-color: #eae5e0;
     }
     
    .min-vh-100 {
        min-height: 100vh;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }

    .card {
        border-radius: 20px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }

    .title {
        font-weight: bold;
        color: #333;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
        padding: 20px;
    }

    .form-group {
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .form-control {
        width: 75%;
        margin: 0 auto;
        border-radius: 50px;
        padding: 10px;
        text-align: center;
    }
    
    .large-btn {
        border-radius: 50px;
        padding: 15px;
        font-size: 1.25rem;
        font-weight: bold;
        background-color: #8b1a1a;
        border: none;
        width: 100%;
    }

    .large-btn:hover {
        background-color: rgb(82, 12, 12);
    }

    .d-grid {
        display: grid;
        place-items: center;
    }

    .mt-4 {
        margin-top: 1.5rem;
        text-transform: uppercase;
    }
</style>

{% endblock content %}

c. Halaman Add Product:
{% extends 'base.html' %}

{% block content %}
{% include 'navbar.html' %}

<div class="container d-flex align-items-center justify-content-center min-vh-100" style="margin-top: 50px;">
  <div class="col-lg-5 col-md-7 col-sm-10">
    <div class="card shadow-lg p-4" style="max-width: 500px; width: 100%; margin: auto;">
      <div class="card-body">
        <h2 class="text-center title text-dark">
          Add Jersey
        </h2>
        <form method="POST" class="w-100">
          {% csrf_token %}
          <div class="form-group mb-3">
            {{ form.as_p }}
          </div>

          <div class="d-grid">
            <button type="submit" class="btn btn-primary btn-block large-btn">Add Jersey</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>

<style>
  body {
    background-color: #eae5e0;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  .min-vh-100 {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card {
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 500px; /* Batasi lebar form */
    margin: 0 auto;
    padding: 20px;
  }

  .title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 20px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  .form-group {
    width: 100%;
  }

  .form-control {
    border-radius: 5px;
    padding: 10px;
    font-size: 1rem;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  .btn {
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: bold;
    background-color: #8b1a1a;
    color: white;
    border: none;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  }

  .btn:hover {
    background-color: rgb(82, 12, 12);
  }

  .btn-block {
    display: block;
    width: 100%;
  }

  @media (max-width: 768px) {
    .title {
      font-size: 1.25rem;
    }

    .form-control {
      font-size: 0.9rem;
    }

    .btn {
      font-size: 0.9rem;
    }
  }

  @media (max-width: 576px) {
    .title {
      font-size: 1.1rem;
    }

    .form-control {
      font-size: 0.85rem;
    }

    .btn {
      font-size: 0.85rem;
    }
  }
</style>

{% endblock content %}

d. Halaman Navbar:
<nav class="navbar navbar-expand-lg navbar-light fixed-top">
  <div class="container">
    <a class="navbar-brand" href="#">JERSEYKU .</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#carouselExampleIndicators">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#catalogue-section">Catalogue</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Welcome, {{ user.username }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link logout-link" href="{% url 'main:logout' %}">Logout</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<style>
body {
  font-family: 'Poppins', sans-serif;
}

.navbar {
  background: linear-gradient(
    to bottom,
    #8b1a1a 5%, 
    #d3b89c 5% 10%, 
    #4b5320 10% 90%, 
    #d3b89c 90% 95%, 
    #8b1a1a 95% 100% 
  );
}

.navbar-light .navbar-brand {
  color: #fff;
  font-size: 25px;
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 2px;
}

.navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .show > .nav-link {
  color: #fff;
}

.navbar-light .navbar-nav .nav-link {
  color: #fff;
}

.navbar-toggler {
  background: #fff;
}

.navbar-nav {
  text-align: center;
}

.nav-link {
  padding: .2rem 1rem;
}

.nav-link.active,.nav-link:focus{
  color: #fff;
}

.navbar-toggler {
  padding: 1px 5px;
  font-size: 18px;
  line-height: 0.3;
}

.navbar-light .navbar-nav .nav-link:focus, .navbar-light .navbar-nav .nav-link:hover {
  color: #fff;
}

.nav-item{
  font-family: 'Poppins', sans-serif;
  margin-right: 20px;
  text-transform: uppercase;
  font-size: 12px;
}

.logout-link {
  border: 2px;
  border-radius: 10px; 
  background-color: #8b1a1a;
  color: white;
}

.logout-link:hover {
  background-color: #701212;
}

.link-area
{
  position:fixed;
  bottom:20px;
  left:20px;  
  padding:15px;
  border-radius:40px;
  background:tomato;
}
.link-area a
{
  text-decoration:none;
  color:#fff;
  font-size:25px;
}
</style>

<script>
          

</script>