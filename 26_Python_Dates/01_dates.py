# ==========================================================
# PYTHON DATES
# ==========================================================
# Dates are not a data type of their own - import the datetime module.
import datetime

x = datetime.datetime.now()
print(x)                       # year, month, day, hour, minute, second, microsecond

# ---------- Date output ----------
print(x.year)
print(x.strftime("%A"))        # weekday name

# ---------- Creating date objects ----------
x = datetime.datetime(2020, 5, 17)    # year, month, day (time is optional)
print(x)

# ---------- strftime() - format dates as readable strings ----------
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))        # June

# Format codes:
now = datetime.datetime.now()
codes = {
    "%a": "Weekday, short",          "%A": "Weekday, full",
    "%w": "Weekday as number 0-6",   "%d": "Day of month 01-31",
    "%b": "Month name, short",       "%B": "Month name, full",
    "%m": "Month as number 01-12",   "%y": "Year, short",
    "%Y": "Year, full",              "%H": "Hour 00-23",
    "%I": "Hour 00-12",              "%p": "AM/PM",
    "%M": "Minute 00-59",            "%S": "Second 00-59",
    "%f": "Microsecond",             "%j": "Day number of year",
    "%U": "Week number (Sun first)", "%W": "Week number (Mon first)",
    "%c": "Local date and time",     "%x": "Local date",
    "%X": "Local time",              "%%": "A % character",
}
for code, meaning in codes.items():
    print(f"{code}  {meaning:28} {now.strftime(code)}")
