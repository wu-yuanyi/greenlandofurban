#-*- coding:utf-8 -*-

import csv
import base


def get_dict_block_park():
    '''
    deal with society.csv
    '''
    #read society.csv
    society_csvfile=open('./society.csv','r',encoding='utf-8')
    dict_society = csv.DictReader(society_csvfile)
    list_society = []
    for item in dict_society:
        list_society.append(item)
    society_csvfile.close()
    #print (list_society)
    
    '''
    save blocks' name in list_block_name as a list
    '''
    list_block_name=[]
    for society in list_society:
        if society['街道名称'] not in list_block_name:
            list_block_name.append(society['街道名称'])
    #print (list_block_name)

    '''
    save blocks' park in dict_block_park as a dict
    '''
    dict_block_park={}.fromkeys(list_block_name,0)
    #print(dict_block_greenland)
    for area in list_society:
        dict_block_park[area['街道名称']]+=float(area['公园服务面积（平方公里）'])
    #print (dict_block_park)
    return dict_block_park



def socefficiency_value():
    '''
    calculate total social efficiency
    '''
    dict_temp = base.get_dict_block_area()
    dict_socefficiency_value = {}
    dict_block_park = get_dict_block_park()
    for key in dict_block_park:
        dict_socefficiency_value[key] = dict_block_park[key] \
            / dict_temp[key]
    #print (dict_socefficiency_value)
    return dict_socefficiency_value
