import PyPDF2
import re
import os
from pathlib import Path

def split_pdf_by_units(pdf_path, output_folder="units"):
    """
    PDF faylni unit bo'yicha bo'laklarga ajratadi
    """
    # Output papkasini yaratish
    Path(output_folder).mkdir(exist_ok=True)
    
    # PDF faylni ochish
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
        
        print(f"Jami sahifalar: {total_pages}")
        
        # Unit boshlash sahifalarini topish
        unit_pages = find_unit_pages(pdf_reader)
        
        if not unit_pages:
            print("Hech qanday unit topilmadi!")
            return
        
        # Har bir unitni alohida PDF ga saqlash
        for i, (unit_name, start_page) in enumerate(unit_pages):
            # Keyingi unitning boshlanish sahifasini aniqlash
            if i + 1 < len(unit_pages):
                end_page = unit_pages[i + 1][1] - 1
            else:
                end_page = total_pages - 1
            
            # Unit uchun PDF yaratish
            create_unit_pdf(pdf_reader, unit_name, start_page, end_page, output_folder)
            print(f"✓ {unit_name}.pdf yaratildi (sahifalar: {start_page + 1}-{end_page + 1})")

def find_unit_pages(pdf_reader):
    """
    PDF da unit boshlash sahifalarini topadi
    """
    unit_pages = []
    unit_patterns = [
        r'Unit\s*(\d+)\.(\d+)',  # Unit 1.1, Unit 1.2
        r'UNIT\s*(\d+)\.(\d+)',  # UNIT 1.1, UNIT 1.2
        r'Chapter\s*(\d+)\.(\d+)', # Chapter 1.1
        r'Lesson\s*(\d+)\.(\d+)'   # Lesson 1.1
    ]
    
    for page_num, page in enumerate(pdf_reader.pages):
        try:
            text = page.extract_text()
            
            for pattern in unit_patterns:
                matches = re.finditer(pattern, text, re.IGNORECASE)
                for match in matches:
                    unit_major = match.group(1)
                    unit_minor = match.group(2)
                    unit_name = f"Unit{unit_major}.{unit_minor}"
                    
                    # Takrorlanishni oldini olish
                    if not any(up[0] == unit_name for up in unit_pages):
                        unit_pages.append((unit_name, page_num))
                        
        except Exception as e:
            print(f"Sahifa {page_num + 1} da xatolik: {e}")
    
    # Sahifa tartibida saralash
    unit_pages.sort(key=lambda x: x[1])
    return unit_pages

def create_unit_pdf(pdf_reader, unit_name, start_page, end_page, output_folder):
    """
    Belgilangan sahifalar orasidan yangi PDF yaratadi
    """
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(start_page, end_page + 1):
        if page_num < len(pdf_reader.pages):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # PDF faylni saqlash
    output_path = os.path.join(output_folder, f"{unit_name}.pdf")
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

def manual_split_pdf(pdf_path, unit_ranges, output_folder="units"):
    """
    Qo'lda belgilangan sahifa oraliqlariga ko'ra PDF ni bo'lish
    unit_ranges: [("Unit1.1", 1, 15), ("Unit1.2", 16, 30), ...]
    """
    Path(output_folder).mkdir(exist_ok=True)
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for unit_name, start_page, end_page in unit_ranges:
            pdf_writer = PyPDF2.PdfWriter()
            
            # Sahifa indekslari 0 dan boshlanadi
            for page_num in range(start_page - 1, end_page):
                if page_num < len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
            
            # PDF faylni saqlash
            output_path = os.path.join(output_folder, f"{unit_name}.pdf")
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"✓ {unit_name}.pdf yaratildi (sahifalar: {start_page}-{end_page})")

