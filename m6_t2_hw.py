'''
Задача №1
Оформить решение в виде модуля, написав необходимые функции.
Вход:

Пользователь должен ввести "правильный" пароль, состоящий из цифр,
букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
*Желательно выводить пояснение, почему пароль не принят и что нужно исправить.

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
Написать, что ввели правильный пароль или сообщить,
что попытки ввести пароль закончились.


Пример: 
правильный пароль -> o58anuahaunH!
правильный пароль -> aaaAAA111!!!
неправильный пароль -> saucacAusacu8  
'''
import string as st

nums = st.digits
ascii_lowercase = st.ascii_lowercase
ascii_uppercase = st.ascii_uppercase
special = '_!@#$%^&'


def check_pas():  #нужно ли писать none, если функция ничего не возвращает?
    ''' Check password '''
    foo = 4
    while foo >= 0: 
        print('You have', foo + 1, 'try'); foo -= 1
        pas_str = input('Enter password: ')
        count_one = count_two = count_three = count_four = False
            
        if  len(pas_str) < 7:
            print('Password is low than 8')
            continue
        elif len(pas_str) > 15:
            print('Password is long than 15')
            continue
        else:
            for char in pas_str:
                if char in nums:
                    #count_one = True if char in nums #а можно ли как-то так, но без else 0
                    count_one = True
                    
            for char in pas_str:
                if char in ascii_lowercase:
                    count_two = True
                    
            for char in pas_str:
                if char in ascii_uppercase:
                    count_three = True

            for char in pas_str:
                if char in special:
                    count_four = True
        # а можно без else 0? пробывал,не рабоатет                    
        print("Password doesn't have nums!") if count_one == False else 0
        print("Password doesn't have lowercase letter!") if count_two == False  else 0
        print("Password doesn't have uppercase letter!") if count_three == False else 0
        print("Password doesn't have special letter!") if count_four == False else 0
           
        if count_one == count_two == count_three == count_four == True:
            print('Password is good')
            break

def main():
    check_pas()
    
if __name__ == '__main__':
    main()