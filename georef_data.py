import rasterio as rio
from numpy import ndarray


def georeference_ndarry(
    data_array: ndarray, src_file_path: str, output_filename: str
) -> None:
    """
    Georeferences a given numpy array. The dimnesions of the array and the source image must match

    Args:
        data_array (ndarray): Array of data to be georef'd.
        src_file_path (str): Path to the source tif image.
        output_filename (str): Path to save the output file.
    """
    with rio.open(src_file_path, "r") as src, rio.open(
        output_filename, "w", **src.profile
    ) as dst:
        src_meta = src.profile
        assert (
            src_meta["width"] == data_array.shape[2]
            and src_meta["height"] == data_array.shape[1]
        ), "Dimensions of the array and src tif doesn't match..."
        dst.write(data_array)
