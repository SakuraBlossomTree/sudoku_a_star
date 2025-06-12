from selenium import webdriver
import time
from solver import solver

driver = webdriver.Chrome()
driver.get("https://nine.websudoku.com/")

stop_time = time.sleep(1)

while True:

    print("Getting the board...")
    stop_time
    board = []
    for row in range(9):
        row_data = []
        for col in range(9):
            cell = driver.find_element("xpath", f"//table[@id='puzzle_grid']/tbody/tr[{row + 1}]/td[{col + 1}]/input")
            value = cell.get_attribute("value")
            if value == "":
                row_data.append(0)
            else:
                row_data.append(int(value))
        board.append(row_data)

    print("Board obtained, solving...")

    solved_board = solver(board)

    print("Board solved, updating the website...")
    
    for row in range(9):
        for col in range(9):
            cell = driver.find_element("xpath", f"//table[@id='puzzle_grid']/tbody/tr[{row + 1}]/td[{col + 1}]/input")
            current_value = cell.get_attribute("value")
            if not current_value:
                cell.clear()
                cell.send_keys(str(solved_board[row][col]))
        
    print("Board updated, submitting changes...")

    cell.send_keys("\n")

    print("Changes submitted, waiting for the next game...")

    time.sleep(2.5)

    new_game_button = driver.find_element("xpath", "//input[@name='newgame']")

    new_game_button.click()