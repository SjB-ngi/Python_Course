from export_single_cpt import lazy_cpt_loader
# Remember to add groundhog and scipy to your uv environment
from groundhog.siteinvestigation.insitutests.pcpt_correlations import behaviourindex_pcpt_robertsonwride
import matplotlib.pyplot as plt

# Loading the CPT using our internal resource
CPT_ID = 1234
cpt_data = lazy_cpt_loader(CPT_ID)

# Preparing two empty lists for storing the results
behaviour_indices = []
behaviour_classes = []

# Looping through the CPT data to calculate the behaviour index and class for each measurement
for qt, fs, sig_v, sig_v_eff in zip(
    cpt_data["qt (MPa)"],
    cpt_data["fs (kPa)"],
    cpt_data["σ,v (kPa)"],
    cpt_data["σ',v (kPa)"]):

    # I see in the documentation that the function returns a dictionary
    result_dict = behaviourindex_pcpt_robertsonwride(
        qt,
        fs/1000, # kPa -> MPa
        sig_v,
        sig_v_eff
        )

    # I'm interested in the behaviour index Ic, and the class Ic class
    behaviour_indices.append(result_dict["Ic [-]"])
    behaviour_classes.append(result_dict["Ic class"])

# I will add it to my dataframe to make things easier during plotting
cpt_data["Ic_groundhog"] = behaviour_indices
cpt_data["Ic_class_groundhog"] = behaviour_classes

# Count the calculated soil-behaviour classes before plotting them.
print(cpt_data["Ic_class_groundhog"].value_counts(dropna=False))

fig, ax = plt.subplots(figsize=(8, 8)) # setting the size to 8x8 inches

for ic_class, df in cpt_data.groupby("Ic_class_groundhog"):
    ax.scatter(
        df["Ic_groundhog"],
        df["Depth (m)"],
        s=10,
        label=ic_class,
    )

# Depth conventionally increases downwards in CPT plots.
ax.invert_yaxis()
ax.set_xlabel("Soil behaviour index, $I_c$ [-]")
ax.set_ylabel("Depth [m]")
ax.set_title(f"CPT {CPT_ID}: Robertson-Wride soil behaviour")
ax.legend(title="Groundhog $I_c$ class")

plt.show()
