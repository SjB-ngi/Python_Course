"""
This script exports a single cone penetration test (CPT) out of the Oberhollenzer dataset
dataset: https://www.tugraz.at/en/institutes/ibg/research/computational-geotechnics-group/database

Intended for use in 2026_04_NGI.py
"""
from pathlib import Path

import pandas as pd

def jupyter_safeguard(func):
    """Decorator to handle Jupyter filepaths"""
    def wrapper(*args):
        try:
            return func(*args, working_dir=".")
        except FileNotFoundError:
            return func(*args, working_dir="..")
    return wrapper

@jupyter_safeguard
def lazy_cpt_loader(ID: int, working_dir=".") -> pd.DataFrame:
    """Export a single CPT by ID from the Oberhollenzer dataset."""

    # Construct the filename for the CPT CSV file based on the ID
    cpt_filename = Path(f"{working_dir}/data/CPT/CPT_{ID}.csv")

    if not cpt_filename.exists():
        # ensure the parent folders exist
        cpt_filename.parent.mkdir(exist_ok=True, parents=True)

        # read the full CPT dataset
        CPT_data = pd.read_csv(f"{working_dir}/data/CPT_PremstallerGeotechnik_revised.csv")
        
        # filter the dataset for the specific CPT ID and reset the index
        cpt_data = CPT_data[CPT_data["ID"] == ID].reset_index(drop=True)
        
        # save the filtered CPT data to a CSV file
        cpt_data.to_csv(cpt_filename)
    else:
        # read the CPT data from the existing CSV file
        cpt_data = pd.read_csv(cpt_filename)

    return cpt_data


# Example usage of the lazy_cpt_loader function if ran as a script
if __name__ == "__main__":
    CPT_ID = 0
    cpt_data = lazy_cpt_loader(CPT_ID)
