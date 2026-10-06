import random

def guessing_game():
    print("أهلاً بك في لعبة تخمين الرقم!")
    print("اخترت رقماً بين 1 و 10. هل يمكنك تخمينه؟")
    
    secret_number = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        guess = input(f"\nلديك {attempts} محاولات. أدخل رقمك: ")
        
        # التأكد من أن المستخدم أدخل رقماً
        if not guess.isdigit():
            print("الرجاء إدخال رقم صحيح!")
            continue
            
        guess = int(guess)
        
        if guess == secret_number:
            print("🎉 مبروك! لقد خمنت الرقم الصحيح!")
            break
        elif guess < secret_number:
            print("رقمك أصغر من الرقم السري.")
        else:
            print("رقمك أكبر من الرقم السري.")
            
        attempts -= 1
        
    if attempts == 0:
        print(f"\nللأسف انتهت محاولاتك. الرقم الصحيح كان {secret_number}.")

# تشغيل اللعبة
guessing_game()