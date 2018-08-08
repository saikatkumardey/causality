import numpy as np

class CrossCorrelator():
    '''
    The outcome of the module should include - 
        (i) a direction (whether X precedes Y or Y precedes X), 
        (ii) an estimate of the delay,
        (iii) the strength of the delayed correlation
    
    Reference: "A practical method for identifying the propagation path of plant-wide disturbances" Margret Bauer, Nina F. Thornhill
    
    '''
    
    def __init__(self,ts1=None,ts2=None,threshold=0.7):
        
        self.threshold = threshold
        self.cross_corr_list = None
        self.corr = None
        self.max_corr = None
        self.min_corr = None
        self.delay = None
        self.max_corr_delay = None
        self.min_corr_delay = None
        self.direction = None # +1 means ts1 to ts2, -1 means ts2 to ts1, 0 means no lag.
        self.rho = None
        self.ts1 = ts1
        self.ts2 = ts2
    
    def get_direction(self):
        if self.delay > 0:
            return 1
        elif self.delay < 0:
            return -1
        else:
            return 0
    
    def get_delay(self):
        return self.delay
    
    def get_correlation(self):
        return self.corr
    
    def correlate(self):
        
        ts1 = self.ts1
        ts2 = self.ts2
        
        if ts1 is None or ts2 is None:
            raise Exception("Time Series cannot be empty")
        
        normalized_ts1 = (ts1 - np.mean(ts1)) / (np.std(ts1) * len(ts1))
        normalized_ts2 = (ts2 - np.mean(ts2)) / (np.std(ts2))
        self.cross_corr_list = np.correlate(normalized_ts1, 
                                         normalized_ts2, 
                                         'full')
        self.max_corr = self.cross_corr_list.max()
        self.min_corr = self.cross_corr_list.min()
        
        self.max_corr_delay = len(ts1) - np.argmax(self.cross_corr_list) - 1
        self.min_corr_delay = len(ts1) - np.argmin(self.cross_corr_list) - 1
        
        print("max corr = {} at lag = {}".format(self.max_corr,self.max_corr_delay))
        print("min corr = {} at lag = {}".format(self.min_corr,self.min_corr_delay))
        
        if self.max_corr + self.min_corr >= 0:
            self.corr =  self.max_corr
            self.delay = self.max_corr_delay
        else:
            self.corr = self.min_corr
            self.delay = self.min_corr_delay
        
        print("delay ",self.delay)
        print("correlation",self.corr)
                
    def get_directionality_index(self):
        pass
    
    def confirm_directionality_significance(self):
        pass
    
    def is_correlated(self):

        if self.corr:
            return abs(self.corr) >= self.threshold
        else:
            raise Exception("Cross-Correlation has not been computed yet.")