import shutil, keyboard, os, time

src_dir0 = r'\\NasTecplas\Pintura\DB'    #   fase 1
src_dir = r'\\NasTecplas\Pintura\DB\BKPS'   #   fase 1  -> fase 2
dst_dir = r'\\NasTecplas\Engenharia\Levy\BKPs'  #   fase 2

def pressionou_f9(evento):
    if evento.name == 'f9':
        print("Você pressionou F9!")
        return True

while True:
    current_time = time.strftime('%H:%M')
    print(current_time)
    if current_time == '07:00' or current_time == '12:30' or current_time == '17:00' or pressionou_f9(keyboard.read_event()):
        for file in os.listdir(src_dir0):
            if file.endswith('.db'):
                try:
                    shutil.copy(os.path.join(src_dir0, file), os.path.join(src_dir, file))
                    print("Arquivo copiado com sucesso! - fase 1")
                except Exception as e:
                    print(f'Erro ao copiar o arquivo {file}: {e} - fase 1')
                    
        time.sleep(2)
        
        for file in os.listdir(src_dir):
            if file.endswith('.db'):
                try:
                    shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, file))
                    print("Arquivo copiado com sucesso! - fase 2")
                except Exception as e:
                    print(f'Erro ao copiar o arquivo {file}: {e} - fase 2')
    
    time.sleep(60)  # espera 1 minuto antes de verificar novamente
