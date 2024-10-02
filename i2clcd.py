from i2clcd import i2clcd
import time
lcd=i2clcd (1,0x27,20)
lcd.init()
lcd.print_long_text("Nuestro grupo de PBE esta compuesto por blanca,ivan,mariona,roger,junle")
