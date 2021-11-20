import base64
#variable holds data/value for further actions
#variable name can't start with number and symbol except underscore
#variable name should be meaningful, variable value can be fixed and changeable such as we can add,remove and reassign them
bd_lib = 1971 #int type variable can't have fractrion
war_mdays = 8.20 #float type variable
country_name = "Bangladesh" #string type variable, can use single/multi quote
East_pak = True #boolean type
West_pak = False
winner = East_pak > West_pak
list_sec = ['1','2','3','4','5','6','7','8','9','10','11'] # list type
tuple_sec_hq = ('Harina','Melaghar','Sreemangal','Karimganj','Banshtola','Burimari','Tarangpur ','Benapole','Hasnabad','Naval','Teldhala')#tuple type
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

East_pakistan = West_pakistan = india = 0 #initialize reward value of ther war with zero to all
East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 # possitive reward for action
muscleX = "Muscle deployed in Year: {year} Bangladesh:{} Pakistan:{} India: {}"
def basic_reward():
    #East_pakistanR, West_pakistanR, indiaR = 1,0.9,0.4 ##local variable ex
    # possitive reward for action
    print(muscleX.format(East_pakistanR, West_pakistanR, indiaR, year=bd_lib))
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
def war_data():
    bd_flag = '7aC87ben7aC87bep'#base64
    print("{:-^100s}".format("Information About 1971 War"))
    print(country_name)
    print(lib_outcome)
#default
