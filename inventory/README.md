# UTS Backend Sistem Manajemen Inventory Menggunakan Framework Django

# Deskripsi Proyek

Proyek ini adalah pengembangan aplikasi web untuk sistem manajemen inventaris barang menggunakan Django. Aplikasi ini mencakup berbagai fitur seperti pengelolaan item (CRUD), kategori, supplier, dan laporan terkait stok barang. Selain itu, proyek ini dilengkapi dengan API untuk pengelolaan data item yang dapat diakses melalui endpoint yang tersedia.

# Alur Pengerjaan Proyek

# 1. Inisialisasi Proyek
   Proyek ini dimulai dengan membuat proyek Django baru menggunakan perintah django-admin startproject inventory_system, kemudian dibuat aplikasi inventory di dalam proyek tersebut dengan menjalankan python manage.py startapp inventory. Setelah itu, aplikasi inventory ditambahkan ke dalam daftar INSTALLED_APPS pada file settings.py agar dikenali dan digunakan oleh proyek Django.

# 2. Membuat Model
   Langkah pertama dalam pengembangan sistem manajemen inventaris ini adalah mendefinisikan model-model utama, yaitu Category, Supplier, dan Item. Masing-masing model memiliki field yang relevan: Item memiliki name, category, supplier, quantity, dan price; Category hanya memiliki name; dan Supplier memiliki name serta contact_info. Setelah semua model selesai didefinisikan, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat serta menerapkan struktur tabel di database.

# 3. Membuat Admin Panel
   Untuk mempermudah pengelolaan data, saya mendaftarkan model Item, Category, dan Supplier di admin.py sehingga seluruh data dapat dikelola melalui antarmuka admin Django. Selain itu, tampilan admin untuk model Item juga disesuaikan agar lebih mudah dalam melihat dan mengelola data item secara efisien.

# 4. Membuat Views dan URL
   Membuat beberapa view untuk menangani permintaan HTTP di sisi server, seperti menampilkan daftar item, menambahkan item baru, mengedit item, dan menghapus item. Masing-masing view tersebut dihubungkan dengan URL yang relevan melalui konfigurasi di urls.py.

# 5. Menambahkan Fitur API
   Proyek dimulai dengan membuat proyek Django inventory_system dan aplikasi inventory, lalu ditambahkan ke INSTALLED_APPS. Saya membuat model Category, Supplier, dan Item, lalu melakukan migrasi database. Model-model tersebut juga didaftarkan ke admin untuk mempermudah pengelolaan data. Selanjutnya, dibuat view dan URL untuk menampilkan daftar item, menambah, mengedit, dan menghapus item. Untuk memperluas fungsionalitas, saya menambahkan API menggunakan Django REST Framework dengan ViewSet dan Serializer untuk masing-masing model. Endpoint API tersedia di /api/items/, /api/suppliers/, dan /api/categories/.

# 6. Membuat Halaman Stok Summary dan Laporan
   Membuat proyek Django inventory_system dengan aplikasi inventory, lalu mendefinisikan model Category, Supplier, dan Item. Setelah migrasi database, semua model didaftarkan ke admin. Saya juga membuat view dan URL untuk CRUD item, serta menambahkan API menggunakan Django REST Framework untuk ketiga model tersebut.Selain itu, ditambahkan fitur ringkasan stok yang menghitung total stok, rata-rata harga, total nilai stok, dan menampilkan item dengan stok rendah menggunakan Django ORM.

# 7. Menggunakan JavaScript untuk Interaksi Lebih Lanjut
   Pada tampilan daftar item, saya menambahkan JavaScript untuk menampilkan data item secara dinamis dari API. Selain itu, ditambahkan fitur hapus item menggunakan metode DELETE API tanpa perlu reload halaman.

# 8. Pengujian dan Debugging
   Setelah semua fitur selesai, saya melakukan pengujian untuk memastikan bahwa semua bagian aplikasi berjalan dengan baik, termasuk memeriksa kompatibilitas antara tampilan frontend dan backend, serta memastikan bahwa semua interaksi, seperti penghapusan item dan pembaruan stok, berfungsi dengan benar.

# 9. Penyempurnaan Tampilan dan UI/UX
   Menyesuaikan tampilan tabel pada halaman daftar item dan stok summary agar lebih mudah dibaca dan digunakan oleh pengguna, dengan membuat tampilan tabel responsif, mudah diakses, dan konsisten dengan desain sistem yang ada.

# 10. Penggunaan Docker
   Mengonfigurasi aplikasi untuk dapat dijalankan dalam container Docker, dengan menyiapkan Dockerfile dan docker-compose.yml untuk mempermudah pengelolaan dependensi dan penyebaran aplikasi, sehingga aplikasi dapat berjalan dengan lancar di berbagai sistem.

# 11. URL
1. http://127.0.0.1:8000/stock-summary/         - Menampilkan ringkasan stok.

2. http://127.0.0.1:8000/items/                 - Menampilkan daftar item.

3. http://127.0.0.1:8000/items/add/             - Menambahkan item baru.

4. http://127.0.0.1:8000/items/edit/<id item>/  - Mengedit item berdasarkan ID.

5. http://127.0.0.1:8000/api/items/             - API untuk mengelola data item.

6. http://127.0.0.1:8000/categories/            - Menampilkan daftar kategori.

7. http://127.0.0.1:8000/categories/add/        - Menambahkan kategori baru.

8. http://127.0.0.1:8000/api/categories/        - API untuk mengelola kategori.

9. http://127.0.0.1:8000/suppliers/             - Menampilkan daftar supplier.

10. http://127.0.0.1:8000/suppliers/add/        - Menambahkan supplier baru.

11. http://127.0.0.1:8000/api/suppliers/        - API untuk mengelola supplier.

12. http://127.0.0.1:8000/admin/                - Akses ke panel admin untuk mengelola data.

