import datetime
from difflib import get_close_matches


def time_dif(start,end):
    #return diffrence betwen two date in hours
    duration=(abs(end-start).days*24*60)+((abs(end-start).seconds)/60)
    duration=round(duration,2)
    return duration

#####################

name_list=['قنبری','عظیم محمدی','میثم محمدی','آسترکی','حشمتی پور','باجلان','مهرآبادی','دولت آبادی','چقایی','جودکی','خراط نژاد','سنجری']

def similar(a):
    useless_char_list=['1','2','3','ـ']
    a=a.strip()
    for c in useless_char_list:
        a=a.replace(c,'')

    if 'ا' == a[0]:
        a=a.replace("ا",
                    "آ",
                    1)
    a=get_close_matches(a,name_list,n=1,cutoff=0.9)

    if 'خر' in a:
        a=name_list[1]    
    elif 'جود' in a:
        a=name_list[2]
    elif 'چق' in a:
        a=name_list[3]
    elif 'دو' in a:
        a=name_list[4]

    elif 'هر' in a:
        a=name_list[5]
    elif 'اج' in a:
        a=name_list[6]
    elif 'حش' in a:
        a=name_list[7]
    elif 'رک' in a:
        a=name_list[8]
    elif 'ثم' in a:
        a=name_list[9]
    elif 'عظ' in a:
        a=name_list[10]
    elif 'قن' in a:
        a=name_list[11]

    return a

   