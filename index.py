import random

def start_game():
    print("--- مرحباً بك في لعبة تخمين الأرقام! ---")
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("خمن رقماً بين 1 و 10: "))
            attempts += 1
            
            if guess < secret_number:
                print("الرقم الحقيقي أكبر من ذلك!")
            elif guess > secret_number:
                print("الرقم الحقيقي أصغر من ذلك!")
            else:
                print(f"مبروك! لقد وجدت الرقم {secret_number} في {attempts} محاولات.")
                break
        except ValueError:
            print("الرجاء إدخال رقم صحيح فقط.")

if __name__ == "__main__":
    start_game()
