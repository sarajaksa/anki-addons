#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

#kanji list from http://www.ziggr.com/heisig/

from aqt import mw
from aqt.qt import *
from aqt.webview import AnkiWebView

heising = [
(u'Lesson 1', u'一九月五口三四七十田二日八目六'),
(u'Lesson 2', u'旭胃凹古吾唱昌晶世早旦胆凸品朋冒明呂亘'),
(u'Lesson 3', u'下丸旧自升昇上寸舌千占専卓中朝博白百'),
(u'Lesson 4', u'員貝頑句見元児勺首旬只貞的肌負頁凡万'),
(u'Lesson 5', u'右乙可具工貢項左召昭真刃切則丁町頂直刀副別有乱賄'),
(u'Lesson 6', u'貫兄好孔克子女如母了'),
(u'Lesson 7', u'外器奇光厚砂砕削汐臭小少省硝肖石多太大妙名夕'),
(u'Lesson 8', u'圧永泳炎沖河火灰涯垣活願漁魚況均圭原源湖江災埼寺州汁順沼消照水川泉測淡潮点吐土灯泊畑煩氷封時'),
(u'Lesson 9', u'安宴完寄鯉向黒字守宵尚宣貯同洞胴富墨埋里量厘'),
(u'Lesson 10', u'案杏株寛机桐苦桂枯札若朱梢植森燥相草村棚柏薄漠苗墓暮朴本妹膜末沫味未模木葉林暦枠'),
(u'Lesson 11', u'荻牛犬告狩状先洗然兆眺桃特猫黙'),
(u'Lesson 12', u'王介界狂玉金現皇合主珠針栓銑全茶柱注鎮釣呈塔銅鉢宝銘理'),
(u'Lesson 13', u'夏各格額軌客車巡処条迅前造辻逃導道迫辺輸落略連'),
(u'Lesson 14', u'運冠輝吉享軍景鯨坑高士舎周週塾熟冗壮荘亭売夢涼京'),
(u'Lesson 15', u'栄詠覚学詰訓敬計警言故語攻獄詩書詔諾談調津訂討読敗牧枚諭話'),
(u'Lesson 16', u'威域減栽載桟試式城成誠浅銭賊弐滅茂'),
(u'Lesson 17', u'越延企建肯止渉証錠是政正礎走題誕超堤定頻賦赴武歩婿歴'),
(u'Lesson 18', u'哀衣壱茨雨雲謁猿遠歌壊海皆喝渇褐乾泣競橋錦芸欠乞昆混裁刺姉姿市旨脂諮資次初商章鐘吹炊制製装霜帯滞嫡帝敵滴適天転冬瞳童曇軟背肺梅帆比敏布幅腹複帽北幌毎幕雷裏立匕嬌'),
(u'Lesson 19', u'暗韻鋭音境鏡激荒識説曽増贈脱廷凍東棟妊培賠放方芳訪亡剖坊妨望肪妄盲'),
(u'Lesson 20', u'県歳染栃燃賓'),
(u'Lesson 21', u'嫁家改確歓観記起亀許蛍権己午豪差雑蚕雌蛇習集准準焦礁詳場進遂羨鮮滝濯達奪地池逐着虫腸蝶電湯独豚虹妃美風奮包泡砲胞唯曜洋羊翌竜羽'),
(u'Lesson 22', u'意因姻悦園憶恩寡回悔患感慣憾忌恐串恵憩固庫悟恒慌国困志思誌床心慎想息惰団壇忠庁庭店添悼忍認泌必怖慕忘忙磨麻愉憂惑曰応憎'),
(u'Lesson 23', u'愛扱育允我会怪戒拐械拡殻獲掛括看揮棄技犠義議及吸去拠桑刑型掲携茎軽撃研互護広抗拘更硬鉱唆才採菜在材財坂史始指支枝肢至持治室捨寂手受授拾充銃叔淑奨将抄招丈推隻接設双操窓存損妥打怠胎台拓担致挑爪提摘撤奴怒投搭督乳乃拍抜反板販批鼻描浮払返弁抱法没摩又抹友雄揚吏流硫到'),
(u'Lesson 24', u'沿鉛翁岩岐公崎山出松訟拙谷炭峠入頒貧分崩密蜜裕容溶欲浴嵐込'),
(u'Lesson 25', u'往加架賀懐街勧敢環還規巨拒協脅径渓堅賢功行衡最撮賛残死耳失取殊趣従瞬殉掌裳賞常殖職臣征聖潜葬臓蔵待替濁男恥置徴懲聴徹迭鉄徒努党堂得徳寧波破婆買罰彼披皮被微姫夫扶復募慢漫役覧律力臨励列劣烈裂労脇'),
(u'Lesson 26', u'委移稲奥稼穫笠季菊救求球筋菌稿香穀策笹算私漆愁秀秋称笑粧粋数税稚築竹秩程等答筒透粘箱秘筆秒粉米穂簿迷誘様利梨粒糧類楼和'),
(u'Lesson 27', u'位依億化仮何佳花荷貨儀久休傾傑件健個佐座催傘仕使侍囚住宿俊傷信人仁畝仙僧側俗卒他体袋貸代但値仲賃停偵伝倒内肉任倍伯伐付府符腐侮伏仏丙柄便保倣褒傍優悠例償'),
(u'Lesson 28', u'以営液瓦喚換宮似善年瓶併幣弊匁夜融塚'),
(u'Lesson 29', u'握易屋居局屈掘啓肩戸雇顧刷施賜尺尽据扇旋層択沢遅昼泥尼尿物塀房堀勿戻訳遊履旅涙炉漏'),
(u'Lesson 30', u'尉慰押果菓課款禁襟甲祭察擦祉視示軸社宗祝伸申崇捜挿袖宙抽笛届奈岬油由裸礼神祥福'),
(u'Lesson 31', u'伊穏科画祈急曲斤近君群康詐作昨暫歯事質儒需所浄侵寝浸尋図誓逝斥析折雪漸訴掃曹槽漕争遭耐逮端断哲斗唐当糖備婦庸用両料録満'),
(u'Lesson 32', u'巻暁券圏錯散芝遮借庶勝焼席惜昔措渡度藤謄廿之杯伴判半版畔否不噴墳憤片乏奔'),
(u'Lesson 33', u'引汚帰弓朽強矯誇巧弘号写弱柔族第知智弔弟班費沸務矛霧矢与'),
(u'Lesson 34', u'渦禍過較滑官棺管距峡挟教狭交効孝校考拷骨師射煮者謝暑渚署身帥髄践促足著跳追賭踏父躍路露老猪諸'),
(u'Lesson 35', u'阿院隠階隔岳陥丘究窮空窪穴控降際阪搾障深陣随窃堕隊探窒陳墜突陪浜附兵陛防窯陽隣'),
(u'Lesson 36', u'維縁絵幾機紀級給緊繰係系経継結懸絹弦玄後紅絞細索糸紫慈滋磁終縦縮緒紹織紳線繕総続孫畜蓄締統縄納縛繁紛紡綿網約幽幼擁羅絡緑累練'),
(u'Lesson 37', u'宛印怨苑卸危擬疑却脚興凝御通犯範貿命厄柳勇踊卵留領令冷鈴零齢腕服'),
(u'Lesson 38', u'飲塩温餓慨概監鑑眼喜既飢銀血限鼓酵酷恨根皿酸爵酌酒樹酬飾食酢酔盛節即尊退短盗豆頭酉配豊飽盆娘盟猛猶養酪濫良浪朗飯館'),
(u'Lesson 39', u'梓亥劾該核刈寒希糾凶叫胸呼幸刻宰殺辞執収術述純壌嬢譲醸新薪親辛勢坪鈍熱卑碑避菱評平壁報睦離陸陵'),
(u'Lesson 40', u'華害割轄漢喫勤謹契潔憲債産実寿春乗剰情垂睡錘姓性星清牲生請青静積籍績責素奏泰嘆鋳漬椿毒難拝俵表俸奉峰縫棒晴精隆麦'),
(u'Lesson 41', u'陰煙価鎌含琴吟栗兼嫌献謙腰今序西遷南楠念標漂票覆野予預要廉'),
(u'Lesson 42', u'偉緯違衛閲快開閣簡間閑韓決侯候罪潤創倉闘俳排輩閥悲扉非聞閉問門欄'),
(u'Lesson 43', u'芋宇刊干幹汗肝岸勲薫倹剣検軒険斜種重叙徐除衝瀬整疎束速勅塗途働動余頼'),
(u'Lesson 44', u'医疫欧殴仰区迎疾匠症枢澄痴痛登痘匿廃発疲匹病癖抑痢僚寮療'),
(u'Lesson 45', u'影映英艶央横黄蚊楽顔形彩済斎剤参惨赦修渋粛彰色診須杉斉赤跡摂絶対彫珍把蛮肥彦文変膨紋薬率塁恋湾'),
(u'Lesson 46', u'遺勘堪甘基旗期棋貴欺遣碁紺甚媒舞某謀無'),
(u'Lesson 47', u'異宜供共恭業顕洪港査湿助畳繊選祖租粗組阻殿爆普譜並暴僕撲翼霊'),
(u'Lesson 48', u'亜悪囲井円解角構溝耕講購再冊触典偏編遍倫輪論'),
(u'Lesson 49', u'浦郭蒲郷響郡郊婚氏紙低底抵邸部舗捕補邦民眠郵廊郎都'),
(u'Lesson 50', u'瓜艦幻孤弧后航伺司嗣詞舟衆循盾船鍛段艇逓派舶搬般盤脈飼'),
(u'Lesson 51', u'暇革気汽極靴呉娯誤妻承蒸衰声衷沈覇函飛敷繭面来益'),
(u'Lesson 52', u'為牙芽雅偽邪釈審喪宅託帳張脹長展髪藩番尾翻毛耗'),
(u'Lesson 53', u'烏援岡緩缶逆挙愚偶遇隅鶏厳綱鋼剛墾懇鎖桜就獣象嘱戦禅塑巣像属単弾暖鳥蔦島陶悩脳鳩晩媛勉鳴免誉揺謡猟逸鶴'),
(u'Lesson 54', u'駅騎戯虐虚驚駆駒虞熊慶劇験虎鹿薦騒駄態駐騰篤能馬膚慮虜麗'),
(u'Lesson 55', u'演塊関鬼魂咲襲醜辱唇娠振震送辰寅濃農魔魅'),
(u'Lesson 56', u'卯丑箇嚇潟且遵藻丹朕屯罷雰巳癒隷錬'),
]

