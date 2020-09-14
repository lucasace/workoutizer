import pandas as pd


def compress_data_for_ui_cache(parser):
    parser.coordinates_list = _compress_coordinates(coordinates=parser.coordinates_list, decimals=4)
    parser.distance_list = _compress_list_of_floats(input_list=parser.distance_list, decimals=2)
    parser.altitude_list = _compress_list_of_floats(input_list=parser.altitude_list, decimals=1)
    parser.heart_rate_list = _ensure_list_of_ints(input_list=parser.heart_rate_list)
    parser.cadence_list = _ensure_list_of_ints(input_list=parser.cadence_list)
    parser.speed_list = _compress_list_of_floats(input_list=parser.speed_list, decimals=1)
    parser.temperature_list = _ensure_list_of_ints(
        _compress_list_of_floats(input_list=parser.temperature_list, decimals=0))
    return parser


def _compress_coordinates(coordinates, decimals):
    return pd.DataFrame(coordinates).round(decimals=decimals).to_numpy().tolist()


def _compress_list_of_floats(input_list: list, decimals):
    return pd.Series(input_list).round(decimals=decimals).to_list()


def _ensure_list_of_ints(input_list):
    return pd.Series(input_list).astype(int).to_list()


def ensure_list_attributes_have_same_length(parser):
    lengths = []
    for attribute, value_list in parser.__dict__.items():
        if attribute.endswith("_list"):
            lengths.append(len(value_list))
    minimal_length = min(lengths)
    for attribute, value_list in parser.__dict__.items():
        if attribute.endswith("_list"):
            compress_list = _compress_list_length(input_list=value_list, desired_length=minimal_length)
            setattr(parser, attribute, compress_list)
    return parser


def _compress_list_length(input_list, desired_length):
    if len(input_list) == desired_length:
        return input_list
    elif desired_length > len(input_list):
        raise ValueError("Desired length is larger than input list. "
                         "This function is only capable of decreasing the size.")

    s = pd.Series(input_list)
    every_nth_item = len(input_list) / desired_length
    iterations = 0
    if len(input_list) % desired_length == 0:
        output_list = s.loc[::int(every_nth_item)].to_list()
    else:
        while len(s) >= desired_length:
            if len(s) / desired_length < 2:
                every_nth_item = len(s)
            s.drop(index=s.loc[::int(every_nth_item)].index[0], inplace=True)
            if len(s) == desired_length:
                break
            every_nth_item = len(s) / desired_length
            iterations += 1
        output_list = s.to_list()
    return output_list
