import telebot
import requests
import locale
from datetime import *
from bs4 import BeautifulSoup as BS

locale.setlocale(locale.LC_ALL, "")

class Unikum():

	def __init__(self, site, token):
		self.req = requests.get(site)
		self.html = BS(self.req.content, "html.parser")

	def __get_today(self, offset):

		self.today = datetime.now()
		self.day = self.today + timedelta(days=offset)

		return self.day

	def __get_formatted_day(self, offset):
		return self.__get_today(offset).strftime("%d %B").lower()[:-1] + "я"		

	def __is_weekend(self, offset):
		if self.__get_today(offset).strftime("%a").lower() == "сб" or self.__get_today(offset).strftime("%a").lower() == "вс":
			return True

	def __get_pair(self, number, offset):
		
		pair = ""

		for num in self.html.select("tr"):
			if self.__get_formatted_day(offset - 1) in num.select("td")[0].text.replace("  ", " "):
				pair += num.select("td")[number].text

		return pair

	def get_timetable(self, offset):

		day = ""
		if offset == 0: day = "СЕГОДНЯ"
		if offset == 1: day = "ЗАВТРА"
		if offset == 2: day = "ПОСЛЕЗАВТРА"

		if offset > 2:
			for i in range(1, offset):
				day += "ПОСЛЕ"

			day += "ЗАВТРА"

		if offset < 0:
			for i in range(-1, offset):
				day += "ПОЗА"
			day += "ВЧЕРА"			

		if self.__is_weekend(offset):
			self.time = [
				"09:00","10:40","12:30",
				"14:10","16:00","17:40"]			
		else:
			self.time = [
				"08:30","10:20","11:15",
				"15:20","17:00","18:40"]

		#_date = self.__get_formatted_day(offset - 1)

		result = "ПАРЫ " + day + ":\n\n"

		for i in range(1, 7): 
			if self.__get_pair(i, offset + 1).strip() != "":
				result += f"({self.time[i - 1]}) " + str(i) + " ПАРА: " + self.__get_pair(i, offset + 1) + "\n"

		return result
switch = {
	"ip_51": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-51.html",
	"ip_52": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-52.html",
	"ip_53": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-53.html",
	"ip_54": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-54.html",
	"ip_55": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-55.html",
	"ip_61": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-61.html",
	"ip_62": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-62.html",
	"ip_63": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-63-1.html",
	"ip_64": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-64-1-1.html",
	"ip_65": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%9F-65-1.html",
	"ie_71": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-71-1.html",
	"ie_72": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-72-1.html",
	"ie_81": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-81.html",
	"ie_82": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-82.html",
    "ie_9": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-9.html",
	"ie_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-10-2.html",
	"ie_11": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%AD-11-1.html",
	"r_71": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A0-71-1.html",
	"r_72": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A0-72-1.html",
	"r_8": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A0-8.html",
	"r_9": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A0-9.html",
	"r_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A0-10-2.html",
	"ii_71": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-71.html",
	"ii_72": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-72-1.html",
	"ii_81": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-81.html",
	"ii_82": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-82.html",
    "ii_9": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-9.html",
	"ii_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-10-2.html",
	"ii_11": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%98%D0%98-11.html",
	"p_51": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-51.html",
	"p_52": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-52.html",
	"p_53": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-53.html",
	"p_54": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-54.html",
	"p_55": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-55.html",
	"p_61": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-61.html",
	"p_62": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-62.html",
	"p_63": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-63-2.html",
	"p_64": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-64.html",
	"p_65": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%BF-65.html",
	"mf_71": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-71.html",
	"mf_72": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-72.html",
	"mf_73": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-73.html",
	"mf_74": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-74.html",
	"mf_81": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-81.html",
	"mf_82": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-82.html",
	"mf_9": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C%D0%A4-9.html",
	"m_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C-10.html",
	"m_11": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%9C-11.html",
	"f_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A4-10.html",
	"f_11": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D0%A4-11.html",
	"x_71": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-71.html",
	"x_72": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-72.html",
	"x_81": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-81.html",
	"x_82": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-82.html",
	"x_9": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-9.html",
	"x_10": "https://genius-school.kuzstu.ru/wp-content/uploads/2022/12/%D1%85-10.html",
}
keys = list(switch.keys())
_token = "5736454551:AAGk6g12gzKUwjXscXZrmo64Wxg-8Qz80P4"

api = telebot.TeleBot(_token)
@api.message_handler(content_types=["text"])

def message_send(message):
	
	msg = message.text.lower()

	if "/расписание" in msg:
		for i in range(0, len(keys)):
			if keys[i] in msg:
				_site = switch[keys[i]]
				unikum = Unikum(_site, _token)
				if "tmr" in msg:
					api.send_message(message.chat.id, unikum.get_timetable(1))
				elif "ytd" in msg:
					api.send_message(message.chat.id, unikum.get_timetable(-1))
				else:
					api.send_message(message.chat.id, unikum.get_timetable(0))
				break
	else:
		api.send_message(message.chat.id, f"Введите /group_[группа]_(вчера: ytd, завтра: tmr), группы: {', '.join(keys)}")

api.polling(none_stop=True)