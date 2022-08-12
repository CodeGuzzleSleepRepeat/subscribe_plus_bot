import requests
import time	
import json
from threading import Thread
import datetime
import matplotlib.pyplot as plt
import numpy
#wzld-fsla-mnph-qvqp-odrt

#pay_token = '401643678:TEST:7df26024-7917-49b4-b9cd-43675a776bb8'		#сбер
								#юмани


#invite_link = 'https://t.me/+X6hgGiQZDGQ5NjBi'
TOKEN2 = '5187720293:AAE3kdYDC7tRBzlsDKIBPfCq2uI0J9WNJA8'
URL = 'https://api.telegram.org/bot'
PRICE = 1
maggot_id = ''
andr_id = ''

my_login = {'BotMother' : '79859590721'}
my_login2 = {}
qiwi_token = 'b6120e43c0718c5cb96270c20405a61e'
past_pay_id = {'BotMother' : {}}

flag = {}
i = {}
bot_token = {}
pay_token2 = {}
channel_id2 = {}
channel_id3 = {}
iter_start = {}
coeff = {}

pay_token =  {}									#юмани


times = []


#invite_link = 'https://t.me/+X6hgGiQZDGQ5NjBi'
TOKEN = {}
URL = 'https://api.telegram.org/bot'
#TOKEN = '5187720293:AAE3kdYDC7tRBzlsDKIBPfCq2uI0J9WNJA8'


bozhenki = {'BotMother' : {}}
mess = {}
banned = {}
flag_channel = {}
flag_content = {}
flag_podpiska = {'BotMother' : {}}
flag_podpiska_long = {}
iter_start = {}
admins = {}

stat_conversion = {}
stat_long = {}
stat_counter = 0
flag_stat = {}

channels = {}
tmp = []

admin_id1 = 0
admin_id2 = 0

channel_id = {}

j = {}
price = {}

def write_bozhenki():
	file = open('bozhenki.txt', "w")
	for bog in bozhenki:
		for b in bozhenki[bog]:
			file.write(bog)
			file.write(' ')
			file.write(str(b))
			file.write(' ')
			file.write(bozhenki[bog][b][0].strftime("%d.%m.%y"))		
			file.write(' ')
			file.write(bozhenki[bog][b][1].strftime("%d.%m.%y"))
			file.write('\n')

def write_admins():
	file = open('admins.txt', "w")
	for admin in admins:
		file.write(admin)
		file.write(' ')
		for i in range(3):
			file.write(str(admins[admin][i]))
			file.write(' ')

def write_channels():
	file = open('channels.txt', "w")
	for ch in channels:
		file.write(ch)
		file.write('./? ')
		length = len(channels[ch][0])
		for i in range(length):
			file.write(str(channels[ch][0][i]))
			file.write(' ')

def get_bozhenki():
	file = open('bozhenki.txt', "r")
	lines = file.read().split('\n')
	lines_len = len(lines)
	for i in range(lines_len):
		if (len(lines[i]) == 0):
			return
		arr = lines[i].split(' ')
		length = len(arr)
		try:
			bozhenki[' '.join(arr[:length - 3])][arr[length - 3]] = [arr[length - 2], arr[length - 1]]
		except:
			bozhenki[' '.join(arr[:length - 3])] = {}

def get_admins():
	file = open('admins.txt', "r")
	lines = file.read().split('\n')
	lines_len = len(lines)
	for i in range(lines_len):
		arr = lines[i].split(' ')
		length = len(arr)
		if length < 3:
			try:
				admins[' '.join(arr[:length - 2])] = ['', '', arr[length - 1]]
			except:
				return
		admins[' '.join(arr[:length - 3])] = [arr[length - 3], arr[length - 2], arr[length - 1]]

def get_channels():
	file = open('channels.txt', "r")
	lines = file.read().split('\n')
	lines_len = len(lines)
	for i in range(lines_len):
		if len(lines[i]) == 0:
			return
		arr = lines[i].split(' ')
		length = len(arr)
		i = 0
		name = ""
		chans = []
		if len(arr) == 0:
			return
		while arr[i].find('./?') == -1:
			name += arr[i] + ' '
			i = i + 1
			if i == len(arr) - 3:
				return
		name += arr[i][:len(arr[i]) - 3]
		i = i + 1
		for j in range(i, length):
			chans.append(arr[j])
		chans2 = chans
		if len(name) > 0:
			channels[name] = [chans2]
		chans.clear()



def get_updates(TOKE, offset=0):
	result = requests.get(f'{URL}{TOKE}/getUpdates?offset={offset}').json()
	return result['result']

def send_message(chat_id, text, TOKEN):
	return requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def get_updates2(offset=0):
    result = requests.get(f'{URL}{TOKEN2}/getUpdates?offset={offset}').json()
    return result['result']

def send_message2(chat_id, text):
	return requests.get(f'{URL}{TOKEN2}/sendMessage?chat_id={chat_id}&text={text}')


def add_payment(name, price, channel, key_channel):
	file = open('payments.txt', "a+")
	file.write(name + ' ' + str(price) + ' ' + datetime.date.today().strftime("%d.%m.%y") +  ' ' + channel + ' ' + key_channel +'\n')
	file.close()

def get_payments(channel_name):
	file = open('payments.txt', "r")
	data = file.read()
	arr = data.split('\n')
	arr_del = []
	length = len(arr)
	for i in range(length):
		try:
			if arr[i].split(' ')[4] != channel_name:
				arr_del.insert(0, i)
		except:
			arr_del.insert(0, i)
	for el in arr_del:
		arr.pop(el)
	return arr



