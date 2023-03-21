import os
import shutil
import time

src_dir = r'\\NasTecplas\Pintura\DB\BKPS'
dst_dir = r'\\NasTecplas\Engenharia\Levy\BKPs'

while True:
    current_time = time.strftime('%H:%M')
    print(current_time)
    
    if current_time == '07:00' or current_time == '12:30' or current_time == '17:00':
        for file in os.listdir(src_dir):
            if file.endswith('.db'):
                try:
                    shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, file))
                    print("Arquivo copiado com sucesso!")
                except Exception as e:
                    print(f'Erro ao copiar o arquivo {file}: {e}')
    
    time.sleep(60)  # espera 1 minuto antes de verificar novamente

