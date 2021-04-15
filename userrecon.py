#!/usr/bin/python3

import requests
from sys import argv

class Result:
  def __init__(self, service_name: str, exists: bool, username: str, url: str) -> None:
    self.service_name = service_name
    self.exists = exists
    self.username = username
    self.url = url

class UserRecon:
  def __init__(self, username) -> None:
    self.username = username
    self.headers = {"user-agent":"userrecon/1.0"}

  def method_status_code(self, url: str):
    response = requests.get(url, headers=self.headers)

    return True if response.status_code == 200 else False

  def check_all(self):
    functions = list(filter(lambda item: (item.startswith("check_") and item != "check_all"), dir(self)))
    functions = [getattr(self, f) for f in functions]
    
    #TODO: nome em negrito
    print(f"[i] Buscando {self.username} em {len(functions)} sites...\n")

    for f in functions:
      result: Result = f()
      
      #TODO: adicionar cor

      if result.exists:
        print(f"[*] {result.service_name}: {result.url}")
      else:
        print(f"[x] {result.service_name}: não encontrado.")
        

  def check_facebook(self) -> Result:
    url = "https://m.facebook.com/"+self.username
    result = self.method_status_code(url)

    return Result("Facebook", result, self.username, url)

  def check_tiktok(self) -> Result:
    url = "https://www.tiktok.com/@"+self.username
    result = self.method_status_code(url)

    return Result("TikTok", result, self.username, url)

  def check_instagram(self) -> Result:
    url = "https://www.instagram.com/"+self.username
    result = self.method_status_code(url)
    
    return Result("Instagram", result, self.username, url)
  
  def check_lastfm(self) -> Result:
    url = "https://www.last.fm/user/"+self.username
    result = self.method_status_code(url)
    
    return Result("Last.fm", result, self.username, url)

banner="""
 █    ██   ██████ ▓█████  ██▀███   ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █ 
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ 
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░   ░░   ░    ░   ░        ░ ░ ░ ▒     ░   ░ ░ 
   ░           ░     ░  ░   ░        ░        ░  ░░ ░          ░ ░           ░ 
                                                  ░                by \033[1;36m@shi0n04\033[m
"""

print(banner)

if len(argv) != 2:
  exit(f"error: invalid argvs\nusage: python3 {argv[0]} username")
    
user_recon = UserRecon(argv[1]).check_all()
