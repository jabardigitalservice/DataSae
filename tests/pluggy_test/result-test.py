"""
this is docstring
"""

import pandas

import pluggy
from datasae.export.result import Result

hookspec = pluggy.HookspecMarker("data-quality-framework-datasae-result")
hookimpl = pluggy.HookimplMarker("data-quality-framework-datasae-result")


class GoogleSheetSpec:
    """A hook specification namespace."""

    @hookspec
    def export_df(self, df):
        """My special little hook that you can customize."""
        print('hook specs ....')
        obj = Result(df)
        print(obj.export())


class Plugin1:
    """A hook implementation namespace."""

    @hookimpl
    def export_df(self, df):
        """

        :param df:
        """
        print("inside Plugin_1.myhook()")
        obj = Result(df)
        df = obj.export()
        print(df.to_json(orient='records'))


# create a manager and add the spec
pm = pluggy.PluginManager("data-quality-framework-datasae-result")
pm.add_hookspecs(GoogleSheetSpec)

# register plugins
pm.register(Plugin1())

q_list = [1, 2, 3, 4, 1, 1, 2, 3, 13, 121]
dataframe = pandas.DataFrame(q_list, columns=['q_data'])

pm.hook.export_df(df=dataframe)
