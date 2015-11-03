# -*- coding: utf-8 -*-
import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from Huxiu.items import HuxiuItem

# add = 0

class HuxiuSpider(CrawlSpider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/chuangye/index/recommend/",
        "http://www.huxiu.com/chuangye/index/new",
        "http://www.huxiu.com/chuangye/index/hot",
    ]

    rules = (

         Rule(SgmlLinkExtractor(allow=("chuangye/index/recommend/([\w]+).html",),)),
         Rule(SgmlLinkExtractor(allow=("chuangye/index/new/([\w]+).html",),)),
         Rule(SgmlLinkExtractor(allow=("chuangye/index/hot/([\w]+).html",),)),

        Rule(SgmlLinkExtractor(allow=('chuangye/content/([\w]+)/[^\s]*', )), callback='parse_item'),

        # Rule(SgmlLinkExtractor(allow=('chuangye/content/735/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/1043/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/789/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/953/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/995/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/970/[^\s]*', )), callback='parse_item'),
        # Rule(SgmlLinkExtractor(allow=('chuangye/content/1013/[^\s]*', )), callback='parse_item'),
    )

    def parse_item(self, response):

        # global add
        # print add
        # add += 1


        sel = Selector(response)
        items = []

        item = HuxiuItem()

        huxiuNo = sel.xpath("/html/body//input[@id='com_id']/@value").extract()
        if huxiuNo:item['huxiuNo'] = huxiuNo[0]
        Name = sel.xpath('/html/body//h1/text()').extract()
        if Name:item['Name'] = Name[0]
        Website = sel.xpath("/html/body//div[@class='info']/a/@href").extract()
        if Website:item['Website'] = Website[0]
        CompanyName = sel.xpath("/html/body//div[@class='form-group content-user'][2]/div/text()").extract()
        if CompanyName:item['CompanyName'] = CompanyName[0]
        FoundDate = sel.xpath("/html/body//div[@class='form-group content-user'][3]/div/text()").extract()
        if FoundDate:item['FoundDate'] = FoundDate[0]
        District= sel.xpath("/html/body//div[@class='form-group content-user'][4]/div/text()").extract()
        if District:item['District'] = District[0]
        CompanyScale = sel.xpath("/html/body//div[@class='form-group content-user'][5]/div/text()").extract()
        if CompanyScale:item['CompanyScale'] = CompanyScale[0]
        FinancingStage = sel.xpath("/html/body//div[@class='form-group content-user'][6]/div/text()").extract()
        if FinancingStage:item['FinancingStage'] = FinancingStage[0]
        Tag = sel.xpath("/html/body//div[@class='form-group content-user'][7]/div/text()").extract()
        if Tag:item['Tag'] = Tag[0]
        Intro = sel.xpath("/html/body//div[@class='form-group content-user'][8]/div/text()").extract()
        if Intro:item['Intro'] = Intro[0]
        BreifIntro = sel.xpath("/html/body//div[@class='form-group content-user'][9]/div/text()").extract()
        if BreifIntro:item['BreifIntro'] = BreifIntro[0]

        FinancingStage1 = sel.xpath("/html/body//div[@class='content-table']//tr[2]/td[2]/text()").extract()
        FinancingDate1 = sel.xpath("/html/body//div[@class='content-table']//tr[2]/td[1]/text()").extract()
        FinancingVC1 = sel.xpath("/html/body//div[@class='content-table']//tr[2]/td[3]/text()").extract()
        amount = sel.xpath("/html/body//div[@class='content-table']//tr[2]/td[4]/text()").extract()
        if FinancingStage1:item['FinancingStage1']=FinancingStage1[0]
        if FinancingDate1:item['FinancingDate1'] = FinancingDate1[0]
        if FinancingVC1:item['FinancingVC1'] = FinancingVC1[0]
        if amount:
            item['FinancingAmount1'] = amount[0]
            if len(amount)==2:item['FinancingUnit1'] = amount[1]

        FinancingStage2 = sel.xpath("/html/body//div[@class='content-table']//tr[3]/td[2]/text()").extract()
        FinancingDate2 = sel.xpath("/html/body//div[@class='content-table']//tr[3]/td[1]/text()").extract()
        FinancingVC2 = sel.xpath("/html/body//div[@class='content-table']//tr[3]/td[3]/text()").extract()
        amount = sel.xpath("/html/body//div[@class='content-table']//tr[3]/td[4]/text()").extract()
        if FinancingStage2:item['FinancingStage2'] = FinancingStage2[0]
        if FinancingDate2:item['FinancingDate2'] = FinancingDate2[0]
        if FinancingVC2:item['FinancingVC2'] = FinancingVC2[0]
        if amount:
            item['FinancingAmount2'] = amount[0]
            if len(amount)==2:item['FinancingUnit2'] = amount[1]

        FinancingStage3 = sel.xpath("/html/body//div[@class='content-table']//tr[4]/td[2]/text()").extract()
        FinancingDate3 = sel.xpath("/html/body//div[@class='content-table']//tr[4]/td[1]/text()").extract()
        FinancingVC3 = sel.xpath("/html/body//div[@class='content-table']//tr[4]/td[3]/text()").extract()
        amount = sel.xpath("/html/body//div[@class='content-table']//tr[4]/td[4]/text()").extract()
        if FinancingStage3:item['FinancingStage3'] = FinancingStage3[0]
        if FinancingDate3:item['FinancingDate3'] = FinancingDate3[0]
        if FinancingVC3:item['FinancingVC3'] = FinancingVC3[0]
        if amount:
            item['FinancingAmount3'] = amount[0]
            if len(amount)==2:item['FinancingUnit3'] = amount[1]

        FinancingStage4 = sel.xpath("/html/body//div[@class='content-table']//tr[5]/td[2]/text()").extract()
        FinancingDate4 = sel.xpath("/html/body//div[@class='content-table']//tr[5]/td[1]/text()").extract()
        FinancingVC4 = sel.xpath("/html/body//div[@class='content-table']//tr[5]/td[3]/text()").extract()
        amount = sel.xpath("/html/body//div[@class='content-table']//tr[5]/td[4]/text()").extract()
        if FinancingStage4:item['FinancingStage4'] = FinancingStage4[0]
        if FinancingDate4:item['FinancingDate4'] = FinancingDate4[0]
        if FinancingVC4:item['FinancingVC4'] = FinancingVC4[0]
        if amount:
            item['FinancingAmount4'] = amount[0]
            if len(amount)==2:item['FinancingUnit4'] = amount[1]

        FinancingStage5 = sel.xpath("/html/body//div[@class='content-table']//tr[6]/td[2]/text()").extract()
        FinancingDate5 = sel.xpath("/html/body//div[@class='content-table']//tr[6]/td[1]/text()").extract()
        FinancingVC5 = sel.xpath("/html/body//div[@class='content-table']//tr[6]/td[3]/text()").extract()
        amount = sel.xpath("/html/body//div[@class='content-table']//tr[6]/td[4]/text()").extract()
        if FinancingStage5:item['FinancingStage5'] = FinancingStage5[0]
        if FinancingDate5:item['FinancingDate5'] = FinancingDate5[0]
        if FinancingVC5:item['FinancingVC5'] = FinancingVC5[0]
        if amount:
            item['FinancingAmount5'] = amount[0]
            if len(amount)==2:item['FinancingUnit5'] = amount[1]


        Founders1 = sel.xpath("/html/body//div[@class='team-name'][2]/span/text()").extract()
        Position1 = sel.xpath("/html/body//div[@class='team-position'][2]/span/text()").extract()
        FounderIntro1 = sel.xpath("/html/body//div[@class='team-introduce'][2]/p/text()").extract()
        if Founders1:item['Founders1'] = Founders1[0]
        if Position1:item['Position1'] = Position1[0]
        if FounderIntro1:item['FounderIntro1'] = FounderIntro1[0]

        Founders2 = sel.xpath("/html/body//div[@class='team-name'][3]/span/text()").extract()
        Position2 = sel.xpath("/html/body//div[@class='team-position'][3]/span/text()").extract()
        FounderIntro2 = sel.xpath("/html/body//div[@class='team-introduce'][3]/p/text()").extract()
        if Founders2:item['Founders2'] = Founders2[0]
        if Position2:item['Position2'] = Position2[0]
        if FounderIntro2:item['FounderIntro2'] = FounderIntro2[0]

        Founders3 = sel.xpath("/html/body//div[@class='team-name'][4]/span/text()").extract()
        Position3 = sel.xpath("/html/body//div[@class='team-position'][4]/span/text()").extract()
        FounderIntro3 = sel.xpath("/html/body//div[@class='team-introduce'][4]/p/text()").extract()
        if Founders3:item['Founders3'] = Founders3[0]
        if Position3:item['Position3'] = Position3[0]
        if FounderIntro3:item['FounderIntro3'] = FounderIntro3[0]

        Founders4 = sel.xpath("/html/body//div[@class='team-name'][5]/span/text()").extract()
        Position4 = sel.xpath("/html/body//div[@class='team-position'][5]/span/text()").extract()
        FounderIntro4 = sel.xpath("/html/body//div[@class='team-introduce'][5]/p/text()").extract()
        if Founders4:item['Founders4'] = Founders4[0]
        if Position4:item['Position4'] = Position4[0]
        if FounderIntro4:item['FounderIntro4'] = FounderIntro4[0]

        Founders5 = sel.xpath("/html/body//div[@class='team-name'][6]/span/text()").extract()
        Position5 = sel.xpath("/html/body//div[@class='team-position'][6]/span/text()").extract()
        FounderIntro5 = sel.xpath("/html/body//div[@class='team-introduce'][6]/p/text()").extract()
        if Founders5:item['Founders5'] = Founders5[0]
        if Position5:item['Position5'] = Position5[0]
        if FounderIntro5:item['FounderIntro5'] = FounderIntro5[0]


        # print repr(item).decode("unicode-escape") + '\n'

        items.append(item)

        return items


