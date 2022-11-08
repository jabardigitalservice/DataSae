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
        generate_profile():
            return pandas data-profiling object
    """
    def __init__(self, df=None, title=None):
        profile = ProfileReport(df, title=title)
        self.profiling = profile.get_profiling(title)

    def generate_profile(self, file_name):
        return self.profiling(file_name)
