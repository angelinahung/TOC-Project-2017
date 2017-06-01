# TOC Project 2017

A telegram bot based on a finite state machine

In this final project, I can communicate with my telegram bot. 

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

In this project, the usage of my bot is to list hotels in Tainan, movie theater timetable and Tainan one day tour.

## Descriptions
First, I need to choose one of three option to ask my bot.
My option:
1. Hotels
2. Movie theater
3. Tainan sights

After the bot reply my needs, you can ask it further questions related to the option.

There, I described the scheme:
1. Hotels:
    a. Top 5 review
        (1.) price
        (2.) location
    b. Top 5 price
        (1.) review
        (2.) location
    c. Top 5 near ncku 
        (1.) review
        (2.) price

2. Movie theater
    a. Guopin
        - Now trending 
    b. Viewshow
        - Now trending

3. Tainan Sights
    -One day tour
        * Dine

## Author
[Angelina Anggara](https://github.com/angelinaanggara1996)

