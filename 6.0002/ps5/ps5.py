# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    coeff_list = [];

    for deg in degs:
    	temp = pylab.polyfit(x,y,deg);
    	coeff_list.append(temp);

    return coeff_list



def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    # TODO
    mean = pylab.mean(y);
    num = 0;
    den = 0;

    for idx in range(len(y)):
    	num += (y[idx]-estimated[idx])**2;
    	den += (y[idx]-mean)**2;

    rsquared = 1-(num/den);
    return rsquared


    


def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # Create array of model output
    modOutputs = [];
    x = pylab.array(x, dtype=pylab.float64);

    for model in models:
    	modOut = [];
    	for xpt in x:
    		outputPt = 0;
    		for idx in range(len(model)):
    			coeff = model[len(model)-1-idx];
    			outputPt +=  coeff*(xpt**idx);

    		modOut.append(outputPt);

    	modOutputs.append(modOut);

    # Convert model outputs to pylab array and generate plots
    for idx in range(len(modOutputs)):
    	modOutputs[idx] = pylab.array(modOutputs[idx]);

    	modelDeg = len(models[idx])-1;
    	rsquaredVal = r_squared(y,modOutputs[idx]);
    	title = "Temperature Model" + "\n" + "Model Degree = " + str(modelDeg) +\
    			"\n" + "R-squared Value = " + str(rsquaredVal);
    	if modelDeg == 1:
    		SEslope = se_over_slope(x, y, modOutputs[idx], models[idx]);
    		title += "\n" + "SE/slope = " + str(SEslope);

    	pylab.figure(idx+1)
    	pylab.plot(x,y,'bo',label="raw data")
    	pylab.plot(x,modOutputs[idx],'r',label="model estimates")
    	pylab.legend()
    	pylab.xlabel("years")
    	pylab.ylabel("degrees C")
    	pylab.title(title)
    pylab.show()




def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    # TODO
    avgTempData = [];

    for yr in years:
    	yrTempDataLOL = []; #List of lists
    	yrTempData = []; #flattened list

    	for city in multi_cities:
    		yrTempDataLOL.append(climate.get_yearly_temp(city,yr));


    	for sublist in yrTempDataLOL:
    		for item in sublist:
    			yrTempData.append(item);

    	avgTempData.append(pylab.mean(yrTempData));

    return avgTempData



def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    # TODO
    mvAvg = [];

    for idx in range(len(y)):
    	if idx+1 < window_length:
    		mvAvg.append(pylab.mean(y[0:idx+1]));
    	else:
    		mvAvg.append(pylab.mean(y[idx+1-window_length:idx+1]));

    mvAvg = pylab.array(mvAvg);
    return mvAvg

    

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    # TODO
    N = len(y);
    num = 0;

    for i in range(N):
    	num += (y[i]-estimated[i])**2;

    rmse = (num/N)**(1/2);
    return rmse


def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    # TODO
    stdTempData = [];
    dayDict = {};


    for yr in years:
    	cityDict = {}

    	for city in multi_cities:
    		cityDict[city] = climate.get_yearly_temp(city,yr);
    		yearLen = len(climate.get_yearly_temp(city,yr))

    	dailyMean = []
    	for day in range(yearLen):
    		dailyTemp = [];
    		for city in multi_cities:
    			dailyTemp.append(cityDict[city][day]);

    		dailyMean.append(pylab.mean(dailyTemp));

    	stdTempData.append(pylab.std(dailyMean));

    return stdTempData

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    # TODO
    # Create array of model output
    modOutputs = [];
    x = pylab.array(x, dtype=pylab.float64);

    for model in models:
    	modOut = [];
    	for xpt in x:
    		outputPt = 0;
    		for idx in range(len(model)):
    			coeff = model[len(model)-1-idx];
    			outputPt +=  coeff*(xpt**idx);

    		modOut.append(outputPt);

    	modOutputs.append(modOut);

    # Convert model outputs to pylab array and generate plots
    for idx in range(len(modOutputs)):
    	modOutputs[idx] = pylab.array(modOutputs[idx]);

    	modelDeg = len(models[idx])-1;
    	rmseVal = rmse(y,modOutputs[idx]);
    	title = "Temperature Model" + "\n" + "Model Degree = " + str(modelDeg) +\
    			"\n" + "RMSE Value = " + str(rmseVal);

    	pylab.figure()
    	pylab.plot(x,y,'bo',label="raw data")
    	pylab.plot(x,modOutputs[idx],'r',label="model estimates")
    	pylab.legend()
    	pylab.xlabel("years")
    	pylab.ylabel("degrees C")
    	pylab.title(title)
    pylab.show()


if __name__ == '__main__':

	#pass
    #print(generate_models(pylab.array([1961, 1962, 1963]),pylab.array([-4.4, -5.5, -6.6]), [1, 2]));
    
    # Part A.4
    tempData = Climate("data.csv");
    nycJan10TempData = [];
    nycAvgTempData = [];
    yr = 1961;
    yrlist = [];

    while yr < 2010:
    	nycJan10TempData.append(tempData.get_daily_temp("NEW YORK", 1, 10, yr));
    	
    	yearOfTemps = tempData.get_yearly_temp("NEW YORK", yr);
    	nycAvgTempData.append(pylab.mean(yearOfTemps));

    	yr += 1;
    	yrlist.append(yr);

    nycJan10TempData = pylab.array(nycJan10TempData);
    nycAvgTempData = pylab.array(nycAvgTempData);
    yrlist = pylab.array(yrlist);

    # Problem 4.I
    models = generate_models(yrlist, nycJan10TempData, [1]);
    # evaluate_models_on_training(yrlist, nycJan10TempData, models)

    #Problem 4.II
    models = generate_models(yrlist, nycAvgTempData, [1]);
    #evaluate_models_on_training(yrlist, nycAvgTempData, models)

    # Part B
    natlYearlyAvgTemp = gen_cities_avg(tempData, CITIES, yrlist)
    models = generate_models(yrlist, natlYearlyAvgTemp, [1]);
    #evaluate_models_on_training(yrlist, natlYearlyAvgTemp, models)

    # Part C
    natlYearlyMvAvgTemp = moving_average(natlYearlyAvgTemp,5);
    models = generate_models(yrlist, natlYearlyMvAvgTemp, [1]);
    #evaluate_models_on_training(yrlist, natlYearlyMvAvgTemp, models)

    # Part D.2
    models = generate_models(yrlist, natlYearlyMvAvgTemp, [1,2,20]);
    #evaluate_models_on_training(yrlist, natlYearlyMvAvgTemp, models)
    testYrList = [2010,2011,2012,2013,2014,2015];
    natlYearlyAvgTempTD = gen_cities_avg(tempData, CITIES, testYrList);
    natlYearlyMvAvgTempTD = moving_average(natlYearlyAvgTempTD,5);
    #evaluate_models_on_testing(testYrList, natlYearlyMvAvgTempTD, models)

    # Part E
    natlYearlyStdTemp = gen_std_devs(tempData, CITIES, yrlist);
    natlYearlyAvg_StdTemp = moving_average(natlYearlyStdTemp,5);
    models = generate_models(yrlist, natlYearlyAvg_StdTemp, [1]);
    #evaluate_models_on_training(yrlist, natlYearlyAvg_StdTemp, models)
