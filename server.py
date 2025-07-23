from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import PyPDF2
import os
import io
import zipfile
from pathlib import Path
import tempfile
import json

app = Flask(__name__)
CORS(app)  # CORS ni yoqish frontend bilan ishlash uchun

# Unit ma'lumotlari
UNIT_RANGES = {
    'coursebook': [
        {"name": "B1+ unit1.1", "start": 7, "end": 8},
        {"name": "B1+ unit1.2", "start": 9, "end": 10},
        {"name": "B1+ unit1.3", "start": 11, "end": 12},
        {"name": "B1+ unit1.4", "start": 13, "end": 14},
        {"name": "B1+ unit1.5", "start": 15, "end": 16},
        {"name": "B1+ unit2.1", "start": 17, "end": 18},
        {"name": "B1+ unit2.2", "start": 19, "end": 20},
        {"name": "B1+ unit2.3", "start": 21, "end": 22},
        {"name": "B1+ unit2.4", "start": 23, "end": 24},
        {"name": "B1+ unit2.5", "start": 25, "end": 26},
        {"name": "B1+ unit3.1", "start": 27, "end": 28},
        {"name": "B1+ unit3.2", "start": 29, "end": 30},
        {"name": "B1+ unit3.3", "start": 31, "end": 32},
        {"name": "B1+ unit3.4", "start": 33, "end": 34},
        {"name": "B1+ unit3.5", "start": 35, "end": 36},
        {"name": "B1+ unit4.1", "start": 37, "end": 38},
        {"name": "B1+ unit4.2", "start": 39, "end": 40},
        {"name": "B1+ unit4.3", "start": 41, "end": 42},
        {"name": "B1+ unit4.4", "start": 43, "end": 44},
        {"name": "B1+ unit4.5", "start": 45, "end": 46},
        {"name": "B1+ unit5.1", "start": 47, "end": 48},
        {"name": "B1+ unit5.2", "start": 49, "end": 50},
        {"name": "B1+ unit5.3", "start": 51, "end": 52},
        {"name": "B1+ unit5.4", "start": 53, "end": 54},
        {"name": "B1+ unit5.5", "start": 55, "end": 56},
        {"name": "B1+ unit6.1", "start": 57, "end": 58},
        {"name": "B1+ unit6.2", "start": 59, "end": 60},
        {"name": "B1+ unit6.3", "start": 61, "end": 62},
        {"name": "B1+ unit6.4", "start": 63, "end": 64},
        {"name": "B1+ unit6.5", "start": 65, "end": 66},
        {"name": "B1+ unit7.1", "start": 67, "end": 68},
        {"name": "B1+ unit7.2", "start": 69, "end": 70},
        {"name": "B1+ unit7.3", "start": 71, "end": 72},
        {"name": "B1+ unit7.4", "start": 73, "end": 74},
        {"name": "B1+ unit7.5", "start": 75, "end": 76},
        {"name": "B1+ unit8.1", "start": 77, "end": 78},
        {"name": "B1+ unit8.2", "start": 79, "end": 80},
        {"name": "B1+ unit8.3", "start": 81, "end": 82},
        {"name": "B1+ unit8.4", "start": 83, "end": 84},
        {"name": "B1+ unit8.5", "start": 85, "end": 86},
        {"name": "B1+ unit9.1", "start": 87, "end": 88},
        {"name": "B1+ unit9.2", "start": 89, "end": 90},
        {"name": "B1+ unit9.3", "start": 91, "end": 92},
        {"name": "B1+ unit9.4", "start": 93, "end": 94},
        {"name": "B1+ unit9.5", "start": 95, "end": 96},
        {"name": "B1+ unit10.1", "start": 97, "end": 98},
        {"name": "B1+ unit10.2", "start": 99, "end": 100},
        {"name": "B1+ unit10.3", "start": 101, "end": 102},
        {"name": "B1+ unit10.4", "start": 103, "end": 104},
        {"name": "B1+ unit10.5", "start": 105, "end": 106},
        {"name": "B1+ unit11.1", "start": 107, "end": 108},
        {"name": "B1+ unit11.2", "start": 109, "end": 110},
        {"name": "B1+ unit11.3", "start": 111, "end": 112},
        {"name": "B1+ unit11.4", "start": 113, "end": 114},
        {"name": "B1+ unit11.5", "start": 115, "end": 116},
        {"name": "B1+ unit12.1", "start": 117, "end": 118},
        {"name": "B1+ unit12.2", "start": 119, "end": 120},
        {"name": "B1+ unit12.3", "start": 121, "end": 122},
        {"name": "B1+ unit12.4", "start": 123, "end": 124},
        {"name": "B1+ unit12.5", "start": 125, "end": 126}
    ],
    'workbook': [
        {"name": "B1+ unit1.1", "start": 5, "end": 6},
        {"name": "B1+ unit1.2", "start": 7, "end": 8},
        {"name": "B1+ unit1.3", "start": 9, "end": 9},
        {"name": "B1+ unit1.4", "start": 10, "end": 10},
        {"name": "B1+ unit2.1", "start": 11, "end": 12},
        {"name": "B1+ unit2.2", "start": 13, "end": 14},
        {"name": "B1+ unit2.3", "start": 15, "end": 15},
        {"name": "B1+ unit2.4", "start": 16, "end": 16},
        {"name": "B1+ unit2.5", "start": 17, "end": 18},
        {"name": "B1+ unit3.1", "start": 19, "end": 20},
        {"name": "B1+ unit3.2", "start": 21, "end": 22},
        {"name": "B1+ unit3.3", "start": 23, "end": 23},
        {"name": "B1+ unit3.4", "start": 24, "end": 24},
        {"name": "B1+ unit4.1", "start": 25, "end": 26},
        {"name": "B1+ unit4.2", "start": 27, "end": 28},
        {"name": "B1+ unit4.3", "start": 29, "end": 29},
        {"name": "B1+ unit4.4", "start": 30, "end": 30},
        {"name": "B1+ unit4.5", "start": 31, "end": 32},
        {"name": "B1+ unit5.1", "start": 33, "end": 34},
        {"name": "B1+ unit5.2", "start": 35, "end": 36},
        {"name": "B1+ unit5.3", "start": 37, "end": 37},
        {"name": "B1+ unit5.4", "start": 38, "end": 38},
        {"name": "B1+ unit6.1", "start": 39, "end": 40},
        {"name": "B1+ unit6.2", "start": 41, "end": 42},
        {"name": "B1+ unit6.3", "start": 43, "end": 43},
        {"name": "B1+ unit6.4", "start": 44, "end": 44},
        {"name": "B1+ unit6.5", "start": 45, "end": 46},
        {"name": "B1+ unit7.1", "start": 47, "end": 48},
        {"name": "B1+ unit7.2", "start": 49, "end": 50},
        {"name": "B1+ unit7.3", "start": 51, "end": 51},
        {"name": "B1+ unit7.4", "start": 52, "end": 52},
        {"name": "B1+ unit8.1", "start": 53, "end": 54},
        {"name": "B1+ unit8.2", "start": 55, "end": 56},
        {"name": "B1+ unit8.3", "start": 57, "end": 57},
        {"name": "B1+ unit8.4", "start": 58, "end": 58},
        {"name": "B1+ unit8.5", "start": 59, "end": 60},
        {"name": "B1+ unit9.1", "start": 61, "end": 62},
        {"name": "B1+ unit9.2", "start": 63, "end": 64},
        {"name": "B1+ unit9.3", "start": 65, "end": 65},
        {"name": "B1+ unit9.4", "start": 66, "end": 66},
        {"name": "B1+ unit10.1", "start": 67, "end": 68},
        {"name": "B1+ unit10.2", "start": 69, "end": 70},
        {"name": "B1+ unit10.3", "start": 71, "end": 71},
        {"name": "B1+ unit10.4", "start": 72, "end": 72},
        {"name": "B1+ unit10.5", "start": 73, "end": 74},
        {"name": "B1+ unit11.1", "start": 75, "end": 76},
        {"name": "B1+ unit11.2", "start": 77, "end": 78},
        {"name": "B1+ unit11.3", "start": 79, "end": 79},
        {"name": "B1+ unit11.4", "start": 80, "end": 80},
        {"name": "B1+ unit12.1", "start": 81, "end": 82},
        {"name": "B1+ unit12.2", "start": 83, "end": 84},
        {"name": "B1+ unit12.3", "start": 85, "end": 85},
        {"name": "B1+ unit12.4", "start": 86, "end": 86},
        {"name": "B1+ unit12.5", "start": 87, "end": 88}
    ]
}

