from tethys_sdk.base import TethysAppBase, url_map_maker


class ConstructionDewateringTool(TethysAppBase):
    """
    Tethys app class for Construction Dewatering Tool.
    """

    name = 'AE Dewatering 2'
    index = 'aemdewater2:home'
    icon = 'aemdewater2/images/icon.gif'
    package = 'aemdewater2'
    root_url = 'aemdewater2'
    color = '#000ff'
    description = 'Simple tool for simulating the water table drawdown due to a system of wells and slurry trenches surrounding an excavation. Model uses TimML to model groundwater behavior.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='aemdewater2',
                           controller='aemdewater2.controllers.home'),
                    UrlMap(name='get_generate_water_table_ajax',
                           url='aemdewater2/generate-water-table',
                           controller='aemdewater2.controllers.generate_water_table'),
        )

        return url_maps
