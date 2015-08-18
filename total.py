#-*- coding:utf-8 -*-

import base
import greenland
import economy
import society



#list_BN：街道名的列表
list_BN = base.get_list_block_name()


#normalize every dictionary
def normalize(dictionary):
    #print (dictionary)
    list_down = sorted(dictionary, key=dictionary.get, reverse=True)
    minimal = dictionary[list_down[len(list_down)-1]]
    maximal = dictionary[list_down[0]]
    for item in dictionary:
        dictionary[item] = (dictionary[item] - minimal) / (maximal - minimal)
    #print (minimal)
    #print (maximal)
    #print (dictionary)
    return dictionary

#城市绿地生态效能
def urban_greenland_ecology(
    Qc=0.625, Tc=1024.125, Qo2=1.667, Po2=650,\
    tree=greenland.conifer_broadleaf['conandbro'], \
    R=4, P=1317.3, E=697.4, C=0.2, \
    t=0.038, W=0.012, p=0.462, T=600):
    dict_ecology = {}
    dict1 = greenland.oxygen_balance_value(Qc, Tc, Qo2, Po2)
    #print (dict1)
    dict2 = greenland.mitigate_pollution_value(tree)
    #print (dict2)
    dict3 = greenland.conserve_water_value(R, P, E, C)
    #print (dict3)
    dict4 = greenland.regulate_climate_value(t, W, p, T)
    #print (dict4)

    for name in list_BN:
        dict_ecology[name] = dict1[name] + dict2[name] + dict3[name] + dict4[name]
    #print(dict_ecology)
    dict_ecology = normalize(dict_ecology)

    return dict_ecology



#城市绿地经济效能
def urban_greenland_economy(x1=0.6,x2=0.3,x3=0.1):
    dict_economy = {}
    dict1 = economy.get_dict_park_value()
    #print (dict1)
    dict2 = economy.get_dict_coverage_value()
    #print (dict2)
    dict3 = economy.get_dict_sence_value(V_average=25)
    #print (dict3)

    for name in list_BN:
         dict_economy[name] = x1 * dict1[name] + x2 * dict2[name] + x3 * dict3[name]

    dict_economy = normalize(dict_economy)
    
    return dict_economy



#城市绿地社会效能
def urban_greenland_society():
    dict_society = society.socefficiency_value()

    dict_society = normalize(dict_society)
    
    return dict_society



#城市绿地综合效能
def urban_greenland_complex(y1=0.4, y2=0.15, y3=0.35):
    dict_complex = {}
    dict1 = urban_greenland_ecology()
    #print dict1
    dict2 = urban_greenland_economy()
    #print dict2
    dict3 = urban_greenland_society()
    #print dict3
    for name in list_BN:
        dict_complex[name] = y1 *dict1[name] + y2 * dict2[name] + y3 * dict3[name]

    return dict_complex
