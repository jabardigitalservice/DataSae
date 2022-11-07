# https://github.com/ydataai/pandas-profiling/blob/master/src/pandas_profiling/config_default.yaml
from pandas_profiling import ProfileReport


class Profiling:
    """
        A class to represent profiling data result.

        ...

        Attributes
        ----------
        df : pandas dataframe
            your pandas dataframe location

        Methods
        -------
        get_profiling():
            return engine data type for connected to postgresql
    """
    def __init__(self, df=None):
        self.df = df

    def get_profiling(self, title):
        """
            return profiling result
        """
        return ProfileReport(self.df, title=title)
