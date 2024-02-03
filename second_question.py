import pandas as pd
import seaborn as sb
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt

df_dolasci = pd.read_csv("data/Доласци туриста - годишњи подаци.csv", delimiter=';')
df_dolasci = df_dolasci.drop(columns=['idindikator', 'IDTer', 'nTuristi', 'nVrPod', 'mes', 'idJedinicaMere', 'nJedinicaMere',
                   'nIzvorI', 'Indikator', 'IDStatusPodatka', 'nStatusPodatka'])

regions_to_eliminate = ['РЕПУБЛИКА СРБИЈА', 'СРБИЈА – СЕВЕР', 'СРБИЈА – ЈУГ', 'Регион Шумадије и Западне Србије',
                        'Регион Јужне и Источне Србије', 'Регион Војводине', 'Београдски регион']

df_dolasci = df_dolasci[df_dolasci['IDVrPod'] != 1]
df_dolasci = df_dolasci.drop(columns='IDVrPod')


# Total
df_dolasci_f = df_dolasci[df_dolasci['IDTuristi'] == 0]
groped_dfs_for_areas = df_dolasci_f[~df_dolasci_f['nTer'].isin(regions_to_eliminate)].groupby("nTer")

for rg in groped_dfs_for_areas:
    print(rg)

plt.figure(figsize=(13, 8))

for region, region_df in groped_dfs_for_areas:
    plt.plot(region_df["god"], region_df["vrednost"], label=region)

plt.xlabel("Година")
plt.ylabel("Укупан број туриста")
plt.title("Укупан број туриста по регионима кроз гоидне")
plt.ticklabel_format(style='plain')
plt.legend(loc='upper left')
plt.show()

# Foreign
df_dolasci_f = df_dolasci[df_dolasci['IDTuristi'] == 2]
groped_dfs_for_areas = df_dolasci_f[~df_dolasci_f['nTer'].isin(regions_to_eliminate)].groupby("nTer")

for rg in groped_dfs_for_areas:
    print(rg)

plt.figure(figsize=(13, 8))

for region, region_df in groped_dfs_for_areas:
    plt.plot(region_df["god"], region_df["vrednost"], label=region)

plt.xlabel("Година")
plt.ylabel("Укупан број страних туриста")
plt.title("Укупан број страних туриста по регионима кроз гоидне")
plt.ticklabel_format(style='plain')
plt.legend(loc='upper left')
plt.show()