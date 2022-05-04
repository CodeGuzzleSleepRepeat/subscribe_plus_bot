import requests
import time	
import json
from threading import Thread
import datetime
#wzld-fsla-mnph-qvqp-odrt

#pay_token = '401643678:TEST:7df26024-7917-49b4-b9cd-43675a776bb8'		#сбер
#pay_token =  '381764678:TEST:35855'									#юмани

my_login = '79859590721'
qiwi_token = 'b6120e43c0718c5cb96270c20405a61e'
past_pay_id = {}

#invite_link = 'https://t.me/+X6hgGiQZDGQ5NjBi'
#TOKEN = '5272742436:AAELVo4gqj4DCD0DEdNMq0PmHCghKGZgyzE'		#test_bot
URL = 'https://api.telegram.org/bot'
TOKEN = '5187720293:AAE3kdYDC7tRBzlsDKIBPfCq2uI0J9WNJA8'		#final_bot


channel_id = -1001770999157

bozhenki = {'test_channel' : {}}
mess = {}
banned = {'test_channel' : set()}
managers = set()
users = set()
flag_content = {}
flag_podpiska = {}
flag_podpiska_long = {}
iter_start = {}

channels = [[channel_id, 'test_channel', 1]]
tmp = []
times = []

flag_channel = 0
j = 0
month_price = 10000
forever_price = 5
admin_id = ''
admin_id2 = ''
admin_name = 'bots4business'
invite_link = ''

def sendInvoice(chat_id, price, title, descr, payload):
	price_json = json.dumps([{'label' : 'Title', 'amount' : price}])
	return requests.get(f'{URL}{TOKEN}/sendInvoice?chat_id={chat_id}&title={title}&description={descr}&payload={payload}&provider_token={pay_token}&currency=RUB&prices={price_json}')

def answerQuery(query_id, flag):
	return requests.get(f'{URL}{TOKEN}/answerPreCheckoutQuery?pre_checkout_query_id={query_id}&ok={flag}')


def get_updates(offset=0):
    result = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
    return result['result']

def send_message(chat_id, text):
	return requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def payment_history_last(rows_num):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + qiwi_token  
    parameters = {'rows': rows_num}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params = parameters)
    return h.json()



def add_payment(name, price, channel):
	file = open('payments.txt', "a+")
	file.write(name + ' ' + str(price) + ' ' + datetime.date.today().strftime("%d.%m.%y") +  ' ' + channel +'\n')
	file.close()

def get_payments():
	file = open('payments.txt', "r")
	data = file.read()
	arr = data.split('\n')
	return arr



def MakeInvite(chat_id):
    return json.loads(requests.post(f'{URL}{TOKEN}/createChatInviteLink?chat_id={chat_id}&member_limit=1').text)


def newInvite(chat_id):
    requests.post(f'{URL}{TOKEN}/revokeChatInviteLink?chat_id={chat_id}&invite_link={invite_link}')
    return json.loads(requests.post(f'{URL}{TOKEN}/createChatInviteLink?chat_id={chat_id}&member_limit=1').text)

def send_link(message):
    global invite_link
    pos = invite_link.rfind('/')
    invite_link = invite_link[:pos + 1] + '%2B'+ invite_link[pos + 2:]
    send_message(message['message']['chat']['id'], invite_link)


def give_access(info, message):
	global j
	global invite_link

	arr_info = info.split('?!/')[1:]
	if int(arr_info[0]) == 100:
		reply_bog_keyboard(message['message']['chat']['id'], 'Куплена подписка навсегда на канал ' + arr_info[2] + ' за ' + str(arr_info[3]) + ' рублей')
	else:
		reply_bog_keyboard(message['message']['chat']['id'], 'Куплена подписка на ' + arr_info[0] + ' месяц(ев) на канал ' + arr_info[2] + ' за ' + str(arr_info[3]) + ' рублей')
	if set([message['message']['from']['id']]).issubset(banned[arr_info[2]]):
		unban(int(arr_info[1]), message['message']['from']['id'])
		banned[arr_info[2]].discard(message['message']['from']['id'])

	try:
		username = message['message']['chat']['username']
	except:
		username = 'No name'
	add_payment(username, arr_info[3], arr_info[2])

		
	try:
		bozhenki[arr_info[2]][message['message']['chat']['id']][1] += datetime.timedelta(days = int(arr_info[0]) * 30)
	except:
		today = datetime.datetime.today()
		end = datetime.datetime.today() + datetime.timedelta(days = int(arr_info[0]) * 30)
		bozhenki[arr_info[2]][message['message']['chat']['id']] = [today, end]
		if j == 0:
			j = 1
			invite_link = MakeInvite(int(arr_info[1]))['result']['invite_link']
		else:
			invite_link = newInvite(int(arr_info[1]))['result']['invite_link']
		send_link(message)

	try:
		if int(arr_info[0]) == 100:
			send_message(admin_id, 'Новая подписка навсегда')
			send_message(admin_id2, 'Новая подписка навсегда')
			return
		send_message(admin_id, 'Новая подписка на ' + arr_info[0] + ' месяц(ев)')
		send_message(admin2_id, 'Новая подписка на ' + arr_info[0] + ' месяц(ев)')
	except:
		i = 0
	return


