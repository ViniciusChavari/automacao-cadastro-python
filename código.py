import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=935, y=406)
pyautogui.write("vinicius@nmail.com")
pyautogui.press("tab") 
pyautogui.write("Vinicius123")
pyautogui.click(x=983, y=572)
time.sleep(3)

import pandas as pd

tabela = pd.read_csv(r"C:\Users\vini_\OneDrive\Documentos\Hashtag Treinamentos\Automações de Tarefas e Bots - Jornada Python [Aula 1]\produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=781, y=289)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)