def MakeInvite(chat_id, TOKEN, lim):
    return json.loads(requests.post(f'{URL}{TOKEN}/createChatInviteLink?chat_id={chat_id}&member_limit={lim}').text)


def newInvite(chat_id, TOKEN):
    requests.post(f'{URL}{TOKEN}/revokeChatInviteLink?chat_id={chat_id}&invite_link={invite_link}')
    return json.loads(requests.post(f'{URL}{TOKEN}/createChatInviteLink?chat_id={chat_id}&member_limit=1').text)

def send_link(chat_id, TOKEN):
    global invite_link
    pos = invite_link.rfind('/')
    invite_link = invite_link[:pos + 1] + '%2B'+ invite_link[pos + 2:]
    send_message(chat_id, invite_link, TOKEN)


def payment_history_last(rows_num, key_channel):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + qiwi_token  
    parameters = {'rows': rows_num}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login[key_channel] + '/payments', params = parameters)
    return h.json()

def give_access_to_mother(info, message):
	arr_info = info.split('?!/')[1:]
	reply_markup3(message['message']['chat']['id'], 'Оплачены услуги бота на ' + arr_info[0] + ' месяц за ' + str(arr_info[3]) + ' рублей. Ваш бот снова работает')
	try:
		bozhenki[arr_info[2]][message['message']['chat']['id']][1] += datetime.timedelta(days = int(arr_info[0]) * 30)
	except:
		today = datetime.datetime.today()
		end = datetime.datetime.today() + datetime.timedelta(days = int(arr_info[0]) * 30)
		bozhenki[arr_info[2]][message['message']['chat']['id']] = [today, end]
	try:
		username = message['message']['chat']['username']
	except:
		username = 'No name'
	add_payment(username, arr_info[3], arr_info[2], 'BotMother')


def request_money(key_channel, cur_channel):
	global PRICE
	send_message2(admins[key_channel][2], 'Превышен лимит в 5000 рублей подписок на канал ' + cur_channel + '\nЧтобы бот продолжл рабтотать, оплатите услуги')
	tmp_ = admins[key_channel][2]
	tmp2 = str(tmp_) + '?!/1?!/HH?!/BotMother?!/' + str(PRICE)
	log = my_login['BotMother']
	send_message2(admins[key_channel][2], f'https://qiwi.com/payment/form/99?amount={PRICE}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={log}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment')
	reply_markup4(admins[key_channel][2], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)')		

def give_access(info, message, key_channel):
	global j
	global invite_link

	arr_info = info.split('?!/')[1:]
	if int(arr_info[0]) == 100:
		reply_bog_keyboard(message['message']['chat']['id'], 'Куплена подписка навсегда на канал ' + arr_info[2] + ' за ' + str(arr_info[3]) + ' рублей', TOKEN[key_channel])
	else:
		reply_bog_keyboard(message['message']['chat']['id'], 'Куплена подписка на ' + arr_info[0] + ' месяц(ев) на канал ' + arr_info[2] + ' за ' + str(arr_info[3]) + ' рублей', TOKEN[key_channel])
	if set([message['message']['from']['id']]).issubset(banned[arr_info[2]]):
		unban(int(arr_info[1]), message['message']['from']['id'], TOKEN[key_channel])
		banned[arr_info[2]].discard(message['message']['from']['id'])

	try:
		username = message['message']['chat']['username']
	except:
		username = 'No name'
	add_payment(username, arr_info[3], arr_info[2], key_channel)

	payments = get_payments(arr_info[2])
	if datetime.datetime.today() >= bozhenki['BotMother'][admins[key_channel][2]][1]:
		date = datetime.datetime.today() - datetime.timedelta(days = 30)
		length = len(payments)
		summ = 0
		for i in range(length):
			arr = payments[length - i - 1].split(' ')
			try:
				if datetime.datetime.strptime(arr[2], '%d.%m.%y') < date:
					break			
				summ += float(arr[1])
				if summ > 1:
					bozhenki['BotMother'].pop(admins[key_channel][2])
					request_money(key_channel, arr_info[2])
			except:
				continue 

		
	try:
		bozhenki[arr_info[2]][message['message']['chat']['id']][1] += datetime.timedelta(days = int(arr_info[0]) * 30)
		stat_long[key_channel][0] += 1
	except:
		today = datetime.datetime.today()
		end = datetime.datetime.today() + datetime.timedelta(days = int(arr_info[0]) * 30)
		bozhenki[arr_info[2]][message['message']['chat']['id']] = [today, end]
		stat_long[key_channel][1] += 1
		stat_conversion[key_channel][0] += 1
		if j[arr_info[2]] == 0:
			j[arr_info[2]] = 1
			invite_link = MakeInvite(int(arr_info[1]), TOKEN[key_channel], 1)['result']['invite_link']
		else:
			invite_link = newInvite(int(arr_info[1]), TOKEN[key_channel])['result']['invite_link']
		send_link(message['message']['chat']['id'], TOKEN[key_channel])

	if int(arr_info[0]) == 100:
		text = 'навсегда'
	else:
		text = 'на ' + arr_info[0] + ' месяц(ев)'

	leng = 3
	if admins[key_channel][2] == admins[key_channel][0] or admins[key_channel][1] == 1:
		leng = 2
	for i in range(leng):
		try:
			send_message(admins[key_channel][i], 'Новая подписка' + text, TOKEN[key_channel])
		except:
			continue