def check_message(message):
	global admin_id
	global j
	global invite_link
	global channel_id
	global banned
	global flag_channel
	global tmp
	global channels
	global past_pay_id
	global times
	global forever_price

	try:
		if message['message']['text'] == 'Подписаться на платный контент на месяц':
			k = 0
			for channel in channels:
				if set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
					continue
				tmp = message['message']['chat']['id']
				tmp2 = str(tmp) + '?!/' + str(1) + '?!/' + str(channel[0]) + '?!/' + channel[1] + '?!/' + str(channel[2])
				send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={channel[2]}%26%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={my_login}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment')
				k += 1
			if k == 0:
				send_message(message['message']['chat']['id'], 'Вы подписаны на все доступные каналы')
			send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)')
			flag_podpiska[message['message']['chat']['id']] = 0
			flag_podpiska_long[message['message']['chat']['id']] = 0
			return
		if message['message']['text'] == 'Когда кончается моя подписка':
			flag_podpiska[message['message']['chat']['id']] = 0
			flag_podpiska_long[message['message']['chat']['id']] = 0
			try:
				for bog in bozhenki:
					try:
						if bozhenki[bog][message['message']['chat']['id']][1].year >= 30:
							send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog + ' неограниченное время')
						else:
							send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog + ' действует до ' + bozhenki[bog][message['message']['chat']['id']][1].strftime("%d.%m.%y"))
					except:
						continue
			except:
				send_message(message['message']['chat']['id'], 'Вы еще не подписаны')
		if message['message']['text'] == 'Подписаться на платный контент на несколько месяцев':	
			send_message(message['message']['chat']['id'], 'От 3 месяцев - скидка 20%\nОт 6 месяцев - скидка 40%\nНавсегда - стоимость 5 рублей')
			send_message(message['message']['chat']['id'], 'Напишите число месяцев, на которое хотите подписаться (чтобы подписаться навсегда введите 100; если передумали - введите 0)')			
			flag_podpiska[message['message']['chat']['id']] = 1
			flag_podpiska_long[message['message']['chat']['id']] = 0
			return
		if message['message']['text'] == 'Продлить подписку':	
			try:
				for bog in bozhenki:
					try:
						if bozhenki[bog][message['message']['chat']['id']][1].year >= 30:
							send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog + ' неограниченное время')
						else:
							send_message(message['message']['chat']['id'], 'Подписка на канал ' + bog + ' действует до ' + bozhenki[bog][message['message']['chat']['id']][1].strftime("%d.%m.%y"))
					except:
						continue
				
				send_message(message['message']['chat']['id'], 'От 3 месяцев - скидка 20%\nОт 6 месяцев - скидка 40%\nНавсегда - стоимость 5 рублей')
				send_message(message['message']['chat']['id'], 'Напишите число месяцев, на которое хотите подписаться (чтобы подписаться навсегда введите 100; если передумали - введите 0)')				
				flag_podpiska_long[message['message']['chat']['id']] = 1
				flag_podpiska[message['message']['chat']['id']] = 0
				return	
			except:
				send_message(message['message']['chat']['id'], 'Вы еще не подписаны')
				return
		if flag_podpiska[message['message']['chat']['id']] == 1:
			if int(message['message']['text']) == 0:
				flag_podpiska[message['message']['chat']['id']] = 0
				return
			try:
				k = 0
				for channel in channels:
					if set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
						continue
					tmp = message['message']['chat']['id']
					tmp2 = str(tmp) + '?!/' + str(message['message']['text']) + '?!/' + str(channel[0]) + '?!/' + channel[1] + '?!/' + str(channel[2])
					modifier = 1
					if int(message['message']['text']) >= 3:
						modifier = 0.8
					if int(message['message']['text']) >= 6:
						modifier = 0.6
					price = channel[2] * int(message['message']['text']) * modifier
					if int(message['message']['text']) == 100:
						price = forever_price
					send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={price}%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={my_login}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment')
					k += 1
				if k == 0:
					send_message(message['message']['chat']['id'], 'Вы подписаны на все доступные каналы')
				send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)')
				flag_podpiska[message['message']['chat']['id']] = 0
			except:
				send_message(message['message']['chat']['id'], 'Ввведите, пожалуйста, целое число')
			return
		if flag_podpiska_long[message['message']['chat']['id']] == 1:
			if int(message['message']['text']) == 0:
				flag_podpiska_long[message['message']['chat']['id']] = 0
				return
			try:
				for channel in channels:
					if not set([message['message']['chat']['id']]).issubset(bozhenki[channel[1]]):
						continue
					tmp = message['message']['chat']['id']
					tmp2 = str(tmp) + '?!/' + str(message['message']['text']) + '?!/' + str(channel[0]) + '?!/' + channel[1] + '?!/' + str(channel[2])
					modifier = 1
					if int(message['message']['text']) >= 3:
						modifier = 0.8
					if int(message['message']['text']) >= 6:
						modifier = 0.6
					price = channel[2] * int(message['message']['text']) * modifier
					if int(message['message']['text']) == 100:
						price = 5
					send_message(message['message']['chat']['id'], 'Канал ' + channel[1] + '\n' + f'https://qiwi.com/payment/form/99?amount={price}%26extra%5B%27comment%27%5D={tmp2}%26currency=643%26extra%5B%27account%27%5D={my_login}%26blocked[0]=sum%26blocked[1]=account%26blocked[2]=comment')
				flag_podpiska_long[message['message']['chat']['id']] = 0
				send_message(message['message']['chat']['id'], 'После оплаты нажмите активировать подписку. Подписка начнет действовать с момента активации (данные о платеже хранятся 90 дней, активируйте подписку не позднее этого срока)')
			except:
				send_message(message['message']['chat']['id'], 'Ввведите, пожалуйста, целое число')
			return

		if message['message']['text'] == 'Показать платежи' and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			flag_channel = 0
			payments = get_payments()
			for pay in payments:
				send_message(message['message']['chat']['id'], pay)
			return
		if message['message']['text'] == 'Показать сумму' and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			flag_channel = 0
			payments = get_payments()
			summ = 0
			date = datetime.datetime.today() - datetime.timedelta(days = 30)
			length = len(payments)
			for i in range(length - 1):
				arr = payments[length - i - 2].split(' ')
				if datetime.datetime.strptime(arr[2], '%d.%m.%y') < date:
					break
				try:			
					summ += int(arr[1])
				except:
					continue
			send_message(message['message']['chat']['id'], summ)
			return
		if message['message']['text'] == 'Добавить канал' and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			flag_channel = 1
			send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала')
			return
		if message['message']['text'] == 'Удалить канал' and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			flag_channel = -1
			send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала')
			return
		if message['message']['text'] == 'Показать добавленные каналы' and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			flag_channel = 0
			for channel in channels:
				send_message(message['message']['chat']['id'], channel[1])
			return
		if flag_channel == 2 and (message['message']['chat']['username'] == 'fcknmaggot'or message['message']['chat']['username'] == admin_name):
			try:
				channels.append([tmp[0], tmp[1], float(message['message']['text'])])
				flag_channel = 0
				send_message(message['message']['chat']['id'], 'Канал успешно добавлен')
			except	:
				send_message(message['message']['chat']['id'], 'Цена введена неправильно, введите еще раз')
			return
	except:
		i = 0

	

	if flag_channel == 1 and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			if str(message).find('forward_from_chat') > -1:
				for channel in channels:
					if channel[1] == message['message']['forward_from_chat']['title']:
						send_message(message['message']['chat']['id'], 'Этот канал уже добавлен')
						flag_channel = 0
						return
				tmp = [message['message']['forward_from_chat']['id'], message['message']['forward_from_chat']['title']]
				bozhenki[message['message']['forward_from_chat']['title']] = {}
				banned[message['message']['forward_from_chat']['title']] = set()
				send_message(message['message']['chat']['id'], 'Введите цену подписки')
				flag_channel = 2
			else:
				send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала')
			return
	if flag_channel == -1 and (message['message']['chat']['username'] == 'fcknmaggot' or message['message']['chat']['username'] == admin_name):
			if str(message).find('forward_from_chat') > -1:
				for channel in channels:
					if channel[1] == message['message']['forward_from_chat']['title']:
						channels.remove(channel)
						send_message(message['message']['chat']['id'], 'Канал удален')
						flag_channel = 0
						return
			else:
				send_message(message['message']['chat']['id'], 'Перешлите сюда любой пост из канала')
			return

		
	if message['message']['text'] == 'Активировать подписку':
		flag = True
		while flag:
			times.append(datetime.datetime.now())
			leng = len(times)
			if leng > 100:
				times.pop(0)
				send_message(message['message']['chat']['id'], 'Проверяем платеж...')
				while (times[leng - 1] - times[0]).seconds < 61:
					time.sleep(1)					
					times[leng - 1] = datetime.datetime.now()
			res = payment_history_last(50)
			length = len(res['data'])
			for i in range(length):
				if res['data'][i]['txnId'] == past_pay_id[message['message']['chat']['id']]:
					flag = False
					send_message(message['message']['chat']['id'], 'Нет новых подписок. Возможно платеж еще не прошел - повторите попытку через некоторое время')
					break
				try:
					chat_id = int(res['data'][i]['comment'].split('?!/')[0])
				except:
					chat_id = -1
				if chat_id == message['message']['chat']['id']:
					give_access(res['data'][i]['comment'], message)
					flag = False
					break
		try:
			past_pay_id[message['message']['chat']['id']] = res['data'][0]['txnId']
		except:
			return
		


