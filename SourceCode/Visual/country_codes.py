from pygal_maps_world.i18n import COUNTRIES



def print_code_name():
    #pygal绘图时使用的是两个字母的国别码，而文件里使用的是三个
    #字母，因此需要使用i18n模块进行转换。先打印国别码和国家名：
    for country_code in sorted(COUNTRIES.keys()):
        print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """根据指定的国家返回Pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code

    #如果没有找到指定的国家，返回None
    return None

#Test
#print(get_country_code('Chinese'))
#print(get_country_code('Andorra'))
