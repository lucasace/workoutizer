import logging
from wizer.ui_cache.compressor import compress_data_for_ui_cache, ensure_list_attributes_have_same_length


log = logging.getLogger(__name__)


def save_ui_cache_to_model(ui_cache_model, parser):

    # only save it to model in case timestamps and at least one more attribute has values
    if (parser.coordinates_list or parser.distance_list or parser.altitude_list or parser.heart_rate_list or
            parser.cadence_list or parser.speed_list or parser.temperature_list) and parser.timestamps_list:
        log.debug(f"saving activity data to ui_cache model")
        parser = compress_data_for_ui_cache(parser=parser)
        parser = ensure_list_attributes_have_same_length(parser=parser)
        ui_cache_object = ui_cache_model(
            coordinates_list=parser.coordinates_list,
            distance_list=parser.distance_list,
            altitude_list=parser.altitude_list,
            heart_rate_list=parser.heart_rate_list,
            cadence_list=parser.cadence_list,
            speed_list=parser.speed_list,
            temperature_list=parser.temperature_list,
            timestamps_list=parser.timestamps_list,
        )
        ui_cache_object.save()
        return ui_cache_object
    else:
        return None
