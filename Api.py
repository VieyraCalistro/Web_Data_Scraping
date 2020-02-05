
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bs4
import requests
import string
from matplotlib.lines import Line2D
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)


def GraphOne():
    url = "https://www.businessinsider.com/nine-most-in-demand-jobs-in-software-engineering-according-to-hired-2019-3#6-machine-learning-engineer-4"
    hdr = {"user-agent" : "Mozilla/5.0"}

    req = requests.get(url, hdr)
    soup = ""
    if(req.status_code == 200):
        print(req.headers["content-type"])

        soup = bs4.BeautifulSoup(req.text, "html.parser")


    growthRate = {
        "field": [],
        "yearlyGrowthRate": []
    }

    counter = 0
    saveTag = ""
    h2TagResults = soup.find_all("h2", class_ = "slide-title-text")
    for h2Tag in h2TagResults:
        if(counter < 1):
            saveTag = h2Tag.get_text()[4:]
        elif(counter >= 1):
            saveTag = h2Tag.get_text()[3:]

        growthRate['field'].append(saveTag)
        counter = counter + 1


    counter = 0
    saveTag = []
    divTagResults = soup.find_all("div", class_= "slide-layout clearfix")
    for tags in divTagResults:
        pTags = tags.find_all("p")
    
        for tag in pTags:
        
            if(counter == 8 or counter == 11 or counter == 21 or counter == 24 or counter == 28):
                saveTag.append(tag.get_text())

            spanTag = tag.find_all("span")

            if(counter == 2 or counter == 5 or counter == 14 or counter == 17):
                saveTag.append(spanTag[0].get_text())

            counter = counter + 1


    growthRate["yearlyGrowthRate"].append(saveTag[0][154:155])
    growthRate["yearlyGrowthRate"].append(saveTag[1][69:70])
    growthRate["yearlyGrowthRate"].append(saveTag[2][141:143])
    growthRate["yearlyGrowthRate"].append(saveTag[3][240:242])
    growthRate["yearlyGrowthRate"].append(saveTag[4][170:172])
    growthRate["yearlyGrowthRate"].append(saveTag[5][155:157])
    growthRate["yearlyGrowthRate"].append(saveTag[6][205:207])
    growthRate["yearlyGrowthRate"].append(saveTag[7][99:102])
    growthRate["yearlyGrowthRate"].append(saveTag[8][150:153])

    growthRateDf = pd.DataFrame(growthRate)
    print(growthRateDf)

    # Convert and save this new DataFrame to a file
    print(f'\nConvert and save the new DataFrame to a file: \n')

    growthRateNumpyArray = np.asarray(growthRateDf)
    np.savetxt("Field Job Growth Rate.csv", growthRateNumpyArray, delimiter=',',
                header="field, yearlyGrowthRate", fmt="%s")

    print(f'Field Job Growth Rate.csv!\n')

    growthRateDf["yearlyGrowthRate"] = growthRateDf["yearlyGrowthRate"].astype("int")

    fig, ax = plt.subplots(figsize=(12, 8))
    growthRateDf["yearlyGrowthRate"].plot.barh(color="#43e312")
    ax.set(title="Year-To-Year Field Job Growth Rate %", xlabel="Percentage", ylabel="Field")
    plt.grid(color="#f21313", linestyle="--")
    ax.set_yticklabels(growthRateDf["field"])
    ax.xaxis.set_major_locator(MultipleLocator(25))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%d"))
    plt.subplots_adjust(left=0.2)
    plt.savefig("Field Job Growth Rate.png")
    print(f'Field Job Growth Rate.png saved!\n')
    plt.show()


