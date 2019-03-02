str = "JSESSIONID=ABAAABAABEEAAJA864DF9FC724CB7A60A180F09462E0336; _ga=GA1.2.2145957749.1551524249; _gid=GA1.2.1404364732.1551524249; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551524250; user_trace_token=20190302185730-f9923590-3cd9-11e9-ba27-525400f775ce; LGSID=20190302185730-f9923729-3cd9-11e9-ba27-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FC%2B%2B%2F%3FlabelWords%3Dlabel; LGUID=20190302185730-f9923992-3cd9-11e9-ba27-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221693e1223f1d4-01a2e63bbc0407-3d644601-1327104-1693e1223f2862%22%2C%22%24device_id%22%3A%221693e1223f1d4-01a2e63bbc0407-3d644601-1327104-1693e1223f2862%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=5efd15df2f718e2c536367a3c623b293970a4149e1ade6abe70ae4f3743a8d09; _putrc=44EB60CA3BC11E73123F89F2B170EADC; login=true; unick=%E9%AB%98%E6%B5%A9%E7%BF%94; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=962760b011b8f699d5068bc324e372abdc5b97d2091a34cc21bdfea126150cce; TG-TRACK-CODE=index_navigation; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551525234; LGRID=20190302191354-43d70121-3cdc-11e9-8924-5254005c3644; SEARCH_ID=da3a76a75cbd47449e1e3d0ff09542e6"
a = "{'"
index = 0
length = len(str)
while index < length:
	if str[index] == '=':
		a = a + "'"
		a = a + ':'
		a = a + "'"
	elif str[index] == ';':
		a = a + "'"
		a = a + ','
		a = a + " '"
		index += 1
	else:
		a = a + str[index]
	index += 1
a = a + "'}"
print(a)