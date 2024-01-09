import pyautogui  
import time

pyautogui.PAUSE = 1 
pyautogui.press("win" )
time.sleep(5) 
pyautogui.write("google chrome")
pyautogui.press("enter")     
time.sleep(5)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)   
time.sleep(2)

pyautogui.press("enter")

pyautogui.click(x=517, y=612)

pyautogui.write("Sabrina.projetopython.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.press("tab")
pyautogui.click(x=919, y=840)
pyautogui.sleep(3)
#importar a base de dados 

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#tabela.index(cada linha da tabela, tab para dentro para executar cada linha)
for linha in tabela.index:

    #cadastro do produto 
    pyautogui.click(x=516, y=436)
    #codigo 
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo 
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs 
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    #rolar a tela positivo para cima negativo para baixo 
    pyautogui.scroll(1000)  
#repetir o proceddo até acabar a base de dados Mouse    1   25.95   6.5     



