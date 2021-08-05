# write a trading bot 

def get_data(symbol, start_date, end_date, interval):
    # make a new plot
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0), colspan=1, rowspan=1)
    # get data
    url_string = 'http://ichart.finance.yahoo.com/table.csv?s=%s&' % symbol + \
    'd=%s&' % str(interval) + \
    'e=%s&' % str(end_date.month - 1) + \
    'f=%s&' % str(end_date.day) + \
    'g=%s&' % str(end_date.year) + \
    'a=%s&' % str(start_date.month - 1) + \
    'b=%s&' % str(start_date.day) + \
    'c=%s&' % str(start_date.year) + \
    'ignore=.csv'
    yahoo_data = urllib.request.urlopen(url_string).readlines()
    #print(yahoo_data)
    # convert to float
    yahoo_data = [x.decode('utf-8').strip() for x in yahoo_data]
    yahoo_data = [x.split(',') for x in yahoo_data]
    #print(yahoo_data)
    yahoo_data = [[x[0],x[1],x[2],x[3],x[4],float(x[5]),float(x[6]),float(x[7]),float(x[8]),float(x[9]),float(x[10]),float(x[11]),float(x[12]),float(x[13])] for x in yahoo_data]
    #print(yahoo_data)
    # make a new plot
    ax1.plot_date(date_format(yahoo_data), yahoo_data[0], '-')
    # format the ticks
    ax1.xaxis.set_major_locator(years)
    ax1.xaxis.set_major