def create_unit_pdf(pdf_reader, start_page, end_page):
    """Belgilangan sahifalar orasidan yangi PDF yaratadi"""
    pdf_writer = PyPDF2.PdfWriter()
    
    # Sahifa indekslari 0 dan boshlanadi, lekin API da 1 dan
    for page_num in range(start_page - 1, end_page):
        if page_num < len(pdf_reader.pages):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Memory buffer ga yozish
    output_buffer = io.BytesIO()
    pdf_writer.write(output_buffer)
    output_buffer.seek(0)
    
    return output_buffer

@app.route('/')
def index():
    """Ana sahifani qaytarish"""
    return send_file('index.html')

@app.route('/api/units/<file_type>')
def get_units(file_type):
    """Unit ro'yxatini qaytarish"""
    if file_type not in UNIT_RANGES:
        return jsonify({'error': 'Noto\'g\'ri fayl turi'}), 400
    
    return jsonify({
        'units': UNIT_RANGES[file_type],
        'total': len(UNIT_RANGES[file_type])
    })

@app.route('/api/process', methods=['POST'])
def process_pdf():
    """PDF faylni unitlarga bo'lish"""
    try:
        # Fayl va parametrlarni olish
        if 'file' not in request.files:
            return jsonify({'error': 'Fayl yuklanmagan'}), 400
        
        file = request.files['file']
        file_type = request.form.get('file_type')
        
        if file.filename == '':
            return jsonify({'error': 'Fayl tanlanmagan'}), 400
        
        if file_type not in UNIT_RANGES:
            return jsonify({'error': 'Noto\'g\'ri fayl turi'}), 400
        
        # PDF ni o'qish
        pdf_reader = PyPDF2.PdfReader(file)
        units = UNIT_RANGES[file_type]
        
        # Har bir unit uchun PDF yaratish
        processed_units = []
        
        with tempfile.TemporaryDirectory() as temp_dir:
            for unit in units:
                try:
                    # Unit PDF yaratish
                    unit_pdf = create_unit_pdf(pdf_reader, unit['start'], unit['end'])
                    
                    # Vaqtinchalik faylga saqlash
                    unit_filename = f"{unit['name']}.pdf"
                    unit_path = os.path.join(temp_dir, unit_filename)
                    
                    with open(unit_path, 'wb') as unit_file:
                        unit_file.write(unit_pdf.getvalue())
                    
                    # Fayl hajmini aniqlash
                    file_size = os.path.getsize(unit_path)
                    
                    processed_units.append({
                        'name': unit['name'],
                        'filename': unit_filename,
                        'pages': f"{unit['start']}-{unit['end']}",
                        'size': f"{file_size // 1024} KB",
                        'path': unit_path
                    })
                    
                except Exception as e:
                    print(f"Unit {unit['name']} ishlanishida xatolik: {e}")
                    continue
            
            # ZIP fayl yaratish
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for unit in processed_units:
                    zip_file.write(unit['path'], unit['filename'])
            
            zip_buffer.seek(0)
            
            return jsonify({
                'success': True,
                'message': f'{len(processed_units)} ta unit muvaffaqiyatli yaratildi',
                'units': processed_units,
                'total': len(processed_units)
            })
            
    except Exception as e:
        return jsonify({'error': f'Xatolik yuz berdi: {str(e)}'}), 500