'''
	try:
		if int(arr_info[0]) == 100:
			send_message(admin_id, 'Новая подписка навсегда', TOKEN[key_channel])
			send_message(admin_id2, 'Новая подписка навсегда', TOKEN[key_channel])
			return
		send_message(admin_id, 'Новая подписка на ' + arr_info[0] + ' месяц(ев)', TOKEN[key_channel])
		send_message(admin2_id, 'Новая подписка на ' + arr_info[0] + ' месяц(ев)', TOKEN[key_channel])
	except:
		i = 0
'''

def check_message(message, key_channel):
	global flag
	global j
	global invite_link
	global channel_id
	global banned
	global flag_channel
	global tmp
	global channels

	try:
		if message['message']['text'] == 'Подписаться на платный контент на месяц':
			k = 0
			for channel in channels[key_channel]:
				if set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
					continue
				tmp_ = message['message']['chat']['id']
				tmp2 = str(tmp_) + '?!/' + str(1) + '?!/' + str(channel[0]) + '?!/' + channel[1].replace(' ', '_') + '?!/' + str(channel[2])
				send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={channel[2]}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={my_login[key_channel]}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment', TOKEN[key_channel])				
				k += 1
			if k == 0:
				send_message(message['message']['chat']['id'], 'Вы подписаны на все доступные каналы', TOKEN[key_channel])
			else:
				send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)', TOKEN[key_channel])
			flag_podpiska[key_channel][message['message']['chat']['id']] = 0
			flag_podpiska_long[key_channel][message['message']['chat']['id']] = 0
			return
		if message['message']['text'] == 'Когда кончается моя подписка':
			flag_podpiska[key_channel][message['message']['chat']['id']] = 0
			flag_podpiska_long[key_channel][message['message']['chat']['id']] = 0
			try:
				for bog in channels[key_channel]:
					try:
						send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog[1] + ' действует до ' + bozhenki[bog[1]][message['message']['chat']['id']][1].strftime("%d.%m.%y"), TOKEN[key_channel])
					except:
						continue
			except:
				send_message(message['message']['chat']['id'], 'Вы еще не подписаны', TOKEN[key_channel])
			return
		if message['message']['text'] == 'Узнать о скидках':
			k = 0
			for channel in channels[key_channel]:
				cur_val = 1
				for counter in range(12):
					if coeff[channel[1]][counter] != cur_val:
						cur_val = coeff[channel[1]][counter]
						k += 1
						send_message(message['message']['chat']['id'], 'Подписка на канал ' + channel[1] + ' от ' + str(counter + 1) + ' месяцев сразу позволяет получить скидку в ' + str(100 - coeff[channel[1]][counter] * 100) + '%', TOKEN[key_channel])
			if k == 0:
				send_message(message['message']['chat']['id'], 'Скидок нет', TOKEN[key_channel])
			return
		if message['message']['text'] == 'Подписаться на платный контент на несколько месяцев':	
			send_message(message['message']['chat']['id'], 'Напишите число месяцев, на которое хотите подписаться (или 0 если передумали)', TOKEN[key_channel])			
			flag_podpiska[key_channel][message['message']['chat']['id']] = 1
			flag_podpiska_long[key_channel][message['message']['chat']['id']] = 0
			return
		if message['message']['text'] == 'Продлить подписку':	
			try:
				k = 0
				for bog in channels[key_channel]:
					try:
						send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog[1] + ' действует до ' + bozhenki[bog[1]][message['message']['chat']['id']][1].strftime("%d.%m.%y"), TOKEN[key_channel])
						k += 1
					except:
						continue
				send_message(message['message']['chat']['id'], 'Напишите число месяцев, на которое хотите продлить подписку (или 0 если передумали)', TOKEN[key_channel])			
				flag_podpiska_long[key_channel][message['message']['chat']['id']] = 1
				flag_podpiska[key_channel][message['message']['chat']['id']] = 0
				if k == 0:
					send_message(message['message']['chat']['id'], 'Вы еще не подписаны', TOKEN[key_channel])
				return	
			except:
				return
		if flag_podpiska[key_channel][message['message']['chat']['id']] == 1:
			try:
				if int(message['message']['text']) == 0:
					flag_podpiska[key_channel][message['message']['chat']['id']] = 0
					return
				k = 0
				for channel in channels[key_channel]:
					if set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
						continue
					tmp_ = message['message']['chat']['id']
					tmp2 = str(tmp_) + '?!/' + str(message['message']['text']) + '?!/' + str(channel[0]) + '?!/' + channel[1].replace(' ', '_') + '?!/' + str(channel[2] * int(message['message']['text']))
					if int(message['message']['text']) >= 12:
						cur_coeff = coeff[channel[1]][11]
					else:
						cur_coeff = coeff[channel[1]][int(message['message']['text']) - 1]
					price = channel[2] * int(message['message']['text']) * cur_coeff
					log = my_login[key_channel]
					send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={price}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={log}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment', TOKEN[key_channel])
					k += 1
				if k == 0:
					send_message(message['message']['chat']['id'], 'Вы подписаны на все доступные каналы', TOKEN[key_channel])
				else:
					send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)', TOKEN[key_channel])					
				flag_podpiska[key_channel][message['message']['chat']['id']] = 0
			except:
				send_message(message['message']['chat']['id'], 'Ввведите, пожалуйста, целое число', TOKEN[key_channel])
			return
		if flag_podpiska_long[key_channel][message['message']['chat']['id']] == 1:
			try:	
				flag_podpiska_long[key_channel][message['message']['chat']['id']] = 0	
				if int(message['message']['text']) == 0:
					return		
				k = 0	
				for channel in channels[key_channel]:
					if not set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
						continue
					tmp_ = message['message']['chat']['id']
					tmp2 = str(tmp_) + '?!/' + str(message['message']['text']) + '?!/' + str(channel[0]) + '?!/' + channel[1].replace(' ', '_') + '?!/' + str(channel[2] * int(message['message']['text']))
					if int(message['message']['text']) > 12:
						cur_coeff = coeff[key_channel][11]
					else:
						cur_coeff = coeff[key_channel][int(message['message']['text']) - 1]
					price = channel[2] * int(message['message']['text']) * cur_coeff
					log = my_login[key_channel]
					send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={price}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={log}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment', TOKEN[key_channel])
					k += 1
				if k != 0:
					send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)', TOKEN[key_channel])

			except:
				send_message(message['message']['chat']['id'], 'Ввведите, пожалуйста, целое число', TOKEN[key_channel])
			return

		if message['message']['text'] == 'Показать платежи' and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			flag_channel[key_channel] = 0
			payments = get_payments(key_channel)
			for pay in payments:
				send_message(message['message']['chat']['id'], pay[:pay.rfind(' ')], TOKEN[key_channel])
			return
		if message['message']['text'] == 'Показать сумму' and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			flag_channel[key_channel] = 0
			payments = get_payments(key_channel)
			summ = 0
			date = datetime.datetime.today() - datetime.timedelta(days = 30)
			length = len(payments)
			for i in range(length):
				arr = payments[length - i - 1].split(' ')
				try:
					if datetime.datetime.strptime(arr[2], '%d.%m.%y') < date:
						break			
					summ += float(arr[1])
				except:
					continue 
			send_message(message['message']['chat']['id'], summ, TOKEN[key_channel])
			return
		if message['message']['text'] == 'Добавить канал' and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			flag_channel[key_channel] = 1
			send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала', TOKEN[key_channel])
			return
		if flag_channel[key_channel] == 2 and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			try:
				channels[key_channel].append([tmp[0], tmp[1], float(message['message']['text'])])
				flag_channel[key_channel] = 0
				send_message(message['message']['chat']['id'], 'Канал успешно добавлен', TOKEN[key_channel])
			except:
				send_message(message['message']['chat']['id'], 'Цена введена неправильно, введите еще раз', TOKEN[key_channel])
			return
	

		if flag_channel[key_channel] == 1 and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			if str(message).find('forward_from_chat') > -1:
				tmp = [message['message']['forward_from_chat']['id'], message['message']['forward_from_chat']['title']]
				bozhenki[message['message']['forward_from_chat']['title']] = {}
				banned[message['message']['forward_from_chat']['title']] = set()
				j[message['message']['forward_from_chat']['title']] = 0
				send_message(message['message']['chat']['id'], 'Введите цену подписки', TOKEN[key_channel])
				flag_channel[key_channel] = 2
			else:
				send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала', TOKEN[key_channel])
			return
		if message['message']['text'] == 'Удалить канал' and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			flag_channel[key_channel] = -1
			send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала', TOKEN[key_channel])
			return
		if message['message']['text'] == 'Показать добавленные каналы' and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			flag_channel[key_channel] = 0
			for channel in channels[key_channel]:
				send_message(message['message']['chat']['id'], channel[1], TOKEN[key_channel])
			return
		if flag_channel[key_channel] == -1 and set([message['message']['chat']['id']]).issubset(set(admins[key_channel])):
			if str(message).find('forward_from_chat') > -1:
				for channel in channels[key_channel]:
					if channel[1] == message['message']['forward_from_chat']['title']:
						channels[key_channel].remove(channel)
						send_message(message['message']['chat']['id'], 'Канал удален', TOKEN[key_channel])
						flag_channel[key_channel] = 0
						return
				else:
					send_message(message['message']['chat']['id'], 'Такой канал не добавлен', TOKEN[key_channel])
			else:
				send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала', TOKEN[key_channel])
			return
	except:
		i = 0

	try:
		if message['message']['text'] == 'Активировать подписку':
			flag_podpiska_long[key_channel][message['message']['chat']['id']] = 0
			flag_podpiska[key_channel][message['message']['chat']['id']] = 0
			flag_b = True
			while flag_b:
				times.append(datetime.datetime.now())
				leng = len(times)
				if leng > 100:
					times.pop(0)
					send_message(message['message']['chat']['id'], 'Проверяем платеж...', TOKEN[key_channel])
					while (times[leng - 1] - times[0]).seconds < 61:
						time.sleep(1)					
						times[leng - 1] = datetime.datetime.now()
				res = payment_history_last(50, key_channel)
				length = len(res['data'])
				for i in range(length):
					flag_chan = False
					for chan in channels[key_channel]:
						if chan[1] == res['data'][i]['comment'].split('?!/')[3]:
							break
					else:
						flag_chan = True
					if res['data'][i]['txnId'] == past_pay_id[key_channel][message['message']['chat']['id']] or flag_chan:
						flag_b = False
						send_message(message['message']['chat']['id'], 'Нет новых подписок. Возможно платеж еще не прошел - повторите попытку через некоторое время', TOKEN[key_channel])
						break
					try:
						chat_id = int(res['data'][i]['comment'].split('?!/')[0])
					except:
						chat_id = -1
					if chat_id == message['message']['chat']['id']:
						give_access(res['data'][i]['comment'], message, key_channel)
						flag_b = False
						break
			try:
				past_pay_id[key_channel][message['message']['chat']['id']] = res['data'][0]['txnId']
			except:
				return
	except:
		return

