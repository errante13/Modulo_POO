import os 
# os.system("cls")

log_file1 =open(os.path.abspath('dia_11/logs/error.log'))
#FileNotFoundError: [Errno 2] No such file or directory: 
# 'C:\\Users\\luis\\Desktop\\Desafio Latam\\dia_11\\logs\\error.log'

log_file2 = open(os.path.abspath("dia_11/index.html"),'r')
print(log_file2.readlines())