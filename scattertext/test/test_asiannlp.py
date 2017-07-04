# -*- coding: utf-8 -*-

from unittest import TestCase

from scattertext.AsianNLP import chinese_nlp, japanese_nlp


class TestAsianNLP(TestCase):
	def setUp(self):
		self.chinese_text = u'''总理主持召开的这场座谈会，旨在听取专家学者和企业界人士对《政府工作报告（征求意见稿）》的意见建议。胡玮炜和另外6名不同专业、领域的专家、企业家受邀参加。\n李克强对胡玮炜的细致提问始终围绕虚拟经济和实体经济，以及新旧动能转换。他关心自行车制造材料，也询问所采用的互联网技术。 “摩拜单车听起来是经营方式的革命，但基础还是自行车，还是要靠实体经济支撑。反过来，实体经济也要靠服务变革来带动。”总理指出。\n当听到这家共享智能单车企业在不到一年的时间发展为拥有80万辆自行车的规模后，李克强充分肯定此类互联网企业对实体经济的带动作用，“某个自行车企业可能就被你带活了，新兴服务业的发展给制造业创造了巨大的市场空间”。\n相关资料显示，受益于共享单车，国内传统的自行车产业正在迎来春天，至少带动了160万辆以上自行车的制造生产。甚至有生产自行车零部件的上市公司因此股票涨停。美国彭博新闻社网站注意到这一现象，评价说“中国正重新成为自行车大国”。'''
		self.japanese_text = u'''（淸實《きよざね》）私共《わたくしども》は、唯《たゞ》君《きみ》の仰《おほ》せのままに、此處《こゝ》までお供《とも》致《いた》して參《まゐ》つたのでござります。丁度《ちやうど》今日《けふ》の午頃《ひるごろ》のこと、わが君《きみ》には急《きふ》に靑褪《あをざ》めた顏《かほ》をなすつて、「都《みやこ》に居《ゐ》ては命《いのち》が危《あやう》い故《ゆゑ》、一刻《いつこく》も早《はや》くわしを何處《どこ》かの山奧《やまおく》へ伴《つ》れて行《い》つて、隱《かく》してくれい。」と仰《おつ》しやりました。それで私共《わたくしども》は取《と》る物《もの》も取《と》り敢《あ》へず、深《ふか》い仔細《しさい》も承《うけたまは》らずに、君《きみ》をお伴《つ》れ申《まを》して、一《ひ》と先《ま》づ田原《たはら》の奧《おく》の大道寺《だいだうじ》の所領《しよりやう》まで逃《に》げのびたのでござりました。すると君《きみ》には、「いや、まだ此處《こゝ》では安心《あんしん》が出來《でき》ない。もつと人里《ひとざと》を離《はな》れた、もつと寂《さび》しい處《ところ》へ行《ゆ》かねばならぬ。」と仰《おつ》しやつて、たうとうこんな山奧《やまおく》へ參《まゐ》つたのでござります。'''

	def test_chinese(self):
		doc = chinese_nlp(self.chinese_text)
		sent1 = doc.sents[0]
		self.assertEqual(str(sent1), u'总理 主持 召开 的 这场 座谈会 ， 旨在 听取 专家学者 和 企业界 人士 对 《 政府 工作 报告 （ 征求意见 稿 ） 》 的 意见建议 。')
		self.assertEqual(len(doc.sents), 11)

	def test_japanese(self):
		doc = japanese_nlp(self.japanese_text)
		doc = japanese_nlp(self.japanese_text)

		sent1 = doc.sents[0]
		self.assertGreater(len(str(sent1)), 10)
		self.assertEqual(len(doc.sents), 7)

