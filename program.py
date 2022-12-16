from PIL import Image, ImageDraw, ImageFont



img = Image.open('leo.jpg')

#Фото

#фамилия
name = ImageDraw.Draw(img)
text = input("Фамилия:")
head = ImageFont.truetype("Cour.ttf", size=32)
name.text((750, 696), text, font=head, fill='#565157')
#имя
fam = ImageDraw.Draw(img)
text = input("Имя:")
head = ImageFont.truetype("Cour.ttf", size=32)
fam.text((764, 791), text, font=head, fill='#565157')
#Отчество
dad = ImageDraw.Draw(img)
text = input("Отчество:")
head = ImageFont.truetype("Cour.ttf", size=32)
dad.text((725, 835), text, font=head, fill='#565157')
#Пол
pol = ImageDraw.Draw(img)
text = input("Пол:")
head = ImageFont.truetype("Cour.ttf", size=32)
fam.text((599,882), text, font=head, fill='#565157')
#Дата рождения
bir = ImageDraw.Draw(img)
text = input("ДД.ММ.ГГ:")
head = ImageFont.truetype("Cour.ttf", size=32)
bir.text((781,882), text, font=head, fill='#565157')
#Место рождения
loc = ImageDraw.Draw(img)
text = input("Место рождения(город, село, поселок):")
head = ImageFont.truetype("Cour.ttf", size=32)
loc.text((699,927), text, font=head, fill='#565157')

loc1 = ImageDraw.Draw(img)
text = input("Место рождения(регион, республика, область):")
head = ImageFont.truetype("Cour.ttf", size=32)
loc1.text((644,979), text, font=head, fill='#565157')
#Паспорт выдан
vidan = ImageDraw.Draw(img)
text = input("Кем выдан(до 4-х слов):")
head = ImageFont.truetype("Cour.ttf", size = 32)
vidan.text((477,107), text, font=head, fill='#565157')

vidan = ImageDraw.Draw(img)
text = input("Кем выдан2(до 4-х слов, если есть продолжение, если нет скип!):")
head = ImageFont.truetype("Cour.ttf", size = 32)
vidan.text((365,165), text, font=head, fill = '#565157')

vidan = ImageDraw.Draw(img)
text = input("Кем выдан3(до 4-х слов, если есть продолжение, если нет скип!):")
head = ImageFont.truetype("Cour.ttf", size=32)
vidan.text((493,208), text, font=head, fill='#565157')

#Дата выдачи
data = ImageDraw.Draw(img)
text = input("Дата выдачи:")
head = ImageFont.truetype("Cour.ttf", size = 29)
data.text((420,256), text, font=head, fill='#565157')

#Код подразделения
cod = ImageDraw.Draw(img)
text = input("Код подразделения:")
head = ImageFont.truetype("Cour.ttf", size = 29)
cod.text((792,256), text, font=head, fill = '#565157')

#Серия
seriya = ImageDraw.Draw(img)
text = input("Серия паспорта(первые 2 цифры):")
head = ImageFont.truetype("Cambria.ttc", size = 29)
seriya.text((1066,175),text, font=head, fill = '#6e3649')
















img.show()











