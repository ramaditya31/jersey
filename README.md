1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Untuk membuat proyek Django baru, saya membuat sebuah directory baru bernama jersey di local. Setelah itu, saya membuka terminal pada directory tersebut dan membuat virtual environment baru serta mengaktifkannya. Sebelum membuat Django, saya membuat dependencies melalui sebuah file bernama requirements.txt (berbeda dengan tutorial, saya menambahkan package Pillow) lalu baru di instalasi. Setelah selesai instalasi, saya baru membuat proyek Django yang saya namakan jersey. Setelah terbentuk proyek baru saya merubah pengaturan Allowed Host untuk keperluan deployment baru setelahnya saya test run. 
- Untuk tahap selanjutnya, yaitu membuat aplikasi baru bernama main, saya melakukan command startapp dan menambahkan aplikasi ke dalam pengaturan proyek jersey, tepatnya di bagian installed apps. Kemudian akan terbentuk sebuah subdirektori yang di dalamnya terdapat berkas-berkas seperti admin.py, apps.py, models.py, test.py, urls.py, views.py, __pycache__, dan subdirektori migrations. Kemudian saya juga menambahkan subdirektori templates untuk menerapkan MVT isinya berupa berkas html (saya membuat dua yaitu base.html dan main.html).
- 
- Kemudian saya membuat sebuah class dengan nama Jersey di berkas models.py tetap pada aplikasi main. Saya juga mengimport module models sebagai kelas dasar. Pada class ini, saya mendeklarasikan beberapa atribut sebagai item yang saya inginkan berada dalam web nantinya. Atribut tersebut berupa name sebagai nama produk (dengan data fields CharField sepanjang 255), price sebagai harga produk (dengan data fields IntegerField), description (dengan data fields TextField), image sebagai foto produk (dengan data fields CharFields sepanjang 2083), dan quantity sebagai jumlah stok (dengan data fields IntegerField). Untuk menyimpan model saya menjalankan command makemigrations untuk membuat berkas migration yang belum diaplikasikan. Kemudian saya aplikasikan perubahan model ke database dengan menjalankan command migrate.
- 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 
urls.py, views.py, models.py, dan berkas html.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

5. Mengapa model pada Django disebut sebagai ORM?

Tautan PWS: 