def reply_keyboard(chat_id, text, TOKEN):
	reply_markup = { "keyboard": [['Подписаться на платный контент на месяц'], ['Подписаться на платный контент на несколько месяцев'], ['Активировать подписку'], ['Узнать о скидках']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

def reply_markup2(chat_id, text):
	reply_markup = { "keyboard": [['Оплатить'], ['Активировать подписку']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN2}/sendMessage', data=data)

def reply_markup3(chat_id, text):
	reply_markup = { "keyboard": [['Новый канал'], ['Просмотреть добавленные каналы'], ['Посмотреть конверсию'], ['Посмотреть статистику продленных подписок']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN2}/sendMessage', data=data)

def reply_markup3_admin(chat_id, text):
	reply_markup = { "keyboard": [['Новый канал'], ['Просмотреть добавленные каналы'], ['Посмотреть конверсию'], ['Посмотреть статистику продленных подписок'], ['Количество ботов']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN2}/sendMessage', data=data)

def reply_markup4(chat_id, text):
	reply_markup = { "keyboard": [['Новый канал'], ['Активировать подписку'], ['Просмотреть добавленные каналы'], ['Посмотреть конверсию'], ['Посмотреть статистику продленных подписок']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN2}/sendMessage', data=data)


def reply_bog_keyboard(chat_id, text, TOKEN):
	reply_markup = { "keyboard": [['Продлить подписку'], ['Когда кончается моя подписка'], ['Подписаться на платный контент на месяц'], ['Подписаться на платный контент на несколько месяцев'], ['Активировать подписку']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)


def reply_admin_keyboard(chat_id, text, TOKEN):
	reply_markup = { "keyboard": [['Добавить канал'], ['Удалить канал'], ['Показать добавленные каналы'], ['Показать платежи'], ['Показать сумму']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

def inline_keyboard(chat_id, text, mes_id, TOKEN):
	reply_markup = {'inline_keyboard': [[{'text': 'Удалить пост', 'callback_data' : str(mes_id)}]]}
	data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
	return requests.post(f'{URL}{TOKEN}/sendMessage', data = data)

def ban(chat_id, user_id, TOKEN):
    return json.loads(requests.get(f'{URL}{TOKEN}/banChatMember?chat_id={chat_id}&user_id={user_id}').text)

def unban(chat_id, user_id, TOKEN):
    return json.loads(requests.get(f'{URL}{TOKEN}/unbanChatMember?chat_id={chat_id}&user_id={user_id}').text)

def send_photo(chat_id, img, TOKEN):
	file = {'photo' : open(img, 'rb')}
	print(file)
	return json.loads(requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', data=file).text)

def send_graph(chat_id, channel, num_of_months):
	global TOKEN2

	arr = {}
	arr_dates = []
	arr_vals = []
	for bog in bozhenki[channel]:
		try:
			arr[bozhenki[channel][bog][0].strftime("%y-%m-%d")] += 1
		except:
			arr[bozhenki[channel][bog][0].strftime("%y-%m-%d")] = 1

	today = datetime.date.today()
	cur_date = today - datetime.timedelta(days = num_of_months * 30)

	while cur_date <= today:
		try:
			arr[cur_date.strftime("%y-%m-%d")] += 0
		except:
			arr[cur_date.strftime("%y-%m-%d")] = 0
		arr_dates.append(cur_date.strftime("%m-%d"))
		arr_vals.append(int(arr[cur_date.strftime("%y-%m-%d")]))
		cur_date += datetime.timedelta(days = 1)


	fig, ax = plt.subplots()
	ax.plot(numpy.array(arr_dates), numpy.array(arr_vals))
	plt.xticks(rotation = 90)
	#plt.savefig('graph_' + str(chat_id) + '.png')
	print(send_photo(chat_id, 'g.png', TOKEN2))




def check_time(bozhenki, key_channel):
	for b in bozhenki:
		try:
			for bog in bozhenki[b]:
				if datetime.datetime.today() == bozhenki[b][bog][1]:
					send_message(bog, 'Ваша подписка истекает сегодня. Продлите, если хотите сохранить доступ к каналу ' + b, TOKEN[key_channel])
				if datetime.datetime.today() > bozhenki[b][bog][1]:				
					bozhenki[b].pop(bog)
					send_message(bog, 'Ваша подписка истекла', TOKEN[key_channel])
					ban(b, bog, TOKEN[key_channel])
					banned[b].add(bog)
		except:
			continue


def run(adm_id, bot_token, my_login2, channel_id2, channel_id3, price):
	global TOKEN
	global pay_token
	global channel_id
	global channels
	global iter_start
	global invite_link
	global maggot_id



	TOKEN[channel_id3] = bot_token
	my_login[channel_id3] = my_login2
	channel_id[channel_id3] = channel_id2
	channels[channel_id3] = [[channel_id2, channel_id3, price]]
	
	res = payment_history_last(1, channel_id3)
	times.append(datetime.datetime.now())
	date = datetime.date.today()
	f = True
	i = 0
	while f: 
		try:
			update_id = get_updates(TOKEN[channel_id3])[-1]['update_id']
			f = False
		except:
			time.sleep(1)

	while True:
		time.sleep(0.1)
		cur_date = datetime.date.today()
		if cur_date > date:
			try:
				date = cur_date
				thread2 = Thread(target = check_time, args = [bozhenki, channel_id3])
				thread2.start()	
			except:
				print('Can`t check time')
		try:
			messages = get_updates(TOKEN[channel_id3], update_id)
		except:
			continue

		for message in messages:
			if update_id < message['update_id']:
				update_id = message['update_id']
				try:
					try:
						invite_l = MakeInvite(int(channel_id[channel_id3]), TOKEN[channel_id3], 100)['result']['invite_link']
						invite_link = invite_l
					except:
						send_message(message['message']['chat']['id'], 'Бот еще не прикреплен к каналу, попробуйте позже', TOKEN[channel_id3])
						send_message(adm_id, 'Добавьте бота админом с правами добавления и удаления пользователей в канал', TOKEN[channel_id3])
						continue
					try:
						iter_start[channel_id3][message['message']['chat']['id']] += 1
						if iter_start[channel_id3][message['message']['chat']['id']] == 1000:
							iter_start[channel_id3][message['message']['chat']['id']] = 1
					except:
						if message['message']['chat']['id'] == admins[channel_id3][2]:
							send_link(maggot_id, TOKEN2)
						iter_start[channel_id3][message['message']['chat']['id']] = 0				
						flag_content[channel_id3][message['message']['chat']['id']] = False
						flag_podpiska[channel_id3][message['message']['chat']['id']] = 0
						flag_podpiska_long[channel_id3][message['message']['chat']['id']] = 0
						past_pay_id[channel_id3][message['message']['chat']['id']] = res['data'][0]['txnId']
				except:
					i = 0
				try:
					if iter_start[channel_id3][message['message']['chat']['id']] == 0 or message['message']['text'] == '/start':
						if set([message['message']['chat']['id']]).issubset(set(admins[channel_id3])):
							reply_admin_keyboard(message['message']['chat']['id'], 'Добро пожаловать', TOKEN[channel_id3])
						else:
							reply_keyboard(message['message']['chat']['id'], 'Добро пожаловать. Вы еще не оформили подписку на канал', TOKEN[channel_id3])
							send_message(message['message']['chat']['id'], 'Бот создан ботом @subscribeplusbot', TOKEN[channel_id3])
							stat_conversion[channel_id3][1] += 1
						i = 1
						continue
				except:
					i = 0

				try:
					bozhenki['BotMother'][admins[channel_id3][2]]
				except:
					send_message(message['message']['chat']['id'], 'Услуги бота не оплачены админом, к сожалению, бот временно не работает', TOKEN[channel_id3])
					continue

				try:
					thread1 = Thread(target=check_message, args=[message, channel_id3])
					thread1.start()
				except:
					send_message(message['message']['chat']['id'], 'Произошел сбой, пожалуйста, отправьте свое сообщение повторно', TOKEN[channel_id3])
					time.sleep(1)


def start_new_bot(chat_id):
	send_message2(chat_id, 'Готово. Добавьте своего бота админом в канал и пользуйтесь (не забудьте дать боту право добавлять и удалять пользователей)')
	thread2 = Thread(target = run, args=[chat_id, bot_token[chat_id], my_login2[chat_id], channel_id2[chat_id], channel_id3[chat_id], price[chat_id]])
	thread2.start()
	flag[chat_id] = 0

def check_message2(message):
	global PRICE
	global maggot_id
	global andr_id
	global stat_counter

	if True:
		if message['message']['text'] == 'Новый канал' and set([message['message']['chat']['id']]).issubset(bozhenki['BotMother']):
			send_message2(message['message']['chat']['id'], 'Создайте нового бота в @BotFather и пришлите сюда токен')
			flag[message['message']['chat']['id']] = 1
			return
		if flag[message['message']['chat']['id']] == 1:
			bot_token[message['message']['chat']['id']] = message['message']['text']
			send_message2(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала, к которому хотите подключить подписку')
			flag[message['message']['chat']['id']] = 2
			return
		if flag[message['message']['chat']['id']] == 4:
			try:
				price[message['message']['chat']['id']] = float(message['message']['text'])
			except:
				send_message(message['message']['chat']['id'], 'Введите целое число')
				return
			send_message2(message['message']['chat']['id'], 'Если хотите добавить скидки на подписку сразу на несколько месяцев, нажмите 1, если хотите закончить настройку бота - 0')
			flag[message['message']['chat']['id']] = 5
			return
		if flag[message['message']['chat']['id']] == 5:
			if message['message']['text'] == '0':
				start_new_bot(message['message']['chat']['id'])
			else:
				send_message2(message['message']['chat']['id'], 'Хотите выбрать стандартную систему скидок (от 3 месяцев скидка 10%, от 6 месяцев скидка 20%, от 12 месяцев - скидка 40%) - нажмите 0.\nЕсли хотите настроить скидки сами - введите число месяцев, с которого хотите ввести скидку.')
				flag[message['message']['chat']['id']] = 6
			return

		if flag[message['message']['chat']['id']] == 6:
			if message['message']['text'] == '0':
				coeff[channel_id3[message['message']['chat']['id']]] = [1, 1, 0.9, 0.9, 0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.6]
				start_new_bot(message['message']['chat']['id'])
			else:
				try:			
					coeff[channel_id3[message['message']['chat']['id']]][int(message['message']['text']) - 1] = -1
					send_message2(message['message']['chat']['id'], 'Введите скидку (в процентах)')
					flag[message['message']['chat']['id']] = 7
				except:
					send_message2(message['message']['chat']['id'], 'Введите число')
			return

		if flag[message['message']['chat']['id']] == 8:
			if message['message']['text'] == '0':
				start_new_bot(message['message']['chat']['id'])
			else:
				try:	
					if int(message['message']['text']) > 12:
						send_message2(message['message']['chat']['id'], 'Скидки доступны для сроков не больше года')
						return
					coeff[channel_id3[message['message']['chat']['id']]][int(message['message']['text']) - 1] = -1
					send_message2(message['message']['chat']['id'], 'Введите скидку (в процентах)')
					flag[message['message']['chat']['id']] = 7
				except:
					send_message2(message['message']['chat']['id'], 'Введите число')
			return

		if flag[message['message']['chat']['id']] == 7:
			try:
				fl = False
				for i in range(12):
					if coeff[channel_id3[message['message']['chat']['id']]][i] == -1:
						fl = True
					if fl:
						coeff[channel_id3[message['message']['chat']['id']]][i] = 1 - int(message['message']['text']) / 100
			except:
				send_message2(message['message']['chat']['id'], 'Введите целое число')
			flag[message['message']['chat']['id']] = 8
			send_message2(message['message']['chat']['id'], 'Если хотите добавить еще одну скидку - введите число месяцев, если хотите закончить настройку - введите 0')
			return
		
		if str(message).find('forward_from_chat') > -1 and flag[message['message']['chat']['id']] == 2:
			channel_id2[message['message']['chat']['id']] = message['message']['forward_from_chat']['id']
			channel_id3[message['message']['chat']['id']] = message['message']['forward_from_chat']['title']
			if set(channel_id3[message['message']['chat']['id']]).issubset(set(channels)):
				send_message2(message['message']['chat']['id'], 'Такой канал уже добавлен')
				flag[message['message']['chat']['id']] = 0
				return
			bozhenki[channel_id3[message['message']['chat']['id']]] = {}
			coeff[channel_id3[message['message']['chat']['id']]] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
			flag_content[channel_id3[message['message']['chat']['id']]] = {}
			stat_conversion[channel_id3[message['message']['chat']['id']]] = [0, 0]
			stat_long[channel_id3[message['message']['chat']['id']]] = [0, 0]
			stat_counter += 1
			flag_podpiska[channel_id3[message['message']['chat']['id']]] = {}
			flag_podpiska_long[channel_id3[message['message']['chat']['id']]] = {}
			banned[channel_id3[message['message']['chat']['id']]] = set()
			flag_channel[channel_id3[message['message']['chat']['id']]] = 0
			j[channel_id3[message['message']['chat']['id']]] = 0
			iter_start[channel_id3[message['message']['chat']['id']]] = {}
			past_pay_id[channel_id3[message['message']['chat']['id']]] = {}
			try:
				admins[channel_id3[message['message']['chat']['id']]] = [maggot_id, andr_id, message['message']['chat']['id']]
			except:
				i = 0
			send_message2(message['message']['chat']['id'], 'Пришлите номер телефона, к которому привязан киви кошелек без плюса (в формате 7**********)')
			flag[message['message']['chat']['id']] = 3
			return
		if flag[message['message']['chat']['id']] == 3:	
			try:
				int(message['message']['text'])	
			except:
				send_message2(message['message']['chat']['id'], 'Неправильно введен номер, попробуйте еще раз')
				return
			my_login2[message['message']['chat']['id']] = message['message']['text']
			send_message2(message['message']['chat']['id'], 'Введите цену месячной подписки')
			flag[message['message']['chat']['id']] = 4
			return
		if message['message']['text'] == 'Оплатить':
			flag_podpiska['BotMother'][message['message']['chat']['id']] = 1
			send_message2(message['message']['chat']['id'], 'Введите число месяцев, на которое хотите подписаться')
			return
		if flag_podpiska['BotMother'][message['message']['chat']['id']] == 1:
			try:
				tmp_ = message['message']['chat']['id']
				tmp2 = str(tmp_) + '?!/' + str(message['message']['text']) + '?!/HH?!/BotMother?!/' + str(PRICE * int(message['message']['text']))
				log = my_login['BotMother']
				send_message2(message['message']['chat']['id'], f'https://qiwi.com/payment/form/99?amount={PRICE}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={log}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment')
				send_message2(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)')
			except:
				send_message2(message['message']['chat']['id'], 'Введите целое число')
			flag_podpiska['BotMother'][message['message']['chat']['id']] = 0
			return

		if message['message']['text'] == 'Просмотреть добавленные каналы':
			k = 0
			for chan in bozhenki:
				if chan == 'BotMother':
					continue
				if set([message['message']['chat']['id']]).issubset(admins[chan]):
					send_message2(message['message']['chat']['id'], chan)
					k += 1
			if k == 0:
				send_message2(message['message']['chat']['id'], 'Вы еще не добавили ни одного канала')
			return

		if message['message']['text'] == 'Активировать подписку':
			flag_podpiska['BotMother'][message['message']['chat']['id']] = 0
			flag_b = True
			while flag_b:
				times.append(datetime.datetime.now())
				leng = len(times)
				if leng > 100:
					times.pop(0)
					send_message2(message['message']['chat']['id'], 'Проверяем платеж...')
					while (times[leng - 1] - times[0]).seconds < 61:
						time.sleep(1)					
						times[leng - 1] = datetime.datetime.now()
				res = payment_history_last(50, 'BotMother')
				length = len(res['data'])
				for i in range(length):
					if res['data'][i]['txnId'] == past_pay_id['BotMother'][message['message']['chat']['id']]:
						flag_b = False
						send_message2(message['message']['chat']['id'], 'Нет новых подписок. Возможно платеж еще не прошел - повторите попытку через некоторое время')
						break
					try:
						chat_id = int(res['data'][i]['comment'].split('?!/')[0])
					except:
						chat_id = -1
					if chat_id == message['message']['chat']['id']:
						give_access_to_mother(res['data'][i]['comment'], message)
						flag_b = False
						break
			try:
				past_pay_id['BotMother'][message['message']['chat']['id']] = res['data'][0]['txnId']
			except:
				return

		if message['message']['text'] == 'Посмотреть конверсию':
			k = 0
			for chan in bozhenki:
				if chan == 'BotMother':
					continue
				if set([message['message']['chat']['id']]).issubset(admins[chan]):
					try:
						val = 100 * stat_conversion[chan][0] / stat_conversion[chan][1]
					except:
						val = 0
					send_message2(message['message']['chat']['id'], chan + ': ' + str(val) + '%')
					k += 1
			if k == 0:
				send_message2(message['message']['chat']['id'], 'Вы еще не добавили ни одного канала')
			return
		if message['message']['text'] == 'Посмотреть статистику продленных подписок':
			k = 0
			for chan in bozhenki:
				if chan == 'BotMother':
					continue
				if set([message['message']['chat']['id']]).issubset(admins[chan]):
					k += 1
					if k == 1:
						send_message2(message['message']['chat']['id'], 'Процент пользователей, продливших подписку от общего числа подписавшихся:')
					try:
						val = 100 * stat_long[chan][0] / stat_long[chan][1]
					except:
						val = 0
					send_message2(message['message']['chat']['id'], chan + ': ' + str(val) + '%')
			if k == 0:
				send_message2(message['message']['chat']['id'], 'Вы еще не добавили ни одного канала')
			return

		if message['message']['text'] == 'Посмотреть график подписок':
			flag_stat[message['message']['chat']['id']] = 1
			send_message2(message['message']['chat']['id'], 'Введите число месяцев, за которое хотите посмотреть график')
			return
		if flag_stat[message['message']['chat']['id']] == 1:
			if True:
				num_months = int(message['message']['text'])
				k = 0
				for chan in bozhenki:
					if chan == 'BotMother':
						continue
					if set([message['message']['chat']['id']]).issubset(admins[chan]):
						k += 1
						send_message2(message['message']['chat']['id'], chan + ':')				
						send_graph(message['message']['chat']['id'], chan, num_months)
				if k == 0:
					send_message2(message['message']['chat']['id'], 'Вы еще не добавили ни одного канала')
			else:
				send_message2(message['message']['chat']['id'], 'Введите целое число')
			flag_stat[message['message']['chat']['id']] = 0
			return

		if message['message']['text'] == 'Количество ботов' and (message['message']['chat']['id'] == maggot_id or message['message']['chat']['id'] == andr_id):
			send_message2(message['message']['chat']['id'], stat_counter)
			return

	else:
		time.sleep(0.2)
		return


def check_mother_time(bozhenki):
	try:
		for bog in bozhenki['BotMother']:
			if datetime.datetime.today() > bozhenki['BotMother'][bog][1]:				
				bozhenki['BotMother'].pop(bog)
				reply_markup2(bog, 'Ваша подписка истекла')
	except:
		return

def main():
	global maggot_id
	global andr_id

	try:
		get_bozhenki()
		get_channels()
		get_admins()
	except:
		print('Something went wrong')

	print(bozhenki)
	print(admins)
	print(channels)

	res = payment_history_last(1, 'BotMother')
	times.append(datetime.datetime.now())
	f = True
	date = datetime.date.today()
	while f: 
	    try:
	        update_id = get_updates2()[-1]['update_id']
	        f = False
	    except:
	        time.sleep(1)


	while True:
		cur_date = datetime.date.today()
		if cur_date > date:
			try:
				date = cur_date
				#thread2 = Thread(target = check_mother_time, args = [bozhenki])
				#thread2.start()	
			except:
				print('Can`t check time')

		messages = get_updates2(update_id)
		for message in messages:
			if update_id < message['update_id']:
				update_id = message['update_id']
				try:
					if message['message']['text'] == '/start':
						1 / 0
					flag[message['message']['chat']['id']]
					thread = Thread(target=check_message2, args=[message])
					thread.start()
				except:
					try:
						username = message['message']['chat']['username']
					except:
						username = ""
					if username == 'fcknmaggot':
						maggot_id = message['message']['chat']['id']
					if username == 'bots4business':
						andr_id = message['message']['chat']['id']
					if username == 'fcknmaggot' or username == 'bots4business':
						reply_markup3_admin(message['message']['chat']['id'], 'Здарова')
						today = datetime.datetime.today()
						end = datetime.datetime.today() + datetime.timedelta(days = 100 * 30)
						bozhenki['BotMother'][message['message']['chat']['id']] = [today, end]
					else:
						reply_markup3(message['message']['chat']['id'], 'Добро пожаловать! Чтобы подключить подписку, нажмите Новый канал')
						send_message2(message['message']['chat']['id'], 'Использование бота бесплатно, пока подписки на ваш канал суммарно не составят 5000 рублей за месяц. Через месяц сумма сбросится')
						
						today = datetime.datetime.today()
						end = datetime.datetime.today() - datetime.timedelta(days = 1)
						bozhenki['BotMother'][message['message']['chat']['id']] = [today, end]

					flag[message['message']['chat']['id']] = 0
					flag_stat[message['message']['chat']['id']] = 0
					flag_podpiska['BotMother'][message['message']['chat']['id']] = 0
					past_pay_id['BotMother'][message['message']['chat']['id']] = res['data'][0]['txnId']
					bot_token[message['message']['chat']['id']] = 0
					channel_id2[message['message']['chat']['id']] = 0
					channel_id3[message['message']['chat']['id']] = 0

try:
	main()
except:
	write_bozhenki()
	write_channels()
	write_admins()