import colorama
import inspect

colorama.init()


for name in dir(colorama):
        print(name)

dir(colorama.Fore)
dir(colorama.Back)
dir(colorama.Style)
hasattr(colorama, "Fore")
callable(colorama.init)

#Fore	клас - Колір тексту
#Back	клас - Колір фону
#Style	клас - Стиль/яскравість тексту
#Cursor	клас - Керування положенням курсора
#AnsiToWin32	клас - Перетворює ANSI-команди для роботи у Windows
#init()	функція - Ініціалізує Colorama
#deinit()	функція - Вимикає Colorama та повертає стандартний stdout/stderr
#reinit()	функція	- Повторно вмикає вже налаштований Colorama
#just_fix_windows_console()	функція	 - Налаштовує Windows-консоль для ANSI-кодів
#colorama_text()	функція/контекстний менеджер - Тимчасово вмикає Colorama всередині блоку with
#__version__	атрибут	Версія Colorama
#__name__	атрибут	Назва модуля
#__file__	атрибут	Шлях до файлу модуля


