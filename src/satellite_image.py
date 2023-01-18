"""
"""
from __future__ import annotations

from typing import Tuple, List, Optional, Dict
from datetime import date
import numpy as np
import rasterio
import torch


class SatelliteImage:
    """ """

    def __init__(
        self,
        array: np.array,
        crs: str,
        bounds,
        transform,
        date: Optional[date] = None,
        normalized: bool = False,
    ):
        """
        Constructor.

        Args:
            array (np.array): _description_
            crs (str): _description_
            bounds (): _description_
            transform (): _description_
            date (Optional[date], optional): _description_. Defaults to None.
            normalized (bool): _description_. Defaults to False.
        """
        raise NotImplementedError()

    def split(self, nfolds: int) -> List[SatelliteImage]:
        """
        Split the SatelliteImage into `nfolds` folds.

        Args:
            nfolds (int): _description_

        Returns:
            List[SatelliteImage]: _description_
        """
        raise NotImplementedError()

    def to_tensor(self) -> torch.Tensor:
        """
        Return SatelliteImage array as a torch.Tensor.

        Returns:
            torch.Tensor: _description_
        """
        raise NotImplementedError()

    def normalize(self, **params: Dict):
        """
        Normalize array values.

        Args:
            params (Dict): _description_
        """

    @staticmethod
    def from_raster(file_path: str, date: Optional[date] = None) -> SatelliteImage:
        """
        Factory method to create a Satellite image from a raster file.

        Args:
            file_path (str): _description_
            date (Optional[date], optional): _description_. Defaults to None.


        Returns:
            SatelliteImage: _description_
        """
        with rasterio.open(file_path) as raster:
            oview = 1
            bands = (
                raster.read(
                    i,
                    out_shape=(
                        1,
                        int(raster.height // oview),
                        int(raster.width // oview),
                    ),
                )
                for i in range(1, 5)
            )
            crs = raster.crs
            bounds = raster.bounds
            transform = raster.transform
            normalized = False
            array = np.dstack(bands)

        return SatelliteImage(array, crs, bounds, transform, date, normalized)
