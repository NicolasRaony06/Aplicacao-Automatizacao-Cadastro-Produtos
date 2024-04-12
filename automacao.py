import pyautogui, pandas, time

pyautogui.PAUSE = 0.8

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

pyautogui.press('tab')
pyautogui.write('automacao@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')

dados = pandas.read_csv('produtos.csv')

for linhas in dados.index:
    pyautogui.click(x=605, y=258)

    pyautogui.write(dados.loc[linhas, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(dados.loc[linhas, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(dados.loc[linhas, 'tipo'])
    pyautogui.press('tab')

    categoria = str(dados.loc[linhas, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(dados.loc[linhas, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(dados.loc[linhas, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = dados.loc[linhas, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)