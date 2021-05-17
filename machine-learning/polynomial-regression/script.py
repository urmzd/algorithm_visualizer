class LinearRegression():

    def calc_loss(self, prediction, target):
        return 1/2 * (prediction - target)**2;

    pass
