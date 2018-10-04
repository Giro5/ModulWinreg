import winreg
key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\ThisIsMyCompany")
winreg.SetValue(key, "MyFolderLike", winreg.REG_SZ, "It's Subkey")
winreg.SetValueEx(key, "JustValueName", 0 , winreg.REG_SZ, "My Value")
key.Close()

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\ThisIsMyCompany", 0, winreg.KEY_ALL_ACCESS)
print("Значение подключа или что-то типа папки:", winreg.QueryValue(key,"MyFolderLike"))
print("\nЗначение переменной или что-то типа того:", winreg.QueryValueEx(key,"JustValueName")[0])
key.Close()

print()
i = 0
while True:
    try:
        print(winreg.EnumKey(winreg.HKEY_CURRENT_USER, i))
    except:
        print("//done//")
        break
    i += 1

try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Valve\\Steam", 0, winreg.KEY_ALL_ACCESS)
    print("\nЗначение из программы Steam - последний использованный никнейм:", winreg.QueryValueEx(key, "LastGameNameUsed")[0])
    key.Close()
except BaseException:
    print("Неудалось вернуть значение из программы Steam")

input("\nДля продолжения нажмите любую клавишу")
winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\ThisIsMyCompany\\MyFolderLike")
winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\ThisIsMyCompany")