def GraphTwo():
    url = "https://www.payscale.com/research/US/Job=Web_Engineer/Salary"
    hdr = {"user-agent" : "Mozilla/5.0"}

    req = requests.get(url, hdr)
    soup = ""
    if(req.status_code == 200):
        print(req.headers["content-type"])

        soup = bs4.BeautifulSoup(req.text, "html.parser")


    results = soup.find_all("div", class_="charttable__footer-item")
    timeFrame = results[1].get_text()

    salaries = {
        "engineer": ["web Software Engineer", "mobile Software Engineer", "machine Learning Software Engineer"],
        "lowSalaries": [],
        "medianSalaries": [],
        "highSalaries": []
    }


    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["lowSalaries"].append(divTag[0].get_text()[4:6])

    divTag = soup.find_all("div", class_="percentile-chart__median")
    salaries["medianSalaries"].append(divTag[0].get_text()[1:3])

    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["highSalaries"].append(divTag[4].get_text()[4:7])


    url = "https://www.payscale.com/research/US/Job=Mobile_Engineer/Salary"
    hdr = {"user-agent" : "Mozilla/5.0"}

    req = requests.get(url, hdr)
    soup = ""
    if(req.status_code == 200):
        print(req.headers["content-type"])

        soup = bs4.BeautifulSoup(req.text, "html.parser")


    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["lowSalaries"].append(divTag[0].get_text()[4:6])

    divTag = soup.find_all("div", class_="percentile-chart__median")
    salaries["medianSalaries"].append(divTag[0].get_text()[1:3])

    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["highSalaries"].append(divTag[4].get_text()[4:7])


    url = "https://www.payscale.com/research/US/Job=Machine_Learning_Engineer/Salary"
    hdr = {"user-agent" : "Mozilla/5.0"}

    req = requests.get(url, hdr)
    soup = ""
    if(req.status_code == 200):
        print(req.headers["content-type"])

        soup = bs4.BeautifulSoup(req.text, "html.parser")


    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["lowSalaries"].append(divTag[0].get_text()[4:6])

    divTag = soup.find_all("div", class_="percentile-chart__median")
    salaries["medianSalaries"].append(divTag[0].get_text()[1:4])

    divTag = soup.find_all("div", class_="percentile-chart__label")
    salaries["highSalaries"].append(divTag[4].get_text()[4:7])


    salariesDf = pd.DataFrame(salaries)
    salariesDf["lowSalaries"] = salariesDf["lowSalaries"].astype("int")
    salariesDf["medianSalaries"] = salariesDf["medianSalaries"].astype("int")
    salariesDf["highSalaries"] = salariesDf["highSalaries"].astype("int")

    print(salariesDf)

    # Convert and save this new DataFrame to a file
    print(f'\nConvert and save the new DataFrame to a file: \n')

    salariesNumpyArray = np.asarray(salariesDf)
    np.savetxt("Engineer Salary.csv", salariesNumpyArray, delimiter=',',
                header="engineer, lowSalaries, medianSalaries, highSalaries", fmt="%s")

    print(f'Engineer Salary.csv!\n')

    fig, ax = plt.subplots(figsize=(10, 8))
    salariesDf.plot.bar(x="engineer", y="highSalaries", ax=ax, color="#77ff80", width=0.4)
    salariesDf.plot.bar(x="engineer", y="medianSalaries", color="#002aff", ax=ax, width=0.4)
    salariesDf.plot.bar(x="engineer", y="lowSalaries", ax=ax, color="#b00000", width=0.4)
    plt.xticks(rotation=55)
    ax.set(title="Engineer Salary (" + timeFrame + ")", ylabel="Amount in U.S Dollar", xlabel="Engineer")
    plt.subplots_adjust(bottom=0.35)
    ax.set_yticklabels(["0", "20K", "40K", "60K", "80K", "100K", "120K", "140K", "160K"])
    ax.grid(visible=True, color='#ff0000', linestyle='--', linewidth=0.5)
    plt.savefig("Engineer Salary.png")
    print(f'Engineer Salary.png saved!\n')
    plt.show()



