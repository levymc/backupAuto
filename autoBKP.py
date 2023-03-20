import os
import shutil
import time

src_dir = r'E:\Projects\Tecplas\DB'
dst_dir = r'E:\Projects\Tecplas\BackupDB'

while True:
    current_time = time.strftime('%H:%M')
    print(current_time)
    
    if current_time == '07:00' or current_time == '17:20' or current_time == '17:00':
        for file in os.listdir(src_dir):
            if file.endswith('.db'):
                try:
                    shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, file))
                    print("Arquivo copiado com sucesso!")
                except Exception as e:
                    print(f'Erro ao copiar o arquivo {file}: {e}')
    
    time.sleep(60)  # espera 1 minuto antes de verificar novamente
