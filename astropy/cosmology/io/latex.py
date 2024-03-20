
import os
from astropy.table import QTable
from astropy.io import ascii

def write_latex(cosmology, file, *, overwrite=False, **kwargs):
    """
    Write the Cosmology to a LaTeX table.

    Parameters
    ----------
    cosmology : `~astropy.cosmology.Cosmology`
        The cosmology instance to write out.
    file : path-like or file-like
        The output destination for the latex table.
    overwrite : bool (optional, keyword-only)
        Whether to overwrite an existing file at the destination.
    **kwargs : dict
        Additional keyword arguments passed to `QTable.write`.

    Raises
    ------
    FileExistsError
        If `overwrite` is False and the file already exists.

    """
    if not overwrite and os.path.exists(file):
        raise FileExistsError(f"{file} already exists and 'overwrite' parameter is False.")

    # Convert the cosmology instance to a QTable.
    table = cosmology.to_format("astropy.table", cls=QTable)

    # Apply LaTeX-specific formatting to table columns as needed.
    # This is a stub based on potential column names that may exist in the table.
    # The actual implementation would have a list of known columns to format.
    latex_format_dict = {
        'H0': r'H_0 [\mathrm{km/s/Mpc}]',
        # Add any other necessary formatting rules here.
    }

    # Apply the latex formatting to the columns
    for col_name, latex_format in latex_format_dict.items():
        if col_name in table.colnames:
            table[col_name].info.format = latex_format

    # Write the table to a LaTeX file.
    table.write(file, format='ascii.latex', overwrite=overwrite, **kwargs)
