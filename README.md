## OpenGov

OpenGov merupakan kependekan dari Open Goverment yang akan di dedikasikan kepada Negara Indonesia untuk mewujudkan Open Data. Repository ini adalah main project untuk menjalan aplikasi Open Goverment lainnya seperti:

1. [E-Budgeting](https://github.com/OpenGovermentID/ogi-budgeting)
2. [E-Procurement](https://github.com/OpenGovermentID/ogi-procurement)
3. [E-Catalogue](https://github.com/OpenGovermentID/ogi-catalogue)
4. [E-Purchasing](https://github.com/OpenGovermentID/ogi-purchasing)
5. [E-Audit](https://github.com/OpenGovermentID/ogi-eaudit)
6. [E-Survey](https://github.com/OpenGovermentID/ogi-esurvey)
7. [E-Healt](https://github.com/OpenGovermentID/ogi-ehealt)

OpenGov ini dibuat menggunakan framework [django](http://www.djangoproject.com)


## Berkontribusi

Untuk berkontribusi dalam pengembangan aplikasi Open Goverment ini, pengembang harus memiliki kemampuan menggunakan Djangoframework dan mengoprasikan sistem operasi berbasi Linux/Unix untuk mempermudah dalam melakukan pengembangan. Untuk memulai mendevelop aplikasi, ikuti langkah-langkah sebagai berikut.

### Persiapan main project

1. Clone aplikasi opengov ini
2. Membuat virtualenv 
3. Instalasi paket yang dibutuhkan opengov, caranya `pip install -r requirements/base.txt`
4. lakukan perintah ini ./manage.py sycndb

### Persiapan berkontribusi di aplikasi

1. Clone salah satu aplikasi yang ada di repostiry ini.
2. Tempatkan aplikasi pada direcrtory yang berbeda
3. Buat symbolic link dengan perintah `ln -s aplikasi opengov/aplikasi` disarankan nama symbolic link harus sama dengan nama aplikasi.
4. Lakukan perintah ini `./manage.py migrate namaaplikasi`
5. Lakukan perintah `compass compile static` untuk meng extraksi stylesheet

Jika anda sudah pernah berkontribusi, silahkan pull terlebih dahulu pada masing-masing aplikasi.
