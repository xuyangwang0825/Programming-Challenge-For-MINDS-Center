# Programming-Challenge-For-MINDS-Center
Programming Challenge For MINDS + Center
> Xuyang Wang
## how to run the program
```python
python main -o a
```
Also, you can get more information using -h parameter

```python
python main -h

# usage: main.py [-h] [-o {a,p,c,o}]
# Welcome to use this sentiment analysis tool!
# optional arguments:
#   -h, --help    show this help message and exit
#   -o {a,p,c,o}  input the operation type
```

## directory
```
.
├── LICENSE
├── README.md
├── Spring\ 2022\ Programming\ Challenge.pdf # instruction
├── __pycache__
│   ├── compute.cpython-38.pyc
│   ├── plot.cpython-38.pyc
│   └── pre_process.cpython-38.pyc
├── data # html data
│   ├── messages1.html
│   ├── messages2.html
│           ...
│   └── messages48.html
├── data.json # json data generated base on html files
├── main.py
├── pre_process.py
├── compute.py
├── plot.py
├── image # images plotted using plotly
│   ├── avg.png
│   └── count.png
└── requirements.txt # package requirement
```

## features
- Export Telegram messages   
    For this part, because I can only export html instead of json in Telegram, shown as the following image, so I conduct pre-process based on html files.

    ![](https://markdown.diobrando0825.cn/2021-12-18-Screen%20Shot%202021-12-18%20at%202.09.49%20AM.png)

- Pre-process the data.   
    The structure of html file is shown as the following picture.

    ![](https://markdown.diobrando0825.cn/2021-12-18-Screen%20Shot%202021-12-18%20at%202.17.15%20AM.png)

    <img src="https://markdown.diobrando0825.cn/2021-12-18-Screen%20Shot%202021-12-18%20at%202.18.05%20AM.png" style="zoom:50%;" />

    So, I can just extract two divs(`'pull_right date details'` and `'text'`) which will be used in sentiment computing part.

    I can get the time of message in first div and get specific text content in second div.

- Compute the sentiment of each message   
    I use `textblob` for sentiment analysis and get the polarity result for each message.
- Plot   
    I plot two images.   
    One is the number of messages per day.
    ![](https://markdown.diobrando0825.cn/2021-12-18-count.png)
    The other is the average sentiment result of messages per day.
    ![](https://markdown.diobrando0825.cn/2021-12-18-avg.png)