import pyautogui
import keyboard

def on_click():
    while True:
        pyautogui.click()
        if keyboard.is_pressed('f7'):
            break


if __name__ == '__main__':
    while True:
        y_or_no = input('Do you want to set a counter? (y/n)')
        print(y_or_no)
        if y_or_no == 'y':
            counter = int(input('How many times do you want to click?'))
            for i in range(counter):
                pyautogui.click()

        elif y_or_no == 'n':
            print('Press F6 to start and F7 to stop')
            while True:
                try:
                    if keyboard.is_pressed('f6'):
                        on_click()
                    elif keyboard.is_pressed('f7'):
                        break
                except:
                    print('Error')
                    break
        else:
            print('Invalid input')
            break
