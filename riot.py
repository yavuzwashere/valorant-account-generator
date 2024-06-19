import pyautogui
import pygetwindow as gw
import subprocess
import time
import pyperclip

def is_program_open(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    return len(windows) > 0

def open_or_focus_program(program_path, window_title):
    if is_program_open(window_title):
        window = gw.getWindowsWithTitle(window_title)[0]
        if window.isMinimized:
            window.restore()
        window.activate()
    else:
        subprocess.Popen(program_path)
        time.sleep(5)  # Programın açılması için bekle

def find_icon_on_screen(icon_image_path, confidence=0.8):
    location = pyautogui.locateOnScreen(icon_image_path, confidence=confidence)
    if location:
        print(f"Icon found at {location}")
    else:
        print("Icon not found on screen")
    return location

# Programın yolu ve pencere başlığı
program_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
window_title = "Riot Client"

if is_program_open(window_title):
    # Belirtilen pencere başlığına sahip pencereyi bul
    window = gw.getWindowsWithTitle(window_title)[0]  
    # Pencereyi kapat
    window.close()

# İkonun resim dosyasının yolu
icon_image_path = r"C:\Users\computeer\Desktop\valo-gen\look\login.PNG"

# Programı aç veya öne getir
open_or_focus_program(program_path, window_title)

# İkonu bulana kadar döngü
icon_location = None
while icon_location is None:
    try:
        icon_location = find_icon_on_screen(icon_image_path)
        if icon_location:
            print(f"Icon located at: {icon_location}")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

            time.sleep(5)

            def scroll_to_bottom(scroll_bar_position):
                # Scroll barın başlangıç noktasına git
                pyautogui.moveTo(scroll_bar_position[0], scroll_bar_position[1] + 10)
                pyautogui.mouseDown()  # Sol fare tuşuna basılı tut
                
                # Scroll barı en aşağıya çek
                pyautogui.moveTo(scroll_bar_position[0], scroll_bar_position[1] + 500)
                
                pyautogui.mouseUp()  # Sol fare tuşunu bırak

            # Scroll barın başlangıç koordinatları (örneğin)
            scroll_bar_position = (845, 220)

            # Scroll barı en aşağıya çek
            scroll_to_bottom(scroll_bar_position)


            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\accept.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            time.sleep(1)

            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\game.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            time.sleep(1)

            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\play.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            time.sleep(1)

            pyautogui.hotkey('tab')
            pyperclip.copy("TEZGAH LAAN BUU")
            pyautogui.hotkey('ctrl', 'v')
            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\tag.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\accept.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            time.sleep(4)

            image_path = r"C:\Users\computeer\Desktop\valo-gen\look\play.PNG"
            button_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
            pyautogui.click(button_location)

            
            
        else:
            print("Icon not found, retrying...")
    except pyautogui.ImageNotFoundException:
        print("Icon not found, retrying...")
    time.sleep(1)  # Bir süre bekleyip tekrar dene

# Döngü sonrasında ikon bulunduğunda yapılacak işlemler
print(f"Final icon location: {icon_location}")