@app.route('/api/download/<file_type>', methods=['POST'])
def download_units(file_type):
    """Barcha unitlarni ZIP qilib yuklab berish"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Fayl yuklanmagan'}), 400
        
        file = request.files['file']
        
        if file_type not in UNIT_RANGES:
            return jsonify({'error': 'Noto\'g\'ri fayl turi'}), 400
        
        # PDF ni o'qish
        pdf_reader = PyPDF2.PdfReader(file)
        units = UNIT_RANGES[file_type]
        
        # ZIP fayl yaratish
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for unit in units:
                try:
                    # Unit PDF yaratish
                    unit_pdf = create_unit_pdf(pdf_reader, unit['start'], unit['end'])
                    
                    # ZIP ga qo'shish
                    unit_filename = f"{unit['name']}.pdf"
                    zip_file.writestr(unit_filename, unit_pdf.getvalue())
                    
                except Exception as e:
                    print(f"Unit {unit['name']} qo'shishda xatolik: {e}")
                    continue
        
        zip_buffer.seek(0)
        
        # ZIP faylni qaytarish
        filename = f"B1+_{file_type}_units.zip"
        return send_file(
            zip_buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='application/zip'
        )
        
    except Exception as e:
        return jsonify({'error': f'Xatolik yuz berdi: {str(e)}'}), 500

@app.route('/api/download-unit/<file_type>/<unit_name>', methods=['POST'])
def download_single_unit(file_type, unit_name):
    """Bitta unitni yuklab berish"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Fayl yuklanmagan'}), 400
        
        file = request.files['file']
        
        if file_type not in UNIT_RANGES:
            return jsonify({'error': 'Noto\'g\'ri fayl turi'}), 400
        
        # Unit topish
        units = UNIT_RANGES[file_type]
        target_unit = None
        
        for unit in units:
            if unit['name'] == unit_name:
                target_unit = unit
                break
        
        if not target_unit:
            return jsonify({'error': 'Unit topilmadi'}), 404
        
        # PDF ni o'qish
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Unit PDF yaratish
        unit_pdf = create_unit_pdf(pdf_reader, target_unit['start'], target_unit['end'])
        
        # PDF faylni qaytarish
        filename = f"{target_unit['name']}.pdf"
        return send_file(
            unit_pdf,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': f'Xatolik yuz berdi: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Sahifa topilmadi'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Server xatosi'}), 500

if __name__ == '__main__':
    print("🚀 PDF Unit Bo'lish Server ishga tushmoqda...")
    print("📖 Coursebook va Workbook fayllarini unitlarga bo'lish uchun server")
    print("🌐 Sayt: http://localhost:5000")
    print("📁 API endpoint'lar:")
    print("   - GET  /api/units/<file_type> - Unit ro'yxati")
    print("   - POST /api/process - PDF ni bo'lish")
    print("   - POST /api/download/<file_type> - ZIP yuklab olish")
    print("   - POST /api/download-unit/<file_type>/<unit_name> - Bitta unit")
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
