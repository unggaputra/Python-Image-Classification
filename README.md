# Ujian Akhir Praktikum - Machine Learning
Project ini adalah penerapan Machine Learning model - Image Classification dengan web deployment

# Overview Dataset
Project ini menggunakan dataset berupa citra berjumlah 2520, jumlah kelas 3, kelas ['paper' 'rock' 'scissors'].
https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/dataset.png?raw=true
## Model
Menggunakan Keras untuk memuat pre-trained model VGG16 tanpa lapisan fully connected dan kemudian membekukan lapisan-lapisan konvolusional awal dengan mengatur layer.trainable = False.
sebuah model transfer learning dibangun dengan menambahkan beberapa lapisan kustom di atas base model. Lapisan-lapisan ini melibatkan operasi seperti flattening, dense layer dengan 256 neuron dan fungsi aktivasi ReLU, dropout layer dengan tingkat dropout 0.5, dan dense layer terakhir dengan fungsi aktivasi softmax sesuai dengan jumlah kelas yang diinginkan.
Model yang dihasilkan dapat digunakan untuk tugas klasifikasi gambar yang spesifik, memanfaatkan pengetahuan yang telah dipelajari oleh VGG16 pada dataset ImageNet tanpa mengubah parameter-parameter konvolusionalnya.


buka folder 'model', download filenya dan letakkan pada folder 'model'

# Untuk membuat virtual environment di Python atau Anaconda Python, Anda dapat mengikuti langkah-langkah berikut:

cd \your\projct\path

## Menggunakan Python dan virtualenv:
1. Install virtualenv (jika belum terinstal):
   ### pip install virtualenv
   
2. Buat virtual environment:
   ### Untuk Python 3
   ### python -m venv venv
   
3. Aktifkan virtual environment:
   ### venv\Scripts\activate

4. Pastikan Anda berada di dalam virtual environment yang aktif, lalu instal semua paket yang diperlukan dari file requirements.txt:
   ### pip install -r requirements.txt

5. Jalankan Aplikasi Flask
   ### python app.py



