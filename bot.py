import sqlite3 
import telebot  
from telebot import types 
 
 
 
bot = telebot.TeleBot('6128199622:AAHz4rI2bcPlw2sowf9EUfbiQCp1njNMLZM') 
 
 
@bot.message_handler(commands=['start']) 
def start(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("Найти вакансию.") 
    btn2 = types.KeyboardButton("Создать вакансию.") 
    markup.add(btn1, btn2) 
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}! Я бот для создания ванкасий и для нахождения вакансий для подростков.'.format(message.from_user), reply_markup=markup) 
     
@bot.message_handler(commands=['help']) 
def help(message): 
    bot.send_message(message.chat.id, 'Я бот-помощник. Я помогаю работодателям и людям, которые нуждаются в работе. Что бы начать введи команду /start') 
 
@bot.message_handler(content_types=['text']) 
def funs(message): 
    if(message.text == "Найти вакансию."): 
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
       btn1 = types.KeyboardButton("Рабочий день до 4 часов.") 
       btn2 = types.KeyboardButton("Рабочий день от 4 до 6 часов.") 
       markup.add(btn1, btn2) 
       bot.send_message(message.chat.id, text="Выбери нужный тебе график", reply_markup=markup)  
        
    elif(message.text == "Создать вакансию."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Курьер") 
        btn2 = types.KeyboardButton("Промоутер") 
        btn3 = types.KeyboardButton("Копиратйер") 
        btn4 = types.KeyboardButton("Рекрутер") 
        btn5 = types.KeyboardButton("Програмист") 
        btn5 = types.KeyboardButton("Оператор") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери вакансию, которую предлогаешь", reply_markup=markup) 
         
    elif(message.text == "Рабочий день до 4 часов."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Курьер.") 
        btn2 = types.KeyboardButton("Промоутер.") 
        btn3 = types.KeyboardButton("Копирайтер.") 
        markup.add(btn1, btn2, btn3) 
        bot.send_message(message.chat.id, text="Выбери нужную тебе вакансию", reply_markup=markup) 
         
    elif(message.text == "Рабочий день от 4 до 6 часов."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Рекрутер.") 
        btn2 = types.KeyboardButton("Програмист.") 
        btn3= types.KeyboardButton("Оператор.") 
        markup.add(btn1, btn2, btn3) 
        bot.send_message(message.chat.id, text="Выбери нужную тебе вакансию", reply_markup=markup) 
         
    elif(message.text == "Курьер"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup) 
             
    elif(message.text == "Промоутер"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup) 
         
    elif(message.text == "Копирайтер"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup)     
         
    elif(message.text == "Рекрутер"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup) 
     
    elif(message.text == "Програмист"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup) 
     
    elif(message.text == "Оператор"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("200") 
        btn2 = types.KeyboardButton("250") 
        btn3= types.KeyboardButton("300") 
        btn4 = types.KeyboardButton("400") 
        btn5 = types.KeyboardButton("500") 
        markup.add(btn1, btn2, btn3, btn4, btn5) 
        bot.send_message(message.chat.id, text="Выбери сумму оплаты за один час. Измеряется в рублях", reply_markup=markup) 
             
    elif(message.text == "Курьер."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,) 
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 200 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup) 
     
    elif(message.text == "Промоутер."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,) 
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 200 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup) 
         
    elif(message.text == "Рекрутер."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,)      
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 450 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup) 
      
    elif(message.text == "Копирайтер."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,) 
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 200 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup)  
         
    elif(message.text == "Програмист."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,)      
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 600 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup) 
     
    elif(message.text == "Оператор."): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Телеграм") 
        btn2 = types.KeyboardButton("Телефон")  
        markup.add(btn1, btn2,) 
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Зарплата по этой должности оценивается, как 200 рублей в час. Теперь выбери, где тебе будет проще связаться.", reply_markup=markup) 
         
    elif(message.text == "200"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back)    
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Когда на твою вакансию кто нибудь откликнется, то я дам тебе знать.",reply_markup=markup) 
     
    elif(message.text == "250"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back)    
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Когда на твою вакансию кто нибудь откликнется, то я дам тебе знать.",reply_markup=markup) 
     
    elif(message.text == "300"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back)    
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Когда на твою вакансию кто нибудь откликнется, то я дам тебе знать.",reply_markup=markup) 
     
    elif(message.text == "500"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back)    
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Когда на твою вакансию кто нибудь откликнется, то я дам тебе знать.",reply_markup=markup) 
     
    elif(message.text == "400"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back)    
        bot.send_message(message.chat.id, text="Я добавил тебя в базу данных. Когда на твою вакансию кто нибудь откликнется, то я дам тебе знать.",reply_markup=markup) 
         
    elif(message.text == "Телефон"):  
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back) 
        bot.send_message(message.chat.id, text="Тебе позвонят, в течение 3х рабочих дней.", reply_markup=markup) 
         
    elif(message.text == "Телеграм"): 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  
        back = types.KeyboardButton("Вернуться в главное меню") 
        markup.add(back) 
        bot.send_message(message.chat.id, text="Тебе напишут, в течение 3х рабочих дней.",  reply_markup=markup) 
         
    elif(message.text == "Вернуться в главное меню"):  
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("Найти вакансию.") 
        btn2 = types.KeyboardButton("Создать вакансию.") 
        markup.add(btn1, btn2) 
        bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}! Я бот для создания ванкасий и для нахождения вакансий для подростков.'.format(message.from_user), reply_markup=markup) 
         
 
 
 
 
bot.polling(none_stop=True)