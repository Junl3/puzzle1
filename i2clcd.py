from i2clcd import i2clcd
import time
lcd=i2clcd (1,0x27,20)
lcd.init()
text= input("Escriba lo que quieras mostrar por pantalla: ")
lcd.print_long_text(text)