# Foydalanish namunasi
if __name__ == "__main__":
    print("=== PDF Unit Bo'lish Dasturi ===\n")
    print("Quyidagi variantlardan birini tanlang:")
    print("1. Coursebook.pdf")
    print("2. Workbook.pdf")
    
    choice = input("\nTanlovingizni kiriting (1 yoki 2): ").strip()
    
    if choice == "1":
        pdf_file = "coursebook.pdf"
        output_folder = "B1+_coursebook_units"
        unit_ranges = [
            ("B1+ unit1.1", 7, 8),                  
            ("B1+ unit1.2", 9, 10),              
            ("B1+ unit1.3", 11, 12),              
            ("B1+ unit1.4", 13, 14), 
            ("B1+ unit1.5", 15, 16), 
            
            ("B1+ unit2.1", 17, 18),               
            ("B1+ unit2.2", 19, 20),              
            ("B1+ unit2.3", 21, 22),               
            ("B1+ unit2.4", 23, 24),                
            ("B1+ unit2.5", 25, 26),

            ("B1+ unit3.1", 27, 28),             
            ("B1+ unit3.2", 29, 30),            
            ("B1+ unit3.3", 31, 32),                
            ("B1+ unit3.4", 33, 34),              
            ("B1+ unit3.5", 35, 36),

            ("B1+ unit4.1", 37, 38),            
            ("B1+ unit4.2", 39, 40), 
            ("B1+ unit4.3", 41, 42),         
            ("B1+ unit4.4", 43, 44),               
            ("B1+ unit4.5", 45, 46),               

            ("B1+ unit5.1", 47, 48),          
            ("B1+ unit5.2", 49, 50),              
            ("B1+ unit5.3", 51, 52),                   
            ("B1+ unit5.4", 53, 54),           
            ("B1+ unit5.5", 55, 56),            

            ("B1+ unit6.1", 57, 58),         
            ("B1+ unit6.2", 59, 60),      
            ("B1+ unit6.3", 61, 62),                                 
            ("B1+ unit6.4", 63, 64),          
            ("B1+ unit6.5", 65, 66),             

            ("B1+ unit7.1", 67, 68),              
            ("B1+ unit7.2", 69, 70),               
            ("B1+ unit7.3", 71, 72),               
            ("B1+ unit7.4", 73, 74),             
            ("B1+ unit7.5", 75, 76),         
            
            ("B1+ unit8.1", 77, 78),             
            ("B1+ unit8.2", 79, 80),          
            ("B1+ unit8.3", 81, 82),                    
            ("B1+ unit8.4", 83, 84),              
            ("B1+ unit8.5", 85, 86),               

            ("B1+ unit9.1", 87, 88),               
            ("B1+ unit9.2", 89, 90),       
            ("B1+ unit9.3", 91, 92),             
            ("B1+ unit9.4", 93, 94),               
            ("B1+ unit9.5", 95, 96),               

            ("B1+ unit10.1", 97, 98),             
            ("B1+ unit10.2", 99, 100),         
            ("B1+ unit10.3", 101, 102),           
            ("B1+ unit10.4", 103, 104),            
            ("B1+ unit10.5", 105, 106),           

            ("B1+ unit11.1", 107, 108),            
            ("B1+ unit11.2", 109, 110),         
            ("B1+ unit11.3", 111, 112),          
            ("B1+ unit11.4", 113, 114),          
            ("B1+ unit11.5", 115, 116),           
            
            ("B1+ unit12.1", 117, 118),      
            ("B1+ unit12.2", 119, 120),         
            ("B1+ unit12.3", 121, 122),            
            ("B1+ unit12.4", 123, 124),           
            ("B1+ unit12.5", 125, 126),
        ]
        
    elif choice == "2":
        pdf_file = "workbook.pdf"
        output_folder = "B1+_workbook_units"
        unit_ranges = [
            ("B1+ unit1.1", 5, 6),
            ("B1+ unit1.2", 7, 8),
            ("B1+ unit1.3", 9, 9),
            ("B1+ unit1.4", 10, 10),
         
            ("B1+ unit2.1", 11, 12),
            ("B1+ unit2.2", 13, 14),
            ("B1+ unit2.3", 15, 15),
            ("B1+ unit2.4", 16, 16),
            ("B1+ unit2.5", 17, 18),

            ("B1+ unit3.1", 19, 20),  
            ("B1+ unit3.2", 21, 22),  
            ("B1+ unit3.3", 23, 23),  
            ("B1+ unit3.4", 24, 24),

            ("B1+ unit4.1", 25, 26),
            ("B1+ unit4.2", 27, 28),
            ("B1+ unit4.3", 29, 29),
            ("B1+ unit4.4", 30, 30),
            ("B1+ unit4.5", 31, 32),

            ("B1+ unit5.1", 33, 34),
            ("B1+ unit5.2", 35, 36),
            ("B1+ unit5.3", 37, 37),
            ("B1+ unit5.4", 38, 38),

            ("B1+ unit6.1", 39, 40),
            ("B1+ unit6.2", 41, 42),
            ("B1+ unit6.3", 43, 43),
            ("B1+ unit6.4", 44, 44),
            ("B1+ unit6.5", 45, 46),

            ("B1+ unit7.1", 47, 48),
            ("B1+ unit7.2", 49, 50),
            ("B1+ unit7.3", 51, 51),
            ("B1+ unit7.4", 52, 52),

            ("B1+ unit8.1", 53, 54),
            ("B1+ unit8.2", 55, 56),
            ("B1+ unit8.3", 57, 57),
            ("B1+ unit8.4", 58, 58),
            ("B1+ unit8.5", 59, 60),

            ("B1+ unit9.1", 61, 62),
            ("B1+ unit9.2", 63, 64),
            ("B1+ unit9.3", 65, 65),
            ("B1+ unit9.4", 66, 66),

            ("B1+ unit10.1", 67, 68),
            ("B1+ unit10.2", 69, 70),
            ("B1+ unit10.3", 71, 71),
            ("B1+ unit10.4", 72, 72),
            ("B1+ unit10.5", 73, 74),

            ("B1+ unit11.1", 75, 76),
            ("B1+ unit11.2", 77, 78),
            ("B1+ unit11.3", 79, 79),
            ("B1+ unit11.4", 80, 80),

            ("B1+ unit12.1", 81, 82),
            ("B1+ unit12.2", 83, 84),
            ("B1+ unit12.3", 85, 85),
            ("B1+ unit12.4", 86, 86),
            ("B1+ unit12.5", 87, 88),
        ]
    else:
        print("❌ Noto'g'ri tanlov! Iltimos 1 yoki 2 ni tanlang.")
        exit()
    
    if os.path.exists(pdf_file):
        print(f"\n✅ PDF fayl topildi: {pdf_file}")
        print(f"📂 Natijalar saqlanadigan papka: {output_folder}")
        
        print(f"\n=== {pdf_file.upper()} UNIT RO'YXATI ===")
        for i, (unit_name, start, end) in enumerate(unit_ranges, 1):
            print(f"{i:2d}. {unit_name}: {start}-{end} sahifalar")
        
        print(f"\n📊 Jami unitlar soni: {len(unit_ranges)}")
        
        confirm = input(f"\n{pdf_file} faylini bo'laklarga ajratishni boshlaysizmi? (y/n): ")
        if confirm.lower() == 'y':
            manual_split_pdf(pdf_file, unit_ranges, output_folder)
            print(f"\n🎉 Barcha unitlar muvaffaqiyatli yaratildi!")
            print(f"📁 Natijalarni '{output_folder}' papkasida ko'ring.")
        else:
            print("❌ Jarayon bekor qilindi.")
        
    else:
        print(f"❌ PDF fayl topilmadi: {pdf_file}")
        print("Fayl nomini to'g'ri kiriting yoki faylni dastur bilan bir papkaga qo'ying.")