def reply_keyboard(chat_id, text):
	reply_markup = { "keyboard": [['Подписаться на платный контент на месяц'], ['Подписаться на платный контент на несколько месяцев'], ['Активировать подписку']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

def reply_bog_keyboard(chat_id, text):
	reply_markup = { "keyboard": [['Продлить подписку'], ['Когда кончается моя подписка'], ['Подписаться на платный контент на месяц'], ['Подписаться на платный контент на несколько месяцев'], ['Активировать подписку']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)


def reply_admin_keyboard(chat_id, text):
	reply_markup = { "keyboard": [['Добавить канал'], ['Показать добавленные каналы'], ['Удалить канал'], ['Показать платежи'], ['Показать сумму']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

def reply_girl_keyboard(chat_id, text):
	reply_markup = { "keyboard": [['Премиум контент']], "resize_keyboard": True, "one_time_keyboard": False}
	data = {'chat_id': chat_id, 'text' : text, 'reply_markup': json.dumps(reply_markup)}
	requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

def inline_keyboard(chat_id, text, mes_id):
	reply_markup = {'inline_keyboard': [[{'text': 'Удалить пост', 'callback_data' : str(mes_id)}]]}
	data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
	return requests.post(f'{URL}{TOKEN}/sendMessage', data = data)

def ban(chat_id, user_id):
    return json.loads(requests.get(f'{URL}{TOKEN}/banChatMember?chat_id={chat_id}&user_id={user_id}').text)

def unban(chat_id, user_id):
    return json.loads(requests.get(f'{URL}{TOKEN}/unbanChatMember?chat_id={chat_id}&user_id={user_id}').text)

def check_time(bozhenki):
	global channel_id
	for b in bozhenki:
		for bog in b:
			if datetime.datetime.today() > bozhenki[bog][1]:				
				bozhenki[b].pop(bog)
				reply_keyboard(bog, 'Ваша подписка истекла')
				banned[b].add(bog)


def run():
	global admin_id
	global admin_id2
	global past_pay_id
	global admin_name	

	date = datetime.date.today()
	f = True
	i = 0
	res = payment_history_last(1)
	while f: 
		try:
			update_id = get_updates()[-1]['update_id']
			f = False
		except:
			time.sleep(1)

	while True:
		time.sleep(0.1)
		cur_date = datetime.date.today()
		if cur_date > date:
			try:
				date = cur_date
				thread2 = Thread(target = check_time, args = [bozhenki])
				thread2.start()	
			except:
				print('Can`t check time')

		messages = get_updates(update_id)
		for message in messages:
			if update_id < message['update_id']:
				update_id = message['update_id']
				try:
					try:
						iter_start[message['message']['chat']['id']] += 1
						if iter_start[message['message']['chat']['id']] == 1000:
							iter_start[message['message']['chat']['id']] = 1
					except:
						iter_start[message['message']['chat']['id']] = 0				
						flag_content[message['message']['chat']['id']] = False
						flag_podpiska[message['message']['chat']['id']] = 0
						flag_podpiska_long[message['message']['chat']['id']] = 0
						past_pay_id[message['message']['chat']['id']] = res['data'][0]['txnId']
				except:
					i = 0
				
				try:
					if iter_start[message['message']['chat']['id']] == 0:
						if message['message']['chat']['username'] == 'fcknmaggot':
							admin_id = message['message']['chat']['id']				
							reply_admin_keyboard(message['message']['chat']['id'], 'Добро пожаловать')
						elif message['message']['chat']['username'] == admin_name:
							admin_id2 = message['message']['chat']['id']
							reply_admin_keyboard(message['message']['chat']['id'], 'Добро пожаловать')
						elif set(message['message']['chat']['username']).issubset(managers):
							reply_girl_keyboard(message['message']['chat']['id'], 'Добро пожаловать')
						else:
							reply_keyboard(message['message']['chat']['id'], 'Добро пожаловать. Вы еще не оформили подписку на канал')
						i = 1
						continue
				except:
					i = 0

				try:
					thread1 = Thread(target=check_message, args=[message])
					thread1.start()
				except:
					send_message(message['message']['chat']['id'], 'Произошел сбой, пожалуйста, отправьте свое сообщение повторно')


run()