def GraphThree():

    url = "https://dqydj.com/number-of-developers-in-america-and-per-state/"
    hdr = {"user-agent" : "Mozilla/5.0"}

    req = requests.get(url, hdr)
    soup = ""
    if(req.status_code == 200):
        print(req.headers["content-type"])

        soup = bs4.BeautifulSoup(req.text, "html.parser")


    spanTags = soup.find_all("span")

    developersPopulation = {
        "state": [],
        "totalWorkers": [],
        "totalDevelopers": [],
        "region": []
    }

    regionData = [1, 4, 6, 3, 1, 2, 5, 3, 3, 3, 3, 4, 2, 7, 7, 7, 7, 6, 6, 5, 6, 5, 7, 7, 6,
                7, 2, 7, 2, 5, 5, 3, 5, 6, 7, 7, 3, 1, 5, 5, 6, 7, 6, 3, 2, 5, 6, 1, 6, 7, 2]

    developersPopulation["region"] = regionData
    counter = 0
    exclude = set(string.punctuation)

    for tag in spanTags:
        if((counter > 35) and ((counter % 6) == 0) and (counter < 337)):
            developersPopulation["state"].append(tag.get_text())
        if((counter > 36) and (((counter - 1) % 6) == 0) and (counter < 338)):
            developersPopulation["totalWorkers"].append("".join(ch for ch in tag.get_text() if ch not in exclude))
        if((counter > 37) and (((counter - 2) % 6) == 0) and (counter < 339)):
            developersPopulation["totalDevelopers"].append("".join(ch for ch in tag.get_text() if ch not in exclude))
        counter = counter + 1


    developersPopulationDf = pd.DataFrame(developersPopulation)
    developersPopulationDf["totalWorkers"] = developersPopulationDf["totalWorkers"].astype("int")
    developersPopulationDf["totalDevelopers"] = developersPopulationDf["totalDevelopers"].astype("int")

    print(developersPopulationDf)

    # Convert and save this new DataFrame to a file
    print(f'\nConvert and save the new DataFrame to a file: \n')

    developerPopulationNumpyArray = np.asarray(developersPopulationDf)
    np.savetxt("Developers Population.csv", developerPopulationNumpyArray, delimiter=',',
                header="state, totalWorkers, totalDevelopers, region", fmt="%s")

    print(f'Developers Population.csv!\n')

    fig, ax = plt.subplots(figsize=(16, 8))
    cm = plt.cm.get_cmap("jet")
    developersPopulationDf.plot.scatter(
        x="totalDevelopers", y="totalWorkers",
        s=developersPopulationDf["totalDevelopers"] / 200,
        c=developersPopulationDf["region"], ax=ax, cmap=cm
    )
    ax.set(title="Total U.S Workers to Developers Ratio By Region (2016)", xlabel="Total Developers", ylabel="Total Workers")
    legendElements = [
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#840000", markersize=10, label="7 - Midwest"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#ff4800", markersize=10, label="6 - Southeast"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#ffe600", markersize=10, label="5 - Northeast"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#77ff80", markersize=10, label="4 - Noncontiguous"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#00d0ff", markersize=10, label="3 - Southwest"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#002aff", markersize=10, label="2 - Rocky Mountains"),
        Line2D([0], [0], lw=0, marker="o", markerfacecolor="#000096", markersize=10, label="1 - Pacific")
    ]
    ax.legend(title="Regions Legend Key", handles=legendElements, loc="lower right")
    ax.grid(visible=True, color='r', linestyle='--', linewidth=0.5)
    ax.xaxis.set_major_locator(MultipleLocator(25_000))
    ax.xaxis.set_major_formatter(FormatStrFormatter("%d"))
    ax.set_xticklabels([
        "0", "0", "25K", "50K", "75K", "100K", "125K", "150K", "175K",
        "200K", "225K", "250K", "275K", "300K", "325K", "350K", "375K",
        "400K", "425K", "450K", "475K", "500K"])
    
    plt.savefig("Developers Population.png")
    print(f'Developers Population.png saved!\n')
    plt.show()


def Main():
    GraphOne()
    GraphTwo()
    GraphThree()


if __name__ == "__main__":
    Main()