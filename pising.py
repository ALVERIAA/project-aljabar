from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

# Dataset email
emails = [
    "Klik link ini untuk mendapatkan hadiah",
    "Verifikasi akun anda sekarang",
    "Meeting besok jam 10 pagi",
    "Laporan tugas telah dikirim",
    "Dapatkan uang gratis sekarang",
    "Password anda harus segera diperbarui"
]

print("Dataset Email:")
for i, email in enumerate(emails):
    print(f"{i+1}. {email}")

labels = [1,1,0,0,1,1]

# Vektorisasi
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

print("\nMatriks Data:")
print(X.toarray())

# Model SVM
model = SVC(kernel='linear')

# Training
model.fit(X, labels)

# Email baru
test_email = [
    "Klik link berikut untuk verifikasi password anda",
    "verifikasi akun anda sekarang",
    "meeting besok jam 10 pagi",
    "laporan tugas telah dikirim",
    "dapatkan uang gratis sekarang",
    "password anda harus segera diperbarui"
]

# Ubah jadi vektor
test_vector = vectorizer.transform(test_email)

# Prediksi
prediction = model.predict(test_vector)

print("\nHASIL DETEKSI EMAIL")
print("-"*40)

for i, email in enumerate(test_email):

    print(f"\nEmail {i+1}:")
    print(email)

    if prediction[i] == 1:
        print("Status: PHISHING")
    else:
        print("Status: NORMAL")