class HeisingList():
    
    def __init__(self):
        self.mw = mw
        self.models = self.mw.col.models.all()
        
        self.window = QDialog(mw)
        self.window.setWindowTitle('List of Words - Choose')
        self.window.layout = QVBoxLayout(self.window)
        self.webView = AnkiWebView()
        self.window.layout.addWidget(self.webView)
        
        report = self.getHeisingStats()
        self.webView.stdHtml(report)
        
        self.window.show()
        self.window.exec_()
        
    def getHeisingStats(self):
        string = ""
        new, old = self.kanjiLists()
        for heisinglesson in heising:
            string = string + "<b><h2>" + heisinglesson[0] + "</b></h2><p style='font-size: 200%;'>"
            for kanji in heisinglesson[1]:
                if kanji in old:
                    string = string + "<span style='color: green;'>" + kanji + "</span>"
                elif kanji in new:
                    string = string + "<span style='color: yellow;'>" + kanji + "</span>"
                else:
                    string = string + "<span style='color: red;'>" + kanji + "</span>"
            string = string + "</p>"
        return string

    def kanjiLists(self):
        new = self.kanjiList("mid:1432286497707 is:new")
        new = set("".join(new))
        old = self.kanjiList("mid:1432286497707 -is:new")
        old = set("".join(old))
        return new, old
        
    def kanjiList(self, searchTerm):
        words = set()
        ids = mw.col.findNotes(searchTerm)
        for i in ids:
            note_id = mw.col.getNote(i)
            kanji = note_id.fields[0]
            words.add(kanji)
        return words

#Menu item
#################################
mw.action = QAction("Heising Stats", mw)
mw.action.triggered.connect(HeisingList)
mw.form.menuTools.addAction(mw.action)
