#An app formobile hosting provider charges usd 0.51 perhour how much doesit costto operate per day, pwe week, per month? how many days can i operate one server with usd 918

prHr = 0.51
prDay = 24*prHr
prWeek = 7*prDay
prMon = 4*prWeek

usrBal = 918

usrDayOp = usrBal / prDay

print("number of days user can operate the server is", usrDayOp)
