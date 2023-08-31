import pandas as pd 
source ='https://assessmentclouddata.blob.core.windows.net/azurevmdata/AZUREDATA.csv?sp=r&st=2023-08-30T06:57:30Z&se=2023-08-30T14:57:30Z&spr=https&sv=2022-11-02&sr=b&sig=ydnEkJoHHDf7TtxJxiYgTiuh19S2g7WZaRAIH1p2nJk%3D'
df = pd.read_csv(source)
print(df)
def vm_tier(memory ,core):
    result = df[(df['Memory'] == memory) & (df['Core'] == core)]['Tier']
    tier = result.values[:]
    return tier
vm_tier(432,64)
def vm_config(tier):
    result = df[df['Tier'] == tier][['Memory', 'Core']]
    memory, core = result['Memory'].values[0], result['Core'].values[0]
    return memory,core

vm_config('Standard_NV6ads_A10_v5')
def vm_tier(memory, core):
    result = df[(df['Memory'] == memory) & (df['Core'] == core)]
    
    if not result.empty:
        return result['Tier'].values[:]A
    else:
        config = df.iloc[((df['Memory'] - memory).abs() + (df['Core'] - core).abs()).idxmin()]
        tiers_config = df[(df['Memory'] == config['Memory']) & (df['Core'] == config['Core'])]['Tier'].values
        return f"Available configuration: Memory:{config['Memory']}, Core:{config['Core']}, Tiers:{config['Tier']},{','.join(tiers_config)}"
vm_tier(128,12)