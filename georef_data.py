import rasterio as rio
from numpy import ndarray


def georeference_ndarry(
    data_array: ndarray, src_file_path: str, output_filename: str
) -> None:
    with rio.open(src_file_path, "r") as src, rio.open(
        output_filename, "w", **src.profile
    ) as dst:
        src_meta = src.profile
        assert (
            src_meta["width"] == 0 and src_meta["height"] == 1
        ), "Dimensions of the array and src tif doesn't match..."
        dst.write(data_array)
