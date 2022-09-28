
class RequestCoachNewTrainingTime:
    pass
    def is_handler  (self,message):
        return 
    def display(self,context,message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)  
        but1 = types.KeyboardButton(choose_date)
        but2 = types.KeyboardButton(choose_time)
        but3 = types.KeyboardButton(choose_type)
        # but4 = types.KeyboardButton()
        # but5 = types.KeyboardButton(createtrain)
        markup.add(but1,but2,but3)
        context.bot.send_message(message.chat.id,"вам надо выбрать несколько параметров тренировки. итак с чего начнем?".format(message.from_user, context.bot.get_me()),parse_mode='html', reply_markup=markup)
        user = User(message)
        user.step = 3
    def request(self,context,message):
        if message.text == choose_date: 
            context.rqRequestCoachNewTraining.display(context,message)
        