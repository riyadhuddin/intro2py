---
title: "Intro to python basics"
date: 2021-11-22T03:50:13+06:00
draft: false
weight: 5
pre: "<b>0. </b>"
---
### Introduction to python with Bangladesh Liberation War
<a href=".."><img src="../static/images/iacdrops.png"></a>
<span style="color: Skyblue;"> <b> Don't know why but I love revisiting my each skills atleast once during every year October, November </span> 

<b> This python repo is the result of doing so. Use this for programming Education purposes only. Some info used here may not be accurate as they are used from wiki and they keep changing. Also, numbers are imaginary and did not use any ranking or titles to our national heroes. As ranking does not matter to them, they are most loved and respected. But please if you find anything inappropriate remembers to issue your comment.

<span style="color: maroon;">Variable holds data/value for further actions. Variable name can't start with number and symbol except underscore.
Variable name should be meaningful and value can be fixed, changeable such as we can add,remove and reassign them.</span> 


```python
bd_lib = 1971 #int type variable can't have fractrion
print(bd_lib)
```

    1971
    




```python
war_mdays = 8.20 #float type variable
war_mdays
```




    8.2




```python
country_name = "Bangladesh" #string type variable, can use single/multi quote
East_pak = 1 #boolean type
West_pak = 0
winner = East_pak > West_pak # 1 is greater than 0 so it return True which is boolean
print("Bangladesh is winner:",winner)
```

    Bangladesh is winner: True
    


```python
list_sec = [1,2,3,4,5,6,7,8,9,10,11] # list type
list_sec
```




    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]




```python
tuple_sec_hq = ('Harina','Melaghar','Sreemangal','Karimganj','Banshtola','Burimari','Tarangpur ','Benapole','Hasnabad','Naval','Teldhala')#tuple type
tuple_sec_hq
```




    ('Harina',
     'Melaghar',
     'Sreemangal',
     'Karimganj',
     'Banshtola',
     'Burimari',
     'Tarangpur ',
     'Benapole',
     'Hasnabad',
     'Naval',
     'Teldhala')




```python
lib_outcome = 'West Pakistan was defeated with the allied help from india, And renamed as Bangladesh'
init_war_cmd_dict = {'Sector':'Sector Commander',
                     '1':['Maj Ziaur Rahman','Captain Rafiqul Islam'],
                     '2':['Major Khaled Mosharraf','Major ATM Haider'],
                     '3':['Major K. M. Shafiullah','Captain A. N. M. Nuruzzaman'],
                     '4':['Major Chitta Ranjan Dutta','Captain A Rob'],
                     '5':' Major Mir Shawkat Ali',
                     '6':'Wing Commander M Khademul Bashar',
                     '7':['Major Nazmul Huq','Major Quazi nooruzzaman'],
                     '8':['Major Abu Osman Chowdhury',' Major Abul Manzoor'],
                     '9':['Major M. A. Jalil','Major MA Manzur','Major Joynal Abedin '],
                     '10':'Commander HQ BD Forces ','11':'Major Abu Taher'} # dictionary type consisting of key, value pair, multiple or single value for a key is reasonable
lib_outcome
```




    'West Pakistan was defeated with the allied help from india, And renamed as Bangladesh'




```python
init_war_cmd_dict
```




    {'Sector': 'Sector Commander',
     '1': ['Maj Ziaur Rahman', 'Captain Rafiqul Islam'],
     '2': ['Major Khaled Mosharraf', 'Major ATM Haider'],
     '3': ['Major K. M. Shafiullah', 'Captain A. N. M. Nuruzzaman'],
     '4': ['Major Chitta Ranjan Dutta', 'Captain A Rob'],
     '5': ' Major Mir Shawkat Ali',
     '6': 'Wing Commander M Khademul Bashar',
     '7': ['Major Nazmul Huq', 'Major Quazi nooruzzaman'],
     '8': ['Major Abu Osman Chowdhury', ' Major Abul Manzoor'],
     '9': ['Major M. A. Jalil', 'Major MA Manzur', 'Major Joynal Abedin '],
     '10': 'Commander HQ BD Forces ',
     '11': 'Major Abu Taher'}




```python
East_pakistan = West_pakistan = "Pakistan" #shared same Name value during 1947-1971
East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 # possitive reward for action
muscleX = "Muscle deployed in Year: {year} Bangladesh:{} Pakistan:{} India: {}"
```


```python
def basic_reward():
    #East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 ##local variable ex
    # possitive reward for action
    print(muscleX.format(East_pakistanR, West_pakistanR, indiaR, year=bd_lib))
```


