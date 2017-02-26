# 基金管理人查询
## url
http://gs.amac.org.cn/amac-infodisc/api/pof/manager?rand=0.6124919103188785&page=0&size=100
POST
参数
rand=0.6124919103188785
page=0
size=100

返回值
content:管理人数据列表
totalElements: 总记录条数
totalPages: 总页数
last: 是否最后一页
first: 是否首页
numberOfElements: 每页显示条数
sort: 排序（里面数据暂时无用）

管理人数据:
"id": "138",
"managerName": "平安道远投资管理（上海）有限公司",
"artificialPersonName": "杨晓华",
"registerNo": "P1000182",
"establishDate": 1300147200000,
"managerHasProduct": null,
"url": "138.html",
"registerDate": 1395014400000,
"registerAddress": "上海市浦东新区张杨路707号生命人寿大厦39楼03室",
"registerProvince": "上海市",
"registerCity": "浦东新区",
"regAdrAgg": "上海市",
"fundCount": 31,
"fundScale": 578299.33,
"paidInCapital": 969555.92,
"subscribedCapital": 813954.7,
"hasSpecialTips": false,
"inBlacklist": false,
"hasCreditTips": false,
"regCoordinate": "31.2351462103,121.526785265",
"officeCoordinate": "36.4064115401,102.003964973",
"officeAddress": "上海市浦东新区陆家嘴环路1333号平安金融大厦11楼",
"officeProvince": "上海市",
"officeCity": "浦东新区",
"primaryInvestType": "证券投资基金"


# 基金产品查询
URL: http://ba.amac.org.cn/pages/amacWeb/user!list.action
POST
filter_LIKES_CPMC
filter_LIKES_GLJG
filter_LIKES_CPBM
filter_GES_SLRQ
filter_LES_SLRQ
page.searchFileName=publicity_web
page.sqlKey=PAGE_PUBLICITY_WEB
page.sqlCKey=SIZE_PUBLICITY_WEB
_search=false
nd=1488121772129
page.pageSize=200
page.pageNo=1
page.orderBy=SLRQ
page.order=desc
