#!/usr/bin/python
# -*- coding: utf-8 -*-
from transitions.extensions import GraphMachine

import urllib
import webbrowser
url1="http://www.atmovies.com.tw/showtime/t06608/a06/"
url2="http://www.atmovies.com.tw/showtime/t06609/a06/"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'hotels'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'top 5 review'
    
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'top 5 price'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'top 5 near ncku'    
    
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'price'

    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'location'

    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == 'review'
    
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == 'location'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == 'review'

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == 'price'    

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'movie theater'

    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == 'guopin'

    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == 'viewshow'

    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == 'now trending'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'tainan sights'

    def is_going_to_state17(self, update):
        text = update.message.text
        return text.lower() == 'one day tour'

    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == 'dine'

    def on_enter_state1(self, update):
        update.message.reply_text("Choose:\n\n1.Top 5 review\n2.Top 5 price\n3.Top 5 near ncku")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
    
    def on_enter_state4(self, update):
        update.message.reply_text("1.Red House & Old Lane(Exceptional 9.7)\nPhone: 0968 377 007\n2.See Love B&B(Exceptional 9.6)\n3.Lucky House(wonderful 9.3)\n4.Tainan Quiet Backpacker(Wonderful 9.4)\n5.For Room(Wonderful 9.4)")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("1.Light Hostel(1000NTD for double room)\nPhone:06 224 0555\n2.Old Man Captain(1000NTD for double room)\nPhone: 0982 697 940\n3.Fuqi Hostel(1100NTD for double room)\nPhone: 06 703 4543\n4.Famous Hotel(1380NTD for double room)\nPhone: 06 226 6111\n5.Fude Lime Hotel(1380NTD for double room)\nPhone: 06 221 6846")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state6(self, update):
        update.message.reply_text("1.Kindness Hotel(No. 97, Section 2, Minquan Road , 700 Tainan, Taiwan)\nPhone: 06-225-3377\n2.ECFAHOTEL-Tainan(8F, No. 145, Section 2, Zhongyi Road, 700 Tainan, Taiwan)\nPhone: 06-227-5566\n3.Fuward Hotel(No. 28, Section 2, Zhongyi Road, 70041 Tainan, Taiwan)\nPhone: 06-225-1000\n4.City Place Hotel(No. 132, Section 2, Zhongyi Road, 70050 Tainan, Taiwan)\n5.Tainan Quiet Backpacker(No. 19, Lane158, Section 2, Zhongyi Road, 700 Tainan, Taiwan)")
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        update.message.reply_text("1.Red House & Old Lane(3600NTD for 5 people family room)\n\n2.See Love B&B(1500NTD for double room)\n\n3.Lucky House(1000NTD for double room)\n\n4.Tainan Quiet Backpacker(1500NTD for triple room)\n\n5.For Room(1480NTD for double room)")
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_text("1.Red House & Old Lane(No.18-1, Ln. 317, Sec. 2, Minzu Rd., West Central Dist., 700 Tainan, Taiwan)\n\n2.See Love B&B(No. 321, Kangle Street, 700 Tainan, Taiwan)\n\n3.Lucky House(No. 7, Lane 79, Section 2, Haian Road, 700 Tainan, Taiwan)\n\n4.Tainan Quiet Backpacker(No. 19, Lane158, Section 2, Zhongyi Road, 700 Tainan, Taiwan)\n\n5.For Room(No. 3, Donghe Road, 701 Tainan, Taiwan)")
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_enter_state9(self, update):
        update.message.reply_text("1.Light Hostel(Excellent 8.8)\n\n2.Old Man Captain(Excellent 8.7)\n\n3.Fuqi Hostel(Very Good 8.4)\n\n4.Famous Hotel(Good 7.8)\n\n5.Fude Lime Hotel(6.5)")
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_enter_state10(self, update):
        update.message.reply_text("1.Light Hostel(No. 20, Lane 309, Youai Street, 700 Tainan, Taiwan)\n\n2.Old Man Captain(No. 2, Section 2, Beimen Road, 701 Tainan, Taiwan)\n\n3.Fuqi Hostel(2F., No. 76, Zhongzheng Road, 70048 Tainan, Taiwan)\n\n4.Famous Hotel(No. 150-1, Section 2, Yongfu Road, 700 Tainan, Taiwan)\n\n5.Fude Lime Hotel(No. 243, Kangle Street, 700 Tainan, Taiwan)")
        self.go_back(update)

    def on_exit_state10(self, update):
        print('Leaving state10')

    def on_enter_state11(self, update):
        update.message.reply_text("1.Kindness Hotel(Superb 9.2)\n\n2.ECFAHOTEL-Tainan(Good 7.7)\n\n3.Fuward Hotel(Fabulous 8.7)\n\n4.City Place Hotel(Fabulous 8.8)\n\n5.Tainan Quiet Backpacker(Superb 9.4)")
        self.go_back(update)

    def on_exit_statE11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        update.message.reply_text("1.Kindness Hotel(2380NTD for double room)\n\n2.ECFAHOTEL-Tainan(500NTD for double room)\n\n3.Fuward Hotel(2299NTD for double room)\n\n4.City Place Hotel(2000NTD for double room)\n\n5.Tainan Quiet Backpacker(1500NTD for triple room)")
        self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_enter_state2(self, update):
        update.message.reply_text("台南國賓影城:\n\n1.神力女超人\n2.吃吃的愛\n3.神鬼奇航：死無對證\n4.海灘救護隊\n5.異形：聖約\n6.亞瑟：王者之劍\n7.我和我的冠軍女兒\n8.玩命關頭8\n\n\n台南大遠百威秀影城:\n\n1.神鬼奇航：死無對證\n2.海灘救護隊\n3.吃吃的愛\n4.大釣哥：紀念重映\n5.神力女超人\n6.神秘家族\n7.亞瑟：王者之劍\n8.異形：聖約\n9.驗屍官\n10.我和我的冠軍女兒\n11.玩命關頭8\n12.星際異攻隊2")
        
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state13(self, update):
        update.message.reply_text("台南國賓影城:\n\n神力女超人:\n10：20\n11：00\n12：00\n13：00\n13：40\n14：40\n15：40\n16：20\n17：20\n18：20\n19：00\n20：00\n21：00\n21：40\n22：40\n23：40\nD-BOX\n11：30\n14：10\n16：50\n19：30\n22：10\n3D版\nVIP廳\n 23：10\nVIP廳\n15：10\n20：30\n12：30\n17：50\n\n吃吃的愛:\n12：30\n14：20\n16：10\n18：00\n19：50\n21：40\n23：30\n\n神鬼奇航：死無對證\n10：40\n13：00\n13：40\n14：20\n15：20\n16：00\n16：40\n17：40\n18：20\n19：00\n\n海灘救護隊\n12：50\n15：00\n17：10\n19：20\n21：30\n23：40\n\n異形：聖約\n12：50\n17：30\n22：20\n\n亞瑟：王者之劍\n15：10\n19：50\n\n我和我的冠軍女兒\nVIP廳\n16：40\n19：40\n\n玩命關頭8\nVIP廳\n14：10\n22：40\n\n")
        webbrowser.open(url1)
        self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')

    def on_enter_state14(self, update):
        update.message.reply_text("台南大遠百威秀影城: \n\n神鬼奇航：死無對證\n10：00\t11：15\t12：30\t13：45\t15：00\t16：15\t17：30\t18：45\t20：00\t21：15\t22：35\t23：45\n\n海灘救護隊\n10：25\t12：40\t15：10\t17：25\t19：55\t22：10\t00：25\n\n吃吃的愛\n10：30\t12：20\t14：10\t16：00\t17：50\t19：40\t21：30\t23：20\n\n大釣哥：紀念重映\n12：45\t17：45\n\n神力女超人\n10：10\t11：50\t12：50\t14：30\t15：05\t15：30\t17：10\t18：10\t19：50\t20：20\t20：50\t22：30\t23：00\t23：30\n\n3D版\n4DX\n11：30\t13：40\t19：00\t21：40\n\n4DX\n16：20\t00：20\n\n神秘家族\n10:15\n\n亞瑟：王者之劍\n21:45\n\n異形：聖約\n19：25\t00：10\n\n驗屍官\n17:40\n\n我和我的冠軍女兒\n14:40\n\n玩命關頭8\n數位\n10：05\n\n星際異攻隊2\n數位\n12：05")
        webbrowser.open(url2)
        self.go_back(update)

    def on_exit_state14(self, update):
        print('Leaving state14')

    def on_enter_state15(self, update):
        update.message.reply_text("1.神力女超人\n2.吃吃的愛\n3.神鬼奇航：死無對證\n4.海灘救護隊\n")
        self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')


    def on_enter_state3(self, update):
        update.message.reply_text("1.Fort Zeelandia\n2.Fort Provintia\n3.Guanziling Hot Spring\n4.Chimei Museum\n5.National Museum of Taiwan Literature\n6.Taijiang National Park\n7.National Museum of Taiwan History\n8.Tainan Flower Night Market\n9.Taiwan Confucian Temple\n10.Haishan Hall\n11.Siraya National Scenic Area\n12.Koxinga Ancestral Shrine\n13.藍晒圖文創園區 Blueprint Culture & Creative Park\n14.天壇\n15.State Temple of the Martial God\n16.Grand Matsu Temple\n17.Former Tainan Assembly Hall\n18.Tainan Wu Garden19.海安路艺术造街\n20.Tainan cultural and creative industrial park\n21.Old Tainan Magistrate Residence\n22.新営糖廠\n23.黑桥牌香肠博物馆\n24.神農老街 Shennong Street\n25.月津港灯節\n26.Soulangh Cultural Park27.New Art Park Camp\n28.Winnie the Pooh painted village\n29.Nanyingluduxin Park\n30.Cigu Salt Mountain\n\n\n If you need a tour guide please type 'one day tour' \n")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state17(self, update):
        update.message.reply_text("1.One Day Tour at Tainan Coastal Ecology\n\nStart from 9AM going to 七股瀉湖, 七股鹽田 ➜  12：00 go to 府城小吃（中餐自理）➜  after lunch go to 康那香不織布創意王國->水晶教堂 ➜  16：30 行程結束 ➜  17：30 送返高鐵/各大飯店\n\nIncluded:1.Tour bus fee\n2.Entrance ticket\n3.Insurance\n4.Bottle water\n5.導覽解說\n\n\nPrice: 1356TWD\n\nPlease go to this link https://www.kkday.com/en/product/380 to further info\n\n 2.One Day Tour at Tainan Ancient Capital and Wusanto Reservoir\n\nStart from 9AM going to ➜ Eternal Golden Castle 50 mins ➜ Tait & Co 30 mins and Anping Tree House 30 mins ➜ Tainan snacks (self-pay) 1 hr ➜ Wushantou Reservoir 1 hr ➜ Yoichi Hatta Memorial Hall 30 mins ➜ Xinhua Old Street 40 mins ➜ Return\n\nIncluded:\n1.Tour bus fee\n2.Entrance ticket\n3. 2 million NTD of travel liability and 30,000NTD medical/health insurance\n4.Bottle water\n5.導覽解說\n\n\nPrice: 1667TWD\n\nPlease go to this link https://www.kkday.com/en/product/277 to further info\n\n3.1-Day Tour to Chimei Museum in Tainan\n\nStart from 08：00 at 台南火車站上車 then 08：30 指定台南市區飯店上車 first we arrived 延平郡王祠（停留40分鐘) ➜  祀典武廟、大天后宮（停留1小時15分鐘）➜ 午餐 臺南美食虱目魚粥＋油條（停留35分鐘) ➜  奇美博物館（停留2.5小時) ➜  台南孔廟魅力商圈 美食小吃點心(米糕、福記肉圓、冰果室)（停留2.5小時）➜ 赤崁樓（停留50分鐘) ➜ 18：00 返回臺南市區飯店大廳、臺南火車站\n\nIncluded:\n1.Tour bus fee\n2.Entrance ticket\n3.Insurance\n4.Bottle water\n5.導覽解說\n6.Lunch Provided\n\n\nPrice: 1717TWD\n\nPlease go to this link https://www.kkday.com/en/product/4682 to further info")
        self.go_back(update)

    def on_exit_state17(self, update):
        print('Leaving state17')

    def on_enter_state16(self, update):
        update.message.reply_text("1.轉角餐廳 Corner Steak House\n\nAddress: No. 12, Lane 22, Daxue Road, East District, Tainan City\nOpens:\n\tThursday	11:30AM–3PM, 5:30–10PM\n\tFriday	11:30AM–3PM, 5:30–10PM\n\tSaturday	11:30AM–3PM, 5:30–10PM\n\tSunday	11:30AM–3PM, 5:30–10PM\n\tMonday	11:30AM–3PM, 5:30–10PM\n\tTuesday	11:30AM–3PM, 5:30–10PM\n\tWednesday	11:30AM–3PM, 5:30–10PM\nPhone:    06 275 4321\n\n2.星期五美式餐厅\n\nAddress: Tainan City, West Central District, Section 1, Ximen Rd, 658號\nOpens:\n\t Everyday 11AM-12AM\nPhone:   06 303 0279\n\n3.Yellow sub's Diner\n\nAddress: No. 295, Dongfeng Road, Annan District, Tainan City\nOpens:\n\tThursday	12AM–9PM, 11PM–12AM\n\tFriday	12AM–9PM, 11PM–12AM\n\tSaturday	12AM–9PM, 11PM–12AM\n\tSunday	12AM–9PM, 11PM–12AM\n\tMonday	11PM–12AM\n\tTuesday	12AM–9PM\n\tWednesday	11PM–12AM\nPhone:   06 200 4200\n\n4.亞芙餐廳 The Artful Dodger\n\nAddress: No. 181-183, Dongfeng Road, North District, Tainan City\nOpens:\n\tThursday	11AM–10PM\n\tFriday	11AM–11PM\n\tSaturday	11AM–11PM\n\tSunday  	11AM–10PM\n\tMonday   11AM–10PM\n\tTuesday	  Closed\n\tWednesday	11AM–10PM\nPhone:  06 237 0370\n\n5.單賣共和國, The Danish Republic\n\nAddress: No. 32, Alley 6, Lane 190, second section, lin sen rd., East District, Tainan City\nOpens: \n\tThursday	10AM–10PM\n\tFriday	  10AM–10PM\n\tSaturday  	10AM–10PM\n\tSunday  	10AM–10PM\nPhone:   06 208 8663")
        self.go_back(update)

    def on_exit_state16(self, update):
        print('Leaving state16')
