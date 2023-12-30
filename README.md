# Ujian Akhir Praktikum - Machine Learning
Project ini adalah penerapan Machine Learning model - Image Classification dengan web deployment

# Overview Dataset
Project ini menggunakan dataset berupa citra berjumlah 2520, jumlah kelas 3, kelas ['paper' 'rock' 'scissors'].
![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/dataset.png?raw=true)

### Preprocessing dan Modelling
 * Preprocessing : ImageDataGenerator(rescale=1./255, rotation_range=30, width_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest', validation_split=0.2)
 * Model :
 * Menggunakan Keras untuk memuat pre-trained model VGG16 tanpa lapisan fully connected dan kemudian membekukan lapisan-lapisan konvolusional awal dengan mengatur layer.trainable = False.
sebuah model transfer learning dibangun dengan menambahkan beberapa lapisan kustom di atas base model. Lapisan-lapisan ini melibatkan operasi seperti flattening, dense layer dengan 256 neuron dan fungsi aktivasi ReLU, dropout layer dengan tingkat dropout 0.5, dan dense layer terakhir dengan fungsi aktivasi softmax sesuai dengan jumlah kelas yang diinginkan.
Model yang dihasilkan dapat digunakan untuk tugas klasifikasi gambar yang spesifik, memanfaatkan pengetahuan yang telah dipelajari oleh VGG16 pada dataset ImageNet tanpa mengubah parameter-parameter konvolusionalnya.
   * Summary Model
     * ![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/summary.png?raw=true)
   * Graph Loss dan Accuracy Model
     * ![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/history.png?raw=true)
   * Evaluation Matrix Model
     * ![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/confusion.png?raw=true)
     * ![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/report.png?raw=true)
### Predict Data
![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/predict.png?raw=true)

### Local Development
![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/index.png?raw=true)
![alt text](https://github.com/unggaputra/Web-Model-Deployment/blob/main/Asset/result.png?raw=true)
## Untuk membuat virtual environment di Python, Anda dapat mengikuti langkah-langkah berikut:
Download Semua folder pada github ini
buka folder 'model', salin link dalam file txt kemudian download filenya dan letakkan pada folder 'model'

cd \your\projct\path pada command prompt atau gunakan windows terminal pada folder project anda, dalam contoh ini berikut filepath saya D:\UMM\7-Semester\Pembelajaran Mesin\Modul 6

## Menggunakan Python dan virtualenv:
1. Install virtualenv (jika belum terinstal):
   * pip install virtualenv
2. Buat virtual environment:
   * python -m venv venv
3. Aktifkan virtual environment:
   * venv\Scripts\activate
4. Pastikan Anda berada di dalam virtual environment yang aktif, lalu instal semua paket yang diperlukan dari file requirements.txt:
   * pip install -r requirements.txt
5. Jalankan Aplikasi Flask
   * python app.py



