def komp_info(model, xotira, ram, video_karta, core, rangi=''):   
    if rangi:
        user_komp_info = {'modeli': model ,
                      'xotirasi': xotira,
                      'rami': ram,
                      'video_kartasi': video_karta,
                      'rangi': rangi, 
                      'Avlod': core}
    else:
        user_komp_info = {'modeli': model ,
                      'xotirasi': xotira,
                      'rami': ram,
                      'video_kartasi': video_karta,                      
                      'Avlod': core}
    return user_komp_info

komplar = []
while True:
    print('Quyidagi ma`lumotlarni kiriting')
    model = input('Modeli > ')
    xotira = input('Xotirasi > ')
    ram = input('Ram > ')
    video_karta = input('Video kartasi > ')
    rangi = input('Rangi > ')
    avlod = input('Avlod > CoreI - ')
    komplar.append(komp_info(model, xotira, ram, video_karta, rangi, avlod))
    more = input('Yana ma`lumot kiritishni istaysizmi? (y/n) > ')
    print(komplar)
    if more == 'n':
        break