```python
def military_casualities(): # all numbers are imaginary
    east_c = 4500
    west_c = 1000
    ind_c = 200
    p_east,p_west,p_ind = east_c*8.2,west_c*8.20,ind_c*13
    p_east_g = int((p_east/3) ** 1.6) * 0.9 * 0.96 #the equation of dumb :p
    print("{:-^80s}".format("This numbers are imaginary, so please don't misread me"))
    print("Bangladesh Military casualities:{}".format(p_east))
    print("Pakistani casualites: {}".format(p_west))
    print("Indian casualties: {}".format(p_ind))
    print("Total Military Casualities: {}".format(p_east+p_ind+p_west))
    print("Bangladesh Total casualities:{: ^15}".format(int(p_east_g)))
```


```python
def war_data():
    bd_flag = '7aC87ben7aC87bep'#base64
    print("{:-^100s}".format("Information About 1971 War"))
    print(country_name)
    print(lib_outcome)
#default
```


```python
# """ Comment out to write python scripts or to implement your custom code, CTRL+A and then CTRL+/ """
# %%writefile scripts/basics.py
# import base64
# bd_lib = 1971 #int type variable can't have fractrion
# war_mdays = 8.20 #float type variable
# country_name = "Bangladesh" #string type variable, can use single/multi quote
# East_pak = True #boolean type
# West_pak = False
# winner = East_pak > West_pak
# list_sec = ['1','2','3','4','5','6','7','8','9','10','11'] # list type
# tuple_sec_hq = ('Harina','Melaghar','Sreemangal','Karimganj','Banshtola','Burimari','Tarangpur ','Benapole','Hasnabad','Naval','Teldhala')#tuple type
# lib_outcome = 'West Pakistan was defeated with the allied help from india, And renamed as Bangladesh'
# init_war_cmd_dict = {'Sector':'Sector Commander',
#                      '1':['Maj Ziaur Rahman','Captain Rafiqul Islam'],
#                      '2':['Major Khaled Mosharraf','Major ATM Haider'],
#                      '3':['Major K. M. Shafiullah','Captain A. N. M. Nuruzzaman'],
#                      '4':['Major Chitta Ranjan Dutta','Captain A Rob'],
#                      '5':' Major Mir Shawkat Ali',
#                      '6':'Wing Commander M Khademul Bashar',
#                      '7':['Major Nazmul Huq','Major Quazi nooruzzaman'],
#                      '8':['Major Abu Osman Chowdhury',' Major Abul Manzoor'],
#                      '9':['Major M. A. Jalil','Major MA Manzur','Major Joynal Abedin '],
#                      '10':'Commander HQ BD Forces ','11':'Major Abu Taher'} # dictionary type consisting of key, value pair, multiple or single value for a key is reasonable

# East_pakistan = West_pakistan = india = 0 #initialize reward value of ther war with zero to all
# East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 # possitive reward for action
# muscleX = "Muscle deployed in Year: {year} Bangladesh:{} Pakistan:{} India: {}"
# def basic_reward():
#     #East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 ##local variable ex
#     # possitive reward for action
#     print(muscleX.format(East_pakistanR, West_pakistanR, indiaR, year=bd_lib))
# def military_casualities(): # all numbers are imaginary
#     east_c = 4500
#     west_c = 1000
#     ind_c = 200
#     p_east,p_west,p_ind = east_c*8.2,west_c*8.20,ind_c*13
#     p_east_g = int((p_east/3) ** 1.6) * 0.9 * 0.96 #the equation of dumb :p
#     print("{:-^80s}".format("This numbers are imaginary, so please don't misread me"))
#     print("Bangladesh Military casualities:{}".format(p_east))
#     print("Pakistani casualites: {}".format(p_west))
#     print("Indian casualties: {}".format(p_ind))
#     print("Total Military Casualities: {}".format(p_east+p_ind+p_west))
#     print("Bangladesh Total casualities:{: ^15}".format(int(p_east_g)))
# def war_data():
#     bd_flag = '7aC87ben7aC87bep'#base64
#     print("{:-^100s}".format("Information About 1971 War"))
#     print(country_name)
#     print(lib_outcome)
# #default
```


```python
valiant_hero = ['Mohiuddin Jahangir', 'Hamidur Rahman','Muhammad Mustafa Kamal','Mohammad Ruhul Amin','Flight Lieutenant Matiur Rahman','Munshi Abdur Rouf','Noor Mohammad Sheikh']
valiant_hero[0:4]#index slicing
```




    ['Mohiuddin Jahangir',
     'Hamidur Rahman',
     'Muhammad Mustafa Kamal',
     'Mohammad Ruhul Amin']



