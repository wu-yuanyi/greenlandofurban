#-*- coding:utf-8 -*-

import csv
import base


conifer_broadleaf = \
{'conifer':[0.118,0.18,33.2],'conandbro':[0.152,0.263,21.65],'broadlef':[0.087,0.345,10.11]}

population=[600,420,170]



def get_dict_block_greenland():
    '''
    deal with greenland.csv
    '''
    #read greenland.csv
    greenland_csvfile=open('./greenland.csv','r',encoding='utf-8')
    dict_greenland = csv.DictReader(greenland_csvfile)
    list_greenland=[]
    for item in dict_greenland:
        list_greenland.append(item)
    greenland_csvfile.close()
    #print (list_greenland)

    '''
    save blocks' name in list_block_name as a list
    '''
    list_block_name=[]
    for greenland in list_greenland:
        if greenland['街道名称'] not in list_block_name:
            list_block_name.append(greenland['街道名称'])
    #print (list_block_name)

    '''
    save blocks' greenland in dict_block_greenland as a dict
    '''
    dict_block_greenland={}.fromkeys(list_block_name,0)
    #print(dict_block_greenland)
    for area in list_greenland:
        dict_block_greenland[area['街道名称']]+=float(area['绿地面积（m2）'])
    #print (dict_block_greenland)
    return dict_block_greenland



def oxygen_balance_value(Qc=0.625,Tc=1024.125,Qo2=1.667,Po2=650, \
                         S=get_dict_block_greenland()):
    '''
    calculate oxygen balance value
    B1=S/10000*Qc*Tc+S*Qo2*Po2
    '''
    dict_oxygen_balance_value = S
    for key in dict_oxygen_balance_value:
        dict_oxygen_balance_value[key] = dict_oxygen_balance_value[key]/10000 * \
            (Qc * Tc + Qo2 * Po2)
    #print (dict_oxygen_balance_value)
    return dict_oxygen_balance_value



def mitigate_pollution_value(tree=conifer_broadleaf['conandbro'], \
                             S=get_dict_block_greenland()):
    '''
    calculate mitigate air pollution value
    B2=S/10000*(Q*Fti+Q*Fti+Q*Fti)[SO2,NOx,dust]
    '''
    dict_mitigate_pollution_value = S
    for key in dict_mitigate_pollution_value:
        dict_mitigate_pollution_value[key] = dict_mitigate_pollution_value[key]/10000 * \
            (tree[0]*population[0] + tree[1]*population[1] + tree[2]*population[2])
    #print (dict_mitigate_pollution_valueprint)
    return dict_mitigate_pollution_value



def conserve_water_value(R=4, P=1317.3, E=697.4, C=0.2, \
                         S=get_dict_block_greenland()):
    '''
    calculate conserve water value
    B3=S/10000*R*(P-E-C*P)
    '''
    dict_conserve_water_value = S
    for key in dict_conserve_water_value:
        dict_conserve_water_value[key] = dict_conserve_water_value[key]/10000 * \
            R * (P- E - (C * P))
    #print (dict_conserve_water_value)
    return dict_conserve_water_value



def regulate_climate_value(t=0.038, W=0.012, p=0.462, T=600, \
                           S=get_dict_block_greenland()):
    '''
    calculate regulate climate value
    B4=S*t*W*P*T
    '''
    dict_regulate_climate_value = S
    for key in dict_regulate_climate_value:
        dict_regulate_climate_value[key] = dict_regulate_climate_value[key] * \
            t * W * p *T
    #print (dict_regulate_climate_value)
    return dict_regulate_climate_value


"""
def ecoefficiency_value():
    '''
    calculate total eco-efficiencyvalue
    '''
    dict_ecoefficiency_value = {}
    dictC1 = oxygen_balance_value()
    dictC2 = mitigate_pollution_value()
    dictC3 = conserve_water_value()
    dictC4 = regulate_climate_value()
    for key in dictC1:
        dict_ecoefficiency_value[key] = dictC1[key] + dictC2[key] + dictC3[key] + dictC4[key]
    #print (dict_ecoefficiency_value)
    return dict_ecoefficiency_value
"""
