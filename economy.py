#-*- coding:utf-8 -*-

import csv
import base
import greenland

'''
deal with economy.csv
'''
#read economy.csv
economy_csvfile=open('./economy.csv','r',encoding='utf-8')
dict_economy = csv.DictReader(economy_csvfile)
list_economy = []
for item in dict_economy:
    list_economy.append(item)
economy_csvfile.close()
#print (list_economy)

'''
save blocks' name in list_block_name as a list
'''
list_block_name=[]
for community in list_economy:
    if community['所属街道'] not in list_block_name:
        list_block_name.append(community['所属街道'])
#print (list_block_name)

list_temporary = []
for num in range(len(list_block_name)):
    list_temporary.append(None)
    list_temporary[num]=[]

for item in list_economy:
    indexnum=list_block_name.index(item['所属街道'])
    list_temporary[indexnum].append(item)

#print (list_temporary)
##################################
#到目前为止，将小区的信息按所属街道分类存在了一个列表里。


listC=[]
listL=[]
listV=[]
for length in range(len(list_temporary)):
    num = sumC = sumL = sumV= 0
    for item in list_temporary[length]:
        num+=1
        sumC+=float(item['最近公园距离（米）'])
        sumL+=float(''.join(list(item['小区绿化覆盖率'])[:-1]))
        sumV+=float(item['景观视线评价'])
    averageC=sumC/num
    averageL=sumL/num
    averageV=sumV/num
    listC.append(averageC)
    listL.append(averageL)
    listV.append(averageV)
#print(listC)
#print(listL)
#print(listV)

#average of distance ogf park
C_average = sum(listC)/len(listC)

#average of coverage of greenland
molecule= 0
denominator= 0
mo_dict = greenland.get_dict_block_greenland()
de_dict = base.get_dict_block_area()
#print (mo_dict)
#print (de_dict)
for item in mo_dict:
    #print (mo_dict[item])
    molecule += mo_dict[item]
    #print ('^^^^^^^^^^^^^^^')
    #print (molecule)
 
for item in de_dict:
    #print (de_dict[item])
    denominator += de_dict[item]
    #print ('***************')
    #print (denominator)
L_average = molecule / denominator /1000000 * 100
#print(L_average)

#average of score of sence
V_average = sum(listV)/len(listV)

def get_dict_park_value():
    '''
    calculate park value
    X1=-0.054*sum{(Ci-C)/C}
    '''
    dict_park_value = {}
    for block in list_block_name:
        Ci_C = sumCi_C = 0
        for community in list_economy:
            if (community['所属街道'] == block):
                Ci_C = (float(community['最近公园距离（米）']) - \
                C_average) / C_average
                sumCi_C += Ci_C
                #print ("Ci-C",Ci_C)
                #print (float(community['最近公园距离（米）']))
                #print (listC[list_block_name.index(block)])
                #print ("sum(Ci-C)",sumCi_C)
        #print('***************************************')
        #print (Ci_C,sumCi_C)
        dict_park_value[block] = -0.054 * sumCi_C
    return dict_park_value



def get_dict_coverage_value():
    '''
    calculate sence value
    X2=0.041*sum{(Vi-V)/V}
    '''
    dict_coverage_value = {}
    for coverage in list_block_name:
        Li_L = sumLi_L = 0
        for community in list_economy:
            if (community['所属街道'] == coverage):
                Li_L = (float(''.join(list(community['小区绿化覆盖率'])[:-1])) - \
                L_average) / L_average
                sumLi_L += Li_L
                #print ("Li-L",Li_L)
                #print (float(community['景观视线评价']))
                #print (listL[list_block_name.index(block)])
                #print ("sum(Li-L)",sumLi_L)
        #print('***************************************')
        #print (Li_L,sumLi_L)
        dict_coverage_value[coverage] = 0.041 * sumLi_L
    return dict_coverage_value



def get_dict_sence_value(V_average=25):
    '''
    calculate sence value
    X2=0.041*sum{(Vi-V)/V}
    '''
    dict_sence_value = {}
    for sence in list_block_name:
        Vi_V = sumVi_V = 0
        for community in list_economy:
            if (community['所属街道'] == sence):
                Vi_V = (float(community['景观视线评价']) - \
                V_average) / V_average
                sumVi_V += Vi_V
                #print ("Vi-V",Vi_V)
                #print (float(community['景观视线评价']))
                #print (listV[list_block_name.index(block)])
                #print ("sum(Vi-V)",sumVi_V)
        #print('***************************************')
        #print (Vi_V,sumVi_V)
        dict_sence_value[sence] = 0.047 * sumVi_V
    return dict_sence_value