<span style="color: green;"><b>Please add by yourself and incase pr me I will merge here</span> 
1. Bir Uttom
2. Bir Bikrom
3. Bir Protik


```python
valiant_hero[0]= 'Captain Mohiuddin Jahangir' # replace value
valiant_hero[0:2]
```




    ['Captain Mohiuddin Jahangir', 'Hamidur Rahman']




```python
list_sec_hq =  [sect for sect in tuple_sec_hq if sect != 'Dhaka']
list_sec_hq
```




    ['Harina',
     'Melaghar',
     'Sreemangal',
     'Karimganj',
     'Banshtola',
     'Burimari',
     'Tarangpur ',
     'Benapole',
     'Hasnabad',
     'Naval',
     'Teldhala']




```python
sect_list = [x for x in range (11) if x % 2 == 0]
sect_list
```




    [0, 2, 4, 6, 8, 10]




```python
# for x in country_name:
#     w_country_name.append('people republic of Bangladesh')
w_country_name = []
w_country_name = country_name
```


```python
w_country_name
```




    'Bangladesh'




```python
init_war_cmd_dict.items()
```




    dict_items([('Sector', 'Sector Commander'), ('1', ['Maj Ziaur Rahman', 'Captain Rafiqul Islam']), ('2', ['Major Khaled Mosharraf', 'Major ATM Haider']), ('3', ['Major K. M. Shafiullah', 'Captain A. N. M. Nuruzzaman']), ('4', ['Major Chitta Ranjan Dutta', 'Captain A Rob']), ('5', ' Major Mir Shawkat Ali'), ('6', 'Wing Commander M Khademul Bashar'), ('7', ['Major Nazmul Huq', 'Major Quazi nooruzzaman']), ('8', ['Major Abu Osman Chowdhury', ' Major Abul Manzoor']), ('9', ['Major M. A. Jalil', 'Major MA Manzur', 'Major Joynal Abedin ']), ('10', 'Commander HQ BD Forces '), ('11', 'Major Abu Taher')])




```python
for key, value in init_war_cmd_dict.items():
    print(key,":",value)
```

    Sector : Sector Commander
    1 : ['Maj Ziaur Rahman', 'Captain Rafiqul Islam']
    2 : ['Major Khaled Mosharraf', 'Major ATM Haider']
    3 : ['Major K. M. Shafiullah', 'Captain A. N. M. Nuruzzaman']
    4 : ['Major Chitta Ranjan Dutta', 'Captain A Rob']
    5 :  Major Mir Shawkat Ali
    6 : Wing Commander M Khademul Bashar
    7 : ['Major Nazmul Huq', 'Major Quazi nooruzzaman']
    8 : ['Major Abu Osman Chowdhury', ' Major Abul Manzoor']
    9 : ['Major M. A. Jalil', 'Major MA Manzur', 'Major Joynal Abedin ']
    10 : Commander HQ BD Forces 
    11 : Major Abu Taher
    

 <b> Why two state that are supposed to rule this subcontinent goes on war and tore apart?
 #
</br> Instead of utilizing west technological advancement and east huge talent to empower the country they brought such brutal experience upon, why?
#
<b> West lust for power, controlling, colonizing mentality and east yearning to get rid of poverty, basic expectancy!! Of course, it was the cause of birth for them in the first place yet they didn't mature and progress. The whole region was looking for an opportunity to subdivide these two as of geopolitical situation and elite knowledge and behavior. None could withstand the blow as West won't mend her manner and East was already on the verge also Eastern Journalism and cultural activities already shed a light on the upcoming contrast, East suffered not less than multiple eras of deprivation. It was already deep-rooted with the 1970 general election and the tree started its first bloom with the 7th March Speech of Bangabandhu Sheikh Mujibur Rahman.


```python
#@riyadhuddin
e_sit = 313
_East = 167
_West = 146 # Lets simplified for calculation as individuals and few other parties may not join them 
if _East < _West:
    print("West will Rule")
else:
    print("East will Rule")
    
```

    East will Rule
    

<b>But the lust and ego of Yahya Khan and others from the west didn't let the East rule, my low IQ does not help to understand if you wish to sit like a stone Why do you even have to offer democracy instead of idiocracy!! 


```python
waste = 'It does no matter, at all costs only we will rule'
if _East > (e_sit/2 + 1):
    if 'rule' in waste:
        print("Even West didn't win but will rule, as west is more mature. Okay!!")
        if _West < (e_sit/2 + 1):
            print("East will fight for the right")
elif _West > (e_sit/2 + 1):
    print("West realy win")
else:
    print("Draw")
```

    Even West didn't win but will rule, as west is more mature. Okay!!
    East will fight for the right
    


```python

```

