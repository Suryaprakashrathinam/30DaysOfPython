import threading
import wget

def pdf1():
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'
    file_path = 'research_paper.pdf'
    wget.download(url, file_path)
    print("Downloaded1")

def pdf2():
    url = 'https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/what_the_mercantilists_got_right.pdf'
    file_path = 'research_paper2.pdf'
    wget.download(url, file_path)
    print("Downloaded2")

def pdf3():
    url = 'https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/africas_manufacturing_puzzle_050125.pdf'
    file_path = 'research_paper3.pdf'
    wget.download(url, file_path)
    print("Downloaded3")

def pdf4():
    url = 'https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/servicing_development.pdf'
    file_path = 'research_paper4.pdf'
    wget.download(url, file_path)
    print("Downloaded4")

def pdf5():
    url = 'https://drodrik.scholar.harvard.edu/sites/scholar.harvard.edu/files/global_distribution_of_authorship_in_economics_-_january_2025.pdf'
    file_path = 'research_paper5.pdf'
    wget.download(url, file_path)
    print("Downloaded5")

task1 = threading.Thread(target=pdf1)
task2 = threading.Thread(target=pdf2)
task3 = threading.Thread(target=pdf3)
task4 = threading.Thread(target=pdf4)
task5 = threading.Thread(target=pdf5)

task1.start()
task2.start()
task3.start()
task4.start()
task5.start()

task1.join()
task2.join()
task3.join()
task4.join()
task5.join()
print("All files downloaded succesfully!")