#-*- coding:utf-8 -*-

import csv
import re



'''
deal with base.csv
'''
#read base.csv
base_csvfile=open('./base.csv','r',encoding='utf-8')
dict_base = csv.DictReader(base_csvfile)
list_base=[]
for item in dict_base:
    list_base.append(item)
base_csvfile.close()


'''
save blocks' name in list_block_name as a list
'''
def get_list_block_name():
    list_block_name=[]
    for block in list_base:
        if block['街道名称'] not in list_block_name:
            list_block_name.append(block['街道名称'])
    #print (list_block_name)
    return list_block_name
list_block_name = get_list_block_name()

def get_dict_block_population():
    '''
    save blocks' population in dict_block_population as a dict
    '''
    dict_block_population={}.fromkeys(list_block_name,0)
    for block in list_base:
        dict_block_population[block['街道名称']]=int(block['人口（人）'])
    #print (dict_block_population)
    return dict_block_population



def get_dict_block_area():
    '''
    save blocks' area in dict_block_area as a dict
    '''
    dict_block_area={}.fromkeys(list_block_name,0)
    for block in list_base:
        dict_block_area[block['街道名称']]=float(block['面积（km2）'])
    #print (dict_block_area)
    return dict_block_area



def get_dict_block_density():
    '''
    save blocks' area in dict_block_density as a dict
    '''
    dict_block_density={}.fromkeys(list_block_name,0)
    for block in list_base:
        dict_block_density[block['街道名称']]=float(block['人口密度（万人/km2）'])
    #print (dict_block_density)
    return dict_block_density
