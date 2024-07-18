from datetime import datetime, timedelta
import config, utils
import pyautogui

def main():
    passwordBot = config.get_bot_password()
    loginBot = config.get_bot_login()

    current_date = datetime.now()
    start_date = current_date.replace(hour=6, minute=0)
    end_date = start_date + timedelta(hours=4)

    utils.openChrome()
    utils.loginSbsWeb(loginBot, passwordBot)
    utils.navigate()
    utils.writeDateTime(start_date)
    utils.writeDateTime(end_date)

    pyautogui.click(650, 360)

if __name__ == "__main__":
    main()
