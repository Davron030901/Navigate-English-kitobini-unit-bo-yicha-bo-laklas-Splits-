# 📚 PDF Unit Bo'lish Dasturi

Bu dastur **Coursebook** va **Workbook** PDF fayllarini individual unitlarga bo'lish uchun mo'ljallangan. Dastur ham terminal orqali, ham web interfeys orqali ishlatilishi mumkin.

## 🌟 Xususiyatlar

- ✅ **Coursebook.pdf** ni 60 ta unitga bo'lish (12 ta unit × 5 ta lesson)
- ✅ **Workbook.pdf** ni 49 ta unitga bo'lish  
- ✅ **Web interfeys** - drag & drop bilan foydalanish
- ✅ **Batch yuklab olish** - barcha unitlarni ZIP qilib
- ✅ **Individual yuklab olish** - har bir unitni alohida
- ✅ **Progress tracking** - jarayon ko'rsatkichi
- ✅ **Responsive dizayn** - mobil qurilmalarda ishlaydi
- ✅ **Dark/Light mode** - mavzu almashish

## 🚀 O'rnatish va Ishga Tushirish

### 1. Repository ni klonlash
```bash
git clone <repository-url>
cd Dars
```

### 2. Virtual environment yaratish
```bash
python -m venv env
env\\Scripts\\activate  # Windows uchun
# yoki
source env/bin/activate  # Linux/Mac uchun
```

### 3. Dependencylarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. PDF fayllarini qo'shish
- `coursebook.pdf` faylini dastur papkasiga qo'ying
- `workbook.pdf` faylini dastur papkasiga qo'ying

## 💻 Foydalanish

### Terminal orqali (main.py)
```bash
python main.py
```

1. Tanlov kiriting: `1` (Coursebook) yoki `2` (Workbook)
2. Tasdiqlash uchun `y` tugmasini bosing
3. Natijalar `B1+_coursebook_units/` yoki `B1+_workbook_units/` papkasida saqlanadi

### Web interfeys orqali (server.py)
```bash
python server.py
```

1. Brauzerda `http://localhost:5000` ga o'ting
2. Fayl turini tanlang (Coursebook yoki Workbook)
3. PDF faylni drag & drop qiling yoki "Fayl tanlash" tugmasini bosing
4. "Bo'lishni Boshlash" tugmasini bosing
5. Har bir unitni alohida yoki barchasini ZIP qilib yuklab oling

## 📁 Fayl Tuzilishi

```
Dars/
├── 📄 main.py              # Terminal versiyasi
├── 🌐 server.py            # Flask web server
├── 🎨 index.html           # Web interfeys
├── 💄 style.css            # Qo'shimcha stillar
├── 📋 requirements.txt     # Python dependencylari
├── 📖 README.md           # Bu fayl
├── 📚 coursebook.pdf      # Asosiy darslik (siz qo'shasiz)
├── 📝 workbook.pdf        # Ish kitobi (siz qo'shasiz)
└── 📁 env/               # Virtual environment
```

## 🔧 Unit Ma'lumotlari

### Coursebook (60 ta unit)
- **Unit 1.1-1.5**: Sahifalar 7-16
- **Unit 2.1-2.5**: Sahifalar 17-26
- **Unit 3.1-3.5**: Sahifalar 27-36
- ... va hokazo 12-unitgacha

### Workbook (49 ta unit)
- **Unit 1.1-1.4**: Sahifalar 5-10
- **Unit 2.1-2.5**: Sahifalar 11-18
- **Unit 3.1-3.4**: Sahifalar 19-24
- ... va hokazo 12-unitgacha

## 🎯 API Endpoints (Developer uchun)

```
GET  /api/units/<file_type>                        # Unit ro'yxati
POST /api/process                                   # PDF ni bo'lish
POST /api/download/<file_type>                      # ZIP yuklab olish
POST /api/download-unit/<file_type>/<unit_name>     # Bitta unit
```

## 🐛 Muammolarni Hal Qilish

### "PDF fayl topilmadi" xatosi
- `coursebook.pdf` va `workbook.pdf` fayllarini dastur papkasiga qo'ying
- Fayl nomlarining to'g'riligini tekshiring

### "Module not found" xatosi
```bash
pip install -r requirements.txt
```

### Web interfeys ishlamayotgan bo'lsa
- Server ishga tushganligini tekshiring: `python server.py`
- Brauzerda `http://localhost:5000` ga o'ting
- Console da xatolarni tekshiring (F12)

### Sahifa raqamlari noto'g'ri bo'lsa
- `main.py` yoki `server.py` dagi `unit_ranges` ni tahrirlang
- PDF fayldagi haqiqiy sahifa raqamlariga mos ravishda o'zgartiring

## 🔒 Xavfsizlik

- Fayl yuklash faqat PDF formatida qabul qilinadi
- Temp fayllar avtomatik o'chiriladi
- CORS himoyasi yoqilgan

## 📞 Yordam

Agar sizda savollar yoki muammolar bo'lsa:

1. **GitHub Issues** orqali muammo haqida xabar bering
2. **README.md** ni diqqat bilan o'qing
3. **Console/Terminal** dagi xato xabarlarini tekshiring

## 📄 Litsenziya

Bu dastur **MIT License** ostida tarqatiladi.

## 🙏 Minnatdorchilik

- **PyPDF2** - PDF ishlash uchun
- **Flask** - Web server uchun
- **PDF.js** - Browser da PDF ko'rish uchun

---

**Muallif**: PDF Unit Bo'lish Dasturi Jamoasi  
**Versiya**: 1.0.0  
**Sanasi**: 2025  

🎉 **Yaxshi ishlatishlar!**
