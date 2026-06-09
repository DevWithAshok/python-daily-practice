def get_series_sum(number,series):
    if series>number:
        return 0
    return (1/series) +get_series_sum(number,series+1)
number = int(input()) #3
series=1
series_sum =round(get_series_sum(number,series),2)
print(series_sum)
