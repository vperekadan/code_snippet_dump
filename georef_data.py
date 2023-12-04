import rasterio as rio
from numpy import ndarray


def georeference_ndarry(data_array: ndarray, src_file_path: str, output_filename: str) -> None:
    with rio.open(src_file_path) as src:
        